#!/usr/bin/env python3
"""
pet-notes-md2pdf.py — PET revision-note Markdown -> styled PDF.

PET-specific wrapper around the common StudyHub Point Markdown/SVG pipeline.
The Markdown content should use the fixed PET note grammar documented in
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
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import md2pdf as pipeline

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
"""

# Fixed PET heading classification. Order matters: specific data-analysis and
# subject terms are checked before generic terms.
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
    """Convert PET semantic boxes to stable HTML before Markdown parsing.

    We intentionally use a separate `::: type` grammar rather than relying on
    raw HTML in every note, so authors can focus on content while the renderer
    owns all colours, borders, spacing and typography.
    """
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


def render_markdown(md):
    # Reuse the common renderer's SVG/icon/figure preprocessing exactly.
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
        # Keep a clear failure rather than silently producing an unstyled PDF.
        raise
    rendered = pipeline.colour_blockquotes(rendered)
    rendered = pipeline.convert_tasks(rendered)
    rendered = decorate_headings(rendered)
    return rendered


def build_document(markdown_text, title, subtitle="", badge="PET"):
    body = render_markdown(markdown_text)
    today = __import__("datetime").date.today().strftime("%d %B %Y")
    cover = f'''<section class="pet-cover"><div style="text-align:center;padding-top:45mm;">
      <div style="font-size:12pt;font-weight:800;letter-spacing:.12em;">STUDYHUB POINT</div>
      <h1 style="font-size:30pt;margin:8mm 0 4mm;">{html.escape(title)}</h1>
      <div style="font-size:15pt;">{html.escape(subtitle)}</div>
      <div style="margin-top:12mm;font-size:12pt;font-weight:700;">{html.escape(badge)}</div>
      <div style="margin-top:8mm;font-size:9pt;">Updated: {today}</div>
    </div></section>'''
    return cover + '<main class="pet-document">' + body + '</main>'


def main(argv=None):
    p = argparse.ArgumentParser(description="PET Markdown notes to styled PDF")
    p.add_argument("input", help="Markdown file")
    p.add_argument("-o", "--output", required=True, help="Output PDF")
    p.add_argument("--title", default="UPSSSC PET Notes")
    p.add_argument("--subtitle", default="Complete Syllabus & Revision Notes")
    p.add_argument("--badge", default="PET 2026")
    args = p.parse_args(argv)

    src = Path(args.input)
    out = Path(args.output)
    if not src.exists():
        p.error(f"Input not found: {src}")
    if not pipeline.WEASYPRINT_AVAILABLE:
        p.error("WeasyPrint is required for PET PDF rendering")

    text = src.read_text(encoding="utf-8")
    document = build_document(text, args.title, args.subtitle, args.badge)

    # Reuse the common style.css and font configuration from the existing
    # renderer. PET_CSS is layered last so PET owns the semantic theme.
    base_css = pipeline.CSS_FILE.read_text(encoding="utf-8") if pipeline.CSS_FILE.exists() else ""
    css = base_css + "\n" + PET_CSS
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
    font_config = FontConfiguration()
    out.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=f'<body class="pet-document">{document}</body>', base_url=str(src.parent.resolve())).write_pdf(
        str(out), stylesheets=[CSS(string=css)], font_config=font_config
    )
    print(f"✓ PET PDF: {out}")


if __name__ == "__main__":
    main()
