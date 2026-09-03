#!/usr/bin/env python3
"""
md2pdf-hb.py — Markdown ➜ PDF  (pure-Python HarfBuzz engine)
=============================================================
Same markdown flavour & look as pdf-system/md2pdf.py but needs NO
WeasyPrint / pango system libraries, so it runs in a plain venv:

    pip install uharfbuzz fonttools reportlab

It uses the bundled handwriting fonts (pdf-system/fonts/PlaypenSansDeva-*)
and shapes Devanagari/Hinglish correctly through HarfBuzz.

USAGE
  python3 pdf-system/md2pdf-hb.py notes.md
  python3 pdf-system/md2pdf-hb.py ch1.md ch2.md -o book.pdf --toc
  python3 pdf-system/md2pdf-hb.py folder/ -o out.pdf --toc

OPTIONS
  -o, --output   output pdf path
  --title        cover title (default: file name)
  --subtitle     cover subtitle
  --badge        cover badge text
  --toc          force table of contents
  --no-toc       disable table of contents
  --no-cover     disable cover page
"""

import argparse, os, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
FONTS = HERE / "fonts"

try:
    import uharfbuzz as hb
    from fontTools.ttLib import TTFont
    from fontTools.pens.recordingPen import RecordingPen
    from fontTools.pens.qu2cuPen import Qu2CuPen
    from reportlab.pdfgen import canvas as rlcanvas
    from reportlab.lib.colors import HexColor
except ImportError as e:
    sys.exit(f"Missing dependency: {e}\n  pip install uharfbuzz fonttools reportlab")

# ------------------------------------------------------------------ palette
INK      = "#1f2431"
INK_BOLD = "#111726"
SOFT     = "#5a6275"
RULE     = "#dfe3ec"
BLUE     = "#1668c4";  BLUE_D   = "#0f4f9c"; BG_BLUE  = "#eaf3ff"
GREEN    = "#127a4d";  BG_GREEN = "#e6f7ee"
AMBER    = "#a8620a";  BG_AMBER = "#fff3dc"
RED      = "#c02b3a";  BG_RED   = "#ffecec"
PURPLE   = "#6b3fa0";  BG_PURPLE= "#f3ecff"
TEAL     = "#0b6f78";  BG_TEAL  = "#e3f7f8"
PINK     = "#b83280";  BG_PINK  = "#fdecf6"
PAGE_W, PAGE_H = 595.0, 842.0
MARGIN = 44.0
BODY = 10.6
LH = 1.42

EMOJI_STYLES = [
    ("💡", "amber"), ("⚡", "amber"), ("🎯", "amber"),
    ("🔑", "green"), ("✅", "green"), ("✔️", "green"),
    ("⚠️", "red"), ("❌", "red"), ("🚫", "red"),
    ("📌", "blue"), ("ℹ️", "blue"), ("📊", "blue"), ("📚", "blue"),
    ("⭐", "purple"), ("🌟", "purple"),
    ("🧠", "teal"), ("📝", "teal"), ("🗒️", "teal"),
]
STYLE_COLORS = {"blue": (BLUE, BG_BLUE), "green": (GREEN, BG_GREEN),
                "amber": (AMBER, BG_AMBER), "red": (RED, BG_RED),
                "purple": (PURPLE, BG_PURPLE), "teal": (TEAL, BG_TEAL),
                "pink": (PINK, BG_PINK)}
CALLOUT_DEFAULTS = {
    "trick": ("ट्रिक", "amber"), "formula": ("सूत्र", "green"),
    "trap": ("जाल", "red"), "example": ("उदाहरण", "purple"),
    "remember": ("याद रखें", "teal"), "question": ("प्रश्न", "pink"),
}

EMOJI_RE = re.compile("[\U0001F000-\U0001FAFF\u2600-\u27BF\uFE0F\u200D]")


def strip_emoji(t: str) -> str:
    return EMOJI_RE.sub("", t or "").strip()


def first_style(t: str) -> str:
    t = t.strip()
    for ch, st in EMOJI_STYLES:
        if t.startswith(ch):
            return st
    return None


# ================================================================== shaping
class Font:
    """One TTF weight: shaping (harfbuzz) + outline drawing (fontTools)."""

    def __init__(self, path: str):
        self.path = path
        self.tt = TTFont(path)
        self.upem = self.tt["head"].unitsPerEm
        self.glyphset = self.tt.getGlyphSet()
        self.glyph_order = self.tt.getGlyphOrder()
        self.face = hb.Face(hb.Blob.from_file_path(path))
        self.hf = hb.Font(self.face)
        self.hf.scale = (self.upem, self.upem)
        self._cache = {}

    def raw(self, text: str):
        text = EMOJI_RE.sub("", text or "")     # drop symbols without glyphs
        if not text:
            return []
        key = text
        if key in self._cache:
            return self._cache[key]
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hf, buf)
        out = [(g.codepoint, p.x_advance, p.x_offset, p.y_offset)
               for g, p in zip(buf.glyph_infos, buf.glyph_positions)]
        self._cache[key] = out
        return out

    def width(self, text: str, size: float) -> float:
        s = size / self.upem
        return sum(dx * s for _, dx, _, _ in self.raw(text))

    # rich text: **bold** aware wrap --------------------------------
    @staticmethod
    def _tokens(text: str):
        """split into (word, bold, had_space_before)"""
        parts = re.split(r"(\*\*[^*]+\*\*)", text)
        toks = []
        for k, p in enumerate(parts):
            if not p:
                continue
            bold = p.startswith("**") and p.endswith("**")
            body = p[2:-2] if bold else p
            lead = True
            for w in body.split(" "):
                if w == "":
                    continue
                toks.append((w, bold, not lead))
                lead = False
        return toks

    def wrap_rich(self, text: str, size: float, max_w: float):
        toks = self._tokens(text)
        space = self.width(" ", size)
        lines, cur, cur_w = [], [], 0.0
        for w, b, sp in toks:
            add = self.width(w, size) + (space if (cur and sp) else 0)
            if cur and cur_w + add > max_w:
                lines.append(cur)
                cur, cur_w = [(w, b, sp)], self.width(w, size)
            else:
                cur.append((w, b, sp))
                cur_w += add
        if cur:
            lines.append(cur)
        return lines

    def wrap_plain(self, text: str, size: float, max_w: float):
        return ["".join(w if not sp else " " + w for w, _, sp in ln)
                for ln in self.wrap_rich(text, size, max_w)]

    # drawing ---------------------------------------------------------
    def draw_line(self, cv, line, x, y, size, color):
        """line: list of (word, bold, had_space_before) OR plain string"""
        if isinstance(line, str):
            line = [(w, False, sp) for (w, _, sp) in self._tokens(line)] or []
        if not line:
            return x
        for w, bold, sp in line:
            if sp:
                self._emit_glyphs(cv, self.raw(" "), x, y, size, color)
                x += self.width(" ", size)
            col = INK_BOLD if bold else color
            self._emit_glyphs(cv, self.raw(w), x, y, size, col)
            x += self.width(w, size)
        return x

    def draw_text(self, cv, text, x, y, size, color):
        self.draw_line(cv, text, x, y, size, color)

    def _emit_glyphs(self, cv, raw, x, y, size, color):
        s = size / self.upem
        cv.saveState()
        cv.setFillColor(HexColor(color))
        for gid, dx, xo, yo in raw:
            name = self.glyph_order[gid] if gid < len(self.glyph_order) else ".notdef"
            g = self.glyphset.get(name)
            if g is None:
                x += dx * s
                continue
            rec = RecordingPen()
            try:
                Qu2CuPen(rec, 0.001).draw(g) if False else g.draw(Qu2CuPen(rec, 0.01))
            except Exception:
                x += dx * s
                continue
            cv.saveState()
            cv.translate(x + xo * s, y + yo * s)
            cv.scale(s, s)
            p = cv.beginPath()
            for op, args in rec.value:
                if op == "moveTo":
                    p.moveTo(*args[0])
                elif op == "lineTo":
                    p.lineTo(*args[0])
                elif op == "curveTo":
                    p.curveTo(*[c for pt in args for c in pt])
                elif op == "qCurveTo":
                    # fallback: glyf quads normally converted by Qu2CuPen
                    for pt in args:
                        p.lineTo(*pt)
                elif op == "closePath":
                    p.close()
            cv.drawPath(p, stroke=0, fill=1)
            cv.restoreState()
            x += dx * s
        cv.restoreState()


# ================================================================ markdown
def md_to_blocks(md: str):
    lines = md.split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        s = lines[i].rstrip()
        if not s.strip():
            i += 1
            continue
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            blocks.append({"t": "h" + str(len(m.group(1))),
                           "x": m.group(2).strip()})
            i += 1
            continue
        if s.startswith("|") and i + 1 < n and \
                re.match(r"^\|[\s:\-|]+\|?\s*$", lines[i + 1]):
            head = [strip_emoji(c).strip() for c in s.strip("|").split("|")]
            rows, i = [], i + 2
            while i < n and lines[i].strip().startswith("|"):
                rows.append([strip_emoji(c).strip()
                             for c in lines[i].strip().strip("|").split("|")])
                i += 1
            blocks.append({"t": "table", "head": head, "rows": rows})
            continue
        if re.match(r"^(-{3,}|\*{3,})\s*$", s):
            blocks.append({"t": "hr"})
            i += 1
            continue
        m = re.match(r"^:::\s*(\w+)(?:\s+(.*))?$", s)
        if m:
            kind = m.group(1).lower()
            label = (m.group(2) or "").strip()
            body, i = [], i + 1
            while i < n and not re.match(r"^:::\s*$", lines[i].strip()):
                body.append(lines[i])
                i += 1
            if i < n:
                i += 1
            dlabel, dcol = CALLOUT_DEFAULTS.get(kind, (kind.title(), "amber"))
            label = strip_emoji(label) or dlabel
            col = dcol if kind in CALLOUT_DEFAULTS else "amber"
            blocks.append({"t": "callout", "label": label, "col": col,
                           "body": "\n".join(body).strip()})
            continue
        if s.startswith(">"):
            q = []
            while i < n and lines[i].strip().startswith(">"):
                q.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append({"t": "quote", "lines": q})
            continue
        if s.startswith("```"):
            code, i = [], i + 1
            while i < n and not lines[i].strip().startswith("```"):
                code.append(lines[i])
                i += 1
            if i < n:
                i += 1
            blocks.append({"t": "code", "lines": code})
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", s)
        if m and not s.startswith("**"):
            items = []
            while i < n:
                mm = re.match(r"^\s*[-*]\s+(.*)$", lines[i])
                if not mm:
                    break
                items.append(mm.group(1).strip())
                i += 1
            blocks.append({"t": "list", "items": items})
            continue
        para = [s.strip()]
        i += 1
        while i < n:
            nx = lines[i].strip()
            if (not nx or nx.startswith(("#", "|", ">", ":::", "```"))
                    or re.match(r"^(-{3,}|\*{3,})\s*$", nx)
                    or (re.match(r"^\s*[-*]\s+", nx) and not nx.startswith("**"))):
                break
            para.append(nx)
            i += 1
        blocks.append({"t": "p", "x": " ".join(para)})
    return blocks


# ================================================================= document
class PdfDoc:
    def __init__(self, out, title, subtitle, badge, cover, toc):
        self.out = out
        self.title = title
        self.subtitle = subtitle
        self.badge = badge
        self.cover = cover
        self.toc = toc
        self.fonts = {}
        for w in ("400", "700"):
            self.fonts[w] = Font(str(FONTS / f"PlaypenSansDeva-{w}.ttf"))
        self.virtual = False            # measuring pass (no canvas draws)
        self.cv = None
        self.page = 1
        self.y = 0.0
        self.headings_pages = []        # (level, text, page) recorded v-pass
        self.toc_items = []
        self.toc_final = []
        self.avail = PAGE_W - 2 * MARGIN

    def f(self, bold=False):
        return self.fonts["700" if bold else "400"]

    # ----------------------------------------------------------- pages
    def _boot(self):
        self.page, self.y = 1, PAGE_H - 46

    def _break(self):
        if not self.virtual:
            self._footer()
            self.cv.showPage()
        self.page += 1
        self.y = PAGE_H - 46

    def ensure(self, h):
        if self.y - h < 62:
            self._break()

    def _footer(self):
        y = 40
        self.cv.setStrokeColor(HexColor(RULE))
        self.cv.setLineWidth(0.6)
        self.cv.line(MARGIN, y - 10, PAGE_W - MARGIN, y - 10)
        txt = f"— {self.page} —"
        w = self.f().width(txt, 8.5)
        self.f().draw_text(self.cv, txt, (PAGE_W - w) / 2, y - 20, 8.5, "#aeb5c5")

    def lh(self, size):
        return size * LH

    # ------------------------------------------------------------ build
    def build(self, blocks):
        # static TOC skeleton (order of h1/h2 in the document)
        self.toc_items = [(b["x"], int(b["t"][1]))
                          for b in blocks if b["t"] in ("h1", "h2")]
        # pass 1 (virtual): compute heading pages
        self.virtual = True
        self._layout(blocks)
        pages = [pg for _, _, pg in self.headings_pages]
        self.toc_final = [(lv, tx, (pages[i] if i < len(pages) else "00"))
                          for i, (tx, lv) in enumerate(self.toc_items)]
        # pass 2 (draw)
        self.virtual = False
        self.cv = rlcanvas.Canvas(self.out, pagesize=(PAGE_W, PAGE_H))
        self.cv.setTitle(self.title)
        self._layout(blocks)
        self._footer()
        self.cv.showPage()
        self.cv.save()

    def _layout(self, blocks):
        self._boot()
        if self.cover:
            if not self.virtual:
                self._draw_cover()
            self._break()
        if self.toc:
            if self.virtual:
                src = [(lv, tx, "00") for tx, lv in self.toc_items]
            else:
                src = self.toc_final
            self._draw_toc(src)
            self._break()
        for b in blocks:
            self._render(b)

    # ----------------------------------------------------------- blocks
    def _render(self, b):
        t = b["t"]
        if t == "h1":
            self._h(b["x"], 17.0, BLUE, BLUE_D, 1)
        elif t == "h2":
            self._h(b["x"], 15.0, PURPLE, None, 2, dash=True)
        elif t == "h3":
            self._h(b["x"], 12.4, TEAL, None, 3, bar=True)
        elif t == "h4":
            self._h(b["x"], 11.0, AMBER, None, 4)
        elif t == "p":
            self._paragraph(b["x"])
        elif t == "list":
            self._list(b["items"])
        elif t == "table":
            self._table(b["head"], b["rows"])
        elif t == "quote":
            self._quote(b["lines"])
        elif t == "callout":
            self._callout(b["label"], b["col"], b["body"])
        elif t == "code":
            self._code(b["lines"])
        elif t == "hr":
            self.ensure(14)
            if not self.virtual:
                self.cv.setStrokeColor(HexColor(RULE))
                self.cv.setLineWidth(0.8)
                self.cv.line(MARGIN, self.y - 4, PAGE_W - MARGIN, self.y - 4)
            self.y -= 12

    def _h(self, text, size, color, bar_color, level, dash=False, bar=False):
        if level == 1:
            if self.y < PAGE_H - 46.5:          # avoid blank page at start
                self._break()
        f = self.f(True)
        lines = f.wrap_rich(text, size, self.avail - 6)
        h = size + (len(lines) - 1) * self.lh(size)
        self.ensure(h + 16 if level == 1 else h + 14)
        if self.virtual and level in (1, 2):
            self.headings_pages.append((level, strip_emoji(text), self.page))
        if not self.virtual:
            cv = self.cv
            if level == 1:
                box_h = h + 18
                cv.setFillColor(HexColor(color))
                cv.roundRect(MARGIN - 8, self.y - box_h + 4,
                             self.avail + 16, box_h, 7, stroke=0, fill=1)
                cv.setFillColor(HexColor(bar_color))
                cv.rect(MARGIN - 8, self.y - box_h + 4 - 3,
                        self.avail + 16, 3, stroke=0, fill=1)
                yy = self.y - 13
            else:
                if bar:
                    cv.setFillColor(HexColor(color))
                    cv.rect(MARGIN - 10, self.y - size + 4, 4, size + 6,
                            stroke=0, fill=1)
                yy = self.y
            for ln in lines:
                f.draw_line(cv, ln, MARGIN, yy, size,
                            "#ffffff" if level == 1 else color)
                yy -= self.lh(size)
            if dash:
                cv.setStrokeColor(HexColor(color))
                cv.setLineWidth(1.0)
                cv.setDash(4, 2)
                cv.line(MARGIN, yy + 4, PAGE_W - MARGIN, yy + 4)
                cv.setDash()
        self.y -= h + (20 if level == 1 else 14)

    def _paragraph(self, text, size=BODY, x=MARGIN, color=INK, max_w=None):
        text = text.replace("\\*", "*")
        max_w = max_w or (PAGE_W - MARGIN - x)
        f = self.f()
        lines = f.wrap_rich(text, size, max_w)
        if not lines:
            return
        h = len(lines) * self.lh(size)
        self.ensure(h + 3)
        if not self.virtual:
            yy = self.y
            for ln in lines:
                f.draw_line(self.cv, ln, x, yy, size, color)
                yy -= self.lh(size)
        self.y -= h + 3

    def _list(self, items):
        f = self.f()
        size = BODY
        for it in items:
            chk = it.startswith("[ ]")
            txt = ("•  " if chk else "•  ") + (it[3:].strip() if chk else it)
            lines = f.wrap_rich(txt, size, self.avail - 14)
            h = len(lines) * self.lh(size)
            self.ensure(h + 3)
            if not self.virtual:
                yy = self.y
                for ln in lines:
                    f.draw_line(self.cv, ln, MARGIN + 14, yy, size, INK)
                    yy -= self.lh(size)
            self.y -= h + 2

    # ---------------------------------------------------------- tables
    def _table(self, head, rows):
        size = 9.0
        pad = 5.0
        ncol = max(len(head), max((len(r) for r in rows), default=0))
        if ncol == 0:
            return
        head = head + [""] * (ncol - len(head))
        rows = [r + [""] * (ncol - len(r)) for r in rows]
        allr = [head] + rows
        nat = []
        for ci in range(ncol):
            mx = max(len(strip_emoji(r[ci] or "")) for r in allr)
            nat.append(max(34.0, mx * size * 0.60 + 2 * pad))
        tot = sum(nat)
        if tot > self.avail:
            nat = [max(28.0, w * self.avail / tot) for w in nat]
        widths = nat
        # wrap every cell
        f = self.f()
        cells = []
        for r in allr:
            cells.append([f.wrap_plain(strip_emoji(r[ci] or "").replace("**", ""),
                                       size, widths[ci] - 2 * pad)
                          for ci in range(ncol)])
        row_h = [max(12.0, max((len(c[ci]) for ci in range(ncol)), default=1)
                     * self.lh(size) + 2 * pad + 2) for c in cells]
        total = sum(row_h)
        # chunk across pages (header repeats on each chunk)
        i, first = 0, True
        while i < len(cells):
            avail_h = self.y - 62
            take, used = 0, 0.0
            for j in range(i, len(row_h)):
                if used > 0 and used + row_h[j] > avail_h:
                    break
                used += row_h[j]
                take += 1
                if used >= avail_h:
                    break
            take = max(take, 1)
            chunk = cells[i:i + take]
            self._table_chunk(head, chunk, widths, row_h[i:i + take],
                              size, pad, first)
            i += take
            first = False
            if i < len(cells):
                self._break()

    def _table_chunk(self, head, cells, widths, row_h, size, pad, draw_head):
        x0, top = MARGIN, self.y
        total_w = sum(widths)
        yy = top
        f = self.f()
        if not self.virtual:
            cv = self.cv
            rows_to_draw = cells if draw_head else cells
            start = 0 if draw_head else 0
            # background + text for each row
            for ri, ws in enumerate(cells):
                rh = row_h[ri]
                if ri == 0 and draw_head:
                    cv.setFillColor(HexColor(BLUE))
                    cv.rect(x0, yy - rh, total_w, rh, stroke=0, fill=1)
                elif ri % 2 == 1:
                    cv.setFillColor(HexColor("#f6f9ff"))
                    cv.rect(x0, yy - rh, total_w, rh, stroke=0, fill=1)
                cx = x0
                for ci, ln in enumerate(ws):
                    ty = yy - pad - size
                    for l in ln:
                        col = "#ffffff" if (ri == 0 and draw_head) else INK
                        f.draw_line(cv, l, cx + pad, ty, size, col)
                        ty -= self.lh(size)
                    cx += widths[ci]
                yy -= rh
            # grid lines
            cv.setStrokeColor(HexColor("#c9d6ea"))
            cv.setLineWidth(0.5)
            cx = x0
            for w in widths:
                cv.line(cx, yy, cx, top)
                cx += w
            cv.line(cx, yy, cx, top)
            yy2 = top
            for k, rh in enumerate(row_h):
                cv.line(x0, yy2 - rh, x0 + total_w, yy2 - rh)
                yy2 -= rh
        self.y = yy - 6

    # --------------------------------------------------------- quotes
    def _quote(self, lines):
        joined = "\n".join(lines)
        style = first_style(lines[0].strip()) if lines else None
        col, bg = STYLE_COLORS.get(style or "amber")
        paras, cur = [], []
        for l in lines:
            l = strip_emoji(re.sub(r"^\s*>\s?", "", l))
            if not l.strip():
                if cur:
                    paras.append(" ".join(cur))
                    cur = []
                continue
            cur.append(l.strip())
        if cur:
            paras.append(" ".join(cur))
        if not paras:
            return
        f = self.f()
        size = BODY - 0.4
        max_w = self.avail - 18
        out = []
        for p in paras:
            out.extend(f.wrap_rich(p, size, max_w))
        if not out:
            return
        box_h = len(out) * self.lh(size) + 14
        self.ensure(box_h + 5)
        if not self.virtual:
            cv = self.cv
            cv.setFillColor(HexColor(bg))
            cv.roundRect(MARGIN - 4, self.y - box_h + 3, self.avail + 8, box_h,
                         5, stroke=0, fill=1)
            cv.setFillColor(HexColor(col))
            cv.rect(MARGIN - 4, self.y - box_h + 3, 4.5, box_h, stroke=0, fill=1)
            yy = self.y - 9
            for ln in out:
                f.draw_line(cv, ln, MARGIN + 10, yy, size, INK)
                yy -= self.lh(size)
        self.y -= box_h + 5

    # -------------------------------------------------------- callouts
    def _callout(self, label, col, body):
        f = self.f()
        size = BODY - 0.4
        max_w = self.avail - 18
        out = []
        for p in re.split(r"\n\s*\n", body):
            p = strip_emoji(p)
            if p:
                out.extend(f.wrap_rich(p, size, max_w))
        if not out:
            return
        lf = self.f(True)
        ll = lf.wrap_rich(label, 9.8, max_w)
        head_h = 0 if not label else (len(ll) * self.lh(9.8) + 6)
        body_h = len(out) * self.lh(size)
        box_h = head_h + body_h + 14
        self.ensure(box_h + 5)
        if not self.virtual:
            cv = self.cv
            cc, bg = STYLE_COLORS[col]
            cv.setFillColor(HexColor(bg))
            cv.roundRect(MARGIN - 4, self.y - box_h + 3, self.avail + 8, box_h,
                         5, stroke=0, fill=1)
            cv.setStrokeColor(HexColor(cc))
            cv.setLineWidth(1.1)
            cv.roundRect(MARGIN - 4, self.y - box_h + 3, self.avail + 8, box_h,
                         5, stroke=1, fill=0)
            yy = self.y - 8
            if label:
                for ln in ll:
                    lf.draw_line(cv, ln, MARGIN + 8, yy, 9.8, cc)
                    yy -= self.lh(9.8)
                yy -= 1
            for ln in out:
                f.draw_line(cv, ln, MARGIN + 8, yy, size, INK)
                yy -= self.lh(size)
        self.y -= box_h + 5

    # ------------------------------------------------------------ code
    def _code(self, lines):
        f = self.f()
        size = 8.8
        max_w = self.avail - 16
        out = []
        for l in lines:
            o = f.wrap_rich(strip_emoji(l) or " ", size, max_w)
            if not o:
                o = [[(" ", False, False)]]
            out.extend(o)
        if not out:
            return
        box_h = len(out) * self.lh(size) + 12
        self.ensure(box_h + 4)
        if not self.virtual:
            cv = self.cv
            cv.setFillColor(HexColor("#f5faf5"))
            cv.roundRect(MARGIN - 4, self.y - box_h + 3, self.avail + 8, box_h,
                         4, stroke=0, fill=1)
            cv.setStrokeColor(HexColor("#b9dcbb"))
            cv.setLineWidth(0.8)
            cv.setDash(3, 2)
            cv.roundRect(MARGIN - 4, self.y - box_h + 3, self.avail + 8, box_h,
                         4, stroke=1, fill=0)
            cv.setDash()
            yy = self.y - 8
            for ln in out:
                f.draw_line(cv, ln, MARGIN + 6, yy, size, "#2c5233")
                yy -= self.lh(size)
        self.y -= box_h + 4

    # ------------------------------------------------------------- toc
    def _draw_toc(self, entries):
        f = self.f(True)
        title = "विषय-सूची  ·  Table of Contents"
        tsize = 15.0
        self.ensure(60)
        if not self.virtual:
            cv = self.cv
            cv.setFillColor(HexColor(BLUE))
            cv.roundRect(MARGIN - 6, self.y - tsize - 10, self.avail + 12,
                         tsize + 22, 6, stroke=0, fill=1)
            f.draw_line(cv, title, MARGIN, self.y - 6, tsize, "#ffffff")
        self.y -= tsize + 30
        f2 = self.f()
        n = 0
        for lv, tx, pg in entries:
            if lv == 1:
                if n > 0:
                    self.ensure(10)
                    self.y -= 6
                text, sz, bold = tx, 11.6, True
                col = INK_BOLD
            else:
                text, sz, bold = f"       {tx}", 10.2, False
                col = SOFT
            ff = f if bold else f2
            lines = ff.wrap_rich(text, sz, self.avail - 64)
            h = len(lines) * self.lh(sz)
            self.ensure(h + 3)
            if not self.virtual:
                yy = self.y
                for ln in lines:
                    ff.draw_line(self.cv, ln, MARGIN, yy, sz, col)
                    yy -= self.lh(sz)
                ps = str(pg)
                pw = f2.width(ps, sz)
                f2.draw_text(self.cv, ps, PAGE_W - MARGIN - pw, self.y - 2, sz,
                             SOFT)
            self.y -= h + 3
            n += 1

    # ------------------------------------------------------------ cover
    def _draw_cover(self):
        cv = self.cv
        W, H = PAGE_W, PAGE_H
        # soft gradient bands
        cv.setFillColor(HexColor("#f4f9ff"))
        cv.rect(0, H - 260, W, 260, stroke=0, fill=1)
        cv.setFillColor(HexColor("#fff6e8"))
        cv.rect(0, 0, W, 120, stroke=0, fill=1)
        cv.setStrokeColor(HexColor(BLUE))
        cv.setLineWidth(3)
        cv.line(60, H - 260, W - 60, H - 260)
        cv.setFillColor(HexColor(BLUE))
        cv.circle(W / 2, H - 320, 44, stroke=0, fill=1)
        f = self.f(True)
        f.draw_text(cv, "IT", W / 2 - f.width("IT", 30) / 2, H - 338, 30,
                    "#ffffff")
        # title
        tsize = 26.0
        lines = f.wrap_rich(self.title, tsize, W - 160)
        yy = H - 420
        for ln in lines:
            w = sum(self.f(True).width(x, tsize) for x, _, _ in ln) + \
                self.f(True).width(" ", tsize) * (len(ln) - 1)
            f.draw_line(cv, ln, (W - w) / 2, yy, tsize, "#14263f")
            yy -= self.lh(tsize)
        f2 = self.f()
        if self.subtitle:
            t2 = self.subtitle
            w2 = f2.width(t2, 12.5)
            f2.draw_text(cv, t2, (W - w2) / 2, yy - 8, 12.5, SOFT)
        # badge
        if self.badge:
            bw = f2.width(self.badge, 10.5) + 40
            bx = (W - bw) / 2
            cv.setStrokeColor(HexColor(GREEN))
            cv.setLineWidth(1.4)
            cv.setDash(4, 3)
            cv.roundRect(bx, yy - 66, bw, 26, 5, stroke=1, fill=0)
            cv.setDash()
            f2.draw_text(cv, self.badge, (W - f2.width(self.badge, 10.5)) / 2,
                         yy - 50, 10.5, GREEN)
        # bottom meta
        f3 = self.f()
        meta = "UP SUPER TET 2026  ·  Primary Level (कक्षा 1–5)  ·  सूचना तकनीकी"
        wm = f3.width(meta, 10.5)
        f3.draw_text(cv, meta, (W - wm) / 2, 70, 10.5, SOFT)


# ==================================================================== main
def main():
    ap = argparse.ArgumentParser(description="Markdown -> PDF (HarfBuzz)")
    ap.add_argument("files", nargs="+")
    ap.add_argument("-o", "--output")
    ap.add_argument("--title", default=None)
    ap.add_argument("--subtitle", default="")
    ap.add_argument("--badge", default="")
    ap.add_argument("--toc", action="store_true", default=None)
    ap.add_argument("--no-toc", action="store_true")
    ap.add_argument("--no-cover", action="store_true")
    a = ap.parse_args()

    files = []
    for f_ in a.files:
        p = Path(f_)
        if p.is_dir():
            files += sorted(p.glob("*.md"))
        elif p.exists():
            files.append(p)
        else:
            sys.exit(f"not found: {f_}")
    if not files:
        sys.exit("no markdown files given")

    md = "\n".join(x.read_text(encoding="utf-8") for x in files)
    blocks = md_to_blocks(md)
    multi = len(files) > 1
    toc = a.toc if a.toc is not None else multi
    if a.no_toc:
        toc = False
    out = a.output or files[0].with_suffix(".pdf").name
    title = a.title or files[0].stem.replace("-", " ").title()
    doc = PdfDoc(out, title, a.subtitle, a.badge,
                 cover=not a.no_cover, toc=toc)
    doc.build(blocks)
    print(f"OK -> {out} ({os.path.getsize(out)} bytes, {doc.page} pages)")


if __name__ == "__main__":
    main()
