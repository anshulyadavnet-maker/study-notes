"""
quadrilaterals.py — visual figures for Chapter 36 (Quadrilaterals & Polygons).

quad-types          : parallelogram, rectangle, square, rhombus, kite, trapezium
quad-diagonals      : diagonals and their special properties
cyclic-quad         : cyclic quadrilateral on a circle
polygon-diagonals   : diagonals drawn from one vertex
regular-polygon     : equal sides and exterior-angle structure
trapezium-midline   : mid-segment parallel to both bases
quad-area           : area model for common quadrilaterals
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3600):
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


def _points(shape):
    if shape == "square":
        return [(55, 45), (205, 45), (205, 195), (55, 195)]
    if shape == "rectangle":
        return [(42, 65), (232, 65), (232, 175), (42, 175)]
    if shape == "parallelogram":
        return [(78, 50), (244, 50), (204, 180), (38, 180)]
    if shape == "rhombus":
        return [(140, 36), (238, 112), (140, 188), (42, 112)]
    if shape == "kite":
        return [(140, 32), (228, 110), (140, 190), (58, 110)]
    # trapezium
    return [(68, 52), (212, 52), (250, 180), (30, 180)]


def _labels(cv, pts):
    for lab, pt, dx, dy in zip("ABCD", pts, (-12, 12, 12, -12), (-8, -8, 12, 12)):
        cv.text(pt[0] + dx, pt[1] + dy, lab, size=10.8, weight=700)


def _parallel_marks(cv, p, color=C["green"]):
    cv.ticks(p[0], p[1], count=1, color=color)
    cv.ticks(p[2], p[3], count=1, color=color)


def _right_marks(cv, pts):
    for pt, p1, p2 in ((pts[0], pts[1], pts[3]), (pts[1], pts[0], pts[2]),
                       (pts[2], pts[1], pts[3]), (pts[3], pts[0], pts[2])):
        cv.right_angle(pt[0], pt[1], p1, p2, size=10, color=C["red"])


# ───────────────────────────── quadrilateral types ──────────────────────────
def quad_types(spec):
    shape = str(spec.get("shape", "parallelogram")).lower()
    pts = _points(shape)
    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 3601))
    cv.text(W / 2, 20, f"{shape}: identify the defining properties from the diagram",
            size=9.8, weight=700, color=C["soft"])
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    _labels(cv, pts)
    if shape in ("parallelogram", "rectangle", "square"):
        _parallel_marks(cv, pts)
        cv.ticks(pts[1], pts[2], count=2, color=C["amber"])
        cv.ticks(pts[3], pts[0], count=2, color=C["amber"])
    if shape in ("rectangle", "square"):
        _right_marks(cv, pts)
    if shape in ("square", "rhombus"):
        for i in range(4): cv.ticks(pts[i], pts[(i + 1) % 4], count=1, color=C["purple"])
    if shape == "kite":
        cv.ticks(pts[0], pts[1], count=1, color=C["green"])
        cv.ticks(pts[0], pts[3], count=1, color=C["green"])
        cv.ticks(pts[1], pts[2], count=2, color=C["amber"])
        cv.ticks(pts[2], pts[3], count=2, color=C["amber"])
    if shape == "trapezium":
        cv.ticks(pts[0], pts[1], count=1, color=C["green"])
        cv.ticks(pts[2], pts[3], count=1, color=C["green"])
    notes = {
        "parallelogram": "opposite sides parallel and equal",
        "rectangle": "four right angles; diagonals equal",
        "square": "all sides equal and four right angles",
        "rhombus": "all sides equal; diagonals perpendicular",
        "kite": "two pairs of adjacent equal sides",
        "trapezium": "one pair of opposite sides parallel",
    }
    _card(cv, 52, 218, 348, 28, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 237, notes.get(shape, "quadrilateral"), size=9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── diagonals ────────────────────────────────────
def quad_diagonals(spec):
    shape = str(spec.get("shape", "parallelogram")).lower()
    pts = _points(shape)
    W, H = 452, 256
    cv = Canvas(W, H, seed=_seed(spec, 3602))
    cv.text(W / 2, 20, f"diagonals of a {shape} reveal extra properties",
            size=10, weight=700, color=C["soft"])
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    _labels(cv, pts)
    cv.line(*pts[0], *pts[2], color=C["red"], w=1.5, dash="4 3")
    cv.line(*pts[1], *pts[3], color=C["red"], w=1.5, dash="4 3")
    M = ((pts[0][0] + pts[2][0]) / 2, (pts[0][1] + pts[2][1]) / 2)
    N = ((pts[1][0] + pts[3][0]) / 2, (pts[1][1] + pts[3][1]) / 2)
    cv.dot(*M, r=3.6, color=C["purple"]); cv.dot(*N, r=3.6, color=C["purple"])
    if shape in ("rhombus", "square", "kite"):
        cv.right_angle(M[0], M[1], pts[0], pts[1], size=11, color=C["purple"])
    if shape in ("parallelogram", "rectangle", "square", "rhombus"):
        cv.ticks(pts[0], M, count=1, color=C["green"])
        cv.ticks(M, pts[2], count=1, color=C["green"])
        cv.ticks(pts[1], N, count=2, color=C["amber"])
        cv.ticks(N, pts[3], count=2, color=C["amber"])
    notes = {
        "parallelogram": "diagonals bisect each other",
        "rectangle": "diagonals bisect and are equal",
        "rhombus": "diagonals bisect at 90 deg",
        "square": "diagonals bisect, equal and perpendicular",
        "kite": "one diagonal bisects the other at 90 deg",
    }
    _card(cv, 62, 214, 328, 26, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 232, notes.get(shape, "diagonals connect opposite vertices"),
            size=8.8, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── cyclic quadrilateral ─────────────────────────
def cyclic_quad(spec):
    W, H = 320, 250
    cx, cy, r = 158, 118, 86
    cv = Canvas(W, H, seed=_seed(spec, 3603))
    cv.text(W / 2, 20, "a cyclic quadrilateral has all four vertices on a circle",
            size=9.8, weight=700, color=C["soft"])
    cv.circle(cx, cy, r, color=C["blue"], w=1.6, fill=C["blue_bg"])
    angles = [150, 45, -35, 235]
    pts = [(cx + r * math.cos(math.radians(a)), cy - r * math.sin(math.radians(a))) for a in angles]
    cv.polygon(pts, color=C["green"], w=1.7, fill=None)
    for lab, pt in zip("ABCD", pts):
        cv.dot(*pt, r=3, color=C["red"])
        cv.text(pt[0] + (10 if pt[0] > cx else -10), pt[1] + (13 if pt[1] > cy else -8),
                lab, size=10.5, weight=700)
    cv.text(78, 214, "angle A + angle C = 180 deg", size=9, color=C["red"], weight=700)
    cv.text(78, 231, "angle B + angle D = 180 deg", size=9, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── polygon diagonals ────────────────────────────
def polygon_diagonals(spec):
    n = int(spec.get("sides", 7))
    W, H = 300, 240
    cx, cy, r = 150, 100, 76
    cv = Canvas(W, H, seed=_seed(spec, 3604))
    cv.text(W / 2, 20, f"from one vertex of an {n}-gon, draw all diagonals",
            size=9.8, weight=700, color=C["soft"])
    pts = [(cx + r * math.cos(-math.pi/2 + 2*math.pi*i/n),
            cy + r * math.sin(-math.pi/2 + 2*math.pi*i/n)) for i in range(n)]
    cv.polygon(pts, color=C["blue"], w=1.7, fill=C["blue_bg"])
    for i in range(2, n - 1):
        cv.line(*pts[0], *pts[i], color=C["red"], w=1.2, dash="4 3")
    cv.text(W / 2, 199, f"diagonals from one vertex = n-3 = {n-3}",
            size=9.5, color=C["red"], weight=700)
    cv.text(W / 2, 217, f"total diagonals = n(n-3)/2 = {n*(n-3)//2}",
            size=9.2, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── regular polygon ──────────────────────────────
def regular_polygon(spec):
    n = int(spec.get("sides", 6))
    W, H = 300, 228
    cx, cy, r = 125, 104, 72
    cv = Canvas(W, H, seed=_seed(spec, 3605))
    pts = [(cx + r * math.cos(-math.pi/2 + 2*math.pi*i/n),
            cy + r * math.sin(-math.pi/2 + 2*math.pi*i/n)) for i in range(n)]
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    for i in range(n): cv.ticks(pts[i], pts[(i+1) % n], count=1, color=C["green"], size=5)
    ext = 360 / n
    cv.text(230, 72, f"n = {n}", size=11, weight=700, color=C["purple"])
    cv.text(230, 96, f"exterior = 360/{n}", size=9, color=C["red"])
    cv.text(230, 116, f"= {_fmt(ext)} deg", size=9.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "equal sides, equal angles, equal exterior turns", size=8.7, color=C["soft"])
    return cv.svg()


# ───────────────────────────── trapezium midline ────────────────────────────
def trapezium_midline(spec):
    a = float(spec.get("a", 14)); b = float(spec.get("b", 8)); h = float(spec.get("height", 6))
    mid = (a + b) / 2
    W, H = 360, 250
    cv = Canvas(W, H, seed=_seed(spec, 3606))
    cv.text(W / 2, 20, "the mid-segment is parallel to both bases",
            size=9.9, weight=700, color=C["soft"])
    x0, y0, scale = 72, 188, 14
    lower = a * scale; upper = b * scale; hh = h * scale
    p = [(x0, y0), (x0 + lower, y0), (x0 + (lower + upper) / 2, y0 - hh),
         (x0 + (lower - upper) / 2, y0 - hh)]
    cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    D = ((p[0][0] + p[3][0]) / 2, (p[0][1] + p[3][1]) / 2)
    E = ((p[1][0] + p[2][0]) / 2, (p[1][1] + p[2][1]) / 2)
    cv.line(*D, *E, color=C["red"], w=2)
    cv.text(x0 + lower / 2, y0 + 17, f"a={_fmt(a)}", size=9.5, color=C["purple"], weight=700)
    cv.text((p[2][0] + p[3][0]) / 2, p[2][1] - 12, f"b={_fmt(b)}", size=9.5, color=C["purple"], weight=700)
    cv.text((D[0] + E[0]) / 2, (D[1] + E[1]) / 2 - 8, f"mid={_fmt(mid)}", size=9, color=C["red"], weight=700)
    _card(cv, 66, 214, 228, 24, C["green"], C["green_bg"], sw=1.4)
    cv.text(180, 231, "mid-segment = (a+b)/2", size=9.2, weight=700, color=C["green"])
    return cv.svg()


# ───────────────────────────── area shapes ──────────────────────────────────
def quad_area(spec):
    shape = str(spec.get("shape", "parallelogram")).lower()
    W, H = 320, 226
    cv = Canvas(W, H, seed=_seed(spec, 3607))
    cv.text(W / 2, 20, f"area formula for a {shape}", size=10.2, weight=700, color=C["soft"])
    if shape == "parallelogram":
        b, h = 10, 6
        p = [(54, 174), (226, 174), (260, 66), (88, 66)]
        formula = "Area = base x height"
        val = b*h
        cv.line(88, 66, 88, 174, color=C["red"], w=1.3, dash="4 3")
        cv.right_angle(88, 174, (110, 174), (88, 66), size=10, color=C["red"])
    elif shape == "rhombus":
        d1, d2 = 12, 8
        p = [(150, 40), (244, 112), (150, 184), (56, 112)]
        formula = "Area = 1/2 x d1 x d2"
        val = d1*d2/2
        cv.line(56, 112, 244, 112, color=C["red"], w=1.2, dash="4 3")
        cv.line(150, 40, 150, 184, color=C["red"], w=1.2, dash="4 3")
        cv.right_angle(150, 112, (170, 112), (150, 92), size=9, color=C["red"])
    else:  # trapezium
        a, b, h = 14, 8, 6
        p = [(50, 174), (260, 174), (220, 66), (90, 66)]
        formula = "Area = 1/2 x (a+b) x h"
        val = (a+b)*h/2
        cv.line(90, 66, 90, 174, color=C["red"], w=1.2, dash="4 3")
        cv.right_angle(90, 174, (110, 174), (90, 66), size=9, color=C["red"])
    cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    _card(cv, 40, 202, 240, 24, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(160, 219, formula, size=8.9, weight=700, color=C["purple"])
    cv.text(160, H - 7, f"example value = {_fmt(val)} square units", size=8.8, color=C["green"])
    return cv.svg()


REGISTRY = {
    "quad-types": quad_types,
    "quad-diagonals": quad_diagonals,
    "cyclic-quad": cyclic_quad,
    "polygon-diagonals": polygon_diagonals,
    "regular-polygon36": regular_polygon,
    "trapezium-midline": trapezium_midline,
    "quad-area": quad_area,
}
