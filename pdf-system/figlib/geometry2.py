"""
geometry2.py — angles, polygons, area shapes, circle theorems,
coordinate plane, congruence/similarity, number line, fractions.
"""
import math
from .sketch import Canvas, C


def _seed(spec, d=7):
    s = spec.get("seed", d)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


def _num(v):
    f = float(v)
    return str(int(f)) if f == int(f) else f"{f:g}"


# ───────────────────────── angle types ─────────────────────────
def angle_types(spec):
    """kind: acute | right | obtuse | straight | reflex"""
    kind = spec.get("kind", "acute")
    deg = {"acute": 50, "right": 90, "obtuse": 130,
           "straight": 180, "reflex": 230}.get(kind, float(spec.get("deg", 50)))
    deg = float(spec.get("deg", deg))
    W, H = 260, 175
    vx, vy, r = 70, 128, 92
    cv = Canvas(W, H, seed=_seed(spec, 31))
    a = math.radians(deg)
    p1 = (vx + r, vy)
    p2 = (vx + r * math.cos(-a), vy + r * math.sin(-a))
    cv.line(vx, vy, *p1, color=C["blue"], w=1.8)
    cv.line(vx, vy, *p2, color=C["blue"], w=1.8)
    if kind == "right":
        cv.right_angle(vx, vy, p1, p2, size=15)
    else:
        cv.arc(vx, vy, 30, -a, 0, color=C["red"], w=1.4)
    lab = spec.get("label", f"{_num(deg)}°")
    la = math.radians(deg / 2)
    cv.text(vx + 46 * math.cos(-la), vy + 46 * math.sin(-la) + 4, lab,
            size=11, color=C["red"], weight=600)
    cv.dot(vx, vy, r=2.6)
    cv.text(vx - 12, vy + 6, spec.get("vertex", "O"), size=11, weight=600)
    return cv.svg()


# ───────────────────────── angle pairs ─────────────────────────
def angle_pair(spec):
    """kind: complementary | supplementary | linear | vertical"""
    kind = spec.get("kind", "complementary")
    W, H = 290, 175
    cv = Canvas(W, H, seed=_seed(spec, 37))
    if kind == "complementary":
        vx, vy, r = 60, 130, 100
        cv.line(vx, vy, vx + r, vy, color=C["blue"], w=1.8)
        cv.line(vx, vy, vx, vy - r, color=C["blue"], w=1.8)
        a = math.radians(float(spec.get("split", 35)))
        cv.line(vx, vy, vx + r * math.cos(-a), vy + r * math.sin(-a),
                color=C["green"], w=1.6)
        cv.arc(vx, vy, 34, -a, 0, color=C["red"], w=1.3)
        cv.arc(vx, vy, 46, -math.pi / 2, -a, color=C["purple"], w=1.3)
        cv.text(vx + 52, vy - 12, "x", size=11, color=C["red"], italic=True,
                weight=600)
        cv.text(vx + 26, vy - 58, "y", size=11, color=C["purple"], italic=True,
                weight=600)
        cv.right_angle(vx, vy, (vx + 20, vy), (vx, vy - 20), size=13,
                       color=C["grey"])
        cv.text(150, 165, "x + y = 90", size=10.5, color=C["soft"], weight=600)
    elif kind in ("supplementary", "linear"):
        vx, vy, r = 145, 118, 118
        cv.line(vx - r, vy, vx + r, vy, color=C["blue"], w=1.8)
        a = math.radians(float(spec.get("split", 60)))
        cv.line(vx, vy, vx + r * math.cos(-a), vy + r * math.sin(-a),
                color=C["green"], w=1.6)
        cv.arc(vx, vy, 34, -a, 0, color=C["red"], w=1.3)
        cv.arc(vx, vy, 44, math.pi - 0.001, math.pi + a, color=C["purple"], w=1.3)
        cv.text(vx + 52, vy - 14, "x", size=11, color=C["red"], italic=True,
                weight=600)
        cv.text(vx - 56, vy - 16, "y", size=11, color=C["purple"], italic=True,
                weight=600)
        cv.dot(vx, vy, r=2.6)
        cv.text(150, 158, "x + y = 180", size=10.5, color=C["soft"], weight=600)
    else:  # vertical
        cx, cy, r = 145, 92, 108
        cv.line(cx - r, cy - 46, cx + r, cy + 46, color=C["blue"], w=1.8)
        cv.line(cx - r, cy + 46, cx + r, cy - 46, color=C["green"], w=1.8)
        cv.dot(cx, cy, r=2.8)
        cv.text(cx, cy - 34, "a", size=11.5, color=C["red"], weight=600,
                italic=True)
        cv.text(cx, cy + 44, "a", size=11.5, color=C["red"], weight=600,
                italic=True)
        cv.text(cx - 62, cy + 6, "b", size=11.5, color=C["purple"], weight=600,
                italic=True)
        cv.text(cx + 62, cy + 6, "b", size=11.5, color=C["purple"], weight=600,
                italic=True)
        cv.text(145, 164, "vertically opposite angles are equal",
                size=9.5, color=C["soft"])
    return cv.svg()


# ───────────────────────── triangle types ─────────────────────────
def triangle_type(spec):
    """kind: equilateral | isosceles | scalene | right | obtuse | acute"""
    k = spec.get("kind", "equilateral")
    W, H = 250, 190
    cv = Canvas(W, H, seed=_seed(spec, 41))
    if k == "equilateral":
        s = 128; ox, oy = (W - s) / 2, 158
        p = [(ox, oy), (ox + s, oy), (ox + s / 2, oy - s * math.sqrt(3) / 2)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        for i in range(3):
            cv.ticks(p[i], p[(i + 1) % 3], count=2)
        for pt, dx, dy in ((p[0], -6, 16), (p[1], 6, 16), (p[2], 0, -10)):
            cv.text(pt[0] + dx, pt[1] + dy, "60°", size=9.5, color=C["red"])
    elif k == "isosceles":
        b, h = 118, 122; ox, oy = (W - b) / 2, 158
        p = [(ox, oy), (ox + b, oy), (ox + b / 2, oy - h)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.ticks(p[0], p[2], count=1); cv.ticks(p[1], p[2], count=1)
        cv.text(p[0][0] - 4, p[0][1] + 16, "x°", size=9.5, color=C["red"])
        cv.text(p[1][0] + 4, p[1][1] + 16, "x°", size=9.5, color=C["red"])
    elif k == "right":
        b, h = 130, 106; ox, oy = 58, 158
        p = [(ox, oy), (ox + b, oy), (ox, oy - h)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.right_angle(ox, oy, p[1], p[2], size=13)
    elif k == "obtuse":
        p = [(38, 150), (212, 150), (78, 62)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.arc(78, 62, 24, 0.35, 2.0, color=C["red"], w=1.3)
        cv.text(96, 74, ">90°", size=9.5, color=C["red"], anchor="start")
    else:  # scalene / acute
        p = [(40, 156), (214, 156), (140, 54)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    for lab, pt in zip(["A", "B", "C"], p):
        dx = -13 if pt[0] < W / 2 else 13
        dy = 6 if pt[1] > 100 else -10
        cv.text(pt[0] + dx, pt[1] + dy, lab, size=11.5, weight=600)
    cv.text(W / 2, 182, spec.get("note", ""), size=9.5, color=C["soft"])
    return cv.svg()


# ───────────────────────── polygon ─────────────────────────
def polygon_fig(spec):
    n = int(spec.get("sides", 6))
    W, H = 250, 210
    cx, cy, r = 125, 100, 78
    cv = Canvas(W, H, seed=_seed(spec, 43))
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    if spec.get("diagonals_from_vertex", False):
        for i in range(2, n - 1):
            cv.line(*pts[0], *pts[i], color=C["green"], w=1.1, dash="4 3")
    tot = (n - 2) * 180
    cv.text(cx, H - 26, f"n = {n}", size=10.5, color=C["soft"], weight=600)
    cv.text(cx, H - 10, f"sum of interior angles = (n-2)x180 = {tot}",
            size=9.5, color=C["purple"])
    return cv.svg()


# ───────────────────────── area shapes ─────────────────────────
def area_shape(spec):
    """shape: rectangle|square|triangle|parallelogram|rhombus|trapezium|circle"""
    sh = spec.get("shape", "rectangle")
    unit = spec.get("unit", "cm")
    W, H = 300, 195
    cv = Canvas(W, H, seed=_seed(spec, 47))
    PUR, GRN = C["purple"], C["green"]

    if sh in ("rectangle", "square"):
        l = float(spec.get("length", 8)); b = float(spec.get("breadth", l if sh == "square" else 5))
        sc = min(180 / l, 108 / b); w_, h_ = l * sc, b * sc
        ox, oy = (W - w_) / 2, 40
        cv.rect(ox, oy, w_, h_, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.text(ox + w_ / 2, oy + h_ + 20, f"{_num(l)} {unit}", size=10.5, color=PUR)
        cv.text(ox - 10, oy + h_ / 2 + 4, f"{_num(b)} {unit}", size=10.5,
                color=PUR, anchor="end")
        area = l * b
        cv.text(W / 2, H - 8, f"Area = {_num(area)} sq {unit}", size=10,
                color=GRN, weight=600)
    elif sh == "triangle":
        b = float(spec.get("base", 12)); h = float(spec.get("height", 8))
        sc = min(190 / b, 104 / h); bw, bh = b * sc, h * sc
        ox, oy = (W - bw) / 2, 32 + bh
        apex = (ox + bw * 0.36, oy - bh)
        p = [(ox, oy), (ox + bw, oy), apex]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.line(apex[0], apex[1], apex[0], oy, color=GRN, w=1.2, dash="4 3")
        cv.right_angle(apex[0], oy, (apex[0] + 18, oy), apex, size=10,
                       color=GRN)
        cv.text(ox + bw / 2, oy + 20, f"b = {_num(b)} {unit}", size=10.5, color=PUR)
        cv.text(apex[0] - 8, (apex[1] + oy) / 2, f"h = {_num(h)}", size=10.5,
                color=GRN, anchor="end")
        cv.text(W / 2, H - 8, f"Area = 1/2 x b x h = {_num(b*h/2)} sq {unit}",
                size=10, color=GRN, weight=600)
    elif sh == "parallelogram":
        b = float(spec.get("base", 10)); h = float(spec.get("height", 6))
        sc = min(150 / b, 96 / h); bw, bh = b * sc, h * sc
        ox, oy, sk = 52, 36 + bh, 38
        p = [(ox, oy), (ox + bw, oy), (ox + bw + sk, oy - bh), (ox + sk, oy - bh)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.line(ox + sk, oy - bh, ox + sk, oy, color=GRN, w=1.2, dash="4 3")
        cv.right_angle(ox + sk, oy, (ox + sk + 16, oy), (ox + sk, oy - bh),
                       size=10, color=GRN)
        cv.text(ox + bw / 2, oy + 20, f"b = {_num(b)}", size=10.5, color=PUR)
        cv.text(ox + sk - 8, oy - bh / 2, f"h = {_num(h)}", size=10.5,
                color=GRN, anchor="end")
        cv.text(W / 2, H - 8, f"Area = b x h = {_num(b*h)} sq {unit}", size=10,
                color=GRN, weight=600)
    elif sh == "rhombus":
        d1 = float(spec.get("d1", 16)); d2 = float(spec.get("d2", 12))
        sc = min(200 / d1, 110 / d2); a, b = d1 * sc / 2, d2 * sc / 2
        cx, cy = W / 2, 92
        p = [(cx, cy - b), (cx + a, cy), (cx, cy + b), (cx - a, cy)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.line(cx - a, cy, cx + a, cy, color=C["red"], w=1.2, dash="4 3")
        cv.line(cx, cy - b, cx, cy + b, color=C["red"], w=1.2, dash="4 3")
        cv.right_angle(cx, cy, (cx + 16, cy), (cx, cy - 16), size=11,
                       color=C["red"])
        cv.text(cx + a / 2, cy - 7, f"d1 = {_num(d1)}", size=10, color=C["red"])
        cv.text(cx + 8, cy - b / 2, f"d2 = {_num(d2)}", size=10, color=C["red"],
                anchor="start")
        cv.text(W / 2, H - 8, f"Area = 1/2 x d1 x d2 = {_num(d1*d2/2)} sq {unit}",
                size=10, color=GRN, weight=600)
    elif sh == "trapezium":
        a = float(spec.get("a", 12)); b = float(spec.get("b", 8))
        h = float(spec.get("height", 5))
        sc = min(190 / a, 96 / h)
        aw, bw, bh = a * sc, b * sc, h * sc
        ox, oy = (W - aw) / 2, 40 + bh
        p = [(ox, oy), (ox + aw, oy), (ox + (aw + bw) / 2, oy - bh),
             (ox + (aw - bw) / 2, oy - bh)]
        cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.line(p[3][0], p[3][1], p[3][0], oy, color=GRN, w=1.2, dash="4 3")
        cv.right_angle(p[3][0], oy, (p[3][0] + 16, oy), p[3], size=10, color=GRN)
        cv.text(ox + aw / 2, oy + 20, f"a = {_num(a)}", size=10.5, color=PUR)
        cv.text((p[2][0] + p[3][0]) / 2, p[2][1] - 8, f"b = {_num(b)}",
                size=10.5, color=PUR)
        cv.text(p[3][0] - 8, oy - bh / 2, f"h = {_num(h)}", size=10.5,
                color=GRN, anchor="end")
        cv.text(W / 2, H - 8,
                f"Area = 1/2 x (a+b) x h = {_num((a+b)*h/2)} sq {unit}",
                size=10, color=GRN, weight=600)
    else:  # circle
        r = float(spec.get("radius", 7))
        cx, cy, R = W / 2, 88, 66
        cv.circle(cx, cy, R, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.line(cx, cy, cx + R, cy, color=GRN, w=1.4)
        cv.dot(cx, cy, r=2.6)
        cv.text(cx + R / 2, cy - 8, f"r = {_num(r)} {unit}", size=10.5,
                color=GRN, weight=600)
        cv.text(W / 2, H - 22, "Area = pi r squared", size=10, color=GRN,
                weight=600)
        cv.text(W / 2, H - 6, "Circumference = 2 pi r", size=10, color=PUR)
    return cv.svg()


# ───────────────────────── circle theorems ─────────────────────────
def circle_theorem(spec):
    """kind: semicircle | inscribed | cyclic-quad | two-tangents | chord-perp"""
    k = spec.get("kind", "semicircle")
    W, H = 290, 225
    cx, cy, r = 145, 112, 82
    cv = Canvas(W, H, seed=_seed(spec, 53))
    cv.circle(cx, cy, r, color=C["blue"], w=1.7,
              fill=C["blue_bg"] if spec.get("fill", True) else None)
    cv.dot(cx, cy, r=2.6); cv.text(cx - 4, cy + 15, "O", size=10.5, weight=600)

    def P(deg):
        a = math.radians(deg)
        return (cx + r * math.cos(a), cy - r * math.sin(a))

    if k == "semicircle":
        A, B = P(180), P(0)
        Cp = P(68)
        cv.line(*A, *B, color=C["purple"], w=1.5)
        cv.line(*A, *Cp, color=C["green"], w=1.6)
        cv.line(*B, *Cp, color=C["green"], w=1.6)
        cv.right_angle(Cp[0], Cp[1], A, B, size=13)
        cv.text(Cp[0], Cp[1] - 10, "C", size=11, weight=600)
        cv.text(A[0] - 12, A[1] + 5, "A", size=11, weight=600)
        cv.text(B[0] + 12, B[1] + 5, "B", size=11, weight=600)
        cv.text(W / 2, H - 10, "angle in a semicircle = 90", size=9.8,
                color=C["red"], weight=600)
    elif k == "inscribed":
        A, B = P(205), P(335)
        Cp, O = P(80), (cx, cy)
        cv.line(*A, *O, color=C["red"], w=1.4)
        cv.line(*B, *O, color=C["red"], w=1.4)
        cv.line(*A, *Cp, color=C["green"], w=1.5)
        cv.line(*B, *Cp, color=C["green"], w=1.5)
        cv.text(cx, cy - 26, "2x", size=11, color=C["red"], weight=600)
        cv.text(Cp[0], Cp[1] + 22, "x", size=11, color=C["green"], weight=600)
        cv.text(A[0] - 12, A[1] + 6, "A", size=11, weight=600)
        cv.text(B[0] + 12, B[1] + 6, "B", size=11, weight=600)
        cv.text(Cp[0], Cp[1] - 10, "C", size=11, weight=600)
        cv.text(W / 2, H - 10, "angle at centre = 2 x angle at circumference",
                size=9.5, color=C["soft"])
    elif k == "cyclic-quad":
        pts = [P(150), P(35), P(310), P(215)]
        cv.polygon(pts, color=C["green"], w=1.7, fill=None)
        for lab, pt in zip("ABCD", pts):
            dx = -13 if pt[0] < cx else 13
            dy = -8 if pt[1] < cy else 15
            cv.text(pt[0] + dx, pt[1] + dy, lab, size=11, weight=600)
        cv.text(pts[0][0] + 20, pts[0][1] + 16, "x", size=10.5, color=C["red"])
        cv.text(pts[2][0] - 20, pts[2][1] - 12, "y", size=10.5, color=C["red"])
        cv.text(W / 2, H - 10, "x + y = 180  (opposite angles)", size=9.8,
                color=C["red"], weight=600)
    elif k == "two-tangents":
        ext = (cx + 148, cy)
        for ang in (34, -34):
            a = math.radians(ang)
            T = (cx + r * math.cos(a), cy - r * math.sin(a))
            cv.line(*T, *ext, color=C["red"], w=1.6)
            cv.line(cx, cy, *T, color=C["grey"], w=1.0, dash="3 3")
            cv.right_angle(T[0], T[1], ext, (cx, cy), size=10, color=C["grey"])
        cv.dot(*ext, r=2.8, color=C["red"])
        cv.text(ext[0] + 8, ext[1] + 5, "P", size=11, weight=600, anchor="start")
        cv.text(W / 2, H - 10, "PA = PB  (tangents from an external point)",
                size=9.5, color=C["red"], weight=600)
    else:  # chord-perp
        A, B = P(200), P(340)
        cv.line(*A, *B, color=C["amber"], w=1.7)
        M = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
        cv.line(cx, cy, *M, color=C["grey"], w=1.2, dash="3 3")
        cv.right_angle(M[0], M[1], A, (cx, cy), size=10, color=C["grey"])
        cv.ticks(A, M, count=1); cv.ticks(M, B, count=1)
        cv.text(A[0] - 12, A[1] + 6, "A", size=11, weight=600)
        cv.text(B[0] + 12, B[1] + 6, "B", size=11, weight=600)
        cv.text(M[0], M[1] + 18, "M", size=10.5, weight=600)
        cv.text(W / 2, H - 10, "perpendicular from O bisects the chord (AM = MB)",
                size=9.3, color=C["soft"])
    return cv.svg()


# ───────────────────────── sector & ring ─────────────────────────
def sector(spec):
    deg = float(spec.get("angle", 90))
    W, H = 260, 205
    cx, cy, r = 118, 118, 88
    cv = Canvas(W, H, seed=_seed(spec, 59))
    a = math.radians(deg)
    p1 = (cx + r, cy)
    p2 = (cx + r * math.cos(-a), cy + r * math.sin(-a))
    steps = max(6, int(deg / 12))
    arc = [(cx + r * math.cos(-a * i / steps), cy + r * math.sin(-a * i / steps))
           for i in range(steps + 1)]
    d = f"M{cx},{cy} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in arc) + " Z"
    cv.raw(f'<path d="{d}" fill="{C["amber_bg"]}" stroke="none"/>')
    cv.circle(cx, cy, r, color=C["grey"], w=1.1)
    cv.line(cx, cy, *p1, color=C["amber"], w=1.7)
    cv.line(cx, cy, *p2, color=C["amber"], w=1.7)
    cv.arc(cx, cy, r, -a, 0, color=C["amber"], w=1.9)
    cv.arc(cx, cy, 30, -a, 0, color=C["red"], w=1.3)
    la = a / 2
    cv.text(cx + 48 * math.cos(-la), cy + 48 * math.sin(-la) + 4,
            f"{_num(deg)}°", size=11, color=C["red"], weight=600)
    cv.text(cx + r / 2, cy - 8, "r", size=10.5, color=C["amber"], italic=True,
            weight=600)
    cv.dot(cx, cy, r=2.6)
    cv.text(W / 2, H - 24, "Area = (angle/360) x pi r squared", size=9.5,
            color=C["green"])
    cv.text(W / 2, H - 8, "Arc = (angle/360) x 2 pi r", size=9.5, color=C["purple"])
    return cv.svg()


def ring(spec):
    R = float(spec.get("R", 7)); rr = float(spec.get("r", 3))
    W, H = 250, 195
    cx, cy = 125, 92
    RR = 78; ri = RR * rr / R
    cv = Canvas(W, H, seed=_seed(spec, 61))
    cv.circle(cx, cy, RR, color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.circle(cx, cy, ri, color=C["blue"], w=1.6, fill=C["paper"])
    cv.line(cx, cy, cx + ri, cy, color=C["red"], w=1.3)
    cv.line(cx + ri, cy, cx + RR, cy, color=C["green"], w=1.3)
    cv.text(cx + ri / 2, cy - 7, f"r={_num(rr)}", size=9.5, color=C["red"])
    cv.text(cx + (ri + RR) / 2, cy - 7, f"R={_num(R)}", size=9.5, color=C["green"])
    cv.dot(cx, cy, r=2.4)
    cv.text(W / 2, H - 8, "Area = pi (R squared - r squared)", size=10,
            color=C["soft"], weight=600)
    return cv.svg()


# ───────────────────────── coordinate plane ─────────────────────────
def coordinate_plane(spec):
    pts = spec.get("points", [])
    if isinstance(pts, str):
        pts = [pts]
    show_dist = spec.get("distance", False)
    W, H = 290, 265
    cx, cy = 145, 132
    step = 26
    cv = Canvas(W, H, seed=_seed(spec, 67))
    # grid
    for i in range(-4, 5):
        cv.raw(f'<line x1="{cx+i*step}" y1="{cy-4.2*step}" x2="{cx+i*step}" '
               f'y2="{cy+4.2*step}" stroke="#e4e9f2" stroke-width="0.7"/>')
        cv.raw(f'<line x1="{cx-4.2*step}" y1="{cy+i*step}" x2="{cx+4.2*step}" '
               f'y2="{cy+i*step}" stroke="#e4e9f2" stroke-width="0.7"/>')
    cv.arrow(cx - 4.4 * step, cy, cx + 4.5 * step, cy, color=C["ink"], w=1.4)
    cv.arrow(cx, cy + 4.4 * step, cx, cy - 4.5 * step, color=C["ink"], w=1.4)
    cv.text(cx + 4.5 * step + 8, cy + 4, "X", size=10.5, weight=600)
    cv.text(cx + 9, cy - 4.5 * step - 4, "Y", size=10.5, weight=600)
    cv.text(cx - 8, cy + 13, "O", size=10, color=C["soft"])
    for q, (sx, sy) in enumerate([(1, -1), (-1, -1), (-1, 1), (1, 1)], start=1):
        cv.text(cx + sx * 2.6 * step, cy + sy * 2.6 * step,
                ["I", "II", "III", "IV"][q - 1], size=11, color=C["grey"])
    plotted = []
    for item in pts:
        s = str(item).strip().strip("()")
        try:
            xs, ys, *lab = [t.strip() for t in s.split(",")]
            x, y = float(xs), float(ys)
        except Exception:
            continue
        px, py = cx + x * step, cy - y * step
        plotted.append((px, py, x, y, lab[0] if lab else None))
        cv.dot(px, py, r=3.4, color=C["red"])
        name = lab[0] if lab else f"({_num(x)},{_num(y)})"
        cv.text(px + 6, py - 8, name, size=9.6, color=C["red"], anchor="start",
                weight=600)
    if show_dist and len(plotted) >= 2:
        a, b = plotted[0], plotted[1]
        cv.line(a[0], a[1], b[0], b[1], color=C["green"], w=1.5, dash="5 3")
        d = math.hypot(a[2] - b[2], a[3] - b[3])
        cv.text((a[0] + b[0]) / 2 + 10, (a[1] + b[1]) / 2 - 6,
                f"d = {d:.0f}" if d == int(d) else f"d = {d:.2f}",
                size=10, color=C["green"], anchor="start", weight=600)
    cv.text(W / 2, H - 6, spec.get("note", ""), size=9.3, color=C["soft"])
    return cv.svg()


# ───────────────────────── congruence / similarity ─────────────────────────
def congruent_pair(spec):
    """rule: SSS | SAS | ASA | RHS | similar"""
    rule = str(spec.get("rule", "SSS")).upper()
    W, H = 320, 175
    cv = Canvas(W, H, seed=_seed(spec, 71))
    scale2 = 1.0 if rule != "SIMILAR" else 0.62

    def tri(ox, oy, s, tag):
        p = [(ox, oy), (ox + 108 * s, oy), (ox + 34 * s, oy - 86 * s)]
        cv.polygon(p, color=C["blue"] if tag == "1" else C["green"], w=1.7,
                   fill=C["blue_bg"] if tag == "1" else C["green_bg"])
        return p

    p1 = tri(26, 132, 1.0, "1")
    p2 = tri(190, 132, scale2, "2")
    for p, names in ((p1, ["A", "B", "C"]), (p2, ["P", "Q", "R"])):
        for lab, pt in zip(names, p):
            dx = -12 if pt[0] < p[1][0] else 12
            dy = 6 if pt[1] > 100 else -9
            cv.text(pt[0] + dx, pt[1] + dy, lab, size=11, weight=600)
    if rule == "SSS":
        for p in (p1, p2):
            cv.ticks(p[0], p[1], 1); cv.ticks(p[1], p[2], 2); cv.ticks(p[2], p[0], 3)
        note = "SSS — three sides equal"
    elif rule == "SAS":
        for p in (p1, p2):
            cv.ticks(p[0], p[1], 1); cv.ticks(p[2], p[0], 2)
            cv.arc(p[0][0], p[0][1], 20, -1.15, 0, color=C["red"], w=1.3)
        note = "SAS — two sides + included angle"
    elif rule == "ASA":
        for p in (p1, p2):
            cv.ticks(p[0], p[1], 1)
            cv.arc(p[0][0], p[0][1], 20, -1.15, 0, color=C["red"], w=1.3)
            cv.arc(p[1][0], p[1][1], 20, math.pi + 0.35, math.pi + 1.4,
                   color=C["purple"], w=1.3)
        note = "ASA — two angles + included side"
    elif rule == "RHS":
        for p in (p1, p2):
            cv.right_angle(p[0][0], p[0][1], p[1], p[2], size=11)
            cv.ticks(p[1], p[2], 1); cv.ticks(p[2], p[0], 2)
        note = "RHS — right angle + hypotenuse + side"
    else:
        for p in (p1, p2):
            cv.arc(p[0][0], p[0][1], 18, -1.15, 0, color=C["red"], w=1.2)
        note = "similar — same shape, sides in proportion"
    cv.text(W / 2, H - 8, note, size=9.6, color=C["soft"], weight=600)
    return cv.svg()


# ───────────────────────── number line ─────────────────────────
def number_line(spec):
    lo = float(spec.get("min", -5)); hi = float(spec.get("max", 5))
    marks = spec.get("mark", [])
    if not isinstance(marks, list):
        marks = [marks]
    W, H = 320, 96
    y = 52; x0, x1 = 26, W - 26
    cv = Canvas(W, H, seed=_seed(spec, 73))
    cv.line(x0, y, x1, y, color=C["ink"], w=1.6)
    cv.arrow(x1 - 14, y, x1 + 4, y, color=C["ink"], w=1.4)
    cv.arrow(x0 + 14, y, x0 - 4, y, color=C["ink"], w=1.4)
    n = int(hi - lo)
    for i in range(n + 1):
        v = lo + i
        px = x0 + (x1 - x0) * i / n
        cv.line(px, y - 5, px, y + 5, color=C["ink"], w=1.1)
        cv.text(px, y + 20, _num(v), size=9.5, color=C["soft"])
    for m in marks:
        try:
            v = float(str(m).split(":")[0])
        except Exception:
            continue
        px = x0 + (x1 - x0) * (v - lo) / (hi - lo)
        cv.dot(px, y, r=4, color=C["red"])
        lab = str(m).split(":")[1] if ":" in str(m) else _num(v)
        cv.text(px, y - 13, lab, size=9.8, color=C["red"], weight=600)
    return cv.svg()


# ───────────────────────── fraction bars ─────────────────────────
def fraction(spec):
    """num/den shaded bar or circle. style: bar | circle"""
    num = int(spec.get("num", 3)); den = int(spec.get("den", 8))
    style = spec.get("style", "bar")
    W, H = 290, 130 if style == "bar" else 170
    cv = Canvas(W, H, seed=_seed(spec, 79))
    if style == "bar":
        x0, y0, w_, h_ = 30, 34, 230, 46
        seg = w_ / den
        for i in range(den):
            fill = C["amber_bg"] if i < num else None
            cv.rect(x0 + i * seg, y0, seg, h_, color=C["amber"], w=1.4,
                    fill=fill)
        cv.text(W / 2, y0 + h_ + 26, f"{num}/{den}", size=13,
                color=C["amber"], weight=700)
    else:
        cx, cy, r = W / 2, 76, 58
        for i in range(den):
            a0 = -math.pi / 2 + 2 * math.pi * i / den
            a1 = -math.pi / 2 + 2 * math.pi * (i + 1) / den
            steps = 8
            arc = [(cx + r * math.cos(a0 + (a1 - a0) * t / steps),
                    cy + r * math.sin(a0 + (a1 - a0) * t / steps))
                   for t in range(steps + 1)]
            if i < num:
                d = f"M{cx},{cy} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in arc) + " Z"
                cv.raw(f'<path d="{d}" fill="{C["amber_bg"]}" stroke="none"/>')
            cv.line(cx, cy, arc[0][0], arc[0][1], color=C["amber"], w=1.2)
        cv.circle(cx, cy, r, color=C["amber"], w=1.7)
        cv.text(cx, cy + r + 26, f"{num}/{den}", size=13, color=C["amber"],
                weight=700)
    return cv.svg()


REGISTRY = {
    "angle": angle_types,
    "angle-pair": angle_pair,
    "triangle-type": triangle_type,
    "polygon": polygon_fig,
    "area-shape": area_shape,
    "circle-theorem": circle_theorem,
    "sector": sector,
    "ring": ring,
    "coordinate-plane": coordinate_plane,
    "congruent": congruent_pair,
    "number-line": number_line,
    "fraction": fraction,
}
