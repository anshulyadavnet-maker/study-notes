"""
triangles.py — visual figures for Chapter 34 (Triangles & Four Centres).

triangle-classify    : classify by sides or angles
triangle-inequality  : compare three side lengths
side-angle           : larger side opposite larger angle
median               : median joins a vertex to the midpoint
altitude             : perpendicular height from a vertex
triangle-bisector    : angle bisector inside a triangle
triangle-centre34    : centroid, incentre, circumcentre or orthocentre
euler-line           : O, G and H on the Euler line
right-triangle-centres: special centres of a right triangle
equilateral-centres  : all centres coincide in an equilateral triangle
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3400):
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


def _triangle():
    return ( (58, 174), (250, 174), (126, 46) )


def _mid(p, q):
    return ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)


def _dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


def _area(a, b, c):
    return abs((b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1])) / 2


def _circumcenter(a, b, c):
    d = 2 * (a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))
    if abs(d) < 1e-9:
        return (150, 110)
    aa = a[0] ** 2 + a[1] ** 2
    bb = b[0] ** 2 + b[1] ** 2
    cc = c[0] ** 2 + c[1] ** 2
    ux = (aa * (b[1] - c[1]) + bb * (c[1] - a[1]) + cc * (a[1] - b[1])) / d
    uy = (aa * (c[0] - b[0]) + bb * (a[0] - c[0]) + cc * (b[0] - a[0])) / d
    return ux, uy


def _incenter(a, b, c):
    wa, wb, wc = _dist(b, c), _dist(c, a), _dist(a, b)
    total = wa + wb + wc
    return ((wa * a[0] + wb * b[0] + wc * c[0]) / total,
            (wa * a[1] + wb * b[1] + wc * c[1]) / total)


def _label_vertices(cv, pts):
    for lab, pt, dx, dy in (("A", pts[0], -14, 7), ("B", pts[1], 14, 7),
                             ("C", pts[2], 0, -10)):
        cv.text(pt[0] + dx, pt[1] + dy, lab, size=11.5, weight=700)


def _base_triangle(cv, fill=True):
    pts = _triangle()
    cv.polygon(list(pts), color=C["blue"], w=1.8, fill=C["blue_bg"] if fill else None)
    _label_vertices(cv, pts)
    return pts


# ───────────────────────────── classification ──────────────────────────────
def triangle_classify(spec):
    kind = str(spec.get("kind", "equilateral")).lower()
    W, H = 452, 264
    cv = Canvas(W, H, seed=_seed(spec, 3401))
    cv.text(W / 2, 20, "triangles can be classified by sides or by angles",
            size=10, weight=700, color=C["soft"])
    if kind == "equilateral":
        pts = [(54, 178), (190, 178), (122, 60)]
        note = "equilateral: 3 equal sides, each angle 60 deg"
        for i in range(3): cv.ticks(pts[i], pts[(i + 1) % 3], count=1)
    elif kind == "isosceles":
        pts = [(42, 178), (202, 178), (122, 56)]
        note = "isosceles: 2 equal sides, 2 equal base angles"
        cv.ticks(pts[0], pts[2], count=1); cv.ticks(pts[1], pts[2], count=1)
    elif kind == "scalene":
        pts = [(40, 178), (220, 178), (142, 52)]
        note = "scalene: all sides different"
    elif kind == "right":
        pts = [(40, 178), (220, 178), (40, 70)]
        note = "right triangle: one angle is 90 deg"
        cv.right_angle(pts[0][0], pts[0][1], pts[1], pts[2], size=14)
    elif kind == "obtuse":
        pts = [(38, 178), (226, 178), (72, 64)]
        note = "obtuse triangle: one angle is greater than 90 deg"
        _angle(cv, 72, 64, 25, 0, 120, C["red"])
    else:
        pts = [(42, 178), (220, 178), (128, 52)]
        note = "acute triangle: all angles are less than 90 deg"
    cv.polygon(pts, color=C["blue"], w=1.8, fill=C["blue_bg"])
    _label_vertices(cv, pts)
    _card(cv, 254, 70, 166, 84, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(337, 94, kind, size=13, weight=700, color=C["purple"])
    cv.text(337, 119, "side test", size=8.5, color=C["soft"])
    cv.text(337, 136, "angle test", size=8.5, color=C["soft"])
    cv.text(W / 2, H - 10, note, size=9.1, color=C["ink"], weight=600)
    return cv.svg()


# ───────────────────────────── triangle inequality ─────────────────────────
def triangle_inequality(spec):
    a, b, c = int(spec.get("a", 5)), int(spec.get("b", 6)), int(spec.get("c", 8))
    W, H = 452, 248
    cv = Canvas(W, H, seed=_seed(spec, 3402))
    cv.text(W / 2, 20, "the sum of any two sides must exceed the third side",
            size=9.8, weight=700, color=C["soft"])
    p = [(55, 176), (255, 176), (135, 54)]
    cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.text(154, 194, f"{c}", size=10.5, color=C["purple"], weight=700)
    cv.text(42, 112, f"{b}", size=10.5, color=C["purple"], weight=700, anchor="end")
    cv.text(233, 108, f"{a}", size=10.5, color=C["purple"], weight=700)
    rows = [(f"a+b > c", f"{a}+{b}>{c}", a + b > c, C["green"]),
            (f"b+c > a", f"{b}+{c}>{a}", b + c > a, C["green"]),
            (f"c+a > b", f"{c}+{a}>{b}", c + a > b, C["green"])]
    for i, (lab, value, ok, col) in enumerate(rows):
        y = 48 + i * 32
        _card(cv, 292, y, 126, 24, col if ok else C["red"], C["green_bg"] if ok else C["red_bg"], r=4, sw=1.2)
        cv.text(355, y + 16, value, size=8.7, weight=700, color=col if ok else C["red"])
    cv.text(W / 2, H - 8, "if any inequality fails, a triangle is impossible",
            size=8.8, color=C["red"])
    return cv.svg()


# ───────────────────────────── side-angle relation ──────────────────────────
def side_angle(spec):
    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 3403))
    cv.text(W / 2, 20, "the larger side faces the larger opposite angle",
            size=10.1, weight=700, color=C["soft"])
    p = [(48, 176), (276, 176), (142, 52)]
    cv.polygon(p, color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.text(152, 194, "a = longest", size=9.3, color=C["purple"], weight=700)
    cv.text(35, 110, "b", size=10, color=C["green"], weight=700, anchor="end")
    cv.text(260, 106, "c", size=10, color=C["amber"], weight=700)
    cv.text(102, 154, "A", size=10, color=C["red"], weight=700)
    cv.text(226, 154, "B", size=10, color=C["green"], weight=700)
    cv.text(140, 79, "C", size=10, color=C["amber"], weight=700)
    cv.arc(142, 52, 23, 30, 145, color=C["red"], w=1.3)
    cv.text(190, 67, "largest angle", size=8.8, color=C["red"], weight=700)
    cv.text(W / 2, H - 8, "side a opposite angle A; compare opposite pairs",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── median ──────────────────────────────────────
def median(spec):
    pts = _triangle(); M = _mid(pts[1], pts[2])
    W, H = 320, 232
    cv = Canvas(W, H, seed=_seed(spec, 3404))
    cv.text(W / 2, 20, "a median joins a vertex to the midpoint of the opposite side",
            size=9.4, weight=700, color=C["soft"])
    cv.polygon(list(pts), color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.line(*pts[0], *M, color=C["red"], w=1.7, dash="4 3")
    cv.dot(*M, r=3.3, color=C["red"])
    cv.ticks(pts[1], M, count=1, color=C["green"])
    cv.ticks(M, pts[2], count=1, color=C["green"])
    _label_vertices(cv, pts)
    cv.text(M[0] + 12, M[1] + 5, "M", size=10.5, color=C["red"], weight=700)
    cv.text(W / 2, H - 8, "AM is a median when MB = MC",
            size=9, color=C["purple"], weight=600)
    return cv.svg()


# ───────────────────────────── altitude ────────────────────────────────────
def altitude(spec):
    pts = _triangle(); foot = (pts[0][0], pts[1][1])
    W, H = 320, 232
    cv = Canvas(W, H, seed=_seed(spec, 3405))
    cv.text(W / 2, 20, "an altitude is perpendicular to the opposite side or its extension",
            size=9.2, weight=700, color=C["soft"])
    cv.polygon(list(pts), color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.line(pts[2][0], pts[2][1], foot[0], foot[1], color=C["red"], w=1.7, dash="4 3")
    cv.right_angle(foot[0], foot[1], pts[1], pts[2], size=12, color=C["red"])
    cv.dot(*foot, r=3, color=C["red"])
    _label_vertices(cv, pts)
    cv.text(foot[0] + 10, foot[1] - 8, "H", size=10.5, color=C["red"], weight=700)
    cv.text(W / 2, H - 8, "height h is the perpendicular distance to the base",
            size=8.8, color=C["purple"], weight=600)
    return cv.svg()


# ───────────────────────────── angle bisector ───────────────────────────────
def triangle_bisector(spec):
    pts = _triangle(); I = _incenter(*pts)
    W, H = 320, 232
    cv = Canvas(W, H, seed=_seed(spec, 3406))
    cv.text(W / 2, 20, "an angle bisector divides a vertex angle into equal parts",
            size=9.3, weight=700, color=C["soft"])
    cv.polygon(list(pts), color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.line(*pts[0], *I, color=C["red"], w=1.7, dash="4 3")
    cv.arc(pts[0][0], pts[0][1], 30, 0, 52, color=C["red"], w=1.3)
    cv.arc(pts[0][0], pts[0][1], 38, 52, 104, color=C["purple"], w=1.3)
    cv.dot(*I, r=3.5, color=C["red"])
    _label_vertices(cv, pts)
    cv.text(I[0] + 10, I[1] - 6, "I", size=10.5, color=C["red"], weight=700)
    cv.text(W / 2, H - 8, "angle bisectors of all three vertices meet at the incentre",
            size=8.5, color=C["ink"])
    return cv.svg()


# ───────────────────────────── four centres ──────────────────────────────────
def triangle_centre34(spec):
    kind = str(spec.get("centre", "centroid")).lower()
    pts = _triangle(); A, B, Cc = pts
    W, H = 320, 244
    cv = Canvas(W, H, seed=_seed(spec, 3410))
    cv.polygon(list(pts), color=C["blue"], w=1.8, fill=C["blue_bg"])
    _label_vertices(cv, pts)
    if kind == "centroid":
        mids = [_mid(B, Cc), _mid(Cc, A), _mid(A, B)]
        for v, m in zip(pts, mids):
            cv.line(*v, *m, color=C["green"], w=1.2, dash="4 3")
            cv.dot(*m, r=2.4, color=C["green"])
        G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
        cv.dot(*G, r=4, color=C["red"])
        label = "G: centroid; medians meet; 2:1"
    elif kind == "incentre":
        I = _incenter(A, B, Cc)
        for v in pts:
            cv.line(*v, *I, color=C["amber"], w=1.1, dash="4 3")
        # approximate incircle radius from distance to AB
        r = abs(I[1] - A[1])
        cv.circle(I[0], I[1], r, color=C["amber"], w=1.2)
        cv.dot(*I, r=4, color=C["red"])
        label = "I: incentre; angle bisectors; equal side distance"
    elif kind == "circumcentre":
        O = _circumcenter(A, B, Cc)
        mids = [_mid(A, B), _mid(B, Cc)]
        for m, side in zip(mids, [(A, B), (B, Cc)]):
            cv.line(*m, *O, color=C["amber"], w=1.1, dash="4 3")
            cv.right_angle(m[0], m[1], side[0], O, size=9, color=C["amber"])
        R = _dist(O, A)
        cv.circle(O[0], O[1], R, color=C["purple"], w=1.2)
        cv.dot(*O, r=4, color=C["red"])
        label = "O: circumcentre; perpendicular bisectors; equal vertex distance"
    else:  # orthocentre
        O = _circumcenter(A, B, Cc)
        Hpt = (A[0] + B[0] + Cc[0] - 2 * O[0], A[1] + B[1] + Cc[1] - 2 * O[1])
        # altitudes from A and B to opposite sides (draw broad construction lines)
        cv.line(A[0], A[1], Hpt[0], Hpt[1], color=C["red"], w=1.2, dash="4 3")
        cv.line(B[0], B[1], Hpt[0], Hpt[1], color=C["red"], w=1.2, dash="4 3")
        cv.dot(*Hpt, r=4, color=C["red"])
        label = "H: orthocentre; altitudes meet"
    cv.text(W / 2, H - 10, label, size=8.1, color=C["soft"], weight=600)
    return cv.svg()


# ───────────────────────────── Euler line ───────────────────────────────────
def euler_line(spec):
    A, B, Cc = _triangle()
    O = _circumcenter(A, B, Cc)
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    Hpt = (A[0] + B[0] + Cc[0] - 2 * O[0], A[1] + B[1] + Cc[1] - 2 * O[1])
    W, H = 320, 244
    cv = Canvas(W, H, seed=_seed(spec, 3411))
    cv.polygon([A, B, Cc], color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.line(*O, *Hpt, color=C["red"], w=1.4, dash="5 3")
    for pt, lab, col in ((O, "O", C["purple"]), (G, "G", C["green"]), (Hpt, "H", C["red"])):
        cv.dot(*pt, r=4, color=col)
        cv.text(pt[0] + 9, pt[1] - 6, lab, size=10.5, weight=700, color=col)
    _label_vertices(cv, [A, B, Cc])
    cv.text(W / 2, H - 10, "Euler line: O, G, H are collinear; OH = 3OG",
            size=8.7, color=C["soft"], weight=600)
    return cv.svg()


# ───────────────────────────── right triangle centres ───────────────────────
def right_triangle_centres(spec):
    A, B, Cc = (58, 174), (252, 174), (58, 58)
    O = _mid(B, Cc)
    Hpt = A
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    W, H = 320, 244
    cv = Canvas(W, H, seed=_seed(spec, 3412))
    cv.polygon([A, B, Cc], color=C["blue"], w=1.8, fill=C["blue_bg"])
    cv.right_angle(A[0], A[1], B, Cc, size=14, color=C["red"])
    cv.line(*A, *O, color=C["green"], w=1.2, dash="4 3")
    cv.dot(*O, r=4, color=C["purple"]); cv.text(O[0] + 8, O[1] - 6, "O", size=10, weight=700, color=C["purple"])
    cv.dot(*Hpt, r=4, color=C["red"]); cv.text(Hpt[0] - 14, Hpt[1] + 8, "H", size=10, weight=700, color=C["red"])
    cv.dot(*G, r=4, color=C["green"]); cv.text(G[0] + 8, G[1] - 6, "G", size=10, weight=700, color=C["green"])
    _label_vertices(cv, [A, B, Cc])
    cv.text(W / 2, H - 10, "right triangle: H is right vertex; O is hypotenuse midpoint",
            size=8.3, color=C["soft"], weight=600)
    return cv.svg()


# ───────────────────────────── equilateral centres ──────────────────────────
def equilateral_centres(spec):
    A, B, Cc = (58, 174), (250, 174), (154, 40)
    G = ((A[0] + B[0] + Cc[0]) / 3, (A[1] + B[1] + Cc[1]) / 3)
    W, H = 320, 238
    cv = Canvas(W, H, seed=_seed(spec, 3413))
    cv.polygon([A, B, Cc], color=C["blue"], w=1.8, fill=C["blue_bg"])
    for v, m in ((A, _mid(B, Cc)), (B, _mid(Cc, A)), (Cc, _mid(A, B))):
        cv.line(*v, *m, color=C["green"], w=1.1, dash="4 3")
    cv.circle(G[0], G[1], 4, color=C["red"], w=1.2)
    cv.dot(*G, r=4, color=C["red"])
    _label_vertices(cv, [A, B, Cc])
    cv.text(G[0] + 10, G[1] - 6, "G=I=O=H", size=9.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 10, "in an equilateral triangle all four centres coincide",
            size=8.6, color=C["soft"], weight=600)
    return cv.svg()


def _angle(cv, vx, vy, r, start, end, color=None):
    cv.arc(vx, vy, r, math.radians(-end), math.radians(-start), color=color or C["red"], w=1.3)


REGISTRY = {
    "triangle-classify": triangle_classify,
    "triangle-inequality": triangle_inequality,
    "side-angle": side_angle,
    "median": median,
    "altitude": altitude,
    "triangle-bisector": triangle_bisector,
    "triangle-centre34": triangle_centre34,
    "euler-line": euler_line,
    "right-triangle-centres": right_triangle_centres,
    "equilateral-centres": equilateral_centres,
}
