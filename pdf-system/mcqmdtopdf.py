#!/usr/bin/env python3
"""
mcqmdtopdf.py — MCQ Markdown ➜ print-friendly PDF.

This is deliberately separate from md2pdf.py.  It reuses the common Markdown,
figure, cover and WeasyPrint pipeline, but adds a light horizontal divider before
each MCQ so questions remain visually separated in one- and two-column print.

Examples
  python3 pdf-system/mcqmdtopdf.py ctet-mcq/01-CDP-MCQ-Part-1.md \
      -o PDF/CTET-CDP-MCQ-Part-1.pdf --title "CTET CDP — Part 1" --toc

  python3 pdf-system/mcqmdtopdf.py \
      ctet-mcq/00-CTET-Detailed-Syllabus.md \
      ctet-mcq/01-CDP-MCQ-Part-1.md \
      ctet-mcq/01-CDP-MCQ-Part-2.md \
      -o PDF/CTET-CDP-COMPLETE.pdf --title "CTET CDP Complete" --toc
"""

import argparse
import html
import re
import sys
from datetime import date
from pathlib import Path

# md2pdf.py and its figlib package live beside this script.  Keeping the import
# here means this wrapper uses exactly the same Markdown/figure implementation
# as the normal study-note pipeline without changing that file.
HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import md2pdf as pipeline  # noqa: E402


QUESTION_START = re.compile(r"<p>\s*<strong>Q\d{1,3}\.?</strong>")

# Kept local to this MCQ-only wrapper so the ordinary chapter renderer is not
# changed.  A subtle solid rule is clearer on paper than a heavy coloured box.
MCQ_CSS = """
.q-sep {
  display:block;
  width:100%;
  height:0;
  border-top:0.8pt solid #c8d1de;
  margin:2.4mm 0 2.0mm;
  break-inside:avoid;
  page-break-inside:avoid;
}
.qcols .q-sep {
  border-top-color:#cbd4e0;
  margin:2.0mm 0 1.8mm;
}
"""


def add_question_separators(rendered_html: str) -> str:
    """Place a horizontal divider before every MCQ after the first one."""
    seen = 0

    def replace(match):
        nonlocal seen
        seen += 1
        if seen == 1:
            return match.group(0)
        return '<div class="q-sep"></div>' + match.group(0)

    return QUESTION_START.sub(replace, rendered_html)


def render_mcq_pdf(files, output, title, subtitle, author, badge,
                   show_toc=True, show_cover=True, two_columns=True,
                   flow=False, extra_css=None):
    """Build an MCQ PDF using md2pdf's existing conversion primitives."""
    if not files:
        raise SystemExit("No Markdown files found.")

    # Get raw rendered sections first.  qcols is applied only after the divider
    # markers are inserted, which keeps the rule in the correct column.
    pipeline._OPTS["qcols"] = False
    rendered_sections = []
    for f in files:
        print(f"    - {f.name}")
        rendered_sections.append(pipeline.md_to_html(f.read_text(encoding="utf-8")))

    content = "\n".join(rendered_sections)
    content = add_question_separators(content)

    toc_html = pipeline.build_toc(content) if show_toc else ""
    if two_columns:
        pipeline._OPTS["qcols"] = True
        content = pipeline.apply_qcols(content)
    else:
        pipeline._OPTS["qcols"] = False

    parts = []
    if show_cover:
        meta = [author, f"{len(files)} MCQ/source file(s)",
                date.today().strftime("%d %B %Y")]
        parts.append(pipeline.build_cover(title, subtitle, meta, badge))
    if toc_html:
        parts.append(toc_html)
    parts.append(content)

    document = (
        '<!DOCTYPE html><html lang="hi"><head><meta charset="utf-8">'
        f'<title>{html.escape(title)}</title></head><body>{"".join(parts)}</body></html>'
    )

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    debug = output.with_suffix(".debug.html")
    debug.write_text(document, encoding="utf-8")

    # md2pdf.py imports the same three objects.  Keeping the actual PDF call in
    # this wrapper is what allows the MCQ-only CSS to be added without touching
    # the general chapter renderer.
    font_config = pipeline.FontConfiguration()
    sheets = [
        pipeline.CSS(filename=str(pipeline.CSS_FILE), font_config=font_config),
        pipeline.CSS(string=MCQ_CSS, font_config=font_config),
    ]
    if flow:
        sheets.append(pipeline.CSS(
            string="h1{page-break-before:auto;margin-top:9mm;}"
                   "h1:first-of-type{margin-top:0;}",
            font_config=font_config,
        ))
    if extra_css:
        sheets.append(pipeline.CSS(filename=str(extra_css), font_config=font_config))

    print("  rendering MCQ PDF ...")
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
        description="MCQ Markdown -> print-friendly PDF with question separators"
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
    parser.add_argument("--no-qcols", action="store_true",
                        help="keep questions in one column")
    parser.add_argument("--flow", action="store_true",
                        help="allow sections to continue on the same page")
    parser.add_argument("--css", help="optional additional CSS file")
    args = parser.parse_args()

    files = pipeline.collect(args.inputs)
    if not files:
        raise SystemExit("No Markdown files found.")

    title = args.title or files[0].stem.replace("-", " ").replace("_", " ")
    output = args.output or str(files[0].with_suffix(".pdf"))
    show_toc = args.toc or (len(files) > 1 and not args.no_toc)

    print(f"  reading {len(files)} file(s)")
    render_mcq_pdf(
        files=files,
        output=output,
        title=title,
        subtitle=args.subtitle,
        author=args.author,
        badge=args.badge,
        show_toc=show_toc and not args.no_toc,
        show_cover=not args.no_cover,
        two_columns=not args.no_qcols,
        flow=args.flow,
        extra_css=args.css,
    )


if __name__ == "__main__":
    main()
