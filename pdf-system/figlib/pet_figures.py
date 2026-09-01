"""Small vector graphs used by the UPSSSC PET mock tests.

The graphs keep labels numeric or alphabetic so they remain sharp and compact;
the Hindi instructions, data tables and explanations are written in Markdown.
"""

from .sketch import Canvas, C


def _seed(spec, default=10100):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def pet_bar_graph(spec):
    categories = spec.get("categories", ["A", "B", "C", "D", "E"])
    values = spec.get("values", [20, 35, 25, 40, 30])
    try:
        categories = [str(x) for x in categories]
        values = [float(x) for x in values]
    except (TypeError, ValueError):
        categories, values = ["A", "B", "C", "D", "E"], [20, 35, 25, 40, 30]
    if len(categories) != len(values) or not values:
        categories, values = ["A", "B", "C", "D", "E"], [20, 35, 25, 40, 30]
    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 10101))
    x0, y0, plot_w, plot_h = 56, 220, 352, 166
    top = max(max(values), 1)
    ceiling = int((top + 9) // 10) * 10
    cv.line(x0, y0, x0 + plot_w, y0, color=C["ink"], w=1.4)
    cv.line(x0, y0, x0, y0 - plot_h, color=C["ink"], w=1.4)
    for tick in range(0, ceiling + 1, 10):
        yy = y0 - plot_h * tick / ceiling
        cv.line(x0 - 4, yy, x0 + plot_w, yy, color="#d8e0ea", w=0.75)
        cv.text(x0 - 10, yy + 3, str(tick), size=7.5, color=C["soft"], anchor="end")
    slot = plot_w / len(values)
    bw = min(38, slot * 0.58)
    colors = [C["blue"], C["green"], C["amber"], C["red"], C["purple"]]
    for i, (lab, val) in enumerate(zip(categories, values)):
        cx = x0 + slot * (i + 0.5)
        hh = plot_h * val / ceiling
        col = colors[i % len(colors)]
        cv.raw(f'<rect x="{cx - bw / 2:.2f}" y="{y0 - hh:.2f}" width="{bw:.2f}" height="{hh:.2f}" fill="{col}" fill-opacity="0.16" stroke="{col}" stroke-width="1.4"/>')
        cv.text(cx, y0 - hh - 8, str(int(val) if val.is_integer() else val), size=8, weight=700, color=col)
        cv.text(cx, y0 + 17, lab, size=8.5, weight=700, color=C["soft"])
    return cv.svg()


def pet_line_graph(spec):
    labels = spec.get("labels", ["2021", "2022", "2023", "2024", "2025"])
    values = spec.get("values", [12, 18, 15, 24, 20])
    try:
        labels = [str(x) for x in labels]
        values = [float(x) for x in values]
    except (TypeError, ValueError):
        labels, values = ["2021", "2022", "2023", "2024", "2025"], [12, 18, 15, 24, 20]
    if len(labels) != len(values) or not values:
        labels, values = ["2021", "2022", "2023", "2024", "2025"], [12, 18, 15, 24, 20]
    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 10102))
    x0, y0, plot_w, plot_h = 56, 220, 352, 166
    top = max(max(values), 1)
    ceiling = int((top + 4) // 5) * 5
    cv.line(x0, y0, x0 + plot_w, y0, color=C["ink"], w=1.4)
    cv.line(x0, y0, x0, y0 - plot_h, color=C["ink"], w=1.4)
    for tick in range(0, ceiling + 1, 5):
        yy = y0 - plot_h * tick / ceiling
        cv.line(x0 - 4, yy, x0 + plot_w, yy, color="#d8e0ea", w=0.75)
        cv.text(x0 - 10, yy + 3, str(tick), size=7.5, color=C["soft"], anchor="end")
    step = plot_w / max(len(values) - 1, 1)
    points = []
    for i, (lab, val) in enumerate(zip(labels, values)):
        x = x0 + step * i
        y = y0 - plot_h * val / ceiling
        points.append((x, y))
        cv.text(x, y0 + 17, lab, size=7.5, weight=700, color=C["soft"])
    for a, b in zip(points, points[1:]):
        cv.line(*a, *b, color=C["blue"], w=2.0)
    for (x, y), val in zip(points, values):
        cv.dot(x, y, r=4.2, color=C["red"])
        cv.text(x, y - 9, str(int(val) if val.is_integer() else val), size=8, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "pet-bar-graph": pet_bar_graph,
    "pet-line-graph": pet_line_graph,
}
