#!/usr/bin/env python3
"""
pet-notes-md2pdf.py — PET revision-note Markdown -> styled PDF.

PET-specific wrapper around the common StudyHub Point Markdown/SVG pipeline.
The Markdown content uses the fixed PET note grammar documented in
pet/00-PET-Notes-Style-Guide.md.

Supported semantic boxes:
  ::: concept        Core concept
  ::: trick          शॉर्टकट / याद रखने की trick
  ::: tip            परीक्षा टिप
  ::: warning        सावधानी / common mistake
  ::: example        उदाहरण
  ::: formula        सूत्र
  ::: remember       याद रखें
  ::: pyq            PYQ focus
  ::: practice       अभ्यास
  ::: fact           महत्वपूर्ण तथ्य
  :::

Figures and icons remain compatible with md2pdf.py:
  :icon-name:
  ```figure
  type: ...
  caption: ...
  ```
"""

import argparse
import html
import os
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import md2pdf as pipeline  # noqa: E402

try:
    from watermark import auto_watermark_pdf
except Exception:
    auto_watermark_pdf = None

# ---------------------------------------------------------------------------
# Branding & Social Links
SOCIAL_LINKS = [
    {
        "platform": "Instagram",
        "handle": "@studyhub.point",
        "url": "https://www.instagram.com/studyhub.point/",
        "cls": "instagram",
        "icon": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#E1306C" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>',
    },
    {
        "platform": "YouTube",
        "handle": "@studyhub.points",
        "url": "https://www.youtube.com/@studyhub.points",
        "cls": "youtube",
        "icon": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#FF0000" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22.54 6.42a2.78 2.78 0 0 0-1.94-2C18.88 4 12 4 12 4s-6.88 0-8.6.46a2.78 2.78 0 0 0-1.94 2A29 29 0 0 0 1 11.75a29 29 0 0 0 .46 5.33A2.78 2.78 0 0 0 3.4 19c1.72.46 8.6.46 8.6.46s6.88 0 8.6-.46a2.78 2.78 0 0 0 1.94-2 29 29 0 0 0 .46-5.25 29 29 0 0 0-.46-5.33z"></path><polygon points="9.75 15.02 15.5 11.75 9.75 8.48 9.75 15.02" fill="#FF0000"></polygon></svg>',
    },
    {
        "platform": "Telegram",
        "handle": "studyhub_point",
        "url": "https://t.me/studyhub_point",
        "cls": "telegram",
        "icon": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#0088cc" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>',
    },
    {
        "platform": "Website",
        "handle": "studyhubpoint",
        "url": "https://studyhubpoint.anshulyadav.net/",
        "cls": "website",
        "icon": '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="#127a4d" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>',
    },
]

# ---------------------------------------------------------------------------
# PET semantic theme
PET_CSS = r"""
/* ================================================================
   STUDYHUB POINT — PET NOTES PRINT THEME
   Restrained ink-friendly colour system; semantic colour, not decoration.
   ================================================================ */
body.pet-document {
  background:#fffdf8;
  color:#20242b;
}

body.pet-document .pet-cover {
  page-break-after:always;
}

body.pet-document h1.pet-heading {
  margin-top:7mm;
  padding:4mm 5mm;
  border-radius:3mm;
  border-left:7pt solid #1769aa;
  background:#eef6ff;
  color:#12385a;
  box-shadow:0 .8mm 0 rgba(23,105,170,.12);
}
body.pet-document h2.pet-heading {
  margin-top:5mm;
  padding:2.8mm 3.5mm;
  border:1pt solid #d4dbe4;
  border-left:5pt solid #1769aa;
  border-radius:2mm;
  background:#f7faff;
  color:#18324b;
}
body.pet-document h3.pet-heading {
  margin-top:3.5mm;
  padding:2mm 3mm;
  border-left:4pt solid #0b7377;
  border-bottom:1pt solid #d4e5e5;
  background:#f3fbfb;
  border-radius:0 1.5mm 1.5mm 0;
}
body.pet-document h4.pet-heading {
  padding:1.5mm 2.5mm;
  border-left:3pt solid #9a6500;
  background:#fff9ec;
  border-radius:0 1.5mm 1.5mm 0;
}

/* Subject colour accents */
body.pet-document .pet-history { border-left-color:#9a3d22 !important; background:#fff6f2 !important; }
body.pet-document .pet-movement { border-left-color:#a04424 !important; background:#fff6f2 !important; }
body.pet-document .pet-geography { border-left-color:#28704b !important; background:#f2faf5 !important; }
body.pet-document .pet-economy { border-left-color:#806000 !important; background:#fffaf0 !important; }
body.pet-document .pet-polity { border-left-color:#555aa6 !important; background:#f5f5ff !important; }
body.pet-document .pet-science { border-left-color:#9d3340 !important; background:#fff5f6 !important; }
body.pet-document .pet-maths { border-left-color:#1769aa !important; background:#eef6ff !important; }
body.pet-document .pet-hindi { border-left-color:#a33a75 !important; background:#fff5fb !important; }
body.pet-document .pet-english { border-left-color:#5c5f91 !important; background:#f6f6ff !important; }
body.pet-document .pet-reasoning { border-left-color:#6951a0 !important; background:#f7f3ff !important; }
body.pet-document .pet-current { border-left-color:#bd3e2d !important; background:#fff5f2 !important; }
body.pet-document .pet-awareness { border-left-color:#087a73 !important; background:#f1fbfa !important; }
body.pet-document .pet-passage { border-left-color:#3d6d9c !important; background:#f3f8fd !important; }
body.pet-document .pet-graph,
body.pet-document .pet-table { border-left-color:#1769aa !important; background:#eef6ff !important; }

/* Semantic note boxes */
body.pet-document .pet-box {
  margin:3.5mm 0;
  padding:3.2mm 4mm;
  border:1pt solid #cfd6de;
  border-left:5pt solid #64748b;
  border-radius:2.2mm;
  page-break-inside:avoid;
  box-shadow:0 .6mm 0 rgba(30,41,59,.035);
}
body.pet-document .pet-box .pet-box-title {
  margin:0 0 1.5mm;
  font-weight:800;
  font-size:10.5pt;
}
body.pet-document .pet-concept { border-left-color:#1769aa; background:#f1f7fd; }
body.pet-document .pet-trick { border-left-color:#a45c00; background:#fff7e8; }
body.pet-document .pet-tip { border-left-color:#0b7377; background:#effafa; }
body.pet-document .pet-warning { border-left-color:#b52e3c; background:#fff1f2; }
body.pet-document .pet-example { border-left-color:#5667a8; background:#f4f5ff; }
body.pet-document .pet-formula { border-left-color:#1769aa; background:#edf5ff; }
body.pet-document .pet-remember { border-left-color:#157347; background:#effaf3; }
body.pet-document .pet-pyq { border-left-color:#7a4e9e; background:#f8f2fc; }
body.pet-document .pet-practice { border-left-color:#236a8b; background:#f0f8fb; }
body.pet-document .pet-fact { border-left-color:#8a6100; background:#fff9ed; }

body.pet-document table {
  page-break-inside:avoid;
}
body.pet-document .pet-subject-index {
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:2.5mm;
}
body.pet-document .pet-chip {
  display:block;
  padding:2mm 3mm;
  border:1pt solid #d4dbe4;
  border-radius:2mm;
  background:#fff;
  font-weight:700;
}

/* Print-safe callout titles */
body.pet-document .callout > .callout-title {
  border-bottom:1pt dashed currentColor;
  padding-bottom:1mm;
}

/* Cover & Back cover styling */
.pet-cover {
  page-break-before:avoid;
  page-break-after:always;
  min-height:92vh;
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  text-align:center;
  padding:15mm 10mm;
  box-sizing:border-box;
}
.pet-cover .kicker {
  font-size:11pt;
  font-weight:800;
  letter-spacing:.12em;
  color:#1769aa;
  text-transform:uppercase;
  margin-bottom:4mm;
}
.pet-cover h1 {
  font-size:26pt;
  line-height:1.2;
  color:#12385a;
  margin:2mm 0 4mm;
}
.pet-cover .rule {
  width:32mm;
  height:3pt;
  background:#1769aa;
  margin:3mm auto 5mm;
  border-radius:2pt;
}
.pet-cover .sub {
  font-size:14pt;
  color:#4b5563;
  margin-bottom:6mm;
}
.pet-cover .meta {
  font-size:10pt;
  color:#6b7280;
  margin-bottom:6mm;
}
.pet-cover .badge {
  display:inline-block;
  background:#eef6ff;
  color:#1769aa;
  border:1pt solid #1769aa;
  padding:2mm 5mm;
  border-radius:3mm;
  font-weight:700;
  font-size:11pt;
  margin-bottom:8mm;
}
.pet-cover .cover-social {
  display:flex;
  flex-wrap:wrap;
  justify-content:center;
  gap:2.5mm;
  margin-top:6mm;
}
.pet-cover .social-pill {
  display:inline-flex;
  align-items:center;
  gap:1.5mm;
  padding:1.5mm 3.5mm;
  border:1pt solid #d1d5db;
  border-radius:20mm;
  background:#ffffff;
  color:#374151;
  font-size:8.5pt;
  font-weight:600;
  text-decoration:none;
}

.pet-back-cover {
  page-break-before:always;
  min-height:85vh;
  display:flex;
  flex-direction:column;
  justify-content:center;
  align-items:center;
  padding:15mm 10mm;
  box-sizing:border-box;
}
.pet-back-cover .bc-card {
  width:100%;
  max-width:160mm;
  border:1.5pt solid #d4dbe4;
  border-radius:4mm;
  padding:8mm 8mm;
  background:#ffffff;
  box-shadow:0 1.5mm 0 rgba(0,0,0,.04);
  text-align:center;
}
.pet-back-cover .bc-logo {
  font-size:18pt;
  font-weight:800;
  color:#12385a;
  letter-spacing:.05em;
}
.pet-back-cover .bc-tagline {
  font-size:10pt;
  color:#4b5563;
  margin:2mm 0 4mm;
}
.pet-back-cover .bc-rule {
  width:25mm;
  height:2pt;
  background:#1769aa;
  margin:2mm auto 4mm;
  border-radius:1pt;
}
.pet-back-cover .bc-heading {
  font-size:11pt;
  font-weight:700;
  color:#1f2937;
  margin-bottom:4mm;
}
.pet-back-cover .bc-grid {
  display:grid;
  grid-template-columns:1fr 1fr;
  gap:2.5mm;
  margin:3mm 0 5mm;
}
.pet-back-cover .bc-item {
  display:flex;
  align-items:center;
  gap:2.5mm;
  padding:2mm 3mm;
  border:1pt solid #e5e7eb;
  border-radius:2mm;
  background:#f9fafb;
  text-decoration:none;
  color:#1f2937;
  text-align:left;
}
.pet-back-cover .bc-platform { font-size:9.5pt;font-weight:700;line-height:1.2; }
.pet-back-cover .bc-handle { font-size:8pt;color:#4b5563;line-height:1.3; }
.pet-back-cover .bc-footer {
  display:flex;justify-content:center;gap:3mm;margin-top:5mm;
  color:#6b7280;font-size:8.5pt;
}
"""

PET_RULES = [
    ("pet-history", ("भारतीय इतिहास", "History")),
    ("pet-movement", ("राष्ट्रीय आंदोलन", "National Movement")),
    ("pet-geography", ("भूगोल", "Geography")),
    ("pet-economy", ("भारतीय अर्थव्यवस्था", "Indian Economy")),
    ("pet-polity", ("संविधान", "लोक प्रशासन", "Indian Constitution", "Public Administration")),
    ("pet-science", ("सामान्य विज्ञान", "General Science")),
    ("pet-maths", ("प्रारम्भिक अंकगणित", "Arithmetic")),
    ("pet-hindi", ("सामान्य हिन्दी", "Hindi")),
    ("pet-english", ("General English", "English")),
    ("pet-reasoning", ("तर्क एवं तर्कशक्ति", "Reasoning")),
    ("pet-current", ("सामयिकी", "Current Affairs")),
    ("pet-awareness", ("सामान्य जागरूकता", "General Awareness")),
    ("pet-passage", ("अपठित हिन्दी गद्यांश", "Hindi Passage")),
    ("pet-graph", ("ग्राफ", "Graph")),
    ("pet-table", ("तालिका", "Table")),
]

HEADING_RE = re.compile(r"<h([1-4])([^>]*)>(.*?)</h\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def clean_heading(text):
    return html.unescape(TAG_RE.sub("", text)).strip()


def heading_class(title):
    low = title.casefold()
    for cls, keys in PET_RULES:
        if any(k.casefold() in low for k in keys):
            return cls
    return "pet-general"


def add_class(attrs, cls):
    m = re.search(r'\bclass="([^"]*)"', attrs)
    if m:
        return attrs[:m.start(1)] + m.group(1) + " " + cls + attrs[m.end(1):]
    return attrs + f' class="{cls}"'


def decorate_headings(h):
    def repl(m):
        level, attrs, inner = m.groups()
        cls = "pet-heading " + heading_class(clean_heading(inner))
        return f"<h{level}{add_class(attrs, cls)}>{inner}</h{level}>"
    return HEADING_RE.sub(repl, h)


def convert_pet_boxes(md):
    """Convert PET semantic boxes to stable HTML before Markdown parsing."""
    allowed = {
        "concept": "Core Concept",
        "trick": "⚡ Trick",
        "tip": "💡 Exam Tip",
        "warning": "⚠ Warning",
        "example": "Example",
        "formula": "Formula",
        "remember": "🔑 Remember",
        "pyq": "PYQ Focus",
        "practice": "Practice",
        "fact": "Important Fact",
    }
    lines = md.splitlines()
    out = []
    stack = None
    title = None
    body = []
    for line in lines:
        m = re.match(r"^:::\s*(\w+)(?:\s+(.*))?$", line.strip())
        if m and stack is None and m.group(1).lower() in allowed:
            stack = m.group(1).lower()
            title = m.group(2).strip() if m.group(2) else allowed[stack]
            body = []
            continue
        if line.strip() == ":::" and stack is not None:
            safe_title = html.escape(title)
            safe_body = "\n".join(body)
            out.append(f'<div class="pet-box pet-{stack}"><p class="pet-box-title">{safe_title}</p>\n{safe_body}\n</div>')
            stack = None
            title = None
            body = []
            continue
        if stack is not None:
            body.append(line)
        else:
            out.append(line)
    if stack is not None:
        safe_title = html.escape(title)
        out.append(f'<div class="pet-box pet-{stack}"><p class="pet-box-title">{safe_title}</p>\n' + "\n".join(body) + "\n</div>")
    return "\n".join(out)


def render_markdown(md, prefix=""):
    md = convert_pet_boxes(md)
    md = pipeline.convert_icons(md)
    md = pipeline.convert_figures(md)
    md = pipeline.split_adjacent_blockquotes(md)
    try:
        import markdown
        rendered = markdown.markdown(
            md,
            extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
            output_format="html5",
        )
    except Exception:
        raise
    rendered = pipeline.colour_blockquotes(rendered)
    rendered = pipeline.convert_tasks(rendered)
    rendered = decorate_headings(rendered)
    if prefix:
        rendered = pipeline.prefix_ids(rendered, prefix)
    return rendered


def social_pills():
    return "".join(
        f'<a href="{s["url"]}" target="_blank" class="social-pill {s["cls"]}">'
        f'{s["icon"]}<span>{html.escape(s["platform"])} · {html.escape(s["handle"])}</span></a>'
        for s in SOCIAL_LINKS
    )


def build_cover(title, subtitle, meta, badge="PET 2026"):
    meta_html = "".join(f"<div>{html.escape(x)}</div>" for x in meta if x)
    return f"""<section class="cover pet-cover">
  <div class="kicker">Study Notes · UPSSSC PET 2026</div>
  <h1>{html.escape(title)}</h1>
  <div class="rule"></div>
  {f'<div class="sub">{html.escape(subtitle)}</div>' if subtitle else ''}
  <div class="meta">{meta_html}</div>
  {f'<div class="badge">{html.escape(badge)}</div>' if badge else ''}
  <div class="cover-social">{social_pills()}</div>
</section>"""


def build_back_cover():
    cards = "".join(
        f'''<a href="{s["url"]}" target="_blank" class="bc-item {s["cls"]}">
          <div class="bc-icon">{s["icon"]}</div>
          <div class="bc-text">
            <span class="bc-platform">{html.escape(s["platform"])}</span>
            <span class="bc-handle">{html.escape(s["handle"])}</span>
          </div>
        </a>'''
        for s in SOCIAL_LINKS
    )
    return f"""<section class="pet-back-cover">
  <div class="bc-card">
    <div class="bc-logo">StudyHub Point</div>
    <div class="bc-tagline">आपकी सफलता, हमारा संकल्प · Best Wishes for Your UPSSSC PET Preparation!</div>
    <div class="bc-rule"></div>
    <div class="bc-heading">हमारे साथ जुड़ें / Connect with Us</div>
    <div class="bc-grid">{cards}</div>
    <div class="bc-footer">
      <span>📚 UPSSSC PET Notes</span><span>•</span><span>🎯 Syllabus & PYQ-based Preparation</span>
    </div>
  </div>
</section>"""


def render_pet_pdf(files, output, title, subtitle="", author="", badge="PET 2026",
                   show_toc=True, show_cover=True, show_back_cover=True,
                   flow=False, extra_css=None, watermark=True,
                   watermark_scale=1.0, watermark_opacity=0.08):
    if not files:
        raise SystemExit("No Markdown files found.")

    pipeline._OPTS["qcols"] = False
    body = []
    for i, f in enumerate(files, 1):
        print(f"    - {f.name}")
        pfx = f"ch{i:02d}" if len(files) > 1 else ""
        body.append(render_markdown(f.read_text(encoding="utf-8"), prefix=pfx))
    content = "\n".join(body)

    parts = []
    if show_cover:
        meta = [author, f"{len(files)} अध्याय-फ़ाइल" if len(files) > 1 else "",
                date.today().strftime("%d %B %Y")]
        parts.append(build_cover(title, subtitle, meta, badge))

    if show_toc:
        t = pipeline.build_toc(content)
        if t:
            parts.append(t)

    parts.append(content)

    if show_back_cover:
        parts.append(build_back_cover())

    document = (
        f'<!DOCTYPE html><html lang="hi"><head><meta charset="utf-8">'
        f'<style>{PET_CSS}</style>'
        f'<title>{html.escape(title)}</title></head>'
        f'<body class="pet-document">{"".join(parts)}</body></html>'
    )

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    debug = output.with_suffix(".debug.html")
    debug.write_text(document, encoding="utf-8")

    print("  rendering PET notes PDF ...")
    rendered = False
    if getattr(pipeline, "WEASYPRINT_AVAILABLE", False):
        try:
            from weasyprint import HTML, CSS
            from weasyprint.text.fonts import FontConfiguration
            font_config = FontConfiguration()
            sheets = [
                CSS(filename=str(pipeline.CSS_FILE), font_config=font_config),
                CSS(string=PET_CSS, font_config=font_config),
            ]
            if flow:
                sheets.append(CSS(
                    string="h1{page-break-before:auto;margin-top:9mm;}"
                           "h1:first-of-type{margin-top:0;}",
                    font_config=font_config,
                ))
            if extra_css:
                sheets.append(CSS(filename=str(extra_css), font_config=font_config))

            HTML(string=document, base_url=str(pipeline.HERE)).write_pdf(
                str(output), stylesheets=sheets, font_config=font_config
            )
            rendered = True
        except Exception as err:
            print(f"  ! WeasyPrint failed ({err}), falling back to Headless Browser...")

    if not rendered:
        pipeline.render_pdf_with_browser(document, output, pipeline.CSS_FILE, extra_css=extra_css, flow=flow)

    debug.unlink(missing_ok=True)

    if watermark and auto_watermark_pdf is not None:
        auto_watermark_pdf(output, scale=watermark_scale, opacity=watermark_opacity)

    size_mb = output.stat().st_size / 1024 / 1024
    try:
        print(f"  ✔ {output}  ({size_mb:.2f} MB)")
    except UnicodeEncodeError:
        print(f"  [OK] {output}  ({size_mb:.2f} MB)")
    return output


def main():
    p = argparse.ArgumentParser(description="PET Markdown notes to styled PDF")
    p.add_argument("inputs", nargs="+", help="Markdown files and/or folders")
    p.add_argument("-o", "--output", help="Output PDF path")
    p.add_argument("--title")
    p.add_argument("--subtitle", default="")
    p.add_argument("--author", default="")
    p.add_argument("--badge", default="PET 2026")
    p.add_argument("--toc", action="store_true", help="include a contents page")
    p.add_argument("--no-toc", action="store_true")
    p.add_argument("--no-cover", action="store_true")
    p.add_argument("--no-back-cover", action="store_true")
    p.add_argument("--flow", action="store_true", help="allow sections to continue on the same page")
    p.add_argument("--css", help="optional additional CSS file")
    p.add_argument("--no-watermark", action="store_true", help="disable watermark on pages")
    p.add_argument("--watermark-scale", type=float, default=1.0, help="watermark scale relative to page width")
    p.add_argument("--watermark-opacity", type=float, default=0.08, help="watermark opacity (0.0 to 1.0)")
    args = p.parse_args()

    files = pipeline.collect(args.inputs)
    if not files:
        raise SystemExit("No Markdown files found.")

    title = args.title or files[0].stem.replace("-", " ").replace("_", " ")
    output = args.output or str(files[0].with_suffix(".pdf"))
    show_toc = args.toc or (len(files) > 1 and not args.no_toc)

    print(f"  reading {len(files)} file(s)")
    render_pet_pdf(
        files=files,
        output=output,
        title=title,
        subtitle=args.subtitle,
        author=args.author,
        badge=args.badge,
        show_toc=show_toc and not args.no_toc,
        show_cover=not args.no_cover,
        show_back_cover=not args.no_back_cover,
        flow=args.flow,
        extra_css=args.css,
        watermark=not args.no_watermark,
        watermark_scale=args.watermark_scale,
        watermark_opacity=args.watermark_opacity,
    )


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass
    main()
