"""
mathtex.py — LaTeX math -> inline SVG for the PDF pipeline.

WeasyPrint has no JavaScript, so MathJax/KaTeX cannot run. Matplotlib's
mathtext engine renders a large TeX subset to SVG with no LaTeX install
required, which keeps the build self-contained and fast.

Syntax in markdown:
    $...$      inline math
    $$...$$    display (centred, larger)
"""
import base64
import io
import re

import matplotlib
matplotlib.use("Agg")
from matplotlib import mathtext              # noqa: E402
from matplotlib import rcParams              # noqa: E402

rcParams["mathtext.fontset"] = "dejavusans"  # matches the book's fallback face

_CACHE = {}

# convenience macros so chapters can be written naturally
MACROS = {
    r"\CP": r"\mathrm{CP}",
    r"\SP": r"\mathrm{SP}",
    r"\MP": r"\mathrm{MP}",
    r"\SI": r"\mathrm{SI}",
    r"\CI": r"\mathrm{CI}",
    r"\per": r"\%",
}


def _expand(tex: str) -> str:
    for k, v in MACROS.items():
        tex = tex.replace(k, v)
    return tex


DEVANAGARI = re.compile(r"[\u0900-\u097F]")


def render(tex: str, display: bool = False) -> str:
    """LaTeX string -> <img> tag holding a base64 SVG."""
    tex = _expand(tex.strip())
    if DEVANAGARI.search(tex):
        # mathtext has no Devanagari glyphs -> silent tofu. Fail loudly and
        # render the Hindi as ordinary text so the page stays readable.
        hindi = "".join(ch for ch in tex if DEVANAGARI.match(ch) or ch.isspace())
        print(f"    ! Devanagari inside math: {tex[:48]!r} — keep Hindi OUTSIDE $…$")
        return f'<span class="texhindi">{hindi.strip()}</span>' 
    key = (tex, display)
    if key in _CACHE:
        return _CACHE[key]

    buf = io.BytesIO()
    try:
        mathtext.math_to_image(f"${tex}$", buf, format="svg", dpi=220)
    except Exception as e:                     # bad TeX -> visible, not silent
        esc = tex.replace("&", "&amp;").replace("<", "&lt;")
        out = (f'<code class="texerr" title="{e}">{esc}</code>')
        _CACHE[key] = out
        return out

    svg = buf.getvalue().decode("utf-8")
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg, flags=re.S)
    svg = svg.strip()

    m = re.search(r'width="([\d.]+)pt"\s+height="([\d.]+)pt"', svg)
    h_pt = float(m.group(2)) if m else 12.0

    b64 = base64.b64encode(svg.encode("utf-8")).decode("ascii")
    if display:
        # display math: scale relative to a 9pt design size, centred by CSS
        style = f"height:{h_pt/8.4:.2f}em;"
        cls = "mathblock"
    else:
        # inline: match x-height of 10.4pt body text and sit on the baseline
        style = f"height:{h_pt/9.6:.2f}em;"
        cls = "mathinline"
    out = (f'<img class="{cls}" style="{style}" alt="math" '
           f'src="data:image/svg+xml;base64,{b64}"/>')
    _CACHE[key] = out
    return out


# ---------------------------------------------------------------- markdown
# $$...$$ first, then $...$ ; skip anything inside code fences/spans.
_DISPLAY = re.compile(r"\$\$(.+?)\$\$", re.S)
_INLINE = re.compile(r"(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)", re.S)
_CODE = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)


def convert(md: str) -> str:
    """Replace $…$ / $$…$$ in markdown with rendered <img> tags."""
    parts = _CODE.split(md)
    for i, chunk in enumerate(parts):
        if chunk.startswith("```") or (chunk.startswith("`") and chunk.endswith("`")):
            continue                                  # leave code untouched
        chunk = _DISPLAY.sub(lambda m: render(m.group(1), True), chunk)
        chunk = _INLINE.sub(lambda m: render(m.group(1), False), chunk)
        parts[i] = chunk
    return "".join(parts)
