"""Vector visuals for CTET Language I Hindi revision notes.

Labels stay in Latin script for reliable SVG rendering; Hindi explanations live
in the surrounding Markdown text.
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
    cv.text(W / 2, 18, "Language I Hindi: revision dashboard", size=9.5, weight=700, color=C["soft"])
    cards = [("15", "comprehension", C["blue"], C["blue_bg"]), ("15", "pedagogy", C["purple"], C["purple_bg"]), ("LSRW", "language skills", C["green"], C["green_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 49, 114, 59, top, col, bg, size=13)
        cv.text(x, 96, bottom, size=7.8, color=col)
    cv.arrow(135, 78, 165, 78, color=C["grey"], w=1.0)
    cv.arrow(285, 78, 315, 78, color=C["grey"], w=1.0)
    _box(cv, 74, 145, 304, 33, "meaning → expression → communication", C["red"], C["red_bg"], size=9)
    cv.text(W / 2, H - 8, "grammar is taught through meaningful language use", size=8.4, color=C["ink"])
    return cv.svg()


def comprehension_ladder(spec):
    W, H = 452, 255
    cv = Canvas(W, H, seed=_seed(spec, 9402))
    cv.text(W / 2, 18, "comprehension ladder: from locating words to evaluating meaning", size=8.9, weight=700, color=C["soft"])
    steps = [("word clue", C["blue"], C["blue_bg"]), ("detail", C["teal"], C["teal_bg"]), ("main idea", C["green"], C["green_bg"]), ("inference", C["amber"], C["amber_bg"]), ("evaluate", C["purple"], C["purple_bg"])]
    for i, (lab, col, bg) in enumerate(steps):
        x = 40 + i * 8; y = 205 - i * 34; w = 250 + i * 31
        _box(cv, x, y, w, 27, lab, col, bg, size=8.0)
    cv.text(226, 238, "evidence + context + reader response", size=8.5, weight=700, color=C["red"])
    return cv.svg()


def lsrw_cycle(spec):
    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 9403))
    cv.text(W / 2, 18, "LSRW cycle: language grows through connected skills", size=9.4, weight=700, color=C["soft"])
    nodes = [("listen", 226, 52, C["blue"], C["blue_bg"]), ("speak", 365, 113, C["green"], C["green_bg"]), ("write", 226, 178, C["purple"], C["purple_bg"]), ("read", 87, 113, C["amber"], C["amber_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 47, y - 18, 94, 36, lab, col, bg, size=9)
    cv.arrow(270, 65, 332, 97, color=C["grey"], w=1.0)
    cv.arrow(332, 129, 270, 164, color=C["grey"], w=1.0)
    cv.arrow(182, 164, 120, 129, color=C["grey"], w=1.0)
    cv.arrow(120, 97, 182, 65, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "input ↔ interaction ↔ expression", size=8.7, color=C["red"], weight=700)
    return cv.svg()


def acquisition_bridge(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9404))
    cv.text(W / 2, 18, "additional-language learning: build a bridge, not a barrier", size=9.1, weight=700, color=C["soft"])
    _box(cv, 34, 68, 126, 48, "home language", C["blue"], C["blue_bg"], size=8.7)
    _box(cv, 292, 68, 126, 48, "school language", C["green"], C["green_bg"], size=8.5)
    cv.line(160, 92, 292, 92, color=C["amber"], w=7)
    cv.line(160, 100, 292, 100, color=C["amber"], w=2)
    cv.text(226, 82, "meaning bridge", size=8.0, weight=700, color=C["amber"])
    _box(cv, 120, 151, 212, 34, "context + interaction + support", C["purple"], C["purple_bg"], size=8.5)
    cv.arrow(97, 120, 157, 148, color=C["blue"], w=1.0)
    cv.arrow(355, 120, 295, 148, color=C["green"], w=1.0)
    cv.text(W / 2, H - 8, "identity and prior knowledge remain valuable", size=8.5, color=C["ink"])
    return cv.svg()


def reading_process(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 9405))
    cv.text(W / 2, 18, "strategic reading: predict, decode, connect, infer and reflect", size=9.0, weight=700, color=C["soft"])
    _flow(cv, ["predict", "decode", "connect", "infer", "reflect"], [C["red"], C["blue"], C["green"], C["amber"], C["purple"]], y=91, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "new question → purposeful re-reading", size=8.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "reader constructs meaning with evidence", size=8.5, color=C["ink"])
    return cv.svg()


def writing_process(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 9406))
    cv.text(W / 2, 18, "process writing: a text improves through planning and revision", size=9.2, weight=700, color=C["soft"])
    _flow(cv, ["plan", "draft", "revise", "edit", "share"], [C["blue"], C["teal"], C["amber"], C["purple"], C["green"]], y=91, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "feedback returns the writer to revision", size=8.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "ideas + audience + language choices", size=8.5, color=C["ink"])
    return cv.svg()


def multilingual_classroom(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9407))
    cv.text(W / 2, 18, "multilingual classroom: languages can work as learning resources", size=9.0, weight=700, color=C["soft"])
    _box(cv, 158, 45, 136, 36, "shared meaning", C["purple"], C["purple_bg"], size=9)
    nodes = [("home", 70, 130, C["blue"]), ("school", 175, 178, C["green"]), ("community", 285, 178, C["amber"]), ("media", 390, 130, C["red"])]
    for lab, x, y, col in nodes:
        _box(cv, x - 40, y - 16, 80, 32, lab, col, "#ffffff", size=8.0)
        cv.line(226, 81, x, y - 18, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "compare, translate, explain and participate", size=8.6, color=C["ink"])
    return cv.svg()


def language_assessment(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9408))
    cv.text(W / 2, 18, "language assessment: evidence informs the next support", size=9.2, weight=700, color=C["soft"])
    _flow(cv, ["observe", "task", "feedback", "support", "re-check"], [C["blue"], C["green"], C["red"], C["amber"], C["purple"]], y=91, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "listening + speaking + reading + writing", size=8.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "assessment is more than spelling marks", size=8.5, color=C["ink"])
    return cv.svg()


def grammar_context(spec):
    W, H = 452, 225
    cv = Canvas(W, H, seed=_seed(spec, 9409))
    cv.text(W / 2, 18, "grammar in context: notice form, connect meaning and use it", size=9.0, weight=700, color=C["soft"])
    _flow(cv, ["context", "notice", "explain", "practise", "communicate"], [C["blue"], C["teal"], C["amber"], C["purple"], C["green"]], y=90, x0=47, x1=405)
    cv.text(W / 2, 160, "example → pattern → purposeful sentence", size=8.8, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "grammar serves meaning and communication", size=8.5, color=C["ink"])
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
