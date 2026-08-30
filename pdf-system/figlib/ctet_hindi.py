"""Small path-backed Hindi labels for CTET revision-note figures.

Hindi text is rendered through pre-shaped glyph outlines in ``hindi_paths``;
there is no Devanagari inside SVG ``<text>``. This is an intentionally small,
tested label set so the notes stay sharp in PDF renderers.
"""

from .sketch import Canvas, C


def _card(cv, x, y, w, h, label, col, bg):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.5"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 5, label, size=14, weight=700, color=col)


def hindi_labels_ctet(spec):
    W, H = 452, 208
    cv = Canvas(W, H, seed=int(spec.get("seed", 9101)))
    cv.text(W / 2, 19, "याद रखें", size=12, weight=700, color=C["soft"])
    _card(cv, 28, 54, 92, 54, "प्रश्न", C["red"], C["red_bg"])
    _card(cv, 132, 54, 92, 54, "प्रमाण", C["blue"], C["blue_bg"])
    _card(cv, 236, 54, 92, 54, "समझ", C["green"], C["green_bg"])
    _card(cv, 340, 54, 84, 54, "सहायता", C["purple"], C["purple_bg"])
    cv.arrow(122, 81, 128, 81, color=C["grey"], w=1.0)
    cv.arrow(226, 81, 232, 81, color=C["grey"], w=1.0)
    cv.arrow(330, 81, 336, 81, color=C["grey"], w=1.0)
    cv.line(72, 145, 382, 145, color=C["amber"], w=1.5, dash="5 3")
    cv.text(W / 2, 174, "सही तरीका", size=10, weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "hindi-labels-ctet": hindi_labels_ctet,
}
