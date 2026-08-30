"""Hindi-labelled vector figures for the separate pure-Hindi Paper I Maths notes."""

from .sketch import Canvas, C


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.2):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=90, x0=48, x1=404, size=7.8):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, label, col, "#ffffff", size=size)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.0)


def math_hindi_dashboard(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9801)))
    cv.text(W / 2, 19, "गणित", size=12, weight=700, color=C["soft"])
    cards = [("15", "विषय-वस्तु", C["blue"], C["blue_bg"]), ("15", "शिक्षणशास्त्र", C["purple"], C["purple_bg"]), ("30", "तर्क", C["green"], C["green_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 48, 114, 59, top, col, bg, size=13)
        cv.text(x, 96, bottom, size=7.5, color=col)
    _box(cv, 74, 145, 304, 33, "समझ → विधि → जाँच", C["red"], C["red_bg"], size=9.0)
    cv.text(W / 2, H - 8, "बच्चे का गणित", size=9.0, weight=700, color=C["ink"])
    return cv.svg()


def math_hindi_fraction(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9802)))
    cv.text(W / 2, 19, "भिन्न", size=12, weight=700, color=C["soft"])
    _box(cv, 44, 55, 150, 34, "अंश", C["blue"], C["blue_bg"], size=9.5)
    _box(cv, 258, 55, 150, 34, "हर", C["green"], C["green_bg"], size=9.5)
    x0, y0, w, h, den, num = 63, 115, 326, 32, 4, 3
    seg = w / den
    for i in range(den):
        fill = C["blue_bg"] if i < num else "#ffffff"
        cv.raw(f'<rect x="{x0 + i * seg:.2f}" y="{y0}" width="{seg:.2f}" height="{h}" fill="{fill}" stroke="{C["blue"]}" stroke-width="1.2"/>')
    cv.text(W / 2, 174, "समान भाग", size=9.5, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "अंश चुने भाग; हर कुल समान भाग", size=8.5, color=C["ink"])
    return cv.svg()


def math_hindi_measurement(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9803)))
    cv.text(W / 2, 19, "मापन", size=12, weight=700, color=C["soft"])
    items = [("लंबाई", 82, 74, C["blue"], C["blue_bg"]), ("भार", 226, 74, C["green"], C["green_bg"]), ("समय", 370, 74, C["purple"], C["purple_bg"]), ("धारिता", 154, 134, C["amber"], C["amber_bg"]), ("इकाई", 298, 134, C["red"], C["red_bg"])]
    for label, x, y, col, bg in items:
        _box(cv, x - 50, y - 17, 100, 34, label, col, bg, size=8.8)
    cv.text(W / 2, 198, "अनुमान और सही इकाई", size=9.0, weight=700, color=C["teal"])
    return cv.svg()


def math_hindi_pedagogy(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=int(spec.get("seed", 9804)))
    cv.text(W / 2, 19, "गणित-शिक्षण", size=11.5, weight=700, color=C["soft"])
    _flow(cv, ["विधि", "समझ", "त्रुटि", "सहायता", "जाँच"], [C["blue"], C["green"], C["red"], C["amber"], C["purple"]], y=88, x0=48, x1=404, size=8.0)
    cv.text(W / 2, 150, "बच्चे की सोच", size=9.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "समझ + तर्क + आत्मविश्वास", size=8.4, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "math-hindi-dashboard": math_hindi_dashboard,
    "math-hindi-fraction": math_hindi_fraction,
    "math-hindi-measurement": math_hindi_measurement,
    "math-hindi-pedagogy": math_hindi_pedagogy,
}
