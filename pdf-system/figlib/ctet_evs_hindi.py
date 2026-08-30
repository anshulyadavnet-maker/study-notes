"""Hindi-labelled vector figures for the separate pure-Hindi Paper I EVS notes."""

from .sketch import Canvas, C


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.5):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=92, x0=48, x1=404, size=7.8):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, label, col, "#ffffff", size=size)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.0)


def evs_hindi_dashboard(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=int(spec.get("seed", 9701)))
    cv.text(W / 2, 19, "मुख्य विषय", size=12, weight=700, color=C["soft"])
    items = [("परिवार", 82, 70, C["blue"], C["blue_bg"]), ("भोजन", 226, 70, C["red"], C["red_bg"]), ("जल", 370, 70, C["teal"], C["teal_bg"]), ("आश्रय", 82, 125, C["amber"], C["amber_bg"]), ("यात्रा", 226, 125, C["purple"], C["purple_bg"]), ("पर्यावरण", 370, 125, C["green"], C["green_bg"])]
    for label, x, y, col, bg in items:
        _box(cv, x - 50, y - 17, 100, 34, label, col, bg, size=8.4)
    _box(cv, 87, 174, 278, 29, "अनुभव → प्रश्न → जाँच", C["purple"], C["purple_bg"], size=9.0)
    return cv.svg()


def evs_hindi_water(spec):
    W, H = 452, 244
    cv = Canvas(W, H, seed=int(spec.get("seed", 9702)))
    cv.text(W / 2, 19, "जल-चक्र", size=12, weight=700, color=C["soft"])
    nodes = [("वाष्पीकरण", 80, 90, C["blue"], C["blue_bg"]), ("संघनन", 226, 55, C["purple"], C["purple_bg"]), ("वर्षण", 372, 90, C["green"], C["green_bg"]), ("संग्रह", 226, 157, C["amber"], C["amber_bg"])]
    for label, x, y, col, bg in nodes:
        _box(cv, x - 55, y - 17, 110, 34, label, col, bg, size=8.3)
    for a, b, col in (((130, 80), (168, 64), C["blue"]), ((284, 64), (322, 80), C["purple"]), ((372, 108), (282, 145), C["green"]), ((170, 145), (80, 108), C["amber"])):
        cv.arrow(*a, *b, color=col, w=1.1)
    cv.text(W / 2, 205, "जल और जीवन", size=9.5, weight=700, color=C["red"])
    return cv.svg()


def evs_hindi_inquiry(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=int(spec.get("seed", 9703)))
    cv.text(W / 2, 19, "जाँच-चक्र", size=12, weight=700, color=C["soft"])
    _flow(cv, ["प्रश्न", "अवलोकन", "कार्य", "चर्चा", "चिंतन"], [C["red"], C["blue"], C["green"], C["amber"], C["purple"]], y=92, x0=48, x1=404, size=8.0)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "अनुभव और प्रमाण", size=9.0, weight=700, color=C["red"])
    return cv.svg()


def evs_hindi_assessment(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=int(spec.get("seed", 9704)))
    cv.text(W / 2, 19, "मूल्यांकन", size=12, weight=700, color=C["soft"])
    _flow(cv, ["अवलोकन", "अभिलेख", "प्रतिपुष्टि", "सहायता", "अगली योजना"], [C["blue"], C["green"], C["red"], C["amber"], C["purple"]], y=92, x0=48, x1=404, size=7.0)
    cv.text(W / 2, 160, "बच्चे की प्रगति", size=9.0, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "evs-hindi-dashboard": evs_hindi_dashboard,
    "evs-hindi-water": evs_hindi_water,
    "evs-hindi-inquiry": evs_hindi_inquiry,
    "evs-hindi-assessment": evs_hindi_assessment,
}
