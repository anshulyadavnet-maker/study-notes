#!/usr/bin/env python3
"""
md2pdf.py — Markdown ➜ handwritten-style PDF (Playpen Sans Deva)

USAGE
  python3 md2pdf.py notes.md                        # -> notes.pdf
  python3 md2pdf.py notes.md -o out.pdf
  python3 md2pdf.py a.md b.md c.md -o book.pdf      # merge many files
  python3 md2pdf.py folder/                         # every *.md in folder, sorted
  python3 md2pdf.py notes.md --title "गणित" --subtitle "SUPER TET" --toc
  python3 md2pdf.py notes.md --no-cover --no-toc

EXTRA MARKDOWN YOU CAN USE
  ::: trick  ⚡ शॉर्टकट
  content...
  :::
  Types: trick | formula | trap | example | remember | question | (default)

  Blockquotes are auto-coloured from their first emoji:
      💡/⚡ amber   🔑/✅ green   ⚠️/❌ red   ℹ️/📌 blue   ⭐ purple   🧠/📝 teal
"""

import argparse, os, re, sys, html
from pathlib import Path

try:
    import markdown
except ImportError as e:
    sys.exit(f"Missing dependency: {e}\n  pip install markdown pygments")

WEASYPRINT_AVAILABLE = False
try:
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
    WEASYPRINT_AVAILABLE = True
except Exception:
    WEASYPRINT_AVAILABLE = False


_OPTS = {}
HERE = Path(__file__).resolve().parent
CSS_FILE = HERE / "style.css"
sys.path.insert(0, str(HERE))
try:
    from figlib import icons as _icons
except Exception:
    _icons = None
try:
    from figlib import mathtex
except Exception as _e:
    mathtex = None
    print(f"  ! mathtex unavailable ({_e}) — $…$ will stay as plain text")
try:
    import figlib
except Exception as _e:          # figures optional
    figlib = None
    print(f"  ! figlib unavailable ({_e}) — ```figure``` blocks will be skipped")



# ------------------------------------------------------------- icons
ICON_RE = re.compile(r":icon-([a-z]+)(?:\|([\d.]+))?:")


def convert_icons(md: str) -> str:
    """:icon-bulb:  or  :icon-bulb|1.4:  -> inline svg"""
    if _icons is None:
        return md
    def repl(m):
        return _icons.render(m.group(1), float(m.group(2) or 1.0))
    # never touch fenced code / inline code
    parts = re.split(r"(```.*?```|`[^`\n]*`)", md, flags=re.S)
    for i, chunk in enumerate(parts):
        if chunk.startswith("`"):
            continue
        parts[i] = ICON_RE.sub(repl, chunk)
    return "".join(parts)


# ------------------------------------------------------------ figures
FIG_BLOCK = re.compile(r"^```figure\s*\n(.*?)^```\s*$", re.S | re.M)


def _atom(v):
    """str -> int / float / bool / stripped str"""
    v = str(v).strip().strip("'\"")
    if v.lower() in ("true", "yes"):
        return True
    if v.lower() in ("false", "no"):
        return False
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        return v


def _parse_spec(body: str) -> dict:
    """Tiny YAML-ish parser: key: value, [a, b] lists, true/false, numbers."""
    spec = {}
    for line in body.strip().split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        k, v = k.strip(), v.strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1].strip()
            if inner.startswith("["):          # nested list e.g. [[1,2,3],[4,5,6]]
                v = [[_atom(t) for t in grp.split(",") if t.strip()]
                     for grp in re.findall(r"\[([^\]]*)\]", inner)]
            else:
                # split on commas OUTSIDE quotes so "3,4,A" stays one item
                parts = re.findall(r'"[^"]*"|\'[^\']*\'|[^,\s][^,]*', inner)
                v = [_atom(x) for x in parts if x.strip()]
        elif v.lower() in ("true", "yes"):
            v = True
        elif v.lower() in ("false", "no"):
            v = False
        else:
            # strip only a MATCHING pair of outer quotes, so a caption that
            # ends in a quoted phrase keeps its closing quote
            if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
                v = v[1:-1]
            try:
                v = int(v)
            except ValueError:
                try:
                    v = float(v)
                except ValueError:
                    pass
        spec[k] = v
    return spec


FIG_ROW_OPEN = '<div class="fig-row cols{n}">'


def group_figure_rows(html: str) -> str:
    """Wrap runs of *adjacent* <figure> elements in a flex row (2-up).

    Uses a scanning tokeniser rather than a regex: figure bodies contain nested
    tags, and a lazy `.*?` will happily span across two figures and swallow the
    prose between them.
    """
    OPEN = '<figure class="fig">'
    CLOSE = "</figure>"
    out = []
    pending = []          # consecutive figures awaiting pairing

    def flush():
        while pending:
            pair = pending[:2]
            del pending[:2]
            if len(pair) == 2:
                out.append(FIG_ROW_OPEN.format(n=2) + "".join(pair) + "</div>")
            else:
                out.append(pair[0])

    i = 0
    while True:
        nxt = html.find(OPEN, i)
        if nxt == -1:
            tail = html[i:]
            if tail.strip():
                flush()
            out.append(tail)
            break
        gap = html[i:nxt]
        if gap.strip():      # real content between figures -> break the run
            flush()
            out.append(gap)
        else:
            out.append("") if False else None   # keep whitespace out of rows
        end = html.find(CLOSE, nxt)
        if end == -1:
            out.append(html[nxt:])
            break
        end += len(CLOSE)
        pending.append(html[nxt:end])
        i = end
    flush()
    return "".join(x for x in out if x is not None)


def convert_figures(md: str) -> str:
    """```figure ... ``` -> <figure class="fig"> inline SVG + numbered caption.

    Numbering is chapter-scoped: the chapter number is read from the nearest
    preceding `# ... N ...` heading, and figures restart at .1 in each chapter.
    """
    state = {"chap": "", "n": 0}

    # pre-scan positions of H1 headings so we know which chapter each figure is in
    def chap_at(pos):
        """Chapter number = nearest preceding heading that names a chapter.

        Books use `## अध्याय 16 — ...` for chapters and `# SET 1 — ...` for the
        volume title, so prefer an explicit अध्याय/Chapter heading and fall back
        to the first number in the nearest H1/H2.
        """
        best = ""
        for hm in re.finditer(r"^(#{1,2})\s+(.*)$", md, re.M):
            if hm.start() > pos:
                break
            title = hm.group(2)
            cm = re.search(r"(?:अध्याय|Chapter|CHAPTER)\s*(\d+)", title)
            if cm:
                best = cm.group(1)
            elif hm.group(1) == "#":
                nums = re.findall(r"\d+", title)
                best = nums[0] if nums else best
        return best

    def repl(m):
        spec = _parse_spec(m.group(1))
        cap = spec.pop("caption", "")
        ch = chap_at(m.start())
        if ch != state["chap"]:
            state["chap"], state["n"] = ch, 0
        state["n"] += 1
        num = f"{ch}.{state['n']}" if ch else str(state["n"])
        if figlib is None:
            return f"*[figure: {spec.get('type','?')}]*"
        try:
            svg = figlib.render(spec)
        except Exception as e:
            print(f"    ! figure error ({spec.get('type')}): {e}")
            return f'<div class="callout trap"><p class="callout-title">figure error</p><p>{html.escape(str(e))}</p></div>'
        label = f'<span class="fignum">चित्र {num}</span>'
        caphtml = f"<figcaption>{label}{' — ' + cap if cap else ''}</figcaption>"
        # figures wider than ~300 units need the full text column
        mw = re.search(r'viewBox="0 0 ([\d.]+)', svg)
        wide = float(mw.group(1)) > 300 if mw else False
        cls = "fig wide" if wide else "fig"
        return f'<figure class="{cls}">{svg}{caphtml}</figure>' 
    return FIG_BLOCK.sub(repl, md)

# ------------------------------------------------- emoji -> printable glyphs
# Colour-emoji fonts are unavailable in most PDF pipelines, so map the emoji we
# use to monochrome symbols that exist in DejaVu Sans. The blockquote colour is
# chosen BEFORE this runs, so box colours are unaffected.
EMOJI_MAP = {
    "💡":"✎", "⚡":"⚡", "🔑":"✔", "✅":"✔", "⭐":"★", "🌟":"★",
    "⚠️":"⚠", "⚠":"⚠", "❌":"✘", "🚫":"✘", "🎯":"◆", "📌":"▶",
    "🧠":"✎", "📝":"✎", "🗒":"✎", "📊":"▶", "📚":"▶", "ℹ️":"▶", "ℹ":"▶",
    "🔥":"◆", "👉":"➤", "➡️":"→", "🎁":"◆", "🇮🇳":"", "🟦":"■", "🟩":"■",
    "🟨":"■", "🟧":"■", "🟪":"■", "🟥":"■", "🎓":"★", "⏭️":"➤", "📖":"▶",
    "✍️":"✍", "🖊":"✎", "🗓️":"▶", "🗓":"▶", "✔️":"✔", "✘":"✘",
}

def swap_emoji(text: str) -> str:
    for a, b in EMOJI_MAP.items():
        text = text.replace(a, b)
    return text


def split_adjacent_blockquotes(md: str) -> str:
    """Blank-line-separated > blocks merge into ONE blockquote in Markdown.
    Insert an HTML comment between them so each becomes its own coloured box."""
    lines, out = md.split("\n"), []
    for i, ln in enumerate(lines):
        out.append(ln)
        if ln.lstrip().startswith(">"):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].lstrip().startswith(">") and j > i + 1:
                out.append("")
                out.append("<!-- -->")
    return "\n".join(out)

# ---------------------------------------------------------------- callouts
CALLOUT_TYPES = {"trick", "formula", "trap", "example", "remember", "question", "info"}
COLS_RE = re.compile(r"^:::\s*cols\s*(\d)?\s*$", re.M)

def convert_callouts(md: str) -> str:
    """::: type Title\n body \n:::   ->  <div class="callout type">"""
    out, stack = [], []
    for line in md.split("\n"):
        cm = COLS_RE.match(line.strip())
        if cm:
            out.append(f'<div class="mcols c{cm.group(1) or 2}" markdown="1">')
            stack.append("cols")
            continue
        m = re.match(r"^:::\s*(\w+)?\s*(.*)$", line.strip())
        if m and not (line.strip() == ":::" and stack):
            ctype = (m.group(1) or "info").lower()
            title = m.group(2).strip()
            if ctype not in CALLOUT_TYPES:
                title = f"{m.group(1) or ''} {title}".strip()
                ctype = "info"
            out.append(f'<div class="callout {ctype}" markdown="1">')
            if title:
                out.append(f'<p class="callout-title">{html.escape(title)}</p>')
            stack.append(ctype)
        elif line.strip() == ":::" and stack:
            out.append("</div>")
            stack.pop()
        else:
            out.append(line)
    while stack:
        out.append("</div>"); stack.pop()
    return "\n".join(out)

# ------------------------------------------------------- blockquote colours
BQ_RULES = [
    ("key",  ["🔑", "✅", "✔"]),
    ("warn", ["⚠", "❌", "✘", "🚫"]),
    ("tip",  ["💡", "⚡", "🎯"]),
    ("star", ["⭐", "🌟"]),
    ("note", ["🧠", "📝", "🗒"]),
    ("info", ["ℹ", "📌", "📊", "📚"]),
]

def colour_blockquotes(soup_html: str) -> str:
    def repl(m):
        inner = m.group(1)
        head = re.sub(r"<[^>]+>", "", inner)[:14]
        for cls, marks in BQ_RULES:
            if any(ch in head for ch in marks):
                return f'<blockquote class="{cls}">{inner}</blockquote>'
        return f"<blockquote>{inner}</blockquote>"
    return re.sub(r"<blockquote>(.*?)</blockquote>", repl, soup_html, flags=re.S)

# --------------------------------------------------------------- checkboxes
def convert_tasks(h: str) -> str:
    h = re.sub(r"<li>\s*\[\s*\]\s*", '<li class="task">', h)
    h = re.sub(r"<li>\s*\[[xX]\]\s*", '<li class="task done">', h)
    return h

# ------------------------------------------------------------- big tables
def mark_long_tables(h: str) -> str:
    def repl(m):
        t = m.group(0)
        return t.replace("<table>", '<table class="long">', 1) if t.count("<tr") > 14 else t
    return re.sub(r"<table>.*?</table>", repl, h, flags=re.S)

# -------------------------------------------------------------------- TOC
def format_toc_title(txt: str) -> str:
    m = re.match(r'^((?:अध्याय|Chapter|CHAPTER|भाग|Part|SET|खंड|खण्ड)\s*[\dA-Za-z\u0966-\u096F]+|\d+\.)', txt, re.I)
    if m:
        prefix = m.group(1).strip()
        rest = txt[len(prefix):].strip()
        if rest and rest[0] in ('—', ':', '-', '·', '.'):
            sep = rest[0]
            rest = rest[1:].strip()
            return f'<span class="num">{prefix}</span> <span class="sep">{sep}</span> {rest}'
        else:
            return f'<span class="num">{prefix}</span> {rest}'
    return txt


def build_toc(h: str) -> str:
    items = re.findall(r'<h([123])[^>]*id="([^"]+)"[^>]*>(.*?)</h[123]>', h, flags=re.S)
    if not items:
        return ""

    def clean_text(txt):
        return re.sub(r'<[^>]+>', '', txt).strip()

    h1_items = [(hid, clean_text(t)) for lvl, hid, t in items if lvl == '1']
    rows = []
    chap_re = re.compile(r'^(अध्याय|Chapter|CHAPTER|भाग|Part|PART|SET|खंड|खण्ड)\s*[\d\w\.\—\:\-]', re.I)

    if len(h1_items) > 1:
        # Multi-chapter document where chapters/parts are H1
        for lvl, hid, raw in items:
            txt = clean_text(raw)
            if not txt:
                continue
            if lvl == '1':
                formatted = format_toc_title(txt)
                is_part = bool(re.match(r'^(भाग|Part|SET|खंड)\b', txt, re.I))
                cls = "toc-part" if is_part else "toc-chap"
                rows.append(f'<li class="{cls}"><a href="#{hid}">{formatted}</a></li>')
            elif lvl == '2':
                # Include explicit chapter headings if placed at H2 level
                if chap_re.match(txt):
                    formatted = format_toc_title(txt)
                    rows.append(f'<li class="toc-chap lvl2"><a href="#{hid}">{formatted}</a></li>')
    else:
        # Single-file or single-H1 document (e.g. chapters are at H2 level)
        for lvl, hid, raw in items:
            txt = clean_text(raw)
            if not txt:
                continue
            if lvl == '1':
                continue
            elif lvl == '2':
                # Filter out noisy non-chapter subsections
                if any(noise in txt for noise in ['सीखने के उद्देश्य', 'परीक्षा में महत्व', 'PYQ', 'परिचय व वेटेज', 'संख्या रेखा पर स्थिति', 'वर्गीकरण']):
                    continue
                formatted = format_toc_title(txt)
                is_part = bool(re.match(r'^(भाग|Part|SET|खंड)\b', txt, re.I))
                cls = "toc-part" if is_part else "toc-chap"
                rows.append(f'<li class="{cls}"><a href="#{hid}">{formatted}</a></li>')

    if not rows:
        return ""

    return ('<section class="toc"><h1>विषय-सूची / Contents</h1><ul>'
            + "".join(rows) + "</ul></section>")

# ------------------------------------------------------------------ cover
def build_cover(title, subtitle, meta, badge) -> str:
    m = "".join(f"<div>{html.escape(x)}</div>" for x in meta if x)
    return f"""<section class="cover">
  <div class="kicker">Study Notes</div>
  <h1>{html.escape(title)}</h1>
  <div class="rule"></div>
  {f'<div class="sub">{html.escape(subtitle)}</div>' if subtitle else ''}
  <div class="meta">{m}</div>
  {f'<div class="badge">{html.escape(badge)}</div>' if badge else ''}
</section>"""

# ------------------------------------------------------------------- main
QCOL_SPLIT = re.compile(r'(?=<h[12][ >])')


def apply_qcols(html: str) -> str:
    """Two-column flow for MCQ-heavy sections.

    Splits at each H1/H2 and wraps the body in .qcols, but only where the
    section really is question-shaped (several **Q..** items and no wide table).
    Headings stay full width.
    """
    parts = QCOL_SPLIT.split(html)
    out = []
    for part in parts:
        qcount = len(re.findall(r"<strong>Q\d", part))
        wide = part.count("<table") > 0 and part.count("<tr") > 8
        figs = "<figure" in part
        if qcount >= 4 and not wide and not figs:
            m = re.match(r"(\s*<h[12][^>]*>.*?</h[12]>)(.*)", part, re.S)
            if m:
                out.append(m.group(1) + f'<div class="qcols">{m.group(2)}</div>')
                continue
        out.append(part)
    return "".join(out)


def prefix_ids(html_str: str, pfx: str) -> str:
    """Prefix all heading IDs and internal hash links with a unique per-file prefix."""
    if not pfx:
        return html_str
    def id_repl(m):
        return f'{m.group(1)}id="{pfx}-{m.group(2)}"'
    html_str = re.sub(r'(<[a-zA-Z0-9_-]+\s+[^>]*?)id="([^"]+)"', id_repl, html_str)
    def href_repl(m):
        return f'{m.group(1)}href="#{pfx}-{m.group(2)}"'
    html_str = re.sub(r'(<a\s+[^>]*?)href="#([^"]+)"', href_repl, html_str)
    return html_str


def md_to_html(text: str, prefix: str = "") -> str:
    text = convert_figures(text)
    text = convert_icons(text)
    if mathtex is not None:
        text = mathtex.convert(text)
    text = split_adjacent_blockquotes(text)
    text = convert_callouts(text)
    md = markdown.Markdown(extensions=[
        "extra", "tables", "fenced_code", "sane_lists",
        "attr_list", "md_in_html", "toc", "nl2br",
    ], extension_configs={"toc": {"permalink": False}})
    h = md.convert(text)
    h = colour_blockquotes(h)   # colour chosen from the ORIGINAL emoji
    h = swap_emoji(h)           # then swap to print-safe glyphs
    h = convert_tasks(h)
    h = mark_long_tables(h)
    h = group_figure_rows(h)
    if _OPTS.get("qcols"):
        h = apply_qcols(h)
    if prefix:
        h = prefix_ids(h, prefix)
    return h


def natural_sort_key(p):
    """Sort strings with embedded numbers naturally (e.g. Chapter-2 before Chapter-10)."""
    s = str(p)
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def collect(inputs):
    files = []
    for p in inputs:
        p = Path(p)
        if p.is_dir():
            md_files = [f for f in p.glob("*.md") if not f.name.startswith("-")]
            files += sorted(md_files, key=natural_sort_key)
        elif p.suffix.lower() in (".md", ".markdown"):
            files.append(p)
        else:
            print(f"  ! skipped (not markdown): {p}")
    return files


def render_pdf_with_browser(doc: str, out_path: Path, css_file: Path, extra_css=None, flow=False):
    import subprocess, shutil
    browser = None
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        shutil.which("msedge"),
        shutil.which("chrome"),
        shutil.which("google-chrome"),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            browser = c
            break

    if not browser:
        sys.exit("Error: Neither WeasyPrint nor Microsoft Edge/Chrome browser is available to render PDF.")

    css_text = css_file.read_text(encoding="utf-8")
    if flow:
        css_text += "\nh1{page-break-before:auto;margin-top:9mm;}h1:first-of-type{margin-top:0;}"
    if extra_css and Path(extra_css).exists():
        css_text += "\n" + Path(extra_css).read_text(encoding="utf-8")

    full_html = doc.replace("</head>", f"<style>{css_text}</style></head>")
    temp_html = HERE / f"temp_{out_path.stem}.html"
    temp_html.write_text(full_html, encoding="utf-8")

    html_uri = temp_html.resolve().as_uri()
    out_pdf = out_path.resolve()
    out_pdf.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        browser,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={out_pdf}",
        "--no-pdf-header-footer",
        html_uri
    ]
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    finally:
        if temp_html.exists():
            temp_html.unlink()


def main():
    ap = argparse.ArgumentParser(description="Markdown -> handwritten-style PDF")
    ap.add_argument("inputs", nargs="+", help="md files and/or folders")
    ap.add_argument("-o", "--output")
    ap.add_argument("--title"); ap.add_argument("--subtitle")
    ap.add_argument("--author", default="")
    ap.add_argument("--badge", default="")
    ap.add_argument("--toc", action="store_true", help="force TOC on")
    ap.add_argument("--no-toc", action="store_true")
    ap.add_argument("--no-cover", action="store_true")
    ap.add_argument("--css", help="extra css file")
    ap.add_argument("--flow", action="store_true",
                    help="chapters continue on the same page instead of "
                         "always starting a new one (saves tail pages)")
    ap.add_argument("--qcols", action="store_true",
                    help="flow MCQ chapters in two columns (question banks)")
    a = ap.parse_args()

    _OPTS["qcols"] = a.qcols
    files = collect(a.inputs)
    if not files:
        sys.exit("No markdown files found.")

    title = a.title or files[0].stem.replace("-", " ").replace("_", " ")
    out = Path(a.output) if a.output else files[0].with_suffix(".pdf")

    print(f"  reading {len(files)} file(s)")
    body = []
    for i, f in enumerate(files, 1):
        print(f"    - {f.name}")
        pfx = f"ch{i:02d}" if len(files) > 1 else ""
        body.append(md_to_html(f.read_text(encoding="utf-8"), prefix=pfx))
    content = "\n".join(body)

    parts = []
    if not a.no_cover:
        from datetime import date
        meta = [a.author, f"{len(files)} अध्याय-फाइल" if len(files) > 1 else "",
                date.today().strftime("%d %B %Y")]
        parts.append(build_cover(title, a.subtitle or "", meta, a.badge))
    want_toc = a.toc or (len(files) > 1 and not a.no_toc)
    if want_toc and not a.no_toc:
        t = build_toc(content)
        if t: parts.append(t)
    parts.append(content)

    doc = f"""<!DOCTYPE html><html lang="hi"><head><meta charset="utf-8">
<title>{html.escape(title)}</title></head><body>{''.join(parts)}</body></html>"""

    debug = out.with_suffix(".debug.html")
    debug.write_text(doc, encoding="utf-8")

    print("  rendering PDF ...")
    rendered = False
    if WEASYPRINT_AVAILABLE:
        try:
            font_config = FontConfiguration()
            sheets = [CSS(filename=str(CSS_FILE), font_config=font_config)]
            if a.flow:
                sheets.append(CSS(string=
                    "h1{page-break-before:auto;margin-top:9mm;}"
                    "h1:first-of-type{margin-top:0;}", font_config=font_config))
            if a.css:
                sheets.append(CSS(filename=a.css, font_config=font_config))

            HTML(string=doc, base_url=str(HERE)).write_pdf(
                str(out), stylesheets=sheets, font_config=font_config)
            rendered = True
        except Exception as err:
            print(f"  ! WeasyPrint failed ({err}), falling back to Headless Browser...")

    if not rendered:
        render_pdf_with_browser(doc, out, CSS_FILE, extra_css=a.css, flow=a.flow)

    debug.unlink(missing_ok=True)
    mb = out.stat().st_size / 1024 / 1024
    try:
        print(f"  ✔ {out}  ({mb:.2f} MB)")
    except UnicodeEncodeError:
        print(f"  [OK] {out}  ({mb:.2f} MB)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()

