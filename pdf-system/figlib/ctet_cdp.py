"""Vector figures for CTET Child Development and Pedagogy revision notes.

SVG labels stay in Latin script for reliable WeasyPrint rendering. Hindi
explanations and captions belong in the Markdown note around each figure.
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=9100):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{bg}" stroke="{col}" stroke-width="1.4"/>')
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


def _flow(cv, labels, colors, y=92, x0=48, x1=404):
    step = (x1 - x0) / (len(labels) - 1)
    xs = [x0 + i * step for i in range(len(labels))]
    for i, (label, col) in enumerate(zip(labels, colors)):
        _box(cv, xs[i] - 43, y - 18, 86, 36, label, col, "#ffffff", size=8.0)
        if i < len(labels) - 1:
            cv.arrow(xs[i] + 47, y, xs[i + 1] - 47, y, color=C["grey"], w=1.0)


def development_domains(spec):
    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 9101))
    cv.text(W / 2, 18, "development is multidimensional and domains interact", size=9.3, weight=700, color=C["soft"])
    cx, cy = 226, 112
    cv.circle(cx, cy, 38, color=C["purple"], w=1.5, fill=C["purple_bg"])
    cv.text(cx, cy + 4, "child", size=9.5, weight=700, color=C["purple"])
    nodes = [("physical", 72, 62, C["red"], C["red_bg"]), ("cognitive", 380, 62, C["blue"], C["blue_bg"]),
             ("social-emotional", 72, 166, C["green"], C["green_bg"]), ("language", 380, 166, C["amber"], C["amber_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 50, y - 17, 100, 34, lab, col, bg, size=7.8)
        cv.line(cx + (x - cx) * .42, cy + (y - cy) * .42, x - (x - cx) * .21, y - (y - cy) * .21, color=col, w=1.0)
    cv.text(W / 2, H - 8, "growth in one domain can support learning in another", size=8.5, color=C["ink"])
    return cv.svg()


def heredity_environment(spec):
    W, H = 452, 226
    cv = Canvas(W, H, seed=_seed(spec, 9102))
    cv.text(W / 2, 18, "development emerges through heredity–environment interaction", size=9.1, weight=700, color=C["soft"])
    _box(cv, 40, 70, 126, 46, "heredity", C["blue"], C["blue_bg"], size=9.2)
    _box(cv, 286, 70, 126, 46, "environment", C["green"], C["green_bg"], size=8.6)
    cv.arrow(171, 82, 280, 82, color=C["grey"], w=1.1)
    cv.arrow(280, 104, 171, 104, color=C["grey"], w=1.1)
    _box(cv, 148, 148, 156, 38, "development", C["purple"], C["purple_bg"], size=9.2)
    cv.arrow(102, 121, 170, 145, color=C["blue"], w=1.0)
    cv.arrow(350, 121, 282, 145, color=C["green"], w=1.0)
    cv.text(W / 2, H - 8, "potential + experience + opportunity", size=8.6, color=C["ink"])
    return cv.svg()


def piaget_stages(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9103))
    cv.text(W / 2, 18, "Piaget: broad stages of cognitive development", size=9.7, weight=700, color=C["soft"])
    x0, y, step = 43, 104, 91
    stages = [("sensorimotor", "0–2", C["blue"], C["blue_bg"]), ("preoperational", "2–7", C["amber"], C["amber_bg"]),
              ("concrete", "7–11", C["green"], C["green_bg"]), ("formal", "11+", C["purple"], C["purple_bg"])]
    cv.line(x0, y, x0 + 3 * step, y, color=C["ink"], w=1.6)
    for i, (lab, age, col, bg) in enumerate(stages):
        x = x0 + i * step
        cv.dot(x, y, r=4, color=col)
        _box(cv, x - 40, y - 57, 80, 30, lab, col, bg, size=7.1)
        cv.text(x, y + 24, age, size=8.4, weight=700, color=col)
    _box(cv, 112, 171, 228, 28, "active child + changing schemas", C["red"], C["red_bg"], size=8.8)
    cv.text(W / 2, H - 8, "ages are approximate; observe the learner's reasoning", size=8.5, color=C["ink"])
    return cv.svg()


def zpd_scaffold(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 9104))
    cv.text(W / 2, 18, "ZPD: assisted performance can move toward independence", size=9.3, weight=700, color=C["soft"])
    _box(cv, 38, 75, 120, 48, "independent now", C["blue"], C["blue_bg"], size=8.5)
    _box(cv, 294, 75, 120, 48, "with support", C["green"], C["green_bg"], size=8.5)
    cv.arrow(167, 99, 285, 99, color=C["red"], w=1.5)
    cv.text(226, 79, "scaffold", size=8.5, weight=700, color=C["red"])
    _box(cv, 122, 154, 208, 34, "fade support -> new independence", C["purple"], C["purple_bg"], size=8.7)
    cv.arrow(354, 128, 319, 151, color=C["green"], w=1.0)
    cv.text(W / 2, H - 8, "prompt, model, practise, fade", size=8.5, color=C["ink"])
    return cv.svg()


def learning_cycle_cdp(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9105))
    cv.text(W / 2, 18, "constructive learning: experience becomes a revised understanding", size=9.0, weight=700, color=C["soft"])
    _flow(cv, ["prior idea", "experience", "discussion", "reflection", "new idea"], [C["blue"], C["green"], C["amber"], C["purple"], C["red"]], y=90, x0=47, x1=405)
    cv.arrow(363, 147, 91, 147, color=C["grey"], w=1.0)
    cv.text(W / 2, 154, "new learning can change the next question", size=8.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "learner is an active meaning-maker", size=8.6, color=C["ink"])
    return cv.svg()


def assessment_loop_cdp(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9106))
    cv.text(W / 2, 18, "assessment for learning: evidence changes the next teaching step", size=9.1, weight=700, color=C["soft"])
    _flow(cv, ["teach", "observe", "diagnose", "feedback", "adapt"], [C["blue"], C["green"], C["amber"], C["red"], C["purple"]], y=90, x0=47, x1=405)
    cv.arrow(363, 148, 91, 148, color=C["grey"], w=1.0)
    cv.text(W / 2, 155, "re-assess after support", size=8.6, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "assessment is part of teaching, not only a final score", size=8.5, color=C["ink"])
    return cv.svg()


def inclusion_udl(spec):
    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 9107))
    cv.text(W / 2, 18, "inclusive teaching removes barriers and offers flexible access", size=9.2, weight=700, color=C["soft"])
    _box(cv, 164, 45, 124, 36, "common goal", C["purple"], C["purple_bg"], size=9)
    nodes = [("see", 68, 128, C["blue"], C["blue_bg"]), ("hear", 166, 174, C["green"], C["green_bg"]),
             ("do", 286, 174, C["amber"], C["amber_bg"]), ("explain", 384, 128, C["red"], C["red_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 42, y - 16, 84, 32, lab, col, bg, size=8.2)
        cv.line(226, 82, x, y - 18, color=C["grey"], w=1.0)
    cv.text(W / 2, H - 8, "multiple ways to access, engage and show learning", size=8.5, color=C["ink"])
    return cv.svg()


def exam_dashboard_cdp(spec):
    W, H = 452, 228
    cv = Canvas(W, H, seed=_seed(spec, 9108))
    cv.text(W / 2, 18, "Paper I CDP at a glance", size=10.2, weight=700, color=C["soft"])
    cards = [("age 6–11", "primary", C["blue"], C["blue_bg"]),
             ("15 + 5 + 10", "30 questions", C["teal"], C["teal_bg"]),
             ("child first", "think + support", C["purple"], C["purple_bg"])]
    xs = [77, 226, 375]
    for x, (top, bottom, col, bg) in zip(xs, cards):
        _box(cv, x - 61, 53, 122, 61, top, col, bg, size=9.0)
        cv.text(x, 99, bottom, size=8.1, color=col)
    cv.arrow(143, 83, 158, 83, color=C["grey"], w=1.0)
    cv.arrow(292, 83, 307, 83, color=C["grey"], w=1.0)
    _box(cv, 78, 151, 296, 32, "observe → understand → scaffold → reassess", C["red"], C["red_bg"], size=9.0)
    cv.text(W / 2, H - 8, "application beats rote recall", size=8.7, weight=700, color=C["ink"])
    return cv.svg()


def theory_map_cdp(spec):
    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 9109))
    cv.text(W / 2, 18, "four theory lenses for one classroom child", size=9.4, weight=700, color=C["soft"])
    cx, cy = 226, 120
    _box(cv, 174, 101, 104, 38, "child", C["purple"], C["purple_bg"], size=10)
    nodes = [("Piaget\nschemas", 75, 63, C["blue"], C["blue_bg"]),
             ("Vygotsky\nsocial support", 377, 63, C["green"], C["green_bg"]),
             ("Kohlberg\nreasoning", 75, 184, C["amber"], C["amber_bg"]),
             ("Bruner\nspiral", 377, 184, C["red"], C["red_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 55, y - 19, 110, 38, lab.replace("\n", " / "), col, bg, size=7.8)
        cv.line(cx + (x - cx) * .35, cy + (y - cy) * .35, x - (x - cx) * .23, y - (y - cy) * .23, color=col, w=1.0)
    cv.text(W / 2, H - 8, "use the lens that explains the learner's response", size=8.4, color=C["ink"])
    return cv.svg()


def motivation_paths_cdp(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9110))
    cv.text(W / 2, 18, "motivation: purpose, choice and feedback shape persistence", size=9.1, weight=700, color=C["soft"])
    _box(cv, 44, 61, 160, 46, "intrinsic: interest + mastery", C["blue"], C["blue_bg"], size=8.0)
    _box(cv, 248, 61, 160, 46, "extrinsic: reward + consequence", C["amber"], C["amber_bg"], size=7.7)
    _box(cv, 140, 146, 172, 38, "meaningful goal", C["green"], C["green_bg"], size=9.0)
    cv.arrow(124, 111, 176, 143, color=C["blue"], w=1.0)
    cv.arrow(328, 111, 276, 143, color=C["amber"], w=1.0)
    cv.text(W / 2, 211, "choice + achievable challenge + specific feedback", size=8.5, weight=700, color=C["purple"])
    return cv.svg()


def teacher_response_cdp(spec):
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 9111))
    cv.text(W / 2, 18, "most-appropriate response: a repeatable decision path", size=9.1, weight=700, color=C["soft"])
    _flow(cv, ["observe", "ask", "diagnose", "support", "re-check"], [C["blue"], C["green"], C["amber"], C["red"], C["purple"]], y=91, x0=48, x1=404)
    cv.arrow(362, 149, 91, 149, color=C["grey"], w=1.0)
    cv.text(W / 2, 156, "new evidence changes the next step", size=8.6, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "never jump from one error to a permanent label", size=8.5, color=C["ink"])
    return cv.svg()


def answer_ladder_cdp(spec):
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 9112))
    cv.text(W / 2, 18, "CDP answer ladder", size=10, weight=700, color=C["soft"])
    steps = [("1  notice the child", C["blue"], C["blue_bg"]),
             ("2  understand the context", C["teal"], C["teal_bg"]),
             ("3  choose inclusive support", C["green"], C["green_bg"]),
             ("4  use evidence again", C["purple"], C["purple_bg"])]
    x, y0, w, h = 60, 48, 332, 33
    for i, (lab, col, bg) in enumerate(steps):
        y = y0 + i * 39
        _box(cv, x + i * 8, y, w - i * 16, h, lab, col, bg, size=8.7)
    cv.text(W / 2, H - 8, "child-centred · inclusive · evidence-based", size=8.6, weight=700, color=C["red"])
    return cv.svg()


def _cat_face(cv, cx, cy, scale=1.0, col=None):
    col = col or C["purple"]
    r = 25 * scale
    cv.circle(cx, cy, r, color=col, w=1.8, fill=C["purple_bg"])
    cv.polygon([(cx-r*.7, cy-r*.55), (cx-r*.95, cy-r*1.25), (cx-r*.18, cy-r*.82)], color=col, w=1.5, fill=C["purple_bg"])
    cv.polygon([(cx+r*.7, cy-r*.55), (cx+r*.95, cy-r*1.25), (cx+r*.18, cy-r*.82)], color=col, w=1.5, fill=C["purple_bg"])
    cv.dot(cx-r*.35, cy-r*.08, r=2.0*scale, color=col)
    cv.dot(cx+r*.35, cy-r*.08, r=2.0*scale, color=col)
    cv.polygon([(cx, cy+r*.12), (cx-r*.16, cy+r*.28), (cx+r*.16, cy+r*.28)], color=col, w=1.0, fill=col)
    cv.line(cx, cy+r*.28, cx, cy+r*.5, color=col, w=1.0)
    cv.line(cx-r*.16, cy+r*.45, cx-r*.58, cy+r*.35, color=col, w=1.0)
    cv.line(cx+r*.16, cy+r*.45, cx+r*.58, cy+r*.35, color=col, w=1.0)
    cv.line(cx-r*.55, cy+r*.2, cx-r*1.0, cy+r*.05, color=col, w=1.0)
    cv.line(cx+r*.55, cy+r*.2, cx+r*1.0, cy+r*.05, color=col, w=1.0)


def _dog_face(cv, cx, cy, scale=1.0, col=None):
    col = col or C["amber"]
    r = 25 * scale
    cv.ellipse(cx, cy, r, r*.95, color=col, w=1.8, fill=C["amber_bg"])
    cv.polygon([(cx-r*.7, cy-r*.45), (cx-r*1.32, cy-r*.1), (cx-r*1.02, cy+r*.7), (cx-r*.48, cy+r*.38)], color=col, w=1.5, fill=C["amber_bg"])
    cv.polygon([(cx+r*.7, cy-r*.45), (cx+r*1.32, cy-r*.1), (cx+r*1.02, cy+r*.7), (cx+r*.48, cy+r*.38)], color=col, w=1.5, fill=C["amber_bg"])
    cv.dot(cx-r*.35, cy-r*.08, r=2.0*scale, color=col)
    cv.dot(cx+r*.35, cy-r*.08, r=2.0*scale, color=col)
    cv.ellipse(cx, cy+r*.18, r*.23, r*.16, color=col, w=1.2, fill=col)
    cv.line(cx, cy+r*.32, cx, cy+r*.53, color=col, w=1.0)
    cv.arc(cx, cy+r*.35, r*.35, 0.15, math.pi-.15, color=col, w=1.0)


def learning_theories_cdp(spec):
    W, H = 452, 318
    cv = Canvas(W, H, seed=_seed(spec, 9113))
    cv.text(W / 2, 18, "learning theories: different explanations, different classroom clues", size=8.9, weight=700, color=C["soft"])
    cards = [
        (34, 43, "Thorndike", "trial + error", C["purple"], C["purple_bg"]),
        (236, 43, "Pavlov", "classical conditioning", C["amber"], C["amber_bg"]),
        (34, 183, "Skinner", "consequence + reinforcement", C["blue"], C["blue_bg"]),
        (236, 183, "Bandura", "model + observation", C["green"], C["green_bg"]),
    ]
    for x, y, title, sub, col, bg in cards:
        _box(cv, x, y, 182, 108, title, col, bg, size=9.8)
        cv.text(x + 91, y + 96, sub, size=7.6, color=col)
    _cat_face(cv, 82, 96, .62, C["purple"])
    cv.text(146, 89, "puzzle", size=7.8, color=C["purple"], anchor="start")
    cv.arrow(132, 105, 170, 105, color=C["purple"], w=1.0)
    cv.text(146, 120, "effect", size=7.8, color=C["purple"], anchor="start")
    _dog_face(cv, 284, 96, .62, C["amber"])
    cv.circle(347, 95, 13, color=C["amber"], w=1.2, fill=C["amber_bg"])
    cv.text(347, 99, "bell", size=6.8, color=C["amber"])
    cv.arrow(311, 96, 332, 96, color=C["amber"], w=1.0)
    cv.line(80, 236, 80, 264, color=C["blue"], w=4.0)
    cv.circle(80, 229, 10, color=C["blue"], w=1.2, fill=C["blue_bg"])
    cv.text(111, 244, "reinforcement", size=7.8, color=C["blue"], anchor="start")
    cv.circle(282, 229, 12, color=C["green"], w=1.3, fill=C["green_bg"])
    cv.circle(282, 229, 4, color=C["green"], w=1.0, fill=C["green_bg"])
    cv.text(306, 244, "observe → imitate", size=7.8, color=C["green"], anchor="start")
    cv.text(W / 2, H - 8, "theory name → mechanism → appropriate classroom use", size=8.4, color=C["ink"])
    return cv.svg()


def paper2_dashboard_cdp(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 9114))
    cv.text(W / 2, 18, "Paper II CDP at a glance", size=10.0, weight=700, color=C["soft"])
    cards = [("age 11–14", "elementary", C["blue"], C["blue_bg"]),
             ("15 + 5 + 10", "30 questions", C["teal"], C["teal_bg"]),
             ("think deeper", "support identity", C["purple"], C["purple_bg"])]
    for x, (top, bottom, col, bg) in zip((76, 226, 376), cards):
        _box(cv, x - 57, 49, 114, 59, top, col, bg, size=10.4 if x != 226 else 11.8)
        cv.text(x, 96, bottom, size=7.8, color=col)
    cv.arrow(135, 78, 165, 78, color=C["grey"], w=1.0)
    cv.arrow(285, 78, 315, 78, color=C["grey"], w=1.0)
    _box(cv, 63, 147, 326, 34, "observe → discuss → challenge → support", C["red"], C["red_bg"], size=8.9)
    cv.text(W / 2, H - 8, "elementary learner + subject context + autonomy", size=8.4, color=C["ink"])
    return cv.svg()


def adolescence_cdp(spec):
    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 9115))
    cv.text(W / 2, 18, "adolescence: change across connected domains", size=9.4, weight=700, color=C["soft"])
    _box(cv, 165, 91, 122, 42, "learner", C["purple"], C["purple_bg"], size=10)
    nodes = [("physical", 73, 64, C["red"], C["red_bg"]), ("cognitive", 379, 64, C["blue"], C["blue_bg"]),
             ("identity", 73, 174, C["amber"], C["amber_bg"]), ("peer/social", 379, 174, C["green"], C["green_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 52, y - 17, 104, 34, lab, col, bg, size=8.1)
        cv.line(226 + (x - 226) * .25, 112 + (y - 112) * .25, x - (x - 226) * .22, y - (y - 112) * .22, color=col, w=1.0)
    cv.text(W / 2, H - 8, "growth is variable; support dignity, voice and belonging", size=8.5, color=C["ink"])
    return cv.svg()


def peer_identity_cdp(spec):
    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 9116))
    cv.text(W / 2, 18, "identity and self-concept are shaped in relationships", size=9.1, weight=700, color=C["soft"])
    _box(cv, 166, 94, 120, 42, "self-concept", C["purple"], C["purple_bg"], size=9.2)
    nodes = [("family", 74, 62, C["blue"], C["blue_bg"]), ("peers", 378, 62, C["green"], C["green_bg"]),
             ("school", 74, 177, C["amber"], C["amber_bg"]), ("media", 378, 177, C["red"], C["red_bg"])]
    for lab, x, y, col, bg in nodes:
        _box(cv, x - 45, y - 17, 90, 34, lab, col, bg, size=8.4)
        cv.line(226 + (x - 226) * .25, 115 + (y - 115) * .25, x - (x - 226) * .22, y - (y - 115) * .22, color=col, w=1.0)
    cv.text(W / 2, H - 8, "respect + autonomy + feedback + belonging", size=8.5, color=C["ink"])
    return cv.svg()


def abstract_reasoning_cdp(spec):
    W, H = 452, 228
    cv = Canvas(W, H, seed=_seed(spec, 9117))
    cv.text(W / 2, 18, "elementary-stage reasoning can move beyond the concrete", size=9.1, weight=700, color=C["soft"])
    _flow(cv, ["concrete", "abstract", "hypothetical", "critical"], [C["blue"], C["green"], C["amber"], C["purple"]], y=88, x0=54, x1=398)
    _box(cv, 100, 146, 252, 33, "represent → generalise → test → justify", C["red"], C["red_bg"], size=8.8)
    cv.text(W / 2, H - 8, "do not skip support; extend thinking step by step", size=8.5, color=C["ink"])
    return cv.svg()


def paper2_assessment_cdp(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 9118))
    cv.text(W / 2, 18, "Paper II assessment: more than recall", size=9.4, weight=700, color=C["soft"])
    _flow(cv, ["concept", "application", "reasoning", "reflection"], [C["blue"], C["green"], C["amber"], C["purple"]], y=88, x0=54, x1=398)
    cv.arrow(350, 146, 102, 146, color=C["grey"], w=1.0)
    cv.text(W / 2, 153, "feedback → revision → independent learning", size=8.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "use subject evidence and learner explanation", size=8.6, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "cdp-development-domains": development_domains,
    "cdp-heredity-environment": heredity_environment,
    "cdp-piaget-stages": piaget_stages,
    "cdp-zpd-scaffold": zpd_scaffold,
    "cdp-learning-cycle": learning_cycle_cdp,
    "cdp-assessment-loop": assessment_loop_cdp,
    "cdp-inclusion-udl": inclusion_udl,
    "cdp-exam-dashboard": exam_dashboard_cdp,
    "cdp-theory-map": theory_map_cdp,
    "cdp-motivation-paths": motivation_paths_cdp,
    "cdp-teacher-response": teacher_response_cdp,
    "cdp-answer-ladder": answer_ladder_cdp,
    "cdp-learning-theories": learning_theories_cdp,
    "cdp-paper2-dashboard": paper2_dashboard_cdp,
    "cdp-adolescence": adolescence_cdp,
    "cdp-peer-identity": peer_identity_cdp,
    "cdp-abstract-reasoning": abstract_reasoning_cdp,
    "cdp-paper2-assessment": paper2_assessment_cdp,
}
