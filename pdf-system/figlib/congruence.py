"""
congruence.py — visual figures for Chapter 35 (Congruence & Similarity).

congruence-rule  : SSS, SAS, ASA or RHS matching marks
not-congruent    : AAA gives same shape but not necessarily same size
similar-aa       : equal angles and proportional corresponding sides
scale-factor     : side, perimeter and area scale relationships
bpt-parallel     : Basic Proportionality Theorem diagram
shadow-similarity : similar triangles from a height and its shadow
cpctc            : corresponding parts of congruent triangles
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3500):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=6, sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
           f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _triangle(cv, ox, oy, scale, labels):
    p = [(ox, oy), (ox + 116 * scale, oy), (ox + 38 * scale, oy - 90 * scale)]
    cv.polygon(p, color=C["blue"], w=1.7, fill=C["blue_bg"])
    for lab, pt, dx, dy in zip(labels, p, (-12, 12, 0), (7, 7, -9)):
        cv.text(pt[0] + dx, pt[1] + dy, lab, size=10.5, weight=700)
    return p


def _fmt(value):
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _mark_sides(cv, p, rule, color):
    if rule == "SSS":
        for i, count in enumerate((1, 2, 3)):
            cv.ticks(p[i], p[(i + 1) % 3], count=count, color=color)
    elif rule == "SAS":
        cv.ticks(p[0], p[1], count=1, color=color)
        cv.ticks(p[0], p[2], count=2, color=color)
        cv.arc(p[0][0], p[0][1], 20, 0, 62, color=C["red"], w=1.2)
    elif rule == "ASA":
        cv.ticks(p[0], p[1], count=1, color=color)
        cv.arc(p[0][0], p[0][1], 18, 0, 62, color=C["red"], w=1.2)
        cv.arc(p[1][0], p[1][1], 18, 118, 180, color=C["purple"], w=1.2)
    elif rule == "RHS":
        cv.right_angle(p[0][0], p[0][1], p[1], p[2], size=12, color=C["red"])
        cv.ticks(p[1], p[2], count=1, color=color)
        cv.ticks(p[2], p[0], count=2, color=color)


# ───────────────────────────── congruence rules ────────────────────────────
def congruence_rule(spec):
    rule = str(spec.get("rule", "SSS")).upper()
    W, H = 452, 260
    cv = Canvas(W, H, seed=_seed(spec, 3501))
    cv.text(W / 2, 20, f"{rule}: enough matching parts prove congruence",
            size=10.2, weight=700, color=C["soft"])
    p1 = _triangle(cv, 34, 190, 0.95, ["A", "B", "C"])
    p2 = _triangle(cv, 254, 190, 0.78, ["P", "Q", "R"])
    _mark_sides(cv, p1, rule, C["blue"])
    _mark_sides(cv, p2, rule, C["green"])
    _card(cv, 94, 218, 264, 28, C["purple"], C["purple_bg"], sw=1.6)
    notes = {"SSS": "3 sides match", "SAS": "2 sides + included angle",
             "ASA": "2 angles + included side", "RHS": "right angle + hypotenuse + side"}
    cv.text(226, 237, f"{rule}: {notes.get(rule, 'matching data')} -> congruent",
            size=8.9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── AAA caution ──────────────────────────────────
def not_congruent(spec):
    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 3502))
    cv.text(W / 2, 20, "AAA fixes shape, but not necessarily size",
            size=10.2, weight=700, color=C["soft"])
    p1 = _triangle(cv, 38, 180, 0.9, ["A", "B", "C"])
    p2 = _triangle(cv, 270, 180, 0.58, ["P", "Q", "R"])
    for p, col in ((p1, C["blue"]), (p2, C["green"])):
        for i in range(3):
            cv.arc(p[i][0], p[i][1], 15, 0, 45, color=col, w=1.1)
    _card(cv, 88, 214, 276, 28, C["red"], C["red_bg"], sw=1.6)
    cv.text(226, 233, "AAA -> similar, not necessarily congruent",
            size=9.2, weight=700, color=C["red"])
    return cv.svg()


# ───────────────────────────── AA similarity ───────────────────────────────
def similar_aa(spec):
    W, H = 452, 264
    cv = Canvas(W, H, seed=_seed(spec, 3503))
    cv.text(W / 2, 20, "AA similarity: two corresponding angles equal",
            size=10.3, weight=700, color=C["soft"])
    p1 = _triangle(cv, 36, 190, 0.95, ["A", "B", "C"])
    p2 = _triangle(cv, 258, 190, 0.72, ["P", "Q", "R"])
    for p, col in ((p1, C["red"]), (p2, C["green"])):
        cv.arc(p[0][0], p[0][1], 18, 0, 56, color=col, w=1.2)
        cv.arc(p[1][0], p[1][1], 18, 120, 180, color=col, w=1.2)
    _card(cv, 76, 218, 300, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 238, "A=P, B=Q -> triangle ABC similar to PQR",
            size=8.9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── scale factor ──────────────────────────────────
def scale_factor(spec):
    k = float(spec.get("k", 2))
    small = float(spec.get("small", 3))
    large = small * k
    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 3504))
    cv.text(W / 2, 20, "similar figures scale sides by k and areas by k squared",
            size=9.8, weight=700, color=C["soft"])
    _card(cv, 38, 48, 164, 58, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(120, 69, "small triangle", size=9.5, weight=700, color=C["blue"])
    cv.text(120, 91, f"side = {_fmt(small)}", size=11, color=C["blue"])
    _card(cv, 250, 48, 164, 58, C["green"], C["green_bg"], sw=1.6)
    cv.text(332, 69, "large triangle", size=9.5, weight=700, color=C["green"])
    cv.text(332, 91, f"side = {_fmt(large)}", size=11, color=C["green"])
    rows = [("side ratio", f"{_fmt(k)}:1", C["blue"]),
            ("perimeter ratio", f"{_fmt(k)}:1", C["purple"]),
            ("area ratio", f"{_fmt(k*k)}:1", C["red"])]
    for i, (lab, value, col) in enumerate(rows):
        y = 132 + i * 30
        _card(cv, 74, y, 304, 23, col, "#ffffff", r=5, sw=1.1)
        cv.text(88, y + 16, lab, size=8.7, anchor="start", color=C["soft"])
        cv.text(364, y + 16, value, size=9.2, anchor="end", weight=700, color=col)
    return cv.svg()


# ───────────────────────────── BPT / parallel line ──────────────────────────
def bpt_parallel(spec):
    W, H = 330, 250
    cv = Canvas(W, H, seed=_seed(spec, 3505))
    cv.text(W / 2, 20, "a line parallel to one side divides the other sides proportionally",
            size=9.3, weight=700, color=C["soft"])
    A, B, Cc = (46, 196), (278, 196), (142, 52)
    cv.polygon([A, B, Cc], color=C["blue"], w=1.8, fill=C["blue_bg"])
    # D on AB and E on AC, DE parallel BC
    D = (A[0] + 0.55 * (B[0] - A[0]), A[1] + 0.55 * (B[1] - A[1]))
    E = (A[0] + 0.55 * (Cc[0] - A[0]), A[1] + 0.55 * (Cc[1] - A[1]))
    cv.line(*D, *E, color=C["red"], w=1.8)
    cv.text(A[0] - 12, A[1] + 7, "A", size=10.5, weight=700)
    cv.text(B[0] + 12, B[1] + 7, "B", size=10.5, weight=700)
    cv.text(Cc[0], Cc[1] - 10, "C", size=10.5, weight=700)
    cv.text(D[0], D[1] + 17, "D", size=10.5, color=C["red"], weight=700)
    cv.text(E[0] - 12, E[1] - 4, "E", size=10.5, color=C["red"], weight=700)
    cv.text(W / 2, 222, "AD/DB = AE/EC", size=10, color=C["purple"], weight=700)
    cv.text(W / 2, H - 8, "DE || BC -> triangles ADE and ABC are similar",
            size=8.6, color=C["ink"])
    return cv.svg()


# ───────────────────────────── shadow similarity ────────────────────────────
def shadow_similarity(spec):
    height = float(spec.get("height", 6))
    shadow = float(spec.get("shadow", 4))
    known_h = float(spec.get("known_height", 1.5))
    known_shadow = float(spec.get("known_shadow", 1))
    object_shadow = height * known_shadow / known_h
    W, H = 452, 260
    cv = Canvas(W, H, seed=_seed(spec, 3506))
    cv.text(W / 2, 20, "same sun angle creates similar right triangles",
            size=10, weight=700, color=C["soft"])
    ground = 176
    # object
    x1 = 112
    cv.line(x1, ground, x1, ground - 110, color=C["blue"], w=4)
    cv.line(x1, ground, x1 + object_shadow * 20, ground, color=C["blue"], w=2)
    cv.text(x1 - 10, ground - 55, f"{_fmt(height)}", size=9.5, color=C["blue"], anchor="end", weight=700)
    cv.text(x1 + object_shadow * 10, ground + 17, f"{_fmt(object_shadow)}", size=9.5, color=C["blue"], weight=700)
    # known stick
    x2 = 310
    cv.line(x2, ground, x2, ground - 55, color=C["green"], w=4)
    cv.line(x2, ground, x2 + known_shadow * 20, ground, color=C["green"], w=2)
    cv.text(x2 - 10, ground - 28, f"{_fmt(known_h)}", size=9.2, color=C["green"], anchor="end", weight=700)
    cv.text(x2 + known_shadow * 10, ground + 17, f"{_fmt(known_shadow)}", size=9.2, color=C["green"], weight=700)
    # common rays
    cv.line(x1, ground - 110, x2 + known_shadow * 20, ground, color=C["amber"], w=1.2, dash="4 3")
    _card(cv, 56, 208, 340, 28, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 227, f"height/shadow = {_fmt(height)}/{_fmt(object_shadow)} = {_fmt(known_h)}/{_fmt(known_shadow)}",
            size=8.9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── CPCTC ────────────────────────────────────────
def cpctc(spec):
    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 3507))
    cv.text(W / 2, 20, "after congruence, corresponding parts are equal",
            size=10, weight=700, color=C["soft"])
    p1 = _triangle(cv, 38, 180, 0.9, ["A", "B", "C"])
    p2 = _triangle(cv, 268, 180, 0.72, ["P", "Q", "R"])
    cv.ticks(p1[0], p1[1], count=1); cv.ticks(p2[0], p2[1], count=1)
    cv.ticks(p1[1], p1[2], count=2); cv.ticks(p2[1], p2[2], count=2)
    cv.arc(p1[0][0], p1[0][1], 18, 0, 55, color=C["red"], w=1.2)
    cv.arc(p2[0][0], p2[0][1], 18, 0, 55, color=C["red"], w=1.2)
    _card(cv, 68, 212, 316, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 230, "ABC congruent to PQR -> AB=PQ, angle A=angle P",
            size=8.5, weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "congruence-rule": congruence_rule,
    "not-congruent": not_congruent,
    "similar-aa": similar_aa,
    "scale-factor": scale_factor,
    "bpt-parallel": bpt_parallel,
    "shadow-similarity": shadow_similarity,
    "cpctc": cpctc,
}
