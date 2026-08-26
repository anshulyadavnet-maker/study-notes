"""
comparison.py — figures for Chapter 32 (Quadratic Comparison).

compare-factor-roots : two factorised quadratics and their root ranges
root-numberline      : place possible roots on a common number line
comparison-cases     : greater, less and cannot-determine outcomes
quadratic-interval   : use a parabola/sign changes to bracket roots
vieta-box            : compare sum and product of roots
formula-bound        : quadratic formula and approximate root bounds
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3200):
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


def _axis(cv, x0=48, x1=408, y=118, lo=0, hi=10):
    cv.line(x0, y, x1, y, color=C["ink"], w=1.5)
    cv.arrow(x1 - 10, y, x1 + 8, y, color=C["ink"], w=1.2)
    for n in range(lo, hi + 1):
        px = x0 + (n - lo) / (hi - lo) * (x1 - x0)
        cv.line(px, y - 4, px, y + 4, color=C["grey"], w=0.9)
        cv.text(px, y + 17, str(n), size=7.8, color=C["soft"])


# ───────────────────────────── factor roots and ranges ──────────────────────
def compare_factor_roots(spec):
    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 3201))
    cv.text(W / 2, 20, "solve both equations, then compare the root ranges",
            size=9.9, weight=700, color=C["soft"])

    _card(cv, 34, 44, 184, 42, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(126, 64, "I: (x-3)(x-4)=0", size=9.3, weight=700, color=C["blue"])
    cv.text(126, 80, "x = 3 or 4", size=9.2, color=C["blue"])
    _card(cv, 234, 44, 184, 42, C["green"], C["green_bg"], sw=1.6)
    cv.text(326, 64, "II: (y-5)(y-6)=0", size=9.3, weight=700, color=C["green"])
    cv.text(326, 80, "y = 5 or 6", size=9.2, color=C["green"])

    _axis(cv, y=132, lo=0, hi=7)
    for n, col, label in ((3, C["blue"], "x"), (4, C["blue"], "x"),
                          (5, C["green"], "y"), (6, C["green"], "y")):
        px = 48 + n / 7 * 360
        cv.dot(px, 132, r=4.5, color=col)
        cv.text(px, 105 if label == "x" else 155, label, size=8.3, weight=700, color=col)
    _card(cv, 80, 194, 292, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 214, "every root of I is less than every root of II -> x < y",
            size=8.9, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── common number line ────────────────────────────
def root_numberline(spec):
    W, H = 452, 248
    cv = Canvas(W, H, seed=_seed(spec, 3202))
    cv.text(W / 2, 20, "compare intervals, not just one selected root",
            size=10.2, weight=700, color=C["soft"])
    _axis(cv, y=126, lo=-3, hi=8)
    x0, span = 48, 360 / 11
    for low, high, col, y, label in ((1, 3, C["blue"], 94, "equation I: [1,3]"),
                                     (5, 7, C["green"], 162, "equation II: [5,7]")):
        x1, x2 = x0 + (low + 3) * span, x0 + (high + 3) * span
        cv.line(x1, y, x2, y, color=col, w=5)
        cv.dot(x1, y, r=4, color=col)
        cv.dot(x2, y, r=4, color=col)
        cv.text((x1 + x2) / 2, y - 12, label, size=8.4, weight=700, color=col)
    _card(cv, 78, 200, 296, 28, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 219, "disjoint intervals give a definite comparison",
            size=9.1, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── outcomes ──────────────────────────────────────
def comparison_cases(spec):
    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 3203))
    cv.text(W / 2, 20, "three possible outcomes in bank comparison questions",
            size=9.8, weight=700, color=C["soft"])
    cases = [("x > y", "all x-roots lie right", C["blue"], C["blue_bg"]),
             ("x < y", "all x-roots lie left", C["green"], C["green_bg"]),
             ("cannot decide", "root ranges overlap", C["red"], C["red_bg"])]
    for i, (answer, note, col, bg) in enumerate(cases):
        x = 28 + i * 142
        _card(cv, x, 54, 126, 76, col, bg, sw=1.6)
        cv.text(x + 63, 82, answer, size=11, weight=700, color=col)
        cv.text(x + 63, 105, note, size=7.8, color=col)
        cv.line(x + 20, 158, x + 106, 158, color=C["ink"], w=1.1)
        if i == 0:
            cv.dot(x + 35, 158, r=3.5, color=C["green"])
            cv.dot(x + 88, 158, r=3.5, color=C["blue"])
            cv.arrow(x + 46, 158, x + 78, 158, color=C["blue"], w=1.2)
        elif i == 1:
            cv.dot(x + 35, 158, r=3.5, color=C["blue"])
            cv.dot(x + 88, 158, r=3.5, color=C["green"])
            cv.arrow(x + 78, 158, x + 46, 158, color=C["green"], w=1.2)
        else:
            cv.dot(x + 50, 158, r=3.5, color=C["blue"])
            cv.dot(x + 72, 158, r=3.5, color=C["green"])
    cv.text(W / 2, H - 10, "never force a relation when possible roots overlap",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── bracket roots by signs ───────────────────────
def quadratic_interval(spec):
    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 3204))
    cv.text(W / 2, 20, "a sign change brackets a root between two test values",
            size=9.7, weight=700, color=C["soft"])
    # Symbolic upward parabola crossing at 2 and 5.
    ox, oy, sx = 226, 190, 34
    cv.line(ox - 5 * sx, oy, ox + 5 * sx, oy, color=C["ink"], w=1.2)
    cv.line(ox, oy - 130, ox, oy + 10, color=C["ink"], w=1.2)
    pts = []
    for i in range(-20, 31):
        x = i / 5
        y = (x - 2) * (x - 5)
        pts.append((ox + x * sx, oy - y * 16))
    for p, q in zip(pts, pts[1:]):
        cv.line(*p, *q, color=C["blue"], w=1.8)
    for x, label, col in ((2, "root", C["red"]), (5, "root", C["red"])):
        px = ox + x * sx
        cv.dot(px, oy, r=4, color=col)
        cv.text(px, oy + 18, label, size=8, weight=700, color=col)
    _card(cv, 48, 54, 156, 34, C["green"], C["green_bg"], sw=1.5)
    cv.text(126, 76, "f(1) > 0, f(3) < 0", size=9.4, weight=700, color=C["green"])
    _card(cv, 248, 54, 156, 34, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(326, 76, "root lies between 1 and 3", size=8.8, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "use intervals to compare without exact radicals",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── Vieta comparison ──────────────────────────────
def vieta_box(spec):
    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 3205))
    cv.text(W / 2, 20, "Vieta gives root sum and product instantly",
            size=10, weight=700, color=C["soft"])
    _card(cv, 42, 48, 368, 34, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(226, 70, "ax^2 + bx + c = 0", size=13, weight=700, color=C["blue"])
    _card(cv, 48, 106, 160, 54, C["green"], C["green_bg"], sw=1.6)
    cv.text(128, 127, "alpha + beta", size=9.8, weight=700, color=C["green"])
    cv.text(128, 147, "= -b/a", size=11, weight=700, color=C["green"])
    _card(cv, 244, 106, 160, 54, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(324, 127, "alpha x beta", size=9.8, weight=700, color=C["amber"])
    cv.text(324, 147, "= c/a", size=11, weight=700, color=C["amber"])
    _card(cv, 70, 190, 312, 28, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 209, "compare sums/products only when they determine the range",
            size=8.7, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── formula and bounds ────────────────────────────
def formula_bound(spec):
    a = float(spec.get("a", 1))
    b = float(spec.get("b", -7))
    c = float(spec.get("c", 12))
    disc = b * b - 4 * a * c
    root = math.sqrt(disc) if disc >= 0 else 0
    r1 = (-b + root) / (2 * a) if disc >= 0 else 0
    r2 = (-b - root) / (2 * a) if disc >= 0 else 0

    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 3206))
    cv.text(W / 2, 20, "formula values can be bounded before full comparison",
            size=9.6, weight=700, color=C["soft"])
    lines = [(f"D = b^2 - 4ac = {_fmt(disc)}", "discriminant", C["blue"], C["blue_bg"]),
             (f"sqrt(D) = {_fmt(root)}", "root part", C["green"], C["green_bg"]),
             (f"x1 = {_fmt(r1)}, x2 = {_fmt(r2)}", "possible roots", C["purple"], C["purple_bg"])]
    for i, (text, note, col, bg) in enumerate(lines):
        y = 50 + i * 42
        _card(cv, 42, y, 368, 30, col, bg, r=5, sw=1.3)
        cv.text(54, y + 20, text, size=9.2, anchor="start", weight=700, color=col)
        cv.text(398, y + 20, note, size=8.2, anchor="end", color=C["soft"])
    _card(cv, 68, 190, 316, 34, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 212, "compare the smaller and larger root ranges separately",
            size=9.1, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "do not compare only one arbitrary root",
            size=8.7, color=C["red"])
    return cv.svg()


REGISTRY = {
    "compare-factor-roots": compare_factor_roots,
    "root-numberline": root_numberline,
    "comparison-cases": comparison_cases,
    "quadratic-interval": quadratic_interval,
    "vieta-box": vieta_box,
    "formula-bound": formula_bound,
}
