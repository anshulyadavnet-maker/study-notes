#!/usr/bin/env python3
"""
mcqmdtopdf.py — MCQ Markdown ➜ print-friendly PDF.

This is deliberately separate from md2pdf.py.  It reuses the common Markdown,
figure, cover and WeasyPrint pipeline, but gives each MCQ a colour-coded,
print-friendly outline so questions remain visually separated in one- and
two-column print.

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
GURMUKHI_RE = re.compile(r"[\u0A00-\u0A7F]")

# Kept local to this MCQ-only wrapper so the ordinary chapter renderer is not
# changed.  The colours are deliberately high-contrast and print-friendly:
# black question text, dark blue options, green answer and dark red explanation.
MCQ_CSS = """
/* One bordered card contains the complete question, options, answer and
   explanation.  Keeping the card together also prevents awkward column/page
   breaks in WeasyPrint. */
.mcq-question {
  display:block;
  box-sizing:border-box;
  width:100%;
  border:0.85pt solid #9eabc0;
  border-left:2.2pt solid #536b88;
  border-radius:1.4mm;
  background:#ffffff;
  padding:1.55mm 2.0mm 1.25mm;
  margin:0 0 2.45mm;
  break-inside:avoid;
  page-break-inside:avoid;
}
.mcq-question .mcq-prompt {
  color:#111111;
  font-weight:600;
  margin:0 0 1.25mm;
  break-after:avoid;
  page-break-after:avoid;
}
.mcq-question .mcq-prompt strong {
  color:#000000;
}
.mcq-question > ul {
  color:#153f73;
  margin:.2em 0 .75em 1.2em;
  padding-left:1.0em;
}
.mcq-question > ul li {
  color:#153f73;
  margin:.12em 0;
}
.mcq-question .mcq-answer {
  color:#177245;
  font-weight:600;
  margin:.55mm 0 .65mm;
}
.mcq-question .mcq-answer strong {
  color:#126238;
}
.mcq-question .mcq-explanation {
  color:#8b2635;
  margin:.45mm 0 .15mm;
}
.mcq-question .mcq-explanation strong {
  color:#741b29;
}
/* The Markdown source uses --- after each MCQ.  The card outline is the
   separator now, so avoid adding a second rule inside the card. */
.mcq-question > hr {
  display:none;
}
/* qcols has slightly smaller type; retain the card padding and keep each card
   intact when the questions flow down the two columns. */
.qcols .mcq-question {
  margin-bottom:2.0mm;
  padding:1.35mm 1.75mm 1.1mm;
}
.qcols .mcq-question .mcq-prompt {
  margin-bottom:1.0mm;
}
.qcols .mcq-question > ul {
  margin-bottom:.55em;
}
/* Punjabi banks use Gurmukhi in HTML.  Prefer a Gurmukhi-capable font when
   the host provides one, while keeping the existing Devanagari documents on
   their original font stack. */
.punjabi-document {
  font-family:'Noto Sans Gurmukhi','Raavi','Nirmala UI','Lohit Punjabi','DejaVu Sans',sans-serif;
}
"""


def add_question_separators(rendered_html: str) -> str:
    """Wrap each complete MCQ in a print-friendly, colour-coded card.

    The Markdown converter emits one question as a prompt paragraph, an
    options list, an answer paragraph, an explanation paragraph and usually an
    ``<hr>``.  We wrap from one Q paragraph up to the next Q paragraph so the
    border covers the whole question without changing the general renderer.
    """
    matches = list(QUESTION_START.finditer(rendered_html))
    if not matches:
        return rendered_html

    out = [rendered_html[:matches[0].start()]]
    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(rendered_html)
        raw_block = rendered_html[start:end]

        # Every MCQ Markdown entry normally ends with `---`, rendered as an
        # <hr />.  Stop the card there so a final question does not swallow the
        # following Quick Answer Index or the next input file's heading.  The
        # explanation paragraph is a safe fallback for banks that omit `---`.
        boundary = re.search(r'<hr\s*/?>', raw_block)
        if boundary is None:
            boundary = re.search(
                r'<p>\s*<strong>Explanation:</strong>.*?</p>',
                raw_block, flags=re.S
            )
        block = raw_block[:boundary.end()] if boundary else raw_block
        tail = raw_block[boundary.end():] if boundary else ""

        block = re.sub(
            r"^<p>\s*(<strong>Q\d{1,3}\.?</strong>)",
            r'<p class="mcq-prompt">\1', block, count=1
        )
        block = re.sub(
            r'<p>\s*(<strong>Answer:</strong>)',
            r'<p class="mcq-answer">\1', block, count=1
        )
        block = re.sub(
            r'<p>\s*(<strong>Explanation:</strong>)',
            r'<p class="mcq-explanation">\1', block, count=1
        )
        out.append('<div class="mcq-question">' + block + '</div>')
        if tail:
            out.append(tail)
    return ''.join(out)


def render_mcq_pdf(files, output, title, subtitle, author, badge,
                   show_toc=True, show_cover=True, two_columns=True,
                   flow=False, extra_css=None):
    """Build an MCQ PDF using md2pdf's existing conversion primitives."""
    if not files:
        raise SystemExit("No Markdown files found.")

    # Get raw rendered sections first.  Question cards are added before qcols is
    # applied so the complete bordered card flows as one unit in a column.
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

    is_punjabi = bool(GURMUKHI_RE.search(content))
    doc_lang = "pa" if is_punjabi else "hi"
    body_class = ' class="punjabi-document"' if is_punjabi else ""
    document = (
        f'<!DOCTYPE html><html lang="{doc_lang}"><head><meta charset="utf-8">'
        f'<title>{html.escape(title)}</title></head><body{body_class}>{"".join(parts)}</body></html>'
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
        description="MCQ Markdown -> print-friendly PDF with colour-coded question cards"
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
