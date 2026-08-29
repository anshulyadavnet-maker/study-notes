"""Vector teaching figures for CTET Paper II Science MCQs.

The labels stay in Latin script so the SVG remains reliable in WeasyPrint;
explanations and Hindi notes belong in the Markdown surrounding each figure.
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=7200):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.5):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=92, x0=44, x1=408):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, label, col, "#ffffff")
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.05)


# ───────────────────────────── food and materials ───────────────────────────
def balanced_plate(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 7201))
    cv.text(W / 2, 18, "food components: a balanced meal contains different nutrients", size=9.4, weight=700, color=C["soft"])
    cx, cy, r = 226, 108, 66
    cv.circle(cx, cy, r, color=C["blue"], w=1.6, fill=C["blue_bg"])
    # Dividing strokes make the plate model readable without text inside wedges.
    cv.line(cx, cy, cx + r, cy, color=C["blue"], w=1.1)
    cv.line(cx, cy, cx - r * 0.5, cy - r * 0.86, color=C["blue"], w=1.1)
    cv.line(cx, cy, cx - r * 0.5, cy + r * 0.86, color=C["blue"], w=1.1)
    labels = [("energy", 118, 73, C["amber"]), ("body-build", 314, 73, C["red"]),
              ("protect", 112, 159, C["green"]), ("water", 340, 159, C["teal"])]
    for lab, x, y, col in labels:
        _box(cv, x - 44, y - 14, 88, 28, lab, col, "#ffffff", size=8.0)
    cv.text(W / 2, H - 8, "variety + suitable quantity + clean water", size=8.7, color=C["purple"], weight=700)
    return cv.svg()


def separation_science2(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=_seed(spec, 7202))
    cv.text(W / 2, 18, "separation method depends on the property of the components", size=9.2, weight=700, color=C["soft"])
    _flow(cv, ["mixture", "method", "separate", "product"], [C["red"], C["amber"], C["blue"], C["green"]], y=88)
    _box(cv, 55, 142, 92, 33, "sieving", C["blue"], C["blue_bg"], size=8.2)
    _box(cv, 180, 142, 92, 33, "filtration", C["green"], C["green_bg"], size=8.2)
    _box(cv, 305, 142, 92, 33, "evaporation", C["purple"], C["purple_bg"], size=8.0)
    cv.text(W / 2, H - 8, "particle size, solubility or magnetism guides the choice", size=8.5, color=C["ink"])
    return cv.svg()


# ───────────────────────────── living world ─────────────────────────────────
def plant_transport_science2(spec):
    W, H = 452, 254
    cv = Canvas(W, H, seed=_seed(spec, 7203))
    cv.text(W / 2, 18, "plant transport: roots, stem and leaves have connected roles", size=9.5, weight=700, color=C["soft"])
    # roots and stem
    cv.line(226, 184, 226, 70, color=C["green"], w=5)
    for dx, yy in ((-32, 205), (-16, 218), (22, 208), (38, 193), (-48, 198)):
        cv.line(226, 184, 226 + dx, yy, color=C["amber"], w=1.7)
    for x, y, side in ((178, 82, -1), (274, 104, 1), (166, 126, -1), (286, 64, 1)):
        pts = [(226, y + 12), (x, y), (x + side * 25, y - 13), (x + side * 20, y + 15)]
        cv.polygon(pts, color=C["green"], w=1.2, fill=C["green_bg"])
    cv.arrow(214, 182, 214, 84, color=C["blue"], w=1.3)
    cv.arrow(238, 82, 238, 179, color=C["red"], w=1.2)
    _box(cv, 43, 73, 98, 30, "water + minerals", C["blue"], C["blue_bg"], size=7.7)
    _box(cv, 311, 73, 98, 30, "food made", C["red"], C["red_bg"], size=8.0)
    cv.text(226, 242, "xylem: upward water path | phloem: food transport", size=8.4, color=C["purple"], weight=700)
    return cv.svg()


def food_web_science2(spec):
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 7204))
    cv.text(W / 2, 18, "food web: organisms are connected through feeding relationships", size=9.5, weight=700, color=C["soft"])
    nodes = [("grass", 72, 112, C["green"], C["green_bg"]), ("insect", 190, 72, C["amber"], C["amber_bg"]),
             ("rabbit", 190, 154, C["blue"], C["blue_bg"]), ("frog", 302, 72, C["purple"], C["purple_bg"]),
             ("hawk", 386, 126, C["red"], C["red_bg"]), ("decomposer", 302, 194, C["teal"], C["teal_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 43, y - 15, 86, 30, lab, col, bg, size=7.8)
    for a, b in (((115, 105), (147, 81)), ((115, 120), (147, 145)), ((233, 72), (259, 72)),
                 ((233, 151), (343, 130)), ((345, 84), (354, 114)), ((233, 162), (274, 188)),
                 ((115, 128), (274, 188))):
        cv.arrow(*a, *b, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "energy and matter move through connected organisms", size=8.5, color=C["ink"])
    return cv.svg()


# ───────────────────────────── motion and force ──────────────────────────────
def motion_graph_science2(spec):
    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 7205))
    cv.text(W / 2, 18, "distance-time graph: slope represents rate of motion", size=9.6, weight=700, color=C["soft"])
    x0, y0, x1, y1 = 66, 204, 398, 52
    cv.line(x0, y0, x1, y0, color=C["ink"], w=1.5)
    cv.line(x0, y0, x0, y1, color=C["ink"], w=1.5)
    cv.arrow(x1 - 12, y0, x1 + 8, y0, color=C["ink"], w=1.1)
    cv.arrow(x0, y1 + 12, x0, y1 - 8, color=C["ink"], w=1.1)
    cv.text(x1 + 12, y0 + 3, "time", size=8.5, color=C["ink"], anchor="start")
    cv.text(x0 - 8, y1 - 8, "distance", size=8.5, color=C["ink"], anchor="end")
    cv.line(80, 184, 360, 76, color=C["blue"], w=2.0)
    cv.line(80, 184, 80, 116, color=C["red"], w=2.0)
    for x, lab in ((80, "0"), (220, "t"), (360, "2t")):
        cv.line(x, y0 - 4, x, y0 + 4, color=C["grey"], w=0.9)
        cv.text(x, y0 + 17, lab, size=8, color=C["soft"])
    cv.text(294, 94, "uniform", size=8.5, weight=700, color=C["blue"])
    cv.text(93, 108, "rest", size=8.5, weight=700, color=C["red"])
    return cv.svg()


def circuit_science2(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 7206))
    cv.text(W / 2, 18, "closed circuit: a complete conducting path allows current", size=9.4, weight=700, color=C["soft"])
    # loop
    cv.line(82, 76, 82, 172, color=C["ink"], w=1.8)
    cv.line(82, 76, 160, 76, color=C["ink"], w=1.8)
    cv.line(210, 76, 348, 76, color=C["ink"], w=1.8)
    cv.line(348, 76, 348, 172, color=C["ink"], w=1.8)
    cv.line(348, 172, 82, 172, color=C["ink"], w=1.8)
    # cell
    cv.line(166, 61, 166, 91, color=C["red"], w=2.3)
    cv.line(190, 54, 190, 98, color=C["red"], w=1.1)
    cv.text(178, 113, "cell", size=8.4, weight=700, color=C["red"])
    # bulb
    cv.circle(348, 124, 19, color=C["amber"], w=1.5, fill=C["amber_bg"])
    cv.line(337, 113, 359, 135, color=C["amber"], w=1.2)
    cv.line(359, 113, 337, 135, color=C["amber"], w=1.2)
    cv.text(348, 157, "bulb", size=8.4, weight=700, color=C["amber"])
    # switch
    cv.dot(82, 124, r=4, color=C["blue"])
    cv.dot(116, 124, r=4, color=C["blue"])
    cv.line(82, 124, 107, 108, color=C["blue"], w=1.8)
    cv.text(99, 151, "closed switch", size=8.2, weight=700, color=C["blue"])
    cv.arrow(236, 76, 284, 76, color=C["green"], w=1.0)
    cv.text(W / 2, H - 8, "cell + wires + closed switch + load", size=8.7, color=C["purple"], weight=700)
    return cv.svg()


def magnet_field_science2(spec):
    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 7207))
    cv.text(W / 2, 18, "bar magnet: field lines form a pattern outside the magnet", size=9.5, weight=700, color=C["soft"])
    _box(cv, 174, 93, 104, 48, "N     S", C["red"], C["red_bg"], size=11)
    for yy, bend in ((54, 34), (72, 22), (160, 22), (178, 34)):
        cv.arc(226, 117, 96 + bend, math.pi + 0.25, 2 * math.pi - 0.25, color=C["blue"], w=1.0)
    cv.arrow(125, 66, 160, 80, color=C["blue"], w=1.0)
    cv.arrow(292, 80, 327, 66, color=C["blue"], w=1.0)
    cv.arrow(126, 168, 160, 154, color=C["blue"], w=1.0)
    cv.arrow(292, 154, 326, 168, color=C["blue"], w=1.0)
    cv.text(W / 2, 213, "outside: N -> S | field is strongest near the poles", size=8.6, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── light and sky ────────────────────────────────
def reflection_ray_science2(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 7208))
    cv.text(W / 2, 18, "reflection: angle of incidence equals angle of reflection", size=9.2, weight=700, color=C["soft"])
    cv.line(226, 48, 226, 204, color=C["purple"], w=3.0)
    cv.text(226, 224, "mirror", size=8.5, weight=700, color=C["purple"])
    cv.line(126, 126, 326, 126, color=C["grey"], w=1.1, dash="5 3")
    cv.text(338, 130, "normal", size=8.2, color=C["grey"], anchor="start")
    cv.arrow(92, 64, 226, 126, color=C["red"], w=1.7)
    cv.arrow(226, 126, 360, 64, color=C["blue"], w=1.7)
    cv.text(145, 92, "i", size=10, weight=700, color=C["red"])
    cv.text(307, 92, "r", size=10, weight=700, color=C["blue"])
    cv.text(W / 2, 42, "i = r", size=10, weight=700, color=C["green"])
    return cv.svg()


def moon_phases_science2(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 7209))
    cv.text(W / 2, 18, "moon phases: the visible lit part changes with position", size=9.4, weight=700, color=C["soft"])
    cx, cy, r = 226, 112, 35
    cv.circle(78, cy, 24, color=C["amber"], w=1.4, fill=C["amber_bg"])
    cv.text(78, 153, "sun", size=8.3, weight=700, color=C["amber"])
    phases = [("new", 168, False), ("quarter", 226, True), ("full", 284, "full"), ("last", 342, "last")]
    for lab, x, state in phases:
        if state is False:
            cv.circle(x, cy, r, color=C["grey"], w=1.3, fill="#3a4050")
        elif state is True:
            cv.circle(x, cy, r, color=C["grey"], w=1.3, fill="#f6f2d7")
            cv.raw(f'<path d="M{x},{cy-r} A{r},{r} 0 0 1 {x},{cy+r} L{x},{cy-r} Z" fill="#3a4050"/>')
        elif state == "full":
            cv.circle(x, cy, r, color=C["grey"], w=1.3, fill="#f6f2d7")
        else:
            cv.circle(x, cy, r, color=C["grey"], w=1.3, fill="#f6f2d7")
            cv.raw(f'<path d="M{x},{cy-r} A{r},{r} 0 0 0 {x},{cy+r} L{x},{cy-r} Z" fill="#3a4050"/>')
        cv.text(x, 163, lab, size=8.0, weight=700, color=C["soft"])
    cv.arrow(108, cy, 140, cy, color=C["grey"], w=1.0)
    cv.text(W / 2, 207, "sunlight illuminates half; position changes what Earth sees", size=8.4, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── resources and environment ────────────────────
def water_resource_science2(spec):
    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 7210))
    cv.text(W / 2, 18, "water resource: rain can recharge surface and groundwater", size=9.5, weight=700, color=C["soft"])
    cv.line(45, 154, 407, 154, color=C["green"], w=1.7)
    cv.raw('<path d="M45 154 Q120 138 200 154 T407 154 L407 224 L45 224 Z" fill="#eaf3ff" stroke="none"/>')
    cv.line(45, 154, 407, 154, color=C["green"], w=1.7)
    cv.line(214, 154, 214, 224, color=C["blue"], w=2.0, dash="5 3")
    cv.text(230, 190, "groundwater", size=8.5, color=C["blue"], anchor="start")
    for x in (124, 155, 186):
        cv.line(x, 49, x - 15, 86, color=C["blue"], w=1.2)
        cv.arrow(x - 15, 86, x - 18, 103, color=C["blue"], w=1.0)
    cv.text(154, 40, "rain", size=8.5, weight=700, color=C["blue"])
    cv.arrow(214, 105, 214, 142, color=C["purple"], w=1.1)
    cv.text(226, 122, "recharge", size=8.2, color=C["purple"], anchor="start")
    _box(cv, 298, 63, 105, 32, "save + reuse", C["green"], C["green_bg"], size=8.2)
    cv.text(W / 2, H - 8, "use water carefully; recharge does not mean unlimited supply", size=8.4, color=C["red"], weight=700)
    return cv.svg()


# ───────────────────────────── science pedagogy ─────────────────────────────
def inquiry_cycle_science2(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 7211))
    cv.text(W / 2, 18, "science inquiry: evidence links a question to an explanation", size=9.4, weight=700, color=C["soft"])
    _flow(cv, ["question", "predict", "test", "evidence", "explain"], [C["red"], C["amber"], C["blue"], C["green"], C["purple"]], y=92, x0=48, x1=404)
    cv.arrow(362, 146, 92, 146, color=C["grey"], w=1.0)
    cv.text(W / 2, 153, "new evidence may lead to a new question", size=8.5, color=C["red"], weight=700)
    cv.text(W / 2, H - 8, "teacher guides; learners observe, reason and communicate", size=8.5, color=C["ink"])
    return cv.svg()


def variables_science2(spec):
    W, H = 452, 228
    cv = Canvas(W, H, seed=_seed(spec, 7212))
    cv.text(W / 2, 18, "fair test: change one factor and keep other conditions controlled", size=9.2, weight=700, color=C["soft"])
    _box(cv, 38, 64, 112, 42, "change", C["red"], C["red_bg"], size=9)
    _box(cv, 170, 64, 112, 42, "measure", C["blue"], C["blue_bg"], size=9)
    _box(cv, 302, 64, 112, 42, "control", C["green"], C["green_bg"], size=9)
    cv.arrow(154, 85, 166, 85, color=C["grey"], w=1.0)
    cv.arrow(286, 85, 298, 85, color=C["grey"], w=1.0)
    cv.line(94, 144, 358, 144, color=C["purple"], w=1.2, dash="5 3")
    cv.text(W / 2, 163, "repeat + record + compare", size=9, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "a fair comparison makes the conclusion more trustworthy", size=8.5, color=C["ink"])
    return cv.svg()


def observation_inference_science2(spec):
    W, H = 452, 224
    cv = Canvas(W, H, seed=_seed(spec, 7213))
    cv.text(W / 2, 18, "observation and inference are related but not identical", size=9.4, weight=700, color=C["soft"])
    _box(cv, 47, 60, 160, 58, "observation / noticed", C["blue"], C["blue_bg"], size=8.1)
    _box(cv, 245, 60, 160, 58, "inference / explanation", C["purple"], C["purple_bg"], size=8.0)
    cv.arrow(215, 89, 237, 89, color=C["grey"], w=1.1)
    cv.text(W / 2, 157, "record evidence first; explain with reasons and alternatives", size=8.7, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "a conclusion should be open to checking", size=8.6, color=C["ink"])
    return cv.svg()


def integrated_science2(spec):
    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 7214))
    cv.text(W / 2, 18, "an environmental question can connect science with other ways of knowing", size=9.0, weight=700, color=C["soft"])
    _box(cv, 161, 45, 130, 36, "water question", C["blue"], C["blue_bg"], size=9)
    nodes = [("science", 73, 133, C["green"]), ("maths", 180, 174, C["amber"]), ("society", 292, 174, C["purple"]), ("technology", 390, 133, C["red"])]
    for lab, x, y, col in nodes:
        _box(cv, x - 43, y - 16, 86, 32, lab, col, "#ffffff", size=8.1)
        cv.line(226, 81, x, y - 18, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "measure, investigate, decide and communicate", size=8.6, color=C["ink"])
    return cv.svg()


def assessment_science2(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 7215))
    cv.text(W / 2, 18, "science assessment can collect cognitive, practical and affective evidence", size=9.0, weight=700, color=C["soft"])
    nodes = [("concept", 90, 91, C["blue"], C["blue_bg"]), ("skill", 226, 91, C["green"], C["green_bg"]), ("attitude", 362, 91, C["purple"], C["purple_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 49, y - 20, 98, 40, lab, col, bg, size=8.8)
    cv.arrow(142, 91, 174, 91, color=C["grey"], w=1.0)
    cv.arrow(278, 91, 310, 91, color=C["grey"], w=1.0)
    cv.line(362, 124, 90, 124, color=C["red"], w=1.0, dash="5 3")
    cv.text(W / 2, 157, "observe + discuss + perform + reflect", size=9, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "use varied evidence to support the next learning step", size=8.6, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "balanced-plate-science2": balanced_plate,
    "separation-science2": separation_science2,
    "plant-transport-science2": plant_transport_science2,
    "food-web-science2": food_web_science2,
    "motion-graph-science2": motion_graph_science2,
    "circuit-science2": circuit_science2,
    "magnet-field-science2": magnet_field_science2,
    "reflection-ray-science2": reflection_ray_science2,
    "moon-phases-science2": moon_phases_science2,
    "water-resource-science2": water_resource_science2,
    "inquiry-cycle-science2": inquiry_cycle_science2,
    "variables-science2": variables_science2,
    "observation-inference-science2": observation_inference_science2,
    "integrated-science2": integrated_science2,
    "assessment-science2": assessment_science2,
}
