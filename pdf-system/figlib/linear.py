"""
linear.py — figures for Chapter 30 (Linear Equations & Graphs).

coordinate-plane   : axes, origin, quadrants and plotted points
linear-table       : an x/y value table for a line
line-graph         : plot points and join them into a straight line
intercept-graph    : x- and y-intercepts of a line
system-intersection: two lines meeting at the solution point
slope-lines        : positive, zero and negative slope comparison
"""
from .sketch import Canvas, C


def _seed(spec, default=3000):
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


def _plot(cv, x, y, ox=226, oy=128, scale=24, color=None, radius=3.5):
    cv.dot(ox + x * scale, oy - y * scale, r=radius, color=color or C["red"])


def _axes(cv, xmin=-5, xmax=5, ymin=-4, ymax=4, ox=226, oy=128, scale=24):
    cv.line(ox + xmin * scale, oy, ox + xmax * scale, oy, color=C["ink"], w=1.3)
    cv.arrow(ox + (xmax - 0.3) * scale, oy, ox + xmax * scale + 8, oy, color=C["ink"], w=1.2)
    cv.line(ox, oy - ymin * scale, ox, oy - ymax * scale, color=C["ink"], w=1.3)
    cv.arrow(ox, oy - (ymax - 0.3) * scale, ox, oy - ymax * scale - 8, color=C["ink"], w=1.2)
    for x in range(xmin, xmax + 1):
        if x:
            px = ox + x * scale
            cv.line(px, oy - 3, px, oy + 3, color=C["grey"], w=0.8)
            cv.text(px, oy + 14, str(x), size=7.2, color=C["soft"])
    for y in range(ymin, ymax + 1):
        if y:
            py = oy - y * scale
            cv.line(ox - 3, py, ox + 3, py, color=C["grey"], w=0.8)
            cv.text(ox - 10, py + 3, str(y), size=7.2, anchor="end", color=C["soft"])
    cv.text(ox + xmax * scale + 12, oy - 5, "x", size=9, weight=700, color=C["ink"])
    cv.text(ox + 7, oy - ymax * scale - 8, "y", size=9, weight=700, color=C["ink"])
    cv.text(ox + 7, oy + 14, "O", size=7.5, weight=700, color=C["ink"])


# ───────────────────────────── coordinate plane ─────────────────────────────
def coordinate_plane(spec):
    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 3001))
    cv.text(W / 2, 20, "a point is written as (x, y): move x, then y",
            size=10.1, weight=700, color=C["soft"])
    ox, oy, scale = 226, 137, 23
    _axes(cv, ox=ox, oy=oy, scale=scale)
    points = [(2, 2, "A", C["blue"]), (-3, 1, "B", C["green"]),
              (-2, -2, "C", C["red"]), (3, -2, "D", C["amber"])]
    for x, y, lab, col in points:
        _plot(cv, x, y, ox, oy, scale, col, 4)
        cv.text(ox + x * scale + 8, oy - y * scale - 8, lab, size=8.6,
                weight=700, color=col)
    cv.text(92, 52, "QII", size=8.5, weight=700, color=C["green"])
    cv.text(332, 52, "QI", size=8.5, weight=700, color=C["blue"])
    cv.text(92, 226, "QIII", size=8.5, weight=700, color=C["red"])
    cv.text(332, 226, "QIV", size=8.5, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "horizontal coordinate x; vertical coordinate y",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── value table ──────────────────────────────────
def linear_table(spec):
    a = int(spec.get("a", 2))
    c = int(spec.get("c", 1))
    xs = [-2, -1, 0, 1, 2]
    ys = [a * x + c for x in xs]

    W, H = 452, 230
    cv = Canvas(W, H, seed=_seed(spec, 3002))
    cv.text(W / 2, 20, f"make points from the table for y = {a}x + {c}",
            size=10.2, weight=700, color=C["soft"])
    x0, y0, cw, ch = 34, 52, 76, 34
    headers = ["x"] + [str(x) for x in xs]
    values = ["y"] + [str(y) for y in ys]
    for row, vals, col, bg in ((0, headers, C["blue"], C["blue_bg"]),
                               (1, values, C["green"], C["green_bg"])):
        for j, value in enumerate(vals):
            x = x0 + j * cw
            _card(cv, x, y0 + row * ch, cw - 4, ch - 4, col, bg, r=4, sw=1.2)
            cv.text(x + (cw - 4) / 2, y0 + row * ch + 20, value, size=10,
                    weight=700, color=col)
    _card(cv, 58, 144, 336, 34, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 166, "each ordered pair (x, y) is a point on the line",
            size=9.3, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "two points are enough to draw a straight line",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── graph a line ─────────────────────────────────
def line_graph(spec):
    a = float(spec.get("a", 2))
    c = float(spec.get("c", 1))
    W, H = 452, 282
    cv = Canvas(W, H, seed=_seed(spec, 3003))
    cv.text(W / 2, 20, f"plot y = { _fmt(a) }x + { _fmt(c) } and join the points",
            size=9.8, weight=700, color=C["soft"])
    ox, oy, scale = 226, 148, 22
    _axes(cv, xmin=-5, xmax=5, ymin=-5, ymax=5, ox=ox, oy=oy, scale=scale)
    pts = [(-4, a * -4 + c), (4, a * 4 + c)]
    cv.line(ox + pts[0][0] * scale, oy - pts[0][1] * scale,
            ox + pts[1][0] * scale, oy - pts[1][1] * scale, color=C["blue"], w=2)
    for x in (-2, 0, 2):
        y = a * x + c
        if -5 <= y <= 5:
            _plot(cv, x, y, ox, oy, scale, C["red"], 4)
            cv.text(ox + x * scale + 7, oy - y * scale - 8,
                    f"({x},{_fmt(y)})", size=7.5, color=C["red"])
    _card(cv, 54, 250, 344, 24, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 267, f"slope m = {_fmt(a)}; y-intercept c = {_fmt(c)}",
            size=9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── intercepts ───────────────────────────────────
def intercept_graph(spec):
    a = int(spec.get("a", 2))
    b = int(spec.get("b", 3))
    c = int(spec.get("c", 6))
    xint = c / a if a else 0
    yint = c / b if b else 0

    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 3004))
    cv.text(W / 2, 20, f"intercepts of {a}x + {b}y = {c}",
            size=10.3, weight=700, color=C["soft"])
    ox, oy, scale = 100, 192, 30
    _axes(cv, xmin=-2, xmax=8, ymin=-2, ymax=5, ox=ox, oy=oy, scale=scale)
    p1 = (ox + xint * scale, oy)
    p2 = (ox, oy - yint * scale)
    cv.line(*p1, *p2, color=C["blue"], w=2)
    cv.dot(*p1, r=4.5, color=C["red"])
    cv.dot(*p2, r=4.5, color=C["green"])
    cv.text(p1[0] + 8, p1[1] - 10, f"({ _fmt(xint) },0)", size=8.3,
            weight=700, color=C["red"])
    cv.text(p2[0] + 8, p2[1] - 8, f"(0,{ _fmt(yint) })", size=8.3,
            weight=700, color=C["green"])
    _card(cv, 252, 74, 164, 38, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(334, 98, f"x-int = {c}/{a} = {_fmt(xint)}", size=9.2, weight=700, color=C["purple"])
    _card(cv, 252, 128, 164, 38, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(334, 152, f"y-int = {c}/{b} = {_fmt(yint)}", size=9.2, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "put y=0 for x-intercept; put x=0 for y-intercept",
            size=8.6, color=C["ink"])
    return cv.svg()


# ───────────────────────────── simultaneous intersection ────────────────────
def system_intersection(spec):
    # x+y=5 and x-y=1 -> (3,2)
    W, H = 452, 282
    cv = Canvas(W, H, seed=_seed(spec, 3005))
    cv.text(W / 2, 20, "the intersection point satisfies both equations",
            size=9.9, weight=700, color=C["soft"])
    ox, oy, scale = 226, 166, 25
    _axes(cv, xmin=-4, xmax=5, ymin=-4, ymax=5, ox=ox, oy=oy, scale=scale)
    # y=5-x and y=x-1
    cv.line(ox - 4 * scale, oy - 1 * scale, ox + 4 * scale, oy - 9 * scale,
            color=C["blue"], w=1.8)
    cv.line(ox - 3 * scale, oy - (-4) * scale, ox + 4 * scale, oy - 3 * scale,
            color=C["green"], w=1.8)
    px, py = ox + 3 * scale, oy - 2 * scale
    cv.dot(px, py, r=5, color=C["red"])
    cv.text(px + 8, py - 10, "(3,2)", size=8.8, weight=700, color=C["red"])
    _card(cv, 54, 242, 344, 24, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 259, "x+y=5 and x-y=1 meet at x=3, y=2", size=9.1,
            weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── slope comparison ─────────────────────────────
def slope_lines(spec):
    W, H = 452, 264
    cv = Canvas(W, H, seed=_seed(spec, 3006))
    cv.text(W / 2, 20, "slope tells the direction and steepness of a line",
            size=10.1, weight=700, color=C["soft"])
    ox, oy, scale = 226, 132, 22
    _axes(cv, xmin=-5, xmax=5, ymin=-4, ymax=4, ox=ox, oy=oy, scale=scale)
    # Positive, zero and negative slopes within the plot.
    cv.line(ox - 4 * scale, oy + 2 * scale, ox + 4 * scale, oy - 2 * scale,
            color=C["blue"], w=1.8)
    cv.line(ox - 4 * scale, oy, ox + 4 * scale, oy,
            color=C["green"], w=1.8)
    cv.line(ox - 4 * scale, oy - 2 * scale, ox + 4 * scale, oy + 2 * scale,
            color=C["red"], w=1.8)
    cv.text(330, 60, "m > 0", size=8.8, weight=700, color=C["blue"])
    cv.text(330, 78, "m = 0", size=8.8, weight=700, color=C["green"])
    cv.text(330, 96, "m < 0", size=8.8, weight=700, color=C["red"])
    _card(cv, 64, 218, 324, 26, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 236, "m = (y2-y1)/(x2-x1)", size=10, weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "coordinate-plane": coordinate_plane,
    "linear-table": linear_table,
    "line-graph": line_graph,
    "intercept-graph": intercept_graph,
    "system-intersection": system_intersection,
    "slope-lines": slope_lines,
}
