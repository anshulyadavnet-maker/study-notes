"""Hindi-labelled vector figures for the pure-Hindi Paper I CDP notes."""

from .sketch import Canvas, C


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.8):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=92, x0=48, x1=404):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, label, col, "#ffffff", size=8.2)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.0)


def cdp_hindi_dashboard(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9601)))
    cv.text(W / 2, 19, "बाल विकास", size=12, weight=700, color=C["soft"])
    cards = [("15", "विकास", C["blue"], C["blue_bg"]), ("5", "समावेशन", C["green"], C["green_bg"]), ("10", "अधिगम", C["purple"], C["purple_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 48, 114, 59, top, col, bg, size=13)
        cv.text(x, 96, bottom, size=8.0, color=col)
    _box(cv, 74, 145, 304, 33, "सोच → सहायता → स्वतंत्रता", C["red"], C["red_bg"], size=8.7)
    cv.text(W / 2, H - 8, "बच्चे का विकास", size=9.0, weight=700, color=C["ink"])
    return cv.svg()


def cdp_hindi_theory_map(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=int(spec.get("seed", 9602)))
    cv.text(W / 2, 19, "मुख्य सिद्धांत", size=12, weight=700, color=C["soft"])
    nodes = [("पियाजे", 92, 76, C["blue"], C["blue_bg"]), ("वायगोत्स्की", 360, 76, C["green"], C["green_bg"]), ("कोहलबर्ग", 92, 146, C["amber"], C["amber_bg"]), ("ब्रूनर", 360, 146, C["purple"], C["purple_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 54, y - 19, 108, 38, lab, col, bg, size=8.6)
    cv.line(146, 76, 306, 76, color=C["grey"], w=1.0)
    cv.line(146, 146, 306, 146, color=C["grey"], w=1.0)
    cv.line(92, 96, 92, 126, color=C["grey"], w=1.0)
    cv.line(360, 96, 360, 126, color=C["grey"], w=1.0)
    _box(cv, 139, 191, 174, 29, "अर्थ-निर्माण", C["red"], C["red_bg"], size=8.8)
    return cv.svg()


def cdp_hindi_inclusion(spec):
    W, H = 452, 220
    cv = Canvas(W, H, seed=int(spec.get("seed", 9603)))
    cv.text(W / 2, 19, "समावेशी कक्षा", size=11.5, weight=700, color=C["soft"])
    for x, lab, col, bg in ((82, "पहुँच", C["blue"], C["blue_bg"]), (190, "सहभागिता", C["green"], C["green_bg"]), (298, "सहायता", C["amber"], C["amber_bg"]), (406, "गरिमा", C["purple"], C["purple_bg"])):
        _box(cv, x - 43, 67, 86, 38, lab, col, bg, size=8.7)
    for x in (125, 233, 341):
        cv.arrow(x, 86, x + 18, 86, color=C["grey"], w=1.0)
    cv.text(W / 2, 151, "सभी बच्चों के लिए", size=9.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "अवसर + सहायता + सम्मान", size=8.5, color=C["ink"])
    return cv.svg()


def cdp_hindi_response(spec):
    W, H = 452, 222
    cv = Canvas(W, H, seed=int(spec.get("seed", 9604)))
    cv.text(W / 2, 19, "शिक्षक की प्रतिक्रिया", size=11.2, weight=700, color=C["soft"])
    _flow(cv, ["अवलोकन", "पूछें", "समझें", "सहायता", "पुनःजाँच"], [C["blue"], C["teal"], C["amber"], C["purple"], C["green"]], y=88, x0=48, x1=404)
    cv.text(W / 2, 151, "सम्मान और प्रमाण", size=9.2, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "देखें → समझें → सहायता दें", size=8.6, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "cdp-hindi-dashboard": cdp_hindi_dashboard,
    "cdp-hindi-theory-map": cdp_hindi_theory_map,
    "cdp-hindi-inclusion": cdp_hindi_inclusion,
    "cdp-hindi-response": cdp_hindi_response,
}
