"""Devanagari path-labelled figures for CTET Language II Sanskrit notes."""

from .sketch import Canvas, C


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.2):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=90, x0=48, x1=404, size=7.7):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, label, col, "#ffffff", size=size)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.0)


def sanskrit_dashboard(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9901)))
    cv.text(W / 2, 19, "संस्कृत", size=12, weight=700, color=C["soft"])
    cards = [("15", "अवबोधन", C["blue"], C["blue_bg"]), ("15", "व्याकरण", C["purple"], C["purple_bg"]), ("30", "भाषा कौशल", C["green"], C["green_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 48, 114, 59, top, col, bg, size=13)
        cv.text(x, 96, bottom, size=7.5, color=col)
    _box(cv, 74, 145, 304, 33, "पढ़ें → समझें → बोलें", C["red"], C["red_bg"], size=8.9)
    cv.text(W / 2, H - 8, "अर्थपूर्ण अभ्यास", size=8.8, weight=700, color=C["ink"])
    return cv.svg()


def sanskrit_comprehension(spec):
    W, H = 452, 255
    cv = Canvas(W, H, seed=int(spec.get("seed", 9902)))
    cv.text(W / 2, 18, "अवबोधन", size=12, weight=700, color=C["soft"])
    steps = [("शब्दार्थ", C["blue"], C["blue_bg"]), ("अन्वय", C["teal"], C["teal_bg"]), ("भाव", C["green"], C["green_bg"]), ("निष्कर्ष", C["amber"], C["amber_bg"]), ("उत्तर", C["purple"], C["purple_bg"])]
    for i, (lab, col, bg) in enumerate(steps):
        x = 40 + i * 8; y = 205 - i * 34; w = 250 + i * 31
        _box(cv, x, y, w, 27, lab, col, bg, size=8.0)
    cv.text(226, 238, "पाठ + संदर्भ + प्रमाण", size=8.4, weight=700, color=C["red"])
    return cv.svg()


def sanskrit_grammar(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9903)))
    cv.text(W / 2, 19, "व्याकरण", size=12, weight=700, color=C["soft"])
    _flow(cv, ["सन्धि", "समास", "कारक", "प्रत्यय", "धातु"], [C["blue"], C["green"], C["red"], C["amber"], C["purple"]], y=88, x0=48, x1=404, size=8.0)
    cv.text(W / 2, 150, "रूप और प्रयोग", size=9.0, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "वाक्य में व्याकरण", size=8.7, color=C["ink"])
    return cv.svg()


def sanskrit_pedagogy(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9904)))
    cv.text(W / 2, 19, "भाषा-शिक्षण", size=11.5, weight=700, color=C["soft"])
    _flow(cv, ["श्रवण", "वाचन", "पठन", "लेखन", "अभ्यास"], [C["blue"], C["green"], C["amber"], C["purple"], C["red"]], y=88, x0=48, x1=404, size=8.0)
    cv.text(W / 2, 150, "संवाद और समझ", size=9.0, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "अर्थपूर्ण संस्कृत", size=8.7, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "sanskrit-dashboard": sanskrit_dashboard,
    "sanskrit-comprehension": sanskrit_comprehension,
    "sanskrit-grammar": sanskrit_grammar,
    "sanskrit-pedagogy": sanskrit_pedagogy,
}
