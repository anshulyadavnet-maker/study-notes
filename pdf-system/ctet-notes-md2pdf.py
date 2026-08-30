#!/usr/bin/env python3
"""
ctet-notes-md2pdf.py — CTET revision-note Markdown ➜ styled PDF.

This renderer is intentionally separate from md2pdf.py and mcqmdtopdf.py.
It reuses the common Markdown, figure, math and font pipeline, but adds a
notes-first design:

* coloured Paper I / Paper II / Language section headings;
* clean theory, revision, warning and exam-tip boxes;
* a readable one-column layout for long explanations and tables;
* a branded cover and back cover with the StudyHub Point links used by the
  study material;
* automatic heading classification through SECTION_STYLES, so a new notes
  section can be given a colour by adding one entry here rather than changing
  the general PDF renderer.

Examples
  python3 pdf-system/ctet-notes-md2pdf.py \
      ctet-notes/00-CTET-Revision-Notes-Blueprint.md \
      -o PDF/CTET-Revision-Notes-Blueprint.pdf \
      --title "CTET Revision Notes" --subtitle "Hindi-medium exam revision" \
      --badge "CTET" --toc

  python3 pdf-system/ctet-notes-md2pdf.py ctet-notes/ -o PDF/CTET-REVISION-NOTES.pdf \
      --title "CTET Revision Notes" --toc --flow
"""

import argparse
import html
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import md2pdf as pipeline  # noqa: E402


# ---------------------------------------------------------------------------
# Branding: keep these links in one place so every notes PDF uses the same
# official study-material links.  Add a new platform here when one is launched.
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
# Notes section classifier.  This is the place to add a new notes section's
# keyword and colour class.  The generic fallback keeps new headings readable
# even before a dedicated entry is added.
SECTION_STYLES = {
    "paper-i": {
        "keywords": ("Paper I", "PART A", "PART 1", "Primary Stage"),
        "label": "Paper I · Primary Stage",
        "colour": "blue",
    },
    "paper-ii": {
        "keywords": ("Paper II", "PART B", "PART 2", "Elementary Stage"),
        "label": "Paper II · Elementary Stage",
        "colour": "purple",
    },
    "cdp": {
        "keywords": ("Child Development", "Development", "CDP"),
        "label": "Child Development & Pedagogy",
        "colour": "teal",
    },
    "learning": {
        "keywords": ("Learning", "अधिगम", "अधिगम और Pedagogy"),
        "label": "Learning & Pedagogy",
        "colour": "teal",
    },
    "inclusion": {
        "keywords": ("Inclusive Education", "Inclusion", "समावेशी शिक्षा"),
        "label": "Inclusive Education",
        "colour": "green",
    },
    "assessment": {
        "keywords": ("Assessment", "Evaluation", "मूल्यांकन"),
        "label": "Assessment & Evidence",
        "colour": "red",
    },
    "maths": {
        "keywords": (
            "Mathematics", "गणित", "Number System", "Integers", "Fractions",
            "Ratio", "Algebra", "Geometry", "Symmetry", "Construction",
            "Mensuration", "Data Handling", "Problem-Solving",
            "Activity-Based", "Nature of Mathematics", "Language of Mathematics",
        ),
        "label": "Mathematics",
        "colour": "blue",
    },
    "evs": {
        "keywords": ("Environmental Studies", "EVS", "पर्यावरण अध्ययन"),
        "label": "Environmental Studies",
        "colour": "green",
    },
    "science": {
        "keywords": (
            "Science", "विज्ञान", "Food", "Materials", "Living World",
            "Motion", "How Things Work", "Electric Current", "Magnets",
            "Light", "Natural Phenomena", "Natural Resources", "Inquiry",
            "Observation", "Experimentation", "Science Pedagogy",
        ),
        "label": "Science",
        "colour": "red",
    },
    "sst": {
        "keywords": ("Social Science", "Social Studies", "सामाजिक विज्ञान"),
        "label": "Social Studies / Social Science",
        "colour": "amber",
    },
    "language": {
        "keywords": ("Language", "भाषा", "Punjabi", "Hindi", "English"),
        "label": "Language",
        "colour": "pink",
    },
    "revision": {
        "keywords": ("Revision", "Revision Sheet", "Last-Minute", "Final"),
        "label": "Revision Focus",
        "colour": "green",
    },
}

HEADING_RE = re.compile(r"<h([1-4])([^>]*)>(.*?)</h\1>", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def clean_heading(text: str) -> str:
    return html.unescape(TAG_RE.sub("", text)).strip()


def section_key(title: str) -> str:
    lowered = title.casefold()

    def matches(keyword: str) -> bool:
        # Word boundaries prevent "Paper I" from matching "Paper II" and
        # prefer an exact phrase such as "Social Science" over "Science".
        pattern = rf"(?<!\\w){re.escape(keyword.casefold())}(?!\\w)"
        return re.search(pattern, lowered, flags=re.I) is not None

    # Longest keywords first: "Social Science" must win over the shorter
    # "Science" keyword, and "Paper II" must not be swallowed by "Paper I".
    rules = sorted(
        SECTION_STYLES.items(),
        key=lambda pair: max(map(len, pair[1]["keywords"])),
        reverse=True,
    )
    for key, rule in rules:
        if any(matches(keyword) for keyword in rule["keywords"]):
            return key
    return "general"


def add_class(attrs: str, classes: str) -> str:
    m = re.search(r'\bclass="([^"]*)"', attrs)
    if m:
        old = m.group(1)
        return attrs[:m.start(1)] + old + " " + classes + attrs[m.end(1):]
    return attrs + f' class="{classes}"'


def decorate_headings(rendered_html: str) -> str:
    """Add predictable classes to headings for notes-specific section styling."""
    def repl(match):
        level, attrs, inner = match.groups()
        title = clean_heading(inner)
        key = section_key(title)
        classes = f"note-heading note-{key}"
        attrs = add_class(attrs, classes)
        return f"<h{level}{attrs}>{inner}</h{level}>"
    return HEADING_RE.sub(repl, rendered_html)


NOTES_CSS = """
/* -------------------------------------------------------------------------
   CTET REVISION NOTES THEME
   The base study-note theme supplies fonts, tables, figures and normal
   callouts.  These local rules make the revision-note hierarchy more visible
   without changing md2pdf.py or the MCQ renderer.
   ------------------------------------------------------------------------- */
body.notes-document {
  background:#fffdf7;
}
body.notes-document h1.note-heading {
  letter-spacing:.01em;
  box-shadow:0 1.2mm 0 rgba(15,79,156,.10);
}
body.notes-document h2.note-heading {
  position:relative;
  padding:3.2mm 4mm 2.5mm;
  border:1.2pt solid #cbd5e1;
  border-left:5pt solid #6b3fa0;
  border-radius:2.2mm;
  background:#fafbff;
  box-shadow:0 .7mm 0 rgba(31,36,49,.04);
}
body.notes-document h3.note-heading {
  padding:2.2mm 3.4mm;
  border-left:4pt solid #0b6f78;
  border-bottom:1pt solid #cfe3e5;
  background:#f4fbfb;
  border-radius:0 1.8mm 1.8mm 0;
}
body.notes-document h4.note-heading {
  padding:1.6mm 2.5mm;
  border-left:3pt solid #a8620a;
  background:#fff9ed;
  border-radius:0 1.5mm 1.5mm 0;
}
/* Section colours are intentionally restrained for economical printing. */
body.notes-document h2.note-paper-i,
body.notes-document h2.note-maths { border-left-color:#1668c4; background:#f3f8ff; }
body.notes-document h2.note-paper-ii { border-left-color:#6b3fa0; background:#f8f4ff; }
body.notes-document h2.note-cdp { border-left-color:#0b6f78; background:#f1fbfb; }
body.notes-document h2.note-learning { border-left-color:#0b6f78; background:#f1fbfb; }
body.notes-document h2.note-inclusion { border-left-color:#127a4d; background:#f1fbf5; }
body.notes-document h2.note-assessment { border-left-color:#c02b3a; background:#fff5f5; }
body.notes-document h2.note-evs { border-left-color:#127a4d; background:#f1fbf5; }
body.notes-document h2.note-science { border-left-color:#c02b3a; background:#fff5f5; }
body.notes-document h2.note-sst { border-left-color:#a8620a; background:#fff9ed; }
body.notes-document h2.note-language { border-left-color:#b83280; background:#fff5fb; }
body.notes-document h2.note-revision { border-left-color:#127a4d; background:#f1fbf5; }

/* A thin section label can be added to future notes using a span with one of
   these classes. */
.note-section-label {
  display:inline-block;
  margin:1mm 0 1mm;
  padding:1mm 2.4mm;
  border-radius:10mm;
  font-size:8.2pt;
  font-weight:700;
  letter-spacing:.04em;
  text-transform:uppercase;
  color:#fff;
}
.note-section-label.blue{background:#1668c4;}
.note-section-label.purple{background:#6b3fa0;}
.note-section-label.teal{background:#0b6f78;}
.note-section-label.green{background:#127a4d;}
.note-section-label.red{background:#c02b3a;}
.note-section-label.amber{background:#a8620a;}
.note-section-label.pink{background:#b83280;}

/* Notes boxes: clear title bars and comfortable reading width. */
.notes-document .callout,
.notes-document blockquote {
  border-radius:2.2mm;
  box-shadow:0 .7mm 0 rgba(31,36,49,.035);
}
.notes-document .callout > .callout-title {
  padding-bottom:1.2mm;
  border-bottom:1pt dashed currentColor;
}
.notes-document .callout.info,
.notes-document blockquote.info { background:#eef7ff; }
.notes-document .callout.remember,
.notes-document blockquote.key { background:#eefaf3; }
.notes-document .callout.trick,
.notes-document blockquote.tip { background:#fff8e9; }
.notes-document .callout.trap,
.notes-document blockquote.warn { background:#fff0f1; }
.notes-document .callout.example,
.notes-document blockquote.star { background:#f8f1ff; }
.notes-document .callout.question { background:#fff1fa; }

.notes-document table {
  font-size:9.7pt;
  box-shadow:0 .8mm 0 rgba(31,36,49,.04);
}
.notes-document pre {
  background:#fbfdff;
  border:1.4pt solid #9cc4ed;
  border-left:4pt solid #1668c4;
}
.notes-document hr {
  border-top:1.5pt solid #c6d4e5;
  margin:7mm 0;
}
.notes-document .note-divider {
  height:0;
  border-top:1.2pt dashed #cbd5e1;
  margin:5mm 0;
}

/* Punjabi notes / bilingual material: use a Gurmukhi-capable system font when
   available; Devanagari notes keep the normal Playpen Sans Deva stack. */
body.punjabi-document {
  font-family:'Noto Sans Gurmukhi','Raavi','Nirmala UI','Lohit Punjabi','DejaVu Sans',sans-serif;
}

/* Cover and back-cover social links. */
.notes-cover .cover-social,
.notes-back-cover .cover-social {
  display:flex;flex-wrap:wrap;justify-content:center;gap:2.2mm;
  margin-top:9mm;
}
.notes-cover .social-pill,
.notes-back-cover .social-pill {
  display:inline-flex;align-items:center;gap:1.5mm;
  padding:2.1mm 3.4mm;border:1px solid #d8dfeb;border-radius:10mm;
  color:#243149;text-decoration:none;font-size:8.5pt;font-weight:600;
  background:#fff;line-height:1.2;
}
.notes-cover .social-pill svg,
.notes-back-cover .social-pill svg { flex:none;vertical-align:-.18em; }
.notes-cover .social-pill.instagram{border-color:#f5c2d1;color:#b8235a;background:#fff5f8;}
.notes-cover .social-pill.youtube{border-color:#fbc7c7;color:#cc0000;background:#fff5f5;}
.notes-cover .social-pill.telegram{border-color:#bfe1f6;color:#0077b5;background:#f2f9fe;}
.notes-cover .social-pill.website{border-color:#bce4cf;color:#0f6c44;background:#f2faf6;}

.notes-back-cover {
  page-break-before:always;
  min-height:235mm;
  display:flex;align-items:center;justify-content:center;
  padding:18mm 12mm;
  background:linear-gradient(145deg,#f4f8ff 0%,#fffdf7 52%,#f1fbf5 100%);
}
.notes-back-cover .bc-card {
  width:100%;max-width:170mm;text-align:center;
  padding:13mm 10mm 10mm;border:1.6pt solid #cbd5e1;
  border-radius:5mm;background:rgba(255,255,255,.92);
  box-shadow:0 3mm 10mm rgba(31,36,49,.08);
}
.notes-back-cover .bc-logo {
  font-size:25pt;font-weight:700;color:#1768bd;margin-bottom:4mm;
}
.notes-back-cover .bc-tagline { font-size:10.5pt;color:#4b5563;line-height:1.7; }
.notes-back-cover .bc-rule { width:38mm;height:3px;background:#f1ae3d;margin:7mm auto; }
.notes-back-cover .bc-heading { font-size:14pt;font-weight:700;color:#263449;margin-bottom:6mm; }
.notes-back-cover .bc-grid {
  display:grid;grid-template-columns:1fr 1fr;gap:3.5mm;text-align:left;
}
.notes-back-cover .bc-item {
  display:flex;align-items:center;gap:3mm;padding:3.2mm 3.4mm;
  border:1px solid #e2e8f0;border-radius:2.5mm;
  text-decoration:none;color:#1f2937;background:#fff;
}
.notes-back-cover .bc-item.instagram{border-color:#f7a8c4;background:#fff0f5;}
.notes-back-cover .bc-item.youtube{border-color:#fca5a5;background:#fff1f2;}
.notes-back-cover .bc-item.telegram{border-color:#93c5fd;background:#eff6ff;}
.notes-back-cover .bc-item.website{border-color:#86efac;background:#f0fdf4;}
.notes-back-cover .bc-icon { width:17mm;text-align:center; }
.notes-back-cover .bc-text { display:flex;flex-direction:column; }
.notes-back-cover .bc-platform { font-size:9.8pt;font-weight:700;line-height:1.2; }
.notes-back-cover .bc-handle { font-size:8pt;color:#4b5563;line-height:1.3; }
.notes-back-cover .bc-footer {
  display:flex;justify-content:center;gap:3mm;margin-top:7mm;
  color:#6b7280;font-size:8.5pt;
}
@media print {
  .notes-back-cover .bc-item { break-inside:avoid; }
}
"""


GURMUKHI_RE = re.compile(r"[\u0A00-\u0A7F]")


def social_pills():
    return "".join(
        f'<a href="{s["url"]}" target="_blank" class="social-pill {s["cls"]}">'
        f'{s["icon"]}<span>{html.escape(s["platform"])} · {html.escape(s["handle"])}</span></a>'
        for s in SOCIAL_LINKS
    )


def build_cover(title, subtitle, meta, badge):
    meta_html = "".join(f"<div>{html.escape(x)}</div>" for x in meta if x)
    return f"""<section class="cover notes-cover">
  <div class="kicker">Study Notes · CTET Revision</div>
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
    return f"""<section class="notes-back-cover">
  <div class="bc-card">
    <div class="bc-logo">StudyHub Point</div>
    <div class="bc-tagline">आपकी सफलता, हमारा संकल्प · Best Wishes for Your CTET Preparation!</div>
    <div class="bc-rule"></div>
    <div class="bc-heading">हमारे साथ जुड़ें / Connect with Us</div>
    <div class="bc-grid">{cards}</div>
    <div class="bc-footer">
      <span>📚 CTET Revision Notes</span><span>•</span><span>🎯 PYQ-based Preparation</span>
    </div>
  </div>
</section>"""


def render_notes_pdf(files, output, title, subtitle, author, badge,
                     show_toc=True, show_cover=True, show_back_cover=True,
                     flow=False, extra_css=None):
    if not files:
        raise SystemExit("No Markdown files found.")

    pipeline._OPTS["qcols"] = False
    rendered = []
    for f in files:
        print(f"    - {f.name}")
        rendered.append(pipeline.md_to_html(f.read_text(encoding="utf-8")))
    content = decorate_headings("\n".join(rendered))
    toc_html = pipeline.build_toc(content) if show_toc else ""

    is_punjabi = bool(GURMUKHI_RE.search(content))
    lang = "pa" if is_punjabi else "hi"
    body_class = " notes-document punjabi-document" if is_punjabi else " notes-document"

    parts = []
    if show_cover:
        meta = [author, f"{len(files)} notes file(s)", date.today().strftime("%d %B %Y")]
        parts.append(build_cover(title, subtitle, meta, badge))
    if toc_html:
        parts.append(toc_html)
    parts.append(content)
    if show_back_cover:
        parts.append(build_back_cover())

    document = (
        f'<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8">'
        f'<title>{html.escape(title)}</title></head><body class="{body_class.strip()}">'
        f'{"".join(parts)}</body></html>'
    )

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    debug = output.with_suffix(".debug.html")
    debug.write_text(document, encoding="utf-8")

    font_config = pipeline.FontConfiguration()
    sheets = [
        pipeline.CSS(filename=str(pipeline.CSS_FILE), font_config=font_config),
        pipeline.CSS(string=NOTES_CSS, font_config=font_config),
    ]
    if flow:
        sheets.append(pipeline.CSS(
            string="h1{page-break-before:auto;margin-top:9mm;}"
                   "h1:first-of-type{margin-top:0;}",
            font_config=font_config,
        ))
    if extra_css:
        sheets.append(pipeline.CSS(filename=str(extra_css), font_config=font_config))

    print("  rendering CTET revision-notes PDF ...")
    try:
        pipeline.HTML(string=document, base_url=str(pipeline.HERE)).write_pdf(
            str(output), stylesheets=sheets, font_config=font_config
        )
    finally:
        debug.unlink(missing_ok=True)

    size_mb = output.stat().st_size / 1024 / 1024
    print(f"  ✔ {output}  ({size_mb:.2f} MB)")
    return output


def main():
    parser = argparse.ArgumentParser(
        description="CTET revision-note Markdown -> styled PDF with social links"
    )
    parser.add_argument("inputs", nargs="+", help="Markdown files and/or folders")
    parser.add_argument("-o", "--output")
    parser.add_argument("--title")
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--author", default="")
    parser.add_argument("--badge", default="")
    parser.add_argument("--toc", action="store_true", help="include a contents page")
    parser.add_argument("--no-toc", action="store_true")
    parser.add_argument("--no-cover", action="store_true")
    parser.add_argument("--no-back-cover", action="store_true")
    parser.add_argument("--flow", action="store_true", help="allow sections to continue on the same page")
    parser.add_argument("--css", help="optional additional CSS file")
    args = parser.parse_args()

    files = pipeline.collect(args.inputs)
    if not files:
        raise SystemExit("No Markdown files found.")
    title = args.title or files[0].stem.replace("-", " ").replace("_", " ")
    output = args.output or str(files[0].with_suffix(".pdf"))
    show_toc = args.toc or (len(files) > 1 and not args.no_toc)

    print(f"  reading {len(files)} file(s)")
    render_notes_pdf(
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
    )


if __name__ == "__main__":
    main()
