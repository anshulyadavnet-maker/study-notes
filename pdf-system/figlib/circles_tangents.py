"""
circles_tangents.py — visual figures for Chapter 37 (Circles & Tangents).

circle-parts37          : centre, radius, diameter, chord, arc and sector
chord-perpendicular     : perpendicular from centre bisects a chord
equal-chords            : equal chords are equally distant from centre
center-angle            : central angle is twice an inscribed angle
same-segment             : angles in the same segment are equal
semicircle-angle         : angle in a semicircle is a right angle
tangent-radius           : tangent is perpendicular to radius at contact
tangent-chord            : tangent-chord theorem / alternate segment
two-tangents             : equal tangents from an external point
common-direct-tangent    : direct common tangent to two circles
common-transverse-tangent: transverse common tangent to two circles
circle-measure           : circumference, area, arc and sector measures
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3700):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=6, sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
           f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(value):
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _pt(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def _arc(cv, cx, cy, r, start, end, color=None, width=1.3):
    cv.arc(cx, cy, r, math.radians(-end), math.radians(-start),
           color=color or C["red"], w=width)


def _circle(cv, cx, cy, r, fill=True):
    cv.circle(cx, cy, r, color=C["blue"], w=1.7,
              fill=C["blue_bg"] if fill else None)
    cv.dot(cx, cy, r=2.7, color=C["ink"])
    cv.text(cx - 8, cy + 15, "O", size=10.5, weight=700)


# ───────────────────────────── circle parts ────────────────────────────────
def circle_parts37(spec):
    W, H = 452, 270
    cx, cy, r = 148, 116, 78
    cv = Canvas(W, H, seed=_seed(spec, 3701))
    cv.text(W / 2, 20, "parts of a circle used throughout geometry",
            size=10.2, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    R = _pt(cx, cy, r, 30)
    cv.line(cx, cy, *R, color=C["green"], w=1.5)
    cv.text((cx + R[0]) / 2 + 5, (cy + R[1]) / 2 - 7, "radius", size=8.7,
            color=C["green"], weight=700)
    D1, D2 = _pt(cx, cy, r, 180), _pt(cx, cy, r, 0)
    cv.line(*D1, *D2, color=C["purple"], w=1.3)
    cv.text(cx, cy - 8, "diameter", size=8.5, color=C["purple"], weight=700)
    A, B = _pt(cx, cy, r, 205), _pt(cx, cy, r, 325)
    cv.line(*A, *B, color=C["amber"], w=1.7)
    cv.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 - 8, "chord", size=8.8,
            color=C["amber"], weight=700)
    _arc(cv, cx, cy, r, 25, 115, C["red"], 2)
    cv.text(238, 58, "arc", size=9, color=C["red"], weight=700)
    _card(cv, 278, 92, 142, 48, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(349, 112, "sector", size=10, weight=700, color=C["purple"])
    cv.text(349, 130, "two radii + arc", size=8.1, color=C["soft"])
    cv.text(W / 2, H - 8, "diameter = 2 x radius", size=9, color=C["ink"])
    return cv.svg()


# ───────────────────────────── chord perpendicular ─────────────────────────
def chord_perpendicular(spec):
    W, H = 452, 260
    cx, cy, r = 150, 124, 86
    cv = Canvas(W, H, seed=_seed(spec, 3702))
    cv.text(W / 2, 20, "a perpendicular from the centre bisects a chord",
            size=10, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    A, B = _pt(cx, cy, r, 205), _pt(cx, cy, r, 335)
    M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
    cv.line(*A, *B, color=C["amber"], w=1.8)
    cv.line(cx, cy, *M, color=C["red"], w=1.5, dash="4 3")
    cv.right_angle(M[0], M[1], A, (cx, cy), size=11, color=C["red"])
    cv.ticks(A, M, count=1, color=C["green"]); cv.ticks(M, B, count=1, color=C["green"])
    cv.text(A[0] - 12, A[1] + 5, "A", size=10.5, weight=700)
    cv.text(B[0] + 12, B[1] + 5, "B", size=10.5, weight=700)
    cv.text(M[0], M[1] + 18, "M", size=10, color=C["red"], weight=700)
    _card(cv, 60, 218, 300, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(210, 236, "OM perpendicular AB -> AM = MB", size=9.1, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── equal chords ─────────────────────────────────
def equal_chords(spec):
    W, H = 452, 272
    cx, cy, r = 225, 132, 96
    cv = Canvas(W, H, seed=_seed(spec, 3703))
    cv.text(W / 2, 20, "equal chords are equally distant from the centre",
            size=9.9, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    A, B = _pt(cx, cy, r, 150), _pt(cx, cy, r, 30)
    Cc, D = _pt(cx, cy, r, 215), _pt(cx, cy, r, 325)
    M1, M2 = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2), ((Cc[0] + D[0]) / 2, (Cc[1] + D[1]) / 2)
    cv.line(*A, *B, color=C["blue"], w=1.8)
    cv.line(*Cc, *D, color=C["green"], w=1.8)
    cv.line(cx, cy, *M1, color=C["red"], w=1.3, dash="4 3")
    cv.line(cx, cy, *M2, color=C["red"], w=1.3, dash="4 3")
    cv.ticks(A, M1, count=1, color=C["purple"]); cv.ticks(M1, B, count=1, color=C["purple"])
    cv.ticks(Cc, M2, count=1, color=C["purple"]); cv.ticks(M2, D, count=1, color=C["purple"])
    cv.text(W / 2, H - 28, "AB = CD  ->  distance from O to AB = distance from O to CD", size=8.5,
            color=C["purple"], weight=700)
    cv.text(W / 2, H - 9, "equal chords subtend equal central angles", size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── central and inscribed angle ───────────────────
def center_angle(spec):
    W, H = 452, 270
    cx, cy, r = 142, 130, 90
    cv = Canvas(W, H, seed=_seed(spec, 3704))
    cv.text(W / 2, 20, "angle at the centre is twice angle at the circumference",
            size=9.8, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    A, B, P = _pt(cx, cy, r, 205), _pt(cx, cy, r, 335), _pt(cx, cy, r, 70)
    cv.line(cx, cy, *A, color=C["red"], w=1.3)
    cv.line(cx, cy, *B, color=C["red"], w=1.3)
    cv.line(*P, *A, color=C["green"], w=1.5)
    cv.line(*P, *B, color=C["green"], w=1.5)
    _arc(cv, cx, cy, 28, 205, 335, C["red"], 1.5)
    _arc(cv, P[0], P[1], 25, 205, 335, C["green"], 1.4)
    cv.text(cx, cy + 38, "2x", size=11, color=C["red"], weight=700)
    cv.text(P[0], P[1] + 20, "x", size=11, color=C["green"], weight=700)
    cv.text(P[0], P[1] - 10, "P", size=10.5, weight=700)
    cv.text(W / 2, H - 10, "central angle = 2 x angle in the same arc", size=8.9, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── same segment ─────────────────────────────────
def same_segment(spec):
    W, H = 452, 266
    cx, cy, r = 226, 132, 92
    cv = Canvas(W, H, seed=_seed(spec, 3705))
    cv.text(W / 2, 20, "angles standing on the same chord are equal",
            size=9.9, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    A, B = _pt(cx, cy, r, 205), _pt(cx, cy, r, 335)
    P, Q = _pt(cx, cy, r, 100), _pt(cx, cy, r, 260)
    cv.line(*A, *B, color=C["amber"], w=1.7)
    for X, col, label in ((P, C["blue"], "x"), (Q, C["green"], "y")):
        cv.line(*X, *A, color=col, w=1.3)
        cv.line(*X, *B, color=col, w=1.3)
        cv.text(X[0] + (8 if X[0] > cx else -8), X[1] - 8, label, size=10.5, color=col, weight=700)
    cv.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 + 18, "common chord AB", size=8.7, color=C["amber"], weight=700)
    _card(cv, 80, 218, 292, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 236, "angle APB = angle AQB", size=9.3, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── semicircle ───────────────────────────────────
def semicircle_angle(spec):
    W, H = 452, 254
    cx, cy, r = 226, 160, 104
    cv = Canvas(W, H, seed=_seed(spec, 3706))
    cv.text(W / 2, 20, "the angle in a semicircle is always a right angle",
            size=10, weight=700, color=C["soft"])
    A, B = (cx-r, cy), (cx+r, cy)
    P = _pt(cx, cy, r, 65)
    cv.arc(cx, cy, r, 0, 180, color=C["blue"], w=1.8)
    cv.line(*A, *B, color=C["purple"], w=1.6)
    cv.line(*P, *A, color=C["green"], w=1.6)
    cv.line(*P, *B, color=C["green"], w=1.6)
    cv.right_angle(P[0], P[1], A, B, size=13, color=C["red"])
    cv.text(A[0] - 12, A[1] + 6, "A", size=10.5, weight=700)
    cv.text(B[0] + 12, B[1] + 6, "B", size=10.5, weight=700)
    cv.text(P[0], P[1] - 10, "P", size=10.5, weight=700)
    _card(cv, 98, 206, 256, 26, C["red"], C["red_bg"], sw=1.4)
    cv.text(226, 224, "angle APB = 90 deg", size=10, weight=700, color=C["red"])
    return cv.svg()


# ───────────────────────────── tangent radius ───────────────────────────────
def tangent_radius(spec):
    W, H = 452, 260
    cx, cy, r = 148, 132, 78
    cv = Canvas(W, H, seed=_seed(spec, 3707))
    cv.text(W / 2, 20, "radius to the point of contact is perpendicular to tangent",
            size=9.5, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    T = (cx, cy-r)
    cv.line(cx-100, T[1], cx+150, T[1], color=C["red"], w=1.8)
    cv.line(cx, cy, *T, color=C["green"], w=1.6)
    cv.right_angle(T[0], T[1], (cx+20, T[1]), (cx, cy), size=13, color=C["red"])
    cv.dot(*T, r=3.2, color=C["red"])
    cv.text(T[0]+9, T[1]-8, "T", size=10.5, color=C["red"], weight=700)
    cv.text(cx+8, (cy+T[1])/2, "r", size=10.5, color=C["green"], weight=700)
    cv.text(286, T[1]-7, "tangent", size=9.2, color=C["red"], weight=700, anchor="start")
    _card(cv, 78, 218, 286, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(221, 236, "OT perpendicular tangent at T", size=9.1, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── tangent chord ────────────────────────────────
def tangent_chord(spec):
    W, H = 452, 270
    cx, cy, r = 150, 140, 80
    cv = Canvas(W, H, seed=_seed(spec, 3708))
    cv.text(W / 2, 20, "angle between tangent and chord equals angle in alternate segment",
            size=9.3, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    T = _pt(cx, cy, r, 90)
    A, B = _pt(cx, cy, r, 205), _pt(cx, cy, r, 25)
    cv.line(*A, *B, color=C["blue"], w=1.7)
    cv.line(cx-100, T[1], cx+150, T[1], color=C["red"], w=1.7)
    cv.line(*T, *A, color=C["green"], w=1.4)
    cv.line(*T, *B, color=C["green"], w=1.4)
    _arc(cv, T[0], T[1], 24, 180, 250, C["red"], 1.3)
    _arc(cv, cx, cy, 28, 205, 335, C["green"], 1.3)
    cv.text(T[0]+8, T[1]-8, "T", size=10, weight=700)
    cv.text(300, T[1]-8, "tangent angle", size=8.8, color=C["red"], weight=700, anchor="start")
    cv.text(W/2, H-10, "tangent-chord angle = angle in the alternate segment", size=8.8, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── equal tangents ───────────────────────────────
def two_tangents(spec):
    W, H = 452, 270
    cx, cy, r = 170, 132, 68
    P = (360, 132)
    cv = Canvas(W, H, seed=_seed(spec, 3709))
    cv.text(W / 2, 20, "tangents drawn from the same external point are equal",
            size=10, weight=700, color=C["soft"])
    _circle(cv, cx, cy, r)
    for ang in (38, -38):
        T = _pt(cx, cy, r, ang)
        cv.line(*P, *T, color=C["red"], w=1.7)
        cv.line(cx, cy, *T, color=C["green"], w=1.1, dash="4 3")
        cv.right_angle(T[0], T[1], P, (cx, cy), size=10, color=C["green"])
        cv.dot(*T, r=3, color=C["red"])
    cv.dot(*P, r=3, color=C["red"])
    cv.text(P[0]+8, P[1]+5, "P", size=10.5, weight=700, anchor="start")
    cv.text(250, 72, "PA", size=10, color=C["red"], weight=700)
    cv.text(250, 204, "PB", size=10, color=C["red"], weight=700)
    _card(cv, 84, 224, 292, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(230, 242, "PA = PB", size=11, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── common direct tangent ────────────────────────
def common_direct_tangent(spec):
    W, H = 452, 270
    c1, c2, y, r1, r2 = 130, 300, 140, 48, 78
    cv = Canvas(W, H, seed=_seed(spec, 3710))
    cv.text(W / 2, 20, "direct common tangent touches both circles on one side",
            size=9.6, weight=700, color=C["soft"])
    cv.circle(c1, y, r1, color=C["blue"], w=1.6, fill=C["blue_bg"])
    cv.circle(c2, y, r2, color=C["green"], w=1.6, fill=C["green_bg"])
    cv.line(c1-80, y-r1-25, c2+90, y-r2-25, color=C["red"], w=1.8)
    cv.line(c1, y, c1, y-r1-25, color=C["grey"], w=1.0, dash="3 3")
    cv.line(c2, y, c2, y-r2-25, color=C["grey"], w=1.0, dash="3 3")
    cv.dot(c1, y, r=2.5); cv.dot(c2, y, r=2.5)
    cv.text(c1, y+8, "O1", size=9, weight=700)
    cv.text(c2, y+8, "O2", size=9, weight=700)
    d = c2-c1
    length = math.sqrt(d*d-(r2-r1)**2)
    _card(cv, 74, 220, 304, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 238, f"direct tangent length = sqrt(d^2-(R-r)^2) ~ {_fmt(length)}",
            size=8.4, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── common transverse tangent ────────────────────
def common_transverse_tangent(spec):
    W, H = 452, 270
    c1, c2, y, r1, r2 = 130, 300, 140, 48, 62
    cv = Canvas(W, H, seed=_seed(spec, 3711))
    cv.text(W / 2, 20, "transverse common tangents cross between the circles",
            size=9.7, weight=700, color=C["soft"])
    cv.circle(c1, y, r1, color=C["blue"], w=1.6, fill=C["blue_bg"])
    cv.circle(c2, y, r2, color=C["green"], w=1.6, fill=C["green_bg"])
    cv.line(c1-70, y-r1-18, c2+70, y+r2+18, color=C["red"], w=1.7)
    cv.line(c1-70, y+r1+18, c2+70, y-r2-18, color=C["red"], w=1.7)
    cv.dot(c1, y, r=2.5); cv.dot(c2, y, r=2.5)
    d = c2-c1
    length = math.sqrt(d*d-(r1+r2)**2)
    _card(cv, 64, 220, 324, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 238, f"transverse tangent length = sqrt(d^2-(R+r)^2) ~ {_fmt(length)}",
            size=8.2, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── circle measures ──────────────────────────────
def circle_measure(spec):
    r = float(spec.get("radius", 7))
    angle = float(spec.get("angle", 90))
    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 3712))
    cv.text(W / 2, 20, "circle measures: circumference, area, arc and sector",
            size=9.7, weight=700, color=C["soft"])
    rows = [("circumference", "2 pi r", 2*math.pi*r, C["blue"], C["blue_bg"]),
            ("area", "pi r^2", math.pi*r*r, C["green"], C["green_bg"]),
            ("arc", f"{_fmt(angle)}/360 x 2 pi r", angle/360*2*math.pi*r, C["amber"], C["amber_bg"]),
            ("sector area", f"{_fmt(angle)}/360 x pi r^2", angle/360*math.pi*r*r, C["purple"], C["purple_bg"])]
    for i, (lab, formula, val, col, bg) in enumerate(rows):
        y = 48 + i * 40
        _card(cv, 34, y, 384, 30, col, bg, r=5, sw=1.3)
        cv.text(48, y+20, lab, size=8.5, anchor="start", weight=700, color=col)
        cv.text(244, y+20, formula, size=8.3, anchor="middle", color=col)
        cv.text(404, y+20, _fmt(val), size=8.9, anchor="end", weight=700, color=col)
    cv.text(W/2, H-8, f"r={_fmt(r)}, angle={_fmt(angle)} degrees; pi kept symbolic in exams",
            size=8.5, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "circle-parts37": circle_parts37,
    "chord-perpendicular": chord_perpendicular,
    "equal-chords": equal_chords,
    "center-angle": center_angle,
    "same-segment": same_segment,
    "semicircle-angle": semicircle_angle,
    "tangent-radius": tangent_radius,
    "tangent-chord": tangent_chord,
    "two-tangents": two_tangents,
    "common-direct-tangent": common_direct_tangent,
    "common-transverse-tangent": common_transverse_tangent,
    "circle-measure": circle_measure,
}
