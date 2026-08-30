"""Vector visuals for CTET Language I Hindi revision notes.

Language-I labels use pre-shaped Devanagari glyph outlines from ``hindi_paths``;
the English Language-II dashboard keeps Latin labels for its subject examples.
"""
from .sketch import Canvas, C


def _seed(spec, default=9400):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.2):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{bg}" stroke="{col}" stroke-width="1.4"/>')
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=92, x0=45, x1=407):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (lab, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, lab, col, "#ffffff", size=7.9)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.0)


def language2_dashboard(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9410))
    cv.text(W / 2, 18, "Language II English: revision dashboard", size=9.5, weight=700, color=C["soft"])
    cards = [("15", "comprehension", C["blue"], C["blue_bg"]), ("15", "pedagogy", C["purple"], C["purple_bg"]), ("LSRW", "language skills", C["green"], C["green_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 49, 114, 59, top, col, bg, size=13)
        cv.text(x, 96, bottom, size=7.8, color=col)
    cv.arrow(135, 78, 165, 78, color=C["grey"], w=1.0)
    cv.arrow(285, 78, 315, 78, color=C["grey"], w=1.0)
    _box(cv, 74, 145, 304, 33, "meaning → interaction → communication", C["red"], C["red_bg"], size=8.9)
    cv.text(W / 2, H - 8, "English is learned through purposeful use", size=8.4, color=C["ink"])
    return cv.svg()


def language_dashboard(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9401))
    cv.text(W / 2, 18, "पुनरावृत्ति", size=12, weight=700, color=C["soft"])
    cards = [("15", "अवबोधन", C["blue"], C["blue_bg"]), ("15", "शिक्षणशास्त्र", C["purple"], C["purple_bg"]), ("चार", "भाषा कौशल", C["green"], C["green_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 49, 114, 59, top, col, bg, size=13)
        cv.text(x, 96, bottom, size=7.8, color=col)
    cv.arrow(135, 78, 165, 78, color=C["grey"], w=1.0)
    cv.arrow(285, 78, 315, 78, color=C["grey"], w=1.0)
    _box(cv, 74, 145, 304, 33, "अर्थ → अभिव्यक्ति → संचार", C["red"], C["red_bg"], size=8.9)
    cv.text(W / 2, H - 8, "अर्थ और संचार", size=9.0, weight=700, color=C["ink"])
    return cv.svg()
def comprehension_ladder(spec):
    W, H = 452, 255
    cv = Canvas(W, H, seed=_seed(spec, 9402))
    cv.text(W / 2, 18, "अवबोधन", size=12, weight=700, color=C["soft"])
    steps = [("शब्द संकेत", C["blue"], C["blue_bg"]), ("विवरण", C["teal"], C["teal_bg"]), ("मुख्य विचार", C["green"], C["green_bg"]), ("निष्कर्ष", C["amber"], C["amber_bg"]), ("मूल्यांकन", C["purple"], C["purple_bg"])]
    for i, (lab, col, bg) in enumerate(steps):
        x = 40 + i * 8; y = 205 - i * 34; w = 250 + i * 31
        _box(cv, x, y, w, 27, lab, col, bg, size=8.0)
    cv.text(226, 238, "प्रमाण + संदर्भ", size=9.0, weight=700, color=C["red"])
    return cv.svg()
def lsrw_cycle(spec):
    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 9403))
    cv.text(W / 2, 18, "भाषा कौशल", size=12, weight=700, color=C["soft"])
    nodes = [("श्रवण", 226, 52, C["blue"], C["blue_bg"]), ("बोलना", 365, 113, C["green"], C["green_bg"]), ("लेखन", 226, 178, C["purple"], C["purple_bg"]), ("पठन", 87, 113, C["amber"], C["amber_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 47, y - 18, 94, 36, lab, col, bg, size=9)
    cv.arrow(270, 65, 332, 97, color=C["grey"], w=1.0)
    cv.arrow(332, 129, 270, 164, color=C["grey"], w=1.0)
    cv.arrow(182, 164, 120, 129, color=C["grey"], w=1.0)
    cv.arrow(120, 97, 182, 65, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "भाषा अभ्यास", size=9.0, color=C["red"], weight=700)
    return cv.svg()
def acquisition_bridge(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9404))
    cv.text(W / 2, 18, "भाषा और अनुभव", size=11.5, weight=700, color=C["soft"])
    _box(cv, 34, 68, 126, 48, "घरेलू भाषा", C["blue"], C["blue_bg"], size=8.7)
    _box(cv, 292, 68, 126, 48, "विद्यालयी भाषा", C["green"], C["green_bg"], size=8.3)
    cv.line(160, 92, 292, 92, color=C["amber"], w=7)
    cv.line(160, 100, 292, 100, color=C["amber"], w=2)
    cv.text(226, 82, "अर्थ का सेतु", size=8.2, weight=700, color=C["amber"])
    _box(cv, 120, 151, 212, 34, "संदर्भ और अंतःक्रिया", C["purple"], C["purple_bg"], size=8.2)
    cv.arrow(97, 120, 157, 148, color=C["blue"], w=1.0)
    cv.arrow(355, 120, 295, 148, color=C["green"], w=1.0)
    cv.text(W / 2, H - 8, "भाषा और अनुभव", size=8.7, color=C["ink"])
    return cv.svg()
def reading_process(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 9405))
    cv.text(W / 2, 18, "पढ़ने की रणनीति", size=11.5, weight=700, color=C["soft"])
    _flow(cv, ["अनुमान", "पठन", "जोड़ना", "निष्कर्ष", "चिंतन"], [C["red"], C["blue"], C["green"], C["amber"], C["purple"]], y=91, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "पुनः पठन", size=9.0, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "प्रमाण", size=8.7, color=C["ink"])
    return cv.svg()
def writing_process(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 9406))
    cv.text(W / 2, 18, "लेखन", size=12, weight=700, color=C["soft"])
    _flow(cv, ["योजना", "प्रारूप", "संशोधन", "संपादन", "साझा करना"], [C["blue"], C["teal"], C["amber"], C["purple"], C["green"]], y=91, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "प्रतिपुष्टि", size=9.0, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "विचार और भाषा", size=8.8, color=C["ink"])
    return cv.svg()
def multilingual_classroom(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9407))
    cv.text(W / 2, 18, "साझा अर्थ", size=12, weight=700, color=C["soft"])
    _box(cv, 158, 45, 136, 36, "साझा अर्थ", C["purple"], C["purple_bg"], size=8.9)
    nodes = [("घर", 70, 130, C["blue"]), ("विद्यालय", 175, 178, C["green"]), ("समुदाय", 285, 178, C["amber"]), ("मीडिया", 390, 130, C["red"])]
    for lab, x, y, col in nodes:
        _box(cv, x - 40, y - 16, 80, 32, lab, col, "#ffffff", size=8.0)
        cv.line(226, 81, x, y - 18, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "तुलना और सहभागिता", size=8.5, color=C["ink"])
    return cv.svg()
def language_assessment(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9408))
    cv.text(W / 2, 18, "मूल्यांकन", size=12, weight=700, color=C["soft"])
    _flow(cv, ["अवलोकन", "कार्य", "प्रतिपुष्टि", "सहायता", "पुनःजाँच"], [C["blue"], C["green"], C["red"], C["amber"], C["purple"]], y=91, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "भाषा कौशल", size=9.0, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "अर्थ और संचार", size=8.7, color=C["ink"])
    return cv.svg()
def grammar_context(spec):
    W, H = 452, 225
    cv = Canvas(W, H, seed=_seed(spec, 9409))
    cv.text(W / 2, 18, "व्याकरण", size=12, weight=700, color=C["soft"])
    _flow(cv, ["संदर्भ", "ध्यान", "समझ", "अभ्यास", "संचार"], [C["blue"], C["teal"], C["amber"], C["purple"], C["green"]], y=90, x0=47, x1=405)
    cv.text(W / 2, 160, "उदाहरण → नियम → वाक्य", size=8.8, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "अर्थ और संचार", size=8.7, color=C["ink"])
    return cv.svg()

REGISTRY = {
    "language2-dashboard": language2_dashboard,
    "language-exam-dashboard": language_dashboard,
    "language-comprehension-ladder": comprehension_ladder,
    "language-lsrw-cycle": lsrw_cycle,
    "language-acquisition-bridge": acquisition_bridge,
    "language-reading-process": reading_process,
    "language-writing-process": writing_process,
    "language-multilingual-classroom": multilingual_classroom,
    "language-assessment": language_assessment,
    "language-grammar-context": grammar_context,
}
