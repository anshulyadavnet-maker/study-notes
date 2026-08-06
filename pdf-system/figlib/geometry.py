"""
geometry.py — geometry figure builders.

Each builder takes a spec dict and returns an SVG string.
Register in REGISTRY; md2pdf.py dispatches on `type:`.
"""
import math
from .sketch import Canvas, C


def _seed(spec, default=7):
    s = spec.get("seed", default)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


# ───────────────────────── right triangle ─────────────────────────
def right_triangle(spec):
    """base, height, labels, show_hyp, unit"""
    b = float(spec.get("base", 4))
    h = float(spec.get("height", 3))
    unit = spec.get("unit", "cm")
    labs = spec.get("labels", ["A", "B", "C"])
    W, H = 300, 200
    pad = 46
    sc = min((W - 2 * pad) / b, (H - 2 * pad) / h)
    bw, bh = b * sc, h * sc
    ox, oy = (W - bw) / 2, (H + bh) / 2

    A = (ox, oy)              # right-angle vertex (bottom-left)
    B = (ox + bw, oy)         # bottom-right
    Cv = (ox, oy - bh)        # top

    cv = Canvas(W, H, seed=_seed(spec))
    cv.polygon([A, B, Cv], color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.right_angle(A[0], A[1], B, Cv, size=12)

    cv.text(A[0] - 12, A[1] + 6, labs[0], size=12, weight=600)
    cv.text(B[0] + 12, B[1] + 6, labs[1], size=12, weight=600)
    cv.text(Cv[0] - 12, Cv[1] - 4, labs[2], size=12, weight=600)

    cv.text((A[0] + B[0]) / 2, A[1] + 20, f"{_num(b)} {unit}",
            size=10.5, color=C["purple"])
    cv.text(A[0] - 20, (A[1] + Cv[1]) / 2, f"{_num(h)} {unit}",
            size=10.5, color=C["purple"], anchor="end")
    if spec.get("show_hyp", True):
        hyp = math.hypot(b, h)
        mx, my = (B[0] + Cv[0]) / 2, (B[1] + Cv[1]) / 2
        cv.text(mx + 26, my - 4, f"{_num(hyp)} {unit}", size=10.5,
                color=C["red"])
    return cv.svg()


# ───────────────────────── triangle centres ─────────────────────────
def triangle_centre(spec):
    """centre: centroid | incentre | circumcentre | orthocentre"""
    kind = spec.get("centre", "centroid")
    W, H = 300, 215
    A = (52, 172); B = (250, 172); Cv = (128, 42)
    cv = Canvas(W, H, seed=_seed(spec, 11))
    cv.polygon([A, B, Cv], color=C["blue"], w=1.8, fill=C["blue_bg"])

    def mid(p, q):
        return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)

    if kind == "centroid":
        mAB, mBC, mCA = mid(A, B), mid(B, Cv), mid(Cv, A)
        for v, m in ((Cv, mAB), (A, mBC), (B, mCA)):
            cv.line(*v, *m, color=C["green"], w=1.2, dash="4 3", double=False)
        G = ((A[0] + B[0] + Cv[0]) / 3, (A[1] + B[1] + Cv[1]) / 3)
        cv.dot(*G, r=3.4, color=C["red"])
        cv.text(G[0] + 15, G[1] - 7, "G", size=11.5, weight=600, color=C["red"])
        for m in (mAB, mBC, mCA):
            cv.dot(*m, r=2, color=C["green"])
        cv.text(150, 205, "medians meet at G  (2 : 1)", size=9.5,
                color=C["green"])
    elif kind == "incentre":
        # incentre from side lengths
        a = math.dist(B, Cv); b = math.dist(Cv, A); c = math.dist(A, B)
        s = a + b + c
        I = ((a * A[0] + b * B[0] + c * Cv[0]) / s,
             (a * A[1] + b * B[1] + c * Cv[1]) / s)
        # inradius = area / semiperimeter
        ar = abs((B[0]-A[0])*(Cv[1]-A[1]) - (Cv[0]-A[0])*(B[1]-A[1])) / 2
        r = ar / (s / 2)
        cv.circle(I[0], I[1], r, color=C["amber"], w=1.3, double=False)
        for v in (A, B, Cv):
            cv.line(*v, *I, color=C["amber"], w=1.0, dash="3 3", double=False)
        cv.dot(*I, r=3.4, color=C["red"])
        cv.text(I[0] + 14, I[1] - 7, "I", size=11.5, weight=600, color=C["red"])
        cv.text(150, 205, "angle bisectors meet at I", size=9.5,
                color=C["amber"])
    cv.text(A[0] - 12, A[1] + 6, "A", size=12, weight=600)
    cv.text(B[0] + 12, B[1] + 6, "B", size=12, weight=600)
    cv.text(Cv[0], Cv[1] - 10, "C", size=12, weight=600)
    return cv.svg()


# ───────────────────────── circle parts ─────────────────────────
def circle_parts(spec):
    """show: radius, diameter, chord, tangent, sector"""
    show = spec.get("show", ["radius", "chord", "tangent"])
    if isinstance(show, str):
        show = [s.strip() for s in show.split(",")]
    W, H = 300, 230
    cx, cy, r = 140, 112, 74
    cv = Canvas(W, H, seed=_seed(spec, 13))
    cv.circle(cx, cy, r, color=C["blue"], w=1.8,
              fill=C["blue_bg"] if spec.get("fill", True) else None)
    cv.dot(cx, cy, r=2.8)
    cv.text(cx - 5, cy + 14, "O", size=11, weight=600)

    if "radius" in show:
        ex, ey = cx + r * math.cos(math.radians(-35)), cy + r * math.sin(math.radians(-35))
        cv.line(cx, cy, ex, ey, color=C["green"], w=1.5, double=False)
        cv.text((cx + ex) / 2 + 4, (cy + ey) / 2 - 6, "r", size=11,
                color=C["green"], weight=600, italic=True)
    if "diameter" in show:
        cv.line(cx - r, cy, cx + r, cy, color=C["purple"], w=1.4, double=False)
        cv.text(cx, cy - 7, "d", size=11, color=C["purple"], italic=True)
    if "chord" in show:
        a1, a2 = math.radians(205), math.radians(325)
        p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
        p2 = (cx + r * math.cos(a2), cy + r * math.sin(a2))
        cv.line(*p1, *p2, color=C["amber"], w=1.6, double=False)
        cv.text((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2 - 8, "chord",
                size=9.5, color=C["amber"])
        # perpendicular from centre
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        cv.line(cx, cy, mx, my, color=C["grey"], w=1.0, dash="3 3", double=False)
        cv.right_angle(mx, my, p1, (cx, cy), size=9, color=C["grey"])
    if "tangent" in show:
        ty = cy - r
        cv.line(cx - 62, ty - 6, cx + 62, ty - 6, color=C["red"], w=1.6,
                double=False)
        cv.line(cx, cy, cx, ty, color=C["grey"], w=1.0, dash="3 3", double=False)
        cv.right_angle(cx, ty - 6, (cx + 20, ty - 6), (cx, cy), size=9,
                       color=C["red"])
        cv.text(cx + 68, ty - 2, "tangent", size=9.5, color=C["red"],
                anchor="start")
    cv.text(150, H - 8, spec.get("note", ""), size=9, color=C["soft"])
    return cv.svg()


# ───────────────────────── quadrilaterals ─────────────────────────
def quadrilateral(spec):
    """shape: square | rectangle | parallelogram | rhombus | trapezium"""
    shape = spec.get("shape", "rectangle")
    W, H = 300, 190
    cv = Canvas(W, H, seed=_seed(spec, 17))
    if shape == "square":
        s = 118; ox, oy = (W - s) / 2, 30
        p = [(ox, oy), (ox + s, oy), (ox + s, oy + s), (ox, oy + s)]
        for i in range(4):
            cv.ticks(p[i], p[(i + 1) % 4], count=1)
    elif shape == "rectangle":
        w_, h_ = 170, 104; ox, oy = (W - w_) / 2, 38
        p = [(ox, oy), (ox + w_, oy), (ox + w_, oy + h_), (ox, oy + h_)]
    elif shape == "parallelogram":
        w_, h_, sk = 150, 100, 40; ox, oy = 44, 38
        p = [(ox + sk, oy), (ox + sk + w_, oy), (ox + w_, oy + h_), (ox, oy + h_)]
    elif shape == "rhombus":
        cx, cy, a, b = 150, 92, 84, 58
        p = [(cx, cy - b), (cx + a, cy), (cx, cy + b), (cx - a, cy)]
        for i in range(4):
            cv.ticks(p[i], p[(i + 1) % 4], count=1)
    else:  # trapezium
        ox, oy = 40, 38
        p = [(ox + 44, oy), (ox + 176, oy), (ox + 220, oy + 100), (ox, oy + 100)]
    cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    if spec.get("diagonals", False):
        cv.line(*p[0], *p[2], color=C["red"], w=1.2, dash="4 3", double=False)
        cv.line(*p[1], *p[3], color=C["red"], w=1.2, dash="4 3", double=False)
    for lab, pt in zip(["A", "B", "C", "D"], p):
        ox_ = -12 if pt[0] < 150 else 12
        oy_ = -8 if pt[1] < 95 else 14
        cv.text(pt[0] + ox_, pt[1] + oy_, lab, size=11.5, weight=600)
    if spec.get("show_angles", False):
        for pt in p:
            cv.text(pt[0], pt[1], "", size=1)
    return cv.svg()


# ───────────────────────── 3-D solids ─────────────────────────
def solid(spec):
    """shape: cube | cuboid | cylinder | cone | sphere | hemisphere"""
    shape = spec.get("shape", "cube")
    W, H = 300, 210
    cv = Canvas(W, H, seed=_seed(spec, 23))
    col, bg = C["teal"], C["teal_bg"]

    if shape in ("cube", "cuboid"):
        w_ = 118 if shape == "cube" else 152
        h_ = 118 if shape == "cube" else 92
        d = 42
        ox, oy = (W - w_ - d) / 2, 52
        f = [(ox, oy + d), (ox + w_, oy + d), (ox + w_, oy + d + h_), (ox, oy + d + h_)]
        cv.polygon(f, color=col, w=1.8, fill=bg)
        top = [(ox, oy + d), (ox + d, oy), (ox + w_ + d, oy), (ox + w_, oy + d)]
        cv.polygon(top, color=col, w=1.6, fill=C["paper"])
        side = [(ox + w_, oy + d), (ox + w_ + d, oy),
                (ox + w_ + d, oy + h_), (ox + w_, oy + d + h_)]
        cv.polygon(side, color=col, w=1.6, fill=C["paper"])
        if shape == "cube":
            cv.text(ox + w_ / 2, oy + d + h_ + 22, "a", size=11.5,
                    color=C["purple"], italic=True, weight=600)
        else:
            cv.text(ox + w_ / 2, oy + d + h_ + 22, "l", size=11,
                    color=C["purple"], italic=True)
            cv.text(ox - 14, oy + d + h_ / 2, "h", size=11, color=C["purple"],
                    italic=True, anchor="end")
            cv.text(ox + w_ + d / 2 + 12, oy + d / 2 + 4, "b", size=11,
                    color=C["purple"], italic=True, anchor="start")
    elif shape == "cylinder":
        cx, ry, rx, h_ = 150, 17, 62, 106
        top_y, bot_y = 46, 46 + h_
        cv.raw(f'<path d="M{cx-rx},{top_y} L{cx-rx},{bot_y} '
               f'A{rx},{ry} 0 0 0 {cx+rx},{bot_y} L{cx+rx},{top_y} Z" '
               f'fill="{bg}" stroke="none"/>')
        cv.ellipse(cx, top_y, rx, ry, color=col, w=1.7, fill=C["paper"])
        cv.line(cx - rx, top_y, cx - rx, bot_y, color=col, w=1.7)
        cv.line(cx + rx, top_y, cx + rx, bot_y, color=col, w=1.7)
        cv.arc(cx, bot_y, rx, 0, math.pi, color=col, w=1.7)
        cv.line(cx, top_y, cx, bot_y, color=C["grey"], w=1.0, dash="3 3",
                double=False)
        cv.text(cx + 8, (top_y + bot_y) / 2, "h", size=11, color=C["purple"],
                italic=True, anchor="start")
        cv.line(cx, top_y, cx + rx, top_y, color=C["green"], w=1.2, double=False)
        cv.text(cx + rx / 2, top_y - 7, "r", size=10.5, color=C["green"],
                italic=True)
    elif shape == "cone":
        cx, ry, rx, h_ = 150, 17, 62, 116
        apex_y, bot_y = 42, 42 + h_
        cv.raw(f'<path d="M{cx},{apex_y} L{cx-rx},{bot_y} '
               f'A{rx},{ry} 0 0 0 {cx+rx},{bot_y} Z" fill="{bg}" stroke="none"/>')
        cv.line(cx, apex_y, cx - rx, bot_y, color=col, w=1.7)
        cv.line(cx, apex_y, cx + rx, bot_y, color=col, w=1.7)
        cv.ellipse(cx, bot_y, rx, ry, color=col, w=1.6)
        cv.line(cx, apex_y, cx, bot_y, color=C["grey"], w=1.0, dash="3 3",
                double=False)
        cv.line(cx, bot_y, cx + rx, bot_y, color=C["green"], w=1.2, double=False)
        cv.text(cx + rx / 2, bot_y + 26, "r", size=10.5, color=C["green"],
                italic=True, weight=600)
        cv.text(cx - 9, (apex_y + bot_y) / 2, "h", size=11, color=C["purple"],
                italic=True, anchor="end")
        cv.text(cx + 38, (apex_y + bot_y) / 2 - 14, "l", size=11, color=C["red"],
                italic=True, anchor="start", weight=600)
        cv.right_angle(cx, bot_y, (cx + 20, bot_y), (cx, apex_y), size=9,
                       color=C["grey"])
    elif shape in ("sphere", "hemisphere"):
        cx, cy, r = 150, 108, 66
        if shape == "sphere":
            cv.circle(cx, cy, r, color=col, w=1.8, fill=bg)
            cv.ellipse(cx, cy, r, 20, color=C["grey"], w=1.0, double=False)
        else:
            cv.raw(f'<path d="M{cx-r},{cy} A{r},{r} 0 0 1 {cx+r},{cy} Z" '
                   f'fill="{bg}" stroke="none"/>')
            cv.arc(cx, cy, r, math.pi, 2 * math.pi, color=col, w=1.8)
            cv.ellipse(cx, cy, r, 18, color=col, w=1.5, double=False)
        cv.line(cx, cy, cx + r, cy, color=C["green"], w=1.3, double=False)
        cv.text(cx + r / 2, cy - 8, "r", size=11, color=C["green"],
                italic=True, weight=600)
        cv.dot(cx, cy, r=2.6)
    return cv.svg()


# ───────────────────────── parallel lines + transversal ─────────────────────────
def parallel_transversal(spec):
    W, H = 320, 215
    cv = Canvas(W, H, seed=_seed(spec, 29))
    y1, y2 = 58, 136
    cv.line(28, y1, 292, y1, color=C["blue"], w=1.8)
    cv.line(28, y2, 292, y2, color=C["blue"], w=1.8)
    # transversal
    x_at = lambda y: 100 + (y - y1) * 0.75
    cv.line(x_at(20), 20, x_at(182), 182, color=C["red"], w=1.6)
    i1 = (x_at(y1), y1); i2 = (x_at(y2), y2)
    cv.dot(*i1, r=2.6, color=C["red"]); cv.dot(*i2, r=2.6, color=C["red"])
    lab = spec.get("angle_labels", ["1", "2", "3", "4", "5", "6", "7", "8"])
    off = 16
    for (px, py), base in ((i1, 0), (i2, 4)):
        cv.text(px - off - 4, py - 8, lab[base + 0], size=10, color=C["purple"])
        cv.text(px + off + 2, py - 8, lab[base + 1], size=10, color=C["purple"])
        cv.text(px - off - 4, py + 17, lab[base + 2], size=10, color=C["purple"])
        cv.text(px + off + 2, py + 17, lab[base + 3], size=10, color=C["purple"])
    cv.text(300, y1 + 4, "l", size=11, color=C["blue"], italic=True,
            anchor="start", weight=600)
    cv.text(300, y2 + 4, "m", size=11, color=C["blue"], italic=True,
            anchor="start", weight=600)
    cv.text(60, 205, "l || m", size=10.5, color=C["soft"], weight=600)
    return cv.svg()


def _num(v):
    return str(int(v)) if float(v) == int(float(v)) else f"{float(v):g}"


REGISTRY = {
    "right-triangle": right_triangle,
    "triangle-centre": triangle_centre,
    "circle": circle_parts,
    "quadrilateral": quadrilateral,
    "solid": solid,
    "parallel-lines": parallel_transversal,
}
