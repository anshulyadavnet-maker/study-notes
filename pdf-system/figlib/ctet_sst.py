"""Vector teaching figures for CTET Paper II Social Science MCQs.

Labels remain in Latin script for reliable SVG text rendering.  The figures
cover timelines, sources, maps, environment, government, inquiry and assessment.
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=8200):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{bg}" stroke="{col}" stroke-width="1.4"/>')
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _arrow_flow(cv, labels, colors, y=96, x0=46, x1=406):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 42, y - 18, 84, 36, label, col, "#ffffff", size=8.0)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 46, y, xs[i + 1] - 46, y, color=C["grey"], w=1.0)


def history_timeline_sst(spec):
    W, H = 452, 220
    cv = Canvas(W, H, seed=_seed(spec, 8201))
    cv.text(W / 2, 18, "timeline: sequence helps connect events and change", size=9.8, weight=700, color=C["soft"])
    x0, x1, y = 56, 396, 102
    cv.line(x0, y, x1, y, color=C["ink"], w=1.7)
    cv.arrow(x1 - 8, y, x1 + 8, y, color=C["ink"], w=1.1)
    events = [("early cities", 0.08, C["blue"]), ("early empire", 0.34, C["green"]), ("medieval", 0.60, C["purple"]), ("colonial", 0.82, C["red"])]
    for lab, pos, col in events:
        x = x0 + (x1 - x0) * pos
        cv.line(x, y - 12, x, y + 12, color=col, w=1.5)
        cv.dot(x, y, r=4.2, color=col)
        cv.text(x, y - 25 if int(pos * 10) % 2 else y + 31, lab, size=7.8, weight=700, color=col)
    _box(cv, 104, 166, 244, 27, "sequence + context + evidence", C["purple"], C["purple_bg"], size=9.0)
    return cv.svg()


def source_triangle_sst(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 8202))
    cv.text(W / 2, 18, "historical evidence: compare sources before making a claim", size=9.3, weight=700, color=C["soft"])
    _box(cv, 40, 60, 108, 40, "inscription", C["blue"], C["blue_bg"], size=8.3)
    _box(cv, 172, 60, 108, 40, "artifact", C["amber"], C["amber_bg"], size=8.3)
    _box(cv, 304, 60, 108, 40, "text", C["green"], C["green_bg"], size=8.3)
    cv.arrow(94, 111, 202, 157, color=C["grey"], w=1.0)
    cv.arrow(226, 111, 226, 157, color=C["grey"], w=1.0)
    cv.arrow(358, 111, 250, 157, color=C["grey"], w=1.0)
    _box(cv, 133, 157, 186, 38, "corroborated claim", C["purple"], C["purple_bg"], size=9.0)
    cv.text(W / 2, H - 8, "source + context + comparison", size=8.7, color=C["ink"])
    return cv.svg()


def medieval_arch_sst(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 8203))
    cv.text(W / 2, 18, "architecture: structure, material and purpose give historical clues", size=9.0, weight=700, color=C["soft"])
    cv.raw('<path d="M52 165 V104 Q82 62 112 104 V165 Z" fill="#eaf3ff" stroke="#1668c4" stroke-width="1.5"/>')
    cv.raw('<path d="M170 165 V104 Q200 62 230 104 V165 Z" fill="#e6f7ee" stroke="#127a4d" stroke-width="1.5"/>')
    cv.raw('<path d="M288 165 V104 Q318 62 348 104 V165 Z" fill="#fff3dc" stroke="#a8620a" stroke-width="1.5"/>')
    cv.line(52, 165, 112, 165, color=C["blue"], w=1.5); cv.line(170, 165, 230, 165, color=C["green"], w=1.5); cv.line(288, 165, 348, 165, color=C["amber"], w=1.5)
    cv.text(82, 188, "arch", size=8.4, weight=700, color=C["blue"])
    cv.text(200, 188, "vault", size=8.4, weight=700, color=C["green"])
    cv.text(318, 188, "dome", size=8.4, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "read buildings as evidence, not decoration only", size=8.5, color=C["purple"])
    return cv.svg()


def national_movement_sst(spec):
    W, H = 452, 234
    cv = Canvas(W, H, seed=_seed(spec, 8204))
    cv.text(W / 2, 18, "national movement: ideas, people and actions changed over time", size=9.1, weight=700, color=C["soft"])
    _arrow_flow(cv, ["policy", "protest", "mass action", "negotiation", "change"], [C["red"], C["amber"], C["blue"], C["purple"], C["green"]], y=88, x0=48, x1=404)
    _box(cv, 112, 147, 228, 34, "many groups, many methods, shared goal", C["purple"], C["purple_bg"], size=8.7)
    cv.text(W / 2, H - 8, "avoid reducing a movement to one event or one person", size=8.4, color=C["ink"])
    return cv.svg()


def globe_latitude_sst(spec):
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 8205))
    cv.text(W / 2, 18, "globe: latitude runs east-west; longitude runs pole to pole", size=9.0, weight=700, color=C["soft"])
    cx, cy, r = 165, 122, 74
    cv.circle(cx, cy, r, color=C["blue"], w=1.6, fill=C["blue_bg"])
    cv.ellipse(cx, cy, r, 27, color=C["green"], w=1.0)
    cv.ellipse(cx, cy, 27, r, color=C["purple"], w=1.0)
    cv.line(cx - r, cy, cx + r, cy, color=C["red"], w=1.5, dash="5 3")
    cv.text(cx + r + 13, cy + 4, "equator 0°", size=8.0, color=C["red"], anchor="start")
    cv.text(cx, cy - r - 13, "N", size=9, weight=700, color=C["purple"])
    cv.text(cx, cy + r + 18, "S", size=9, weight=700, color=C["purple"])
    _box(cv, 284, 78, 122, 36, "latitude", C["green"], C["green_bg"], size=8.5)
    _box(cv, 284, 132, 122, 36, "longitude", C["purple"], C["purple_bg"], size=8.5)
    return cv.svg()


def map_grid_sst(spec):
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 8206))
    cv.text(W / 2, 18, "map reading: grid, scale, direction and symbols work together", size=9.1, weight=700, color=C["soft"])
    x0, y0, s = 62, 52, 34
    for c in range(8):
        cv.line(x0 + c * s, y0, x0 + c * s, y0 + 5 * s, color="#cbd4e0", w=0.8)
    for r in range(6):
        cv.line(x0, y0 + r * s, x0 + 7 * s, y0 + r * s, color="#cbd4e0", w=0.8)
    cv.line(x0 + 20, y0 + 4 * s - 12, x0 + 6 * s, y0 + 18, color=C["red"], w=2.0)
    cv.dot(x0 + 20, y0 + 4 * s - 12, r=4, color=C["blue"]); cv.dot(x0 + 6 * s, y0 + 18, r=4, color=C["green"])
    cv.text(x0 + 20, y0 + 4 * s + 12, "A", size=8, weight=700, color=C["blue"])
    cv.text(x0 + 6 * s, y0 + 8, "B", size=8, weight=700, color=C["green"])
    _box(cv, 326, 63, 86, 30, "N", C["purple"], C["purple_bg"], size=9)
    _box(cv, 326, 111, 86, 30, "scale", C["amber"], C["amber_bg"], size=8.3)
    _box(cv, 326, 159, 86, 30, "legend", C["blue"], C["blue_bg"], size=8.3)
    return cv.svg()


def air_water_cycle_sst(spec):
    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 8207))
    cv.text(W / 2, 18, "air and water: natural processes connect atmosphere and surface", size=9.2, weight=700, color=C["soft"])
    _arrow_flow(cv, ["heat", "evaporation", "cloud", "rain", "runoff"], [C["red"], C["amber"], C["purple"], C["blue"], C["green"]], y=84, x0=48, x1=404)
    cv.line(58, 155, 394, 155, color=C["blue"], w=1.8)
    cv.raw('<path d="M58 155 Q145 138 225 155 T394 155 L394 207 L58 207 Z" fill="#eaf3ff" stroke="none"/>')
    cv.line(58, 155, 394, 155, color=C["blue"], w=1.8)
    cv.text(W / 2, 183, "surface water + groundwater + atmosphere", size=8.4, color=C["purple"], weight=700)
    return cv.svg()


def agriculture_sst(spec):
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 8208))
    cv.text(W / 2, 18, "agriculture depends on soil, water, climate, labour and markets", size=9.0, weight=700, color=C["soft"])
    nodes = [("soil", 75, 86, C["amber"]), ("water", 184, 54, C["blue"]), ("climate", 294, 54, C["purple"]), ("labour", 376, 110, C["red"]), ("market", 286, 176, C["green"]), ("crop", 136, 176, C["teal"])]
    for lab, x, y, col in nodes:
        _box(cv, x - 43, y - 16, 86, 32, lab, col, "#ffffff", size=8.0)
    for a, b in (((105, 87), (143, 170)), ((184, 70), (155, 160)), ((294, 70), (286, 160)), ((355, 118), (326, 164)), ((243, 176), (179, 176))):
        cv.arrow(*a, *b, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "human and physical factors interact", size=8.6, color=C["ink"])
    return cv.svg()


def government_levels_sst(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 8209))
    cv.text(W / 2, 18, "government works through connected levels and institutions", size=9.4, weight=700, color=C["soft"])
    _box(cv, 174, 46, 104, 36, "Union", C["red"], C["red_bg"], size=9)
    _box(cv, 174, 104, 104, 36, "State", C["blue"], C["blue_bg"], size=9)
    _box(cv, 174, 162, 104, 36, "Local", C["green"], C["green_bg"], size=9)
    cv.arrow(226, 87, 226, 99, color=C["grey"], w=1.0); cv.arrow(226, 145, 226, 157, color=C["grey"], w=1.0)
    _box(cv, 50, 104, 84, 36, "citizens", C["purple"], C["purple_bg"], size=8.2)
    _box(cv, 318, 104, 84, 36, "services", C["amber"], C["amber_bg"], size=8.2)
    cv.arrow(138, 122, 168, 122, color=C["grey"], w=1.0); cv.arrow(284, 122, 314, 122, color=C["grey"], w=1.0)
    return cv.svg()


def parliament_media_sst(spec):
    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 8210))
    cv.text(W / 2, 18, "democracy: representation, debate and public information", size=9.2, weight=700, color=C["soft"])
    _box(cv, 44, 64, 112, 42, "citizens", C["blue"], C["blue_bg"], size=9)
    _box(cv, 170, 64, 112, 42, "parliament", C["purple"], C["purple_bg"], size=8.7)
    _box(cv, 296, 64, 112, 42, "government", C["green"], C["green_bg"], size=8.7)
    cv.arrow(160, 85, 166, 85, color=C["grey"], w=1.0); cv.arrow(286, 85, 292, 85, color=C["grey"], w=1.0)
    _box(cv, 170, 145, 112, 42, "media", C["amber"], C["amber_bg"], size=9)
    cv.arrow(226, 112, 226, 139, color=C["red"], w=1.0)
    cv.arrow(282, 166, 350, 111, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "information enables questioning and accountability", size=8.5, color=C["ink"])
    return cv.svg()


def judiciary_sst(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 8211))
    cv.text(W / 2, 18, "judicial structure: disputes can move through levels of courts", size=9.2, weight=700, color=C["soft"])
    _box(cv, 174, 45, 104, 34, "Supreme", C["red"], C["red_bg"], size=8.8)
    _box(cv, 174, 100, 104, 34, "High Court", C["purple"], C["purple_bg"], size=8.5)
    _box(cv, 174, 155, 104, 34, "District", C["blue"], C["blue_bg"], size=8.8)
    cv.arrow(226, 82, 226, 94, color=C["grey"], w=1.0); cv.arrow(226, 137, 226, 149, color=C["grey"], w=1.0)
    _box(cv, 43, 100, 92, 34, "citizen", C["green"], C["green_bg"], size=8.7)
    cv.arrow(139, 117, 168, 117, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "independence + rule of law + remedy", size=8.6, color=C["ink"])
    return cv.svg()


def inquiry_cycle_sst(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 8212))
    cv.text(W / 2, 18, "social-science inquiry: question, source, interpretation and argument", size=9.0, weight=700, color=C["soft"])
    _arrow_flow(cv, ["question", "source", "compare", "interpret", "argue"], [C["red"], C["blue"], C["amber"], C["purple"], C["green"]], y=92, x0=48, x1=404)
    cv.arrow(362, 148, 92, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "new evidence may revise the argument", size=8.5, color=C["red"], weight=700)
    cv.text(W / 2, H - 8, "claims need evidence and context", size=8.6, color=C["ink"])
    return cv.svg()


def map_skills_sst(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 8213))
    cv.text(W / 2, 18, "map skill: locate, measure, interpret and communicate", size=9.2, weight=700, color=C["soft"])
    _arrow_flow(cv, ["locate", "scale", "pattern", "explain"], [C["blue"], C["amber"], C["purple"], C["green"]], y=88)
    _box(cv, 120, 147, 212, 34, "map + data + question", C["red"], C["red_bg"], size=9.0)
    cv.text(W / 2, H - 8, "a map is evidence, not just a picture to colour", size=8.5, color=C["ink"])
    return cv.svg()


def discussion_democracy_sst(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 8214))
    cv.text(W / 2, 18, "democratic discussion: listen, reason, respond and revise", size=9.2, weight=700, color=C["soft"])
    _arrow_flow(cv, ["listen", "evidence", "reason", "respond", "revise"], [C["blue"], C["green"], C["amber"], C["purple"], C["red"]], y=90, x0=48, x1=404)
    _box(cv, 102, 148, 248, 34, "respectful disagreement is learning", C["teal"], C["teal_bg"], size=8.8)
    cv.text(W / 2, H - 8, "roles and norms make participation more equitable", size=8.5, color=C["ink"])
    return cv.svg()


def assessment_sst(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 8215))
    cv.text(W / 2, 18, "SST assessment: knowledge, skills, reasoning and participation", size=9.0, weight=700, color=C["soft"])
    nodes = [("concept", 75, 90, C["blue"], C["blue_bg"]), ("source/map", 190, 90, C["green"], C["green_bg"]), ("argument", 305, 90, C["purple"], C["purple_bg"]), ("participate", 390, 150, C["amber"], C["amber_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 48, y - 18, 96, 36, lab, col, bg, size=8.0)
    cv.arrow(124, 90, 142, 90, color=C["grey"], w=1.0); cv.arrow(239, 90, 257, 90, color=C["grey"], w=1.0); cv.arrow(335, 105, 360, 137, color=C["grey"], w=1.0)
    cv.line(342, 165, 112, 165, color=C["red"], w=1.0, dash="5 3")
    cv.text(W / 2, 190, "feedback -> next teaching step", size=9, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "history-timeline-sst": history_timeline_sst,
    "source-triangle-sst": source_triangle_sst,
    "medieval-arch-sst": medieval_arch_sst,
    "national-movement-sst": national_movement_sst,
    "globe-latitude-sst": globe_latitude_sst,
    "map-grid-sst": map_grid_sst,
    "air-water-cycle-sst": air_water_cycle_sst,
    "agriculture-sst": agriculture_sst,
    "government-levels-sst": government_levels_sst,
    "parliament-media-sst": parliament_media_sst,
    "judiciary-sst": judiciary_sst,
    "inquiry-cycle-sst": inquiry_cycle_sst,
    "map-skills-sst": map_skills_sst,
    "discussion-democracy-sst": discussion_democracy_sst,
    "assessment-sst": assessment_sst,
}
