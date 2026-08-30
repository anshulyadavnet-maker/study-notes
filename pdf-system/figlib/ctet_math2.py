"""Figures for CTET Paper II Mathematics MCQs.

These are small, vector SVG teaching models for the Class VI-VIII topics:
integers, fractions, ratio, algebra, coordinate geometry, angles, construction,
quadrilaterals, mensuration, solids and data handling.
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=6200):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=5, sw=1.3):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
        f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>'
    )


def _bar(cv, x, y, width, height, den, num, col, bg):
    seg = width / den
    for i in range(den):
        fill = bg if i < num else "#ffffff"
        cv.raw(
            f'<rect x="{x + i * seg:.2f}" y="{y}" width="{seg:.2f}" '
            f'height="{height}" fill="{fill}" stroke="{col}" stroke-width="1.1"/>'
        )


# ───────────────────────────── integer number line ──────────────────────────
def integer_line_p2(spec):
    point = int(spec.get("point", -3))
    other = int(spec.get("other", 2))
    lo, hi = -5, 5
    W, H = 452, 190
    cv = Canvas(W, H, seed=_seed(spec, 6201))
    cv.text(W / 2, 20, "integers on a number line: right is greater", size=10, weight=700, color=C["soft"])
    x0, x1, y = 45, 407, 94
    cv.line(x0, y, x1, y, color=C["ink"], w=1.6)
    cv.arrow(x1 - 10, y, x1 + 8, y, color=C["ink"], w=1.2)
    step = (x1 - x0) / (hi - lo)
    for value in range(lo, hi + 1):
        x = x0 + (value - lo) * step
        cv.line(x, y - 7, x, y + 7, color=C["ink"], w=1.1)
        cv.text(x, y + 23, str(value), size=8.7, color=C["soft"])
    for value, label, col in ((point, "A", C["red"]), (other, "B", C["blue"])):
        x = x0 + (value - lo) * step
        cv.dot(x, y, r=4.5, color=col)
        cv.text(x, y - 20, f"{label}={value}", size=8.8, weight=700, color=col)
    sign = ">" if point > other else "<" if point < other else "="
    _card(cv, 142, 140, 168, 27, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 158, f"{point} {sign} {other}", size=10, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── fraction comparison ──────────────────────────
def fraction_compare_p2(spec):
    an, ad = int(spec.get("a_num", 3)), int(spec.get("a_den", 4))
    bn, bd = int(spec.get("b_num", 5)), int(spec.get("b_den", 8))
    W, H = 452, 224
    cv = Canvas(W, H, seed=_seed(spec, 6202))
    cv.text(W / 2, 20, "compare fractions with equal whole bars", size=10, weight=700, color=C["soft"])
    _bar(cv, 70, 58, 300, 35, ad, an, C["blue"], C["blue_bg"])
    _bar(cv, 70, 116, 300, 35, bd, bn, C["green"], C["green_bg"])
    cv.text(38, 81, f"{an}/{ad}", size=10, weight=700, color=C["blue"], anchor="start")
    cv.text(38, 139, f"{bn}/{bd}", size=10, weight=700, color=C["green"], anchor="start")
    _card(cv, 128, 174, 196, 27, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 192, f"{an}/{ad} = {an * bd}/{ad * bd}", size=9.2, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── ratio strips ─────────────────────────────────
def ratio_strip_p2(spec):
    a, b = int(spec.get("a", 2)), int(spec.get("b", 3))
    W, H = 452, 218
    cv = Canvas(W, H, seed=_seed(spec, 6203))
    cv.text(W / 2, 20, "ratio strip: equal-sized units make the comparison visible", size=9.6, weight=700, color=C["soft"])
    unit, x0 = 45, 55
    for i in range(a):
        _card(cv, x0 + i * unit, 58, unit - 3, 38, C["blue"], C["blue_bg"], sw=1.2)
        cv.text(x0 + i * unit + (unit - 3) / 2, 82, "A", size=9, weight=700, color=C["blue"])
    for i in range(b):
        _card(cv, x0 + i * unit, 118, unit - 3, 38, C["green"], C["green_bg"], sw=1.2)
        cv.text(x0 + i * unit + (unit - 3) / 2, 142, "B", size=9, weight=700, color=C["green"])
    cv.text(24, 81, f"A={a}", size=9, weight=700, color=C["blue"], anchor="start")
    cv.text(24, 141, f"B={b}", size=9, weight=700, color=C["green"], anchor="start")
    _card(cv, 146, 177, 160, 27, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 195, f"A : B = {a} : {b}", size=10, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── algebra balance ──────────────────────────────
def algebra_balance_p2(spec):
    value = int(spec.get("value", 4))
    constant = int(spec.get("constant", 3))
    total = value + constant
    W, H = 452, 232
    cv = Canvas(W, H, seed=_seed(spec, 6204))
    cv.text(W / 2, 20, "equation balance: do the same operation on both sides", size=9.6, weight=700, color=C["soft"])
    # beam and fulcrum
    cv.line(62, 96, 390, 96, color=C["ink"], w=2.2)
    cv.polygon([(214, 96), (238, 96), (226, 128)], color=C["purple"], w=1.3, fill=C["purple_bg"])
    cv.line(226, 128, 226, 134, color=C["purple"], w=1.2)
    cv.line(194, 134, 258, 134, color=C["purple"], w=1.2)
    _card(cv, 74, 48, 82, 35, C["blue"], C["blue_bg"], sw=1.4)
    cv.text(115, 71, "x", size=13, weight=700, color=C["blue"])
    for i in range(constant):
        x = 166 + i * 27
        _card(cv, x, 54, 21, 25, C["amber"], C["amber_bg"], sw=1.1)
        cv.text(x + 10.5, 71, "1", size=8, weight=700, color=C["amber"])
    _card(cv, 300, 48, 82, 35, C["green"], C["green_bg"], sw=1.4)
    cv.text(341, 71, str(total), size=12, weight=700, color=C["green"])
    cv.text(115, 167, f"x + {constant} = {total}", size=10.5, weight=700, color=C["blue"])
    cv.text(226, 198, f"subtract {constant} from both sides -> x = {value}", size=9.2, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── coordinate grid ──────────────────────────────
def coordinate_grid_p2(spec):
    W, H = 452, 260
    cv = Canvas(W, H, seed=_seed(spec, 6205))
    cv.text(W / 2, 18, "coordinate plane: x first, y second", size=10, weight=700, color=C["soft"])
    cx, cy, step = 226, 130, 27
    cv.line(74, cy, 378, cy, color=C["ink"], w=1.5)
    cv.arrow(366, cy, 384, cy, color=C["ink"], w=1.2)
    cv.line(cx, 34, cx, 226, color=C["ink"], w=1.5)
    cv.arrow(cx, 42, cx, 28, color=C["ink"], w=1.2)
    for i in range(-5, 6):
        x = cx + i * step
        if i:
            cv.line(x, cy - 3, x, cy + 3, color=C["grey"], w=0.8)
            cv.text(x, cy + 16, str(i), size=7.5, color=C["soft"])
        y = cy - i * step
        if i:
            cv.line(cx - 3, y, cx + 3, y, color=C["grey"], w=0.8)
            cv.text(cx - 11, y + 3, str(i), size=7.5, color=C["soft"])
    cv.text(388, cy + 4, "x", size=9, weight=700, color=C["ink"])
    cv.text(cx + 8, 28, "y", size=9, weight=700, color=C["ink"])
    for name, px, py, col in (("A", 2, 3, C["red"]), ("B", -3, -2, C["blue"])):
        x, y = cx + px * step, cy - py * step
        cv.dot(x, y, r=4.3, color=col)
        cv.text(x + 10, y - 8, f"{name}({px},{py})", size=8, weight=700, color=col, anchor="start")
    return cv.svg()


# ───────────────────────────── parallel lines and transversal ───────────────
def parallel_lines_p2(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 6206))
    cv.text(W / 2, 18, "parallel lines cut by a transversal", size=10, weight=700, color=C["soft"])
    cv.line(55, 72, 397, 72, color=C["blue"], w=1.8)
    cv.line(55, 166, 397, 166, color=C["blue"], w=1.8)
    cv.line(145, 205, 307, 34, color=C["red"], w=1.8)
    for x in (100, 340):
        cv.line(x, 64, x + 18, 80, color=C["blue"], w=1.0)
        cv.line(x, 158, x + 18, 174, color=C["blue"], w=1.0)
    cv.text(170, 66, "1", size=9, weight=700, color=C["purple"])
    cv.text(265, 160, "2", size=9, weight=700, color=C["green"])
    cv.text(350, 211, "same-side / alternate angle reasoning", size=8.8, color=C["ink"], anchor="end")
    return cv.svg()


# ───────────────────────────── triangle construction ────────────────────────
def triangle_construction_p2(spec):
    W, H = 452, 248
    cv = Canvas(W, H, seed=_seed(spec, 6207))
    cv.text(W / 2, 18, "construct a triangle from given side lengths", size=9.8, weight=700, color=C["soft"])
    A, B, Cc = (92, 178), (350, 178), (238, 64)
    cv.polygon([A, B, Cc], color=C["blue"], w=1.7, fill=C["blue_bg"])
    cv.text(82, 193, "A", size=9, weight=700, color=C["blue"])
    cv.text(360, 193, "B", size=9, weight=700, color=C["blue"])
    cv.text(238, 55, "C", size=9, weight=700, color=C["blue"])
    cv.text(221, 195, "base", size=8.3, color=C["soft"])
    # construction arcs from the two endpoints
    cv.arc(A[0], A[1], 150, -1.38, -0.32, color=C["red"], w=1.1)
    cv.arc(B[0], B[1], 145, -2.82, -1.78, color=C["green"], w=1.1)
    cv.ticks(A, B, count=1, color=C["purple"])
    cv.text(W / 2, 229, "draw the base, intersect arcs, then join the intersection to endpoints", size=8.5, color=C["ink"])
    return cv.svg()


# ───────────────────────────── quadrilateral diagonals ───────────────────────
def quadrilateral_diagonals_p2(spec):
    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 6208))
    cv.text(W / 2, 18, "quadrilateral: diagonals join opposite vertices", size=9.8, weight=700, color=C["soft"])
    pts = [(86, 65), (356, 65), (388, 168), (55, 168)]
    cv.polygon(pts, color=C["blue"], w=1.7, fill=C["blue_bg"])
    cv.line(*pts[0], *pts[2], color=C["red"], w=1.5, dash="5 3")
    cv.line(*pts[1], *pts[3], color=C["green"], w=1.5, dash="5 3")
    for label, (x, y) in zip("ABCD", pts):
        cv.dot(x, y, r=3, color=C["purple"])
        cv.text(x, y - 10 if y < 100 else y + 19, label, size=9, weight=700, color=C["purple"])
    cv.text(W / 2, 208, "AC and BD are the two diagonals", size=9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── area grid ────────────────────────────────────
def area_grid_p2(spec):
    cols, rows = int(spec.get("cols", 6)), int(spec.get("rows", 4))
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 6209))
    cv.text(W / 2, 18, "area by counting unit squares", size=10, weight=700, color=C["soft"])
    x0, y0, s = 88, 50, 38
    for r in range(rows):
        for c in range(cols):
            fill = C["blue_bg"] if (r + c) % 2 == 0 else "#ffffff"
            cv.raw(
                f'<rect x="{x0 + c * s}" y="{y0 + r * s}" width="{s}" height="{s}" '
                f'fill="{fill}" stroke="{C["blue"]}" stroke-width="1.0"/>'
            )
    cv.text(x0 + cols * s / 2, y0 + rows * s + 22, f"length = {cols} units", size=8.8, color=C["blue"])
    cv.text(x0 - 12, y0 + rows * s / 2 + 3, f"width = {rows}", size=8.8, color=C["green"], anchor="end")
    _card(cv, 140, 215, 172, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 233, f"area = {cols} x {rows} = {cols * rows} sq units", size=8.9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── cuboid net ───────────────────────────────────
def cuboid_net_p2(spec):
    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 6210))
    cv.text(W / 2, 18, "a cuboid net has six rectangular faces", size=9.8, weight=700, color=C["soft"])
    x0, y0, w, h = 153, 88, 54, 34
    faces = [(x0, y0), (x0 + w, y0), (x0 + 2 * w, y0), (x0 + 3 * w, y0),
             (x0 + w, y0 - h), (x0 + w, y0 + h)]
    cols = [C["blue"], C["green"], C["amber"], C["purple"], C["red"], C["teal"]]
    bgs = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["purple_bg"], C["red_bg"], C["teal_bg"]]
    for i, (x, y) in enumerate(faces):
        cv.raw(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'fill="{bgs[i]}" stroke="{cols[i]}" stroke-width="1.3"/>'
        )
        cv.text(x + w / 2, y + h / 2 + 4, str(i + 1), size=9, weight=700, color=cols[i])
    cv.text(W / 2, 191, "two faces may be congruent in pairs; all six fold into the cuboid", size=8.5, color=C["ink"])
    return cv.svg()


# ───────────────────────────── double bar graph ─────────────────────────────
def double_bar_p2(spec):
    W, H = 452, 255
    cv = Canvas(W, H, seed=_seed(spec, 6211))
    cv.text(W / 2, 18, "double bar graph: compare two data sets", size=10, weight=700, color=C["soft"])
    base, x0, bw, gap, scale = 205, 62, 24, 16, 12
    labels = ["A", "B", "C", "D"]
    first = [4, 7, 5, 8]
    second = [6, 5, 8, 7]
    for i, lab in enumerate(labels):
        x = x0 + i * (2 * bw + gap + 25)
        for dx, val, col, bg in ((0, first[i], C["blue"], C["blue_bg"]),
                                  (bw + 2, second[i], C["green"], C["green_bg"])):
            hh = val * scale
            cv.raw(
                f'<rect x="{x + dx}" y="{base - hh}" width="{bw}" height="{hh}" '
                f'fill="{bg}" stroke="{col}" stroke-width="1.1"/>'
            )
        cv.text(x + bw + 1, base + 18, lab, size=8.5, weight=700, color=C["soft"])
    cv.line(48, base, 414, base, color=C["ink"], w=1.2)
    cv.text(62, 233, "blue = set 1", size=8.5, color=C["blue"], anchor="start")
    cv.text(155, 233, "green = set 2", size=8.5, color=C["green"], anchor="start")
    return cv.svg()


REGISTRY = {
    "integer-line-paper2": integer_line_p2,
    "fraction-compare-paper2": fraction_compare_p2,
    "ratio-strip-paper2": ratio_strip_p2,
    "algebra-balance-paper2": algebra_balance_p2,
    "coordinate-grid-paper2": coordinate_grid_p2,
    "parallel-lines-paper2": parallel_lines_p2,
    "triangle-construction-paper2": triangle_construction_p2,
    "quadrilateral-diagonals-paper2": quadrilateral_diagonals_p2,
    "area-grid-paper2": area_grid_p2,
    "cuboid-net-paper2": cuboid_net_p2,
    "double-bar-paper2": double_bar_p2,
}
