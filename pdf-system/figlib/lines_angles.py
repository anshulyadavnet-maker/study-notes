"""
lines_angles.py — visual figures for Chapter 33 (Lines & Angles).

point-line-ray       : point, line, ray and segment vocabulary
angle-types          : acute, right, obtuse, straight and reflex angles
angle-pairs          : complementary, supplementary, adjacent and linear pairs
vertical-angles      : vertically opposite angles at an intersection
parallel-transversal : two parallel lines cut by a transversal
parallel-angle-chase : a given angle propagated through parallel lines
perpendicular        : perpendicular lines and four right angles
triangle-angle-sum   : three interior angles adding to 180 degrees
triangle-exterior    : exterior angle theorem
polygon-sum          : n-gon diagonals and interior-angle sum
regular-polygon      : equal exterior angles in a regular polygon
angle-bisector       : a ray dividing an angle into two equal parts
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3300):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=6, sw=1.4):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
        f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>'
    )


def _fmt(value):
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _ray(cv, vx, vy, length, angle, color=None, width=1.7):
    a = math.radians(angle)
    return (vx + length * math.cos(a), vy - length * math.sin(a))


def _angle(cv, vx, vy, r, start_deg, end_deg, color=None, width=1.3):
    cv.arc(vx, vy, r, math.radians(-end_deg), math.radians(-start_deg),
           color=color or C["red"], w=width)


# ───────────────────────────── point, line, ray, segment ────────────────────
def point_line_ray(spec):
    W, H = 452, 254
    cv = Canvas(W, H, seed=_seed(spec, 3301))
    cv.text(W / 2, 20, "the four basic objects of line geometry",
            size=10.4, weight=700, color=C["soft"])

    rows = [("line AB", 44, "extends both ways", "A", "B", "line"),
            ("ray CD", 94, "starts at C", "C", "D", "ray"),
            ("segment EF", 144, "two fixed endpoints", "E", "F", "segment")]
    for i, (lab, y, note, left, right, kind) in enumerate(rows):
        col = [C["blue"], C["green"], C["purple"]][i]
        cv.text(36, y + 5, lab, size=8.8, anchor="start", weight=700, color=col)
        if kind == "line":
            cv.arrow(118, y, 36, y, color=col, w=1.4)
            cv.arrow(360, y, 402, y, color=col, w=1.4)
        elif kind == "ray":
            cv.dot(126, y, r=3.2, color=col)
            cv.arrow(126, y, 402, y, color=col, w=1.4)
        else:
            cv.line(126, y, 402, y, color=col, w=1.7)
            cv.dot(126, y, r=3.1, color=col)
            cv.dot(402, y, r=3.1, color=col)
        cv.text(126, y - 9, left, size=8.5, color=col, anchor="middle", weight=700)
        cv.text(402, y - 9, right, size=8.5, color=col, anchor="middle", weight=700)
        cv.text(420, y + 4, note, size=7.5, color=C["soft"], anchor="start")
    cv.text(W / 2, 204, "point = exact position; line has no endpoint; ray has one; segment has two",
            size=8.7, color=C["ink"])
    cv.text(W / 2, H - 8, "symbols and diagrams must match the wording",
            size=8.7, color=C["soft"])
    return cv.svg()


# ───────────────────────────── angle types ──────────────────────────────────
def angle_types(spec):
    kind = str(spec.get("kind", "acute")).lower()
    degrees = {"zero": 0, "acute": 45, "right": 90, "obtuse": 125,
               "straight": 180, "reflex": 225, "complete": 360}.get(kind, 45)
    degrees = float(spec.get("degrees", degrees))
    W, H = 300, 220
    vx, vy, length = 72, 158, 114
    cv = Canvas(W, H, seed=_seed(spec, 3302))
    if degrees < 360:
        p1 = _ray(cv, vx, vy, length, 0)
        p2 = _ray(cv, vx, vy, length, degrees)
        cv.line(vx, vy, *p1, color=C["blue"], w=1.8)
        cv.line(vx, vy, *p2, color=C["blue"], w=1.8)
        if kind == "right":
            cv.right_angle(vx, vy, p1, p2, size=14, color=C["red"])
        elif degrees > 0:
            _angle(cv, vx, vy, 34, 0, degrees, C["red"], 1.4)
        if degrees > 0:
            a = math.radians(degrees / 2)
            cv.text(vx + 48 * math.cos(a), vy - 48 * math.sin(a) + 4,
                    f"{_fmt(degrees)} deg", size=9.8, color=C["red"], weight=700)
    else:
        cv.circle(vx, vy, 36, color=C["red"], w=1.5, fill=C["red_bg"])
        cv.dot(vx, vy, r=3)
        cv.text(vx + 48, vy - 20, "360 deg", size=10, color=C["red"], weight=700)
    cv.dot(vx, vy, r=2.7, color=C["ink"])
    cv.text(vx - 12, vy + 7, "O", size=10.5, weight=700)
    cv.text(190, 64, str(kind), size=14, weight=700, color=C["purple"])
    cv.text(190, 88, "0 < acute < 90", size=8.5, color=C["soft"])
    cv.text(190, 106, "right = 90", size=8.5, color=C["soft"])
    cv.text(190, 124, "90 < obtuse < 180", size=8.5, color=C["soft"])
    cv.text(190, 142, "straight = 180", size=8.5, color=C["soft"])
    cv.text(W / 2, H - 8, "reflex lies between 180 and 360 degrees",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── angle pairs ──────────────────────────────────
def angle_pairs(spec):
    kind = str(spec.get("kind", "linear")).lower()
    W, H = 330, 226
    cv = Canvas(W, H, seed=_seed(spec, 3303))
    vx, vy = 92, 130
    if kind in ("complementary", "right"):
        p1 = _ray(cv, vx, vy, 112, 0)
        p2 = _ray(cv, vx, vy, 112, 90)
        pm = _ray(cv, vx, vy, 112, 38)
        cv.line(vx, vy, *p1, color=C["blue"], w=1.7)
        cv.line(vx, vy, *p2, color=C["blue"], w=1.7)
        cv.line(vx, vy, *pm, color=C["green"], w=1.6)
        _angle(cv, vx, vy, 31, 0, 38, C["red"])
        _angle(cv, vx, vy, 42, 38, 90, C["purple"])
        cv.right_angle(vx, vy, p1, p2, size=13, color=C["grey"])
        note = "complementary: x + y = 90"
    elif kind in ("supplementary", "linear"):
        p1 = _ray(cv, vx, vy, 118, 0)
        p2 = _ray(cv, vx, vy, 118, 180)
        pm = _ray(cv, vx, vy, 118, 62)
        cv.line(vx, vy, *p1, color=C["blue"], w=1.7)
        cv.line(vx, vy, *p2, color=C["blue"], w=1.7)
        cv.line(vx, vy, *pm, color=C["green"], w=1.6)
        _angle(cv, vx, vy, 31, 0, 62, C["red"])
        _angle(cv, vx, vy, 42, 62, 180, C["purple"])
        note = "linear pair: x + y = 180"
    else:  # adjacent
        p1 = _ray(cv, vx, vy, 118, 0)
        p2 = _ray(cv, vx, vy, 118, 62)
        p3 = _ray(cv, vx, vy, 118, 128)
        for p, col in ((p1, C["blue"]), (p2, C["green"]), (p3, C["purple"])):
            cv.line(vx, vy, *p, color=col, w=1.6)
        _angle(cv, vx, vy, 28, 0, 62, C["red"])
        _angle(cv, vx, vy, 40, 62, 128, C["amber"])
        note = "adjacent: common vertex and common arm"
    cv.dot(vx, vy, r=2.7)
    cv.text(205, 76, note, size=10, weight=700, color=C["soft"])
    cv.text(205, 101, "angles share a vertex", size=8.6, color=C["ink"])
    cv.text(205, 119, "and do not overlap", size=8.6, color=C["ink"])
    cv.text(W / 2, H - 8, "identify the pair before applying 90 or 180",
            size=8.6, color=C["red"])
    return cv.svg()


# ───────────────────────────── vertical angles ──────────────────────────────
def vertical_angles(spec):
    W, H = 310, 220
    cx, cy = 142, 104
    cv = Canvas(W, H, seed=_seed(spec, 3304))
    cv.text(W / 2, 20, "intersecting lines create equal opposite angles",
            size=9.9, weight=700, color=C["soft"])
    cv.line(34, 174, 250, 34, color=C["blue"], w=1.8)
    cv.line(34, 34, 250, 174, color=C["green"], w=1.8)
    cv.dot(cx, cy, r=2.8)
    _angle(cv, cx, cy, 35, 34, 146, C["red"])
    _angle(cv, cx, cy, 35, 214, 326, C["red"])
    _angle(cv, cx, cy, 45, 146, 214, C["purple"])
    _angle(cv, cx, cy, 45, 326, 394, C["purple"])
    cv.text(cx, cy - 45, "a", size=11, weight=700, color=C["red"])
    cv.text(cx, cy + 55, "a", size=11, weight=700, color=C["red"])
    cv.text(cx - 55, cy + 3, "b", size=11, weight=700, color=C["purple"])
    cv.text(cx + 55, cy + 3, "b", size=11, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "a = a and b = b; adjacent pair sums to 180",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── parallel transversal ─────────────────────────
def parallel_transversal(spec):
    W, H = 360, 258
    cv = Canvas(W, H, seed=_seed(spec, 3305))
    cv.text(W / 2, 20, "a transversal creates eight related angles",
            size=10.1, weight=700, color=C["soft"])
    y1, y2 = 72, 158
    cv.line(28, y1, 332, y1, color=C["blue"], w=1.8)
    cv.line(28, y2, 332, y2, color=C["blue"], w=1.8)
    x_at = lambda y: 100 + (y - y1) * 0.66
    cv.line(x_at(26), 26, x_at(204), 204, color=C["red"], w=1.7)
    for y, base in ((y1, 0), (y2, 4)):
        px = x_at(y)
        cv.dot(px, y, r=2.6, color=C["red"])
        for i, (dx, dy) in enumerate(((-18, -13), (18, -13), (-18, 17), (18, 17))):
            cv.text(px + dx, y + dy, str(base + i + 1), size=9.2,
                    color=C["purple"], weight=700)
    cv.text(328, y1 - 8, "l", size=11, color=C["blue"], italic=True)
    cv.text(328, y2 - 8, "m", size=11, color=C["blue"], italic=True)
    cv.text(W / 2, H - 8, "l parallel m: corresponding and alternate angles match",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── parallel angle chase ─────────────────────────
def parallel_angle_chase(spec):
    given = int(spec.get("given", 65))
    W, H = 360, 250
    cv = Canvas(W, H, seed=_seed(spec, 3306))
    cv.text(W / 2, 20, "copy the given angle using corresponding or alternate positions",
            size=9.4, weight=700, color=C["soft"])
    y1, y2 = 68, 148
    cv.line(28, y1, 332, y1, color=C["blue"], w=1.8)
    cv.line(28, y2, 332, y2, color=C["blue"], w=1.8)
    x_at = lambda y: 100 + (y - y1) * 0.65
    cv.line(x_at(28), 28, x_at(200), 200, color=C["red"], w=1.7)
    p1, p2 = x_at(y1), x_at(y2)
    cv.dot(p1, y1, r=2.6, color=C["red"]); cv.dot(p2, y2, r=2.6, color=C["red"])
    _angle(cv, p1, y1, 25, 0, 58, C["amber"])
    _angle(cv, p2, y2, 25, 180, 238, C["green"])
    cv.text(p1 + 27, y1 - 18, f"{given} deg", size=9, color=C["amber"], weight=700)
    cv.text(p2 - 29, y2 + 28, f"x = {given} deg", size=9, color=C["green"], weight=700)
    _card(cv, 60, 208, 240, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(180, 226, "alternate interior angles are equal", size=8.8,
            weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── perpendicular lines ──────────────────────────
def perpendicular(spec):
    W, H = 300, 215
    cx, cy = 150, 105
    cv = Canvas(W, H, seed=_seed(spec, 3307))
    cv.text(W / 2, 20, "perpendicular lines form four right angles",
            size=9.9, weight=700, color=C["soft"])
    cv.line(36, cy, 264, cy, color=C["blue"], w=1.8)
    cv.line(cx, 34, cx, 180, color=C["green"], w=1.8)
    cv.right_angle(cx, cy, (cx + 20, cy), (cx, cy - 20), size=13, color=C["red"])
    cv.text(cx + 20, cy - 25, "90 deg", size=8.5, color=C["red"], weight=700)
    cv.text(42, cy + 26, "l", size=11, color=C["blue"], italic=True)
    cv.text(cx + 9, 42, "m", size=11, color=C["green"], italic=True)
    cv.text(W / 2, H - 8, "l perpendicular m", size=10, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── triangle angle sum ───────────────────────────
def triangle_angle_sum(spec):
    A, B, Cc = 50, 60, 70
    W, H = 320, 230
    cv = Canvas(W, H, seed=_seed(spec, 3308))
    cv.text(W / 2, 20, "the three interior angles of a triangle sum to 180",
            size=9.8, weight=700, color=C["soft"])
    p = [(55, 174), (264, 174), (150, 52)]
    cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.text(75, 157, "50", size=10, color=C["red"], weight=700)
    cv.text(227, 157, "60", size=10, color=C["green"], weight=700)
    cv.text(147, 82, "70", size=10, color=C["purple"], weight=700)
    for lab, pt, dx, dy in (("A", p[0], -14, 6), ("B", p[1], 14, 6), ("C", p[2], 0, -10)):
        cv.text(pt[0] + dx, pt[1] + dy, lab, size=11, weight=700)
    _card(cv, 72, 196, 224, 24, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(184, 213, "50 + 60 + 70 = 180 deg", size=9.2, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── triangle exterior ────────────────────────────
def triangle_exterior(spec):
    W, H = 330, 230
    cv = Canvas(W, H, seed=_seed(spec, 3309))
    cv.text(W / 2, 20, "an exterior angle equals the two remote interior angles",
            size=9.2, weight=700, color=C["soft"])
    A, B, Cc = (52, 174), (250, 174), (150, 60)
    cv.polygon([A, B, Cc], color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.line(*B, 304, 174, color=C["red"], w=1.7)
    cv.text(80, 155, "A", size=10, color=C["green"], weight=700)
    cv.text(224, 155, "B", size=10, color=C["purple"], weight=700)
    cv.text(147, 84, "C", size=10, color=C["green"], weight=700)
    cv.text(274, 158, "ext", size=9.2, color=C["red"], weight=700)
    cv.text(120, 158, "x", size=10, color=C["green"], weight=700)
    cv.text(187, 158, "y", size=10, color=C["purple"], weight=700)
    cv.text(255, 145, "x+y", size=10, color=C["red"], weight=700)
    _card(cv, 68, 196, 244, 24, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(190, 213, "exterior angle = x + y", size=9.5, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── polygon angle sum ────────────────────────────
def polygon_sum(spec):
    n = int(spec.get("sides", 6))
    W, H = 300, 230
    cx, cy, r = 150, 102, 72
    cv = Canvas(W, H, seed=_seed(spec, 3310))
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    for i in range(2, n - 1):
        cv.line(*pts[0], *pts[i], color=C["green"], w=1.1, dash="4 3")
    triangles = n - 2
    cv.text(W / 2, 194, f"diagonals from one vertex = {n-3}", size=9.4,
            color=C["green"], weight=700)
    cv.text(W / 2, 211, f"interior sum = ({n}-2) x 180 = {triangles*180} deg",
            size=9.4, color=C["purple"], weight=700)
    return cv.svg()


# ───────────────────────────── regular polygon ──────────────────────────────
def regular_polygon(spec):
    n = int(spec.get("sides", 6))
    W, H = 300, 226
    cx, cy, r = 130, 105, 72
    cv = Canvas(W, H, seed=_seed(spec, 3311))
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    for i in range(n):
        cv.ticks(pts[i], pts[(i + 1) % n], count=1, color=C["green"], size=5)
    exterior = 360 / n
    cv.text(230, 74, f"n = {n}", size=11, weight=700, color=C["purple"])
    cv.text(230, 98, f"exterior = 360/{n}", size=9, color=C["red"])
    cv.text(230, 118, f"= {_fmt(exterior)} deg", size=9.5, weight=700, color=C["red"])
    cv.text(150, H - 8, "all sides and all angles are equal",
            size=8.8, color=C["soft"])
    return cv.svg()


# ───────────────────────────── angle bisector ───────────────────────────────
def angle_bisector(spec):
    total = float(spec.get("angle", 80))
    half = total / 2
    W, H = 310, 215
    vx, vy = 62, 158
    cv = Canvas(W, H, seed=_seed(spec, 3312))
    p1 = _ray(cv, vx, vy, 122, 0)
    p2 = _ray(cv, vx, vy, 122, total)
    pm = _ray(cv, vx, vy, 122, half)
    cv.line(vx, vy, *p1, color=C["blue"], w=1.7)
    cv.line(vx, vy, *p2, color=C["blue"], w=1.7)
    cv.line(vx, vy, *pm, color=C["green"], w=1.7)
    _angle(cv, vx, vy, 34, 0, half, C["red"])
    _angle(cv, vx, vy, 46, half, total, C["purple"])
    cv.text(vx + 52, vy - 12, f"{_fmt(half)}", size=9.5, color=C["red"], weight=700)
    cv.text(vx + 34, vy - 48, f"{_fmt(half)}", size=9.5, color=C["purple"], weight=700)
    cv.text(vx + 18, vy + 8, "O", size=10.5, weight=700)
    cv.text(190, 66, f"total angle = {_fmt(total)} deg", size=9.7, weight=700, color=C["soft"])
    cv.text(190, 88, "bisector makes two equal angles", size=8.8, color=C["ink"])
    cv.text(W / 2, H - 8, f"each part = {_fmt(total)}/2 = {_fmt(half)} deg",
            size=9.5, color=C["green"], weight=700)
    return cv.svg()


REGISTRY = {
    "point-line-ray": point_line_ray,
    "angle-types": angle_types,
    "angle-pairs": angle_pairs,
    "vertical-angles": vertical_angles,
    "parallel-transversal": parallel_transversal,
    "parallel-angle-chase": parallel_angle_chase,
    "perpendicular": perpendicular,
    "triangle-angle-sum": triangle_angle_sum,
    "triangle-exterior": triangle_exterior,
    "polygon-sum": polygon_sum,
    "regular-polygon": regular_polygon,
    "angle-bisector": angle_bisector,
}
