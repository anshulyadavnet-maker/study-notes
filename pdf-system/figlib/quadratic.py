"""
quadratic.py — figures for Chapter 31 (Quadratic Equations).

quadratic-form   : identify a, b, c and the degree-two structure
factor-roots     : factorised equation and its two root branches
formula-steps    : quadratic formula with discriminant and roots
discriminant     : positive, zero and negative discriminant cases
parabola-roots   : a parabola crossing the x-axis at its roots
root-relations   : sum/product of roots and construction of equation
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=3100):
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


def _sqrt_fmt(value):
    if value < 0:
        return "sqrt(negative)"
    root = math.sqrt(value)
    return _fmt(root) if abs(root - round(root)) < 1e-9 else f"sqrt({_fmt(value)})"


# ───────────────────────────── standard form ────────────────────────────────
def quadratic_form(spec):
    a = int(spec.get("a", 2))
    b = int(spec.get("b", -7))
    c = int(spec.get("c", 3))
    bsign = "+" if b >= 0 else "-"
    expr = f"{a}x^2 {bsign} {_fmt(abs(b))}x + {_fmt(c)} = 0"

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 3101))
    cv.text(W / 2, 20, "every quadratic equation has degree two",
            size=10.4, weight=700, color=C["soft"])
    _card(cv, 38, 48, 376, 42, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 75, expr, size=14, weight=700, color=C["purple"])

    vals = [("a", str(a), "x^2 coefficient", C["blue"], C["blue_bg"]),
            ("b", str(b), "x coefficient", C["green"], C["green_bg"]),
            ("c", str(c), "constant", C["amber"], C["amber_bg"])]
    for i, (lab, val, note, col, bg) in enumerate(vals):
        x = 28 + i * 142
        _card(cv, x, 126, 128, 54, col, bg, sw=1.5)
        cv.text(x + 64, 146, f"{lab} = {val}", size=11, weight=700, color=col)
        cv.text(x + 64, 166, note, size=7.8, color=C["soft"])
    cv.text(W / 2, 214, "a must not be zero; otherwise the equation becomes linear",
            size=8.8, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "roots are the x-values that make the equation zero",
            size=8.6, color=C["ink"])
    return cv.svg()


# ───────────────────────────── factor roots ──────────────────────────────────
def factor_roots(spec):
    r1 = int(spec.get("r1", 2))
    r2 = int(spec.get("r2", 3))
    W, H = 420, 258
    cv = Canvas(W, H, seed=_seed(spec, 3102))
    cv.text(W / 2, 20, "factorisation turns one quadratic into two root choices",
            size=9.9, weight=700, color=C["soft"])
    _card(cv, 48, 48, 324, 34, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(210, 70, f"(x-{r1})(x-{r2}) = 0", size=12, weight=700, color=C["blue"])
    cv.line(210, 84, 128, 112, color=C["grey"], w=1.2)
    cv.line(210, 84, 292, 112, color=C["grey"], w=1.2)
    _card(cv, 42, 112, 172, 38, C["green"], C["green_bg"], sw=1.5)
    cv.text(128, 137, f"x-{r1}=0", size=11, weight=700, color=C["green"])
    _card(cv, 206, 112, 172, 38, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(292, 137, f"x-{r2}=0", size=11, weight=700, color=C["amber"])
    _card(cv, 66, 180, 288, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(210, 202, f"roots: x={r1} or x={r2}", size=10.5, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "zero-product property gives both roots",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── quadratic formula ────────────────────────────
def formula_steps(spec):
    a = float(spec.get("a", 2))
    b = float(spec.get("b", -7))
    c = float(spec.get("c", 3))
    disc = b * b - 4 * a * c
    root_disc = math.sqrt(disc) if disc >= 0 else 0
    r1 = (-b + root_disc) / (2 * a) if disc >= 0 else 0
    r2 = (-b - root_disc) / (2 * a) if disc >= 0 else 0
    bsign = "+" if b >= 0 else "-"

    W, H = 452, 292
    cv = Canvas(W, H, seed=_seed(spec, 3103))
    cv.text(W / 2, 20, "quadratic formula works even when factoring is not obvious",
            size=9.5, weight=700, color=C["soft"])
    lines = [
        (f"{_fmt(a)}x^2 {bsign} {_fmt(abs(b))}x + {_fmt(c)} = 0", "given", C["blue"], C["blue_bg"]),
        (f"D = b^2 - 4ac = {_fmt(disc)}", "discriminant", C["green"], C["green_bg"]),
        (f"x = (-b +/- sqrt(D)) / (2a)", "formula", C["amber"], C["amber_bg"]),
        (f"x = {_fmt(r1)} or {_fmt(r2)}", "roots", C["purple"], C["purple_bg"]),
    ]
    for i, (text, note, col, bg) in enumerate(lines):
        y = 44 + i * 44
        _card(cv, 34, y, 326, 32, col, bg, r=5, sw=1.4)
        cv.text(48, y + 21, text, size=9.5, anchor="start", weight=700, color=col)
        cv.text(404, y + 21, note, size=8.4, anchor="end", color=C["soft"])
    _card(cv, 76, 226, 300, 28, C["red"], C["red_bg"], sw=1.5)
    cv.text(226, 245, f"D={_fmt(disc)}; sqrt(D)={_fmt(root_disc)}",
            size=9.3, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "plus and minus give two possible roots",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── discriminant cases ───────────────────────────
def discriminant(spec):
    W, H = 452, 276
    cv = Canvas(W, H, seed=_seed(spec, 3104))
    cv.text(W / 2, 20, "D = b^2 - 4ac decides the nature of the roots",
            size=9.8, weight=700, color=C["soft"])
    cases = [("D > 0", "two real roots", C["blue"], C["blue_bg"]),
             ("D = 0", "equal real roots", C["green"], C["green_bg"]),
             ("D < 0", "no real roots", C["red"], C["red_bg"])]
    for i, (label, note, col, bg) in enumerate(cases):
        x = 28 + i * 142
        _card(cv, x, 54, 126, 62, col, bg, sw=1.6)
        cv.text(x + 63, 78, label, size=12, weight=700, color=col)
        cv.text(x + 63, 99, note, size=8.2, color=col)

    # small symbolic curves below the cards
    for i, col in enumerate((C["blue"], C["green"], C["red"])):
        ox = 90 + i * 142
        cv.line(ox - 48, 205, ox + 48, 205, color=C["grey"], w=0.9)
        cv.line(ox, 148, ox, 228, color=C["grey"], w=0.9)
        if i == 0:
            pts = [(ox - 42, 220), (ox - 20, 184), (ox, 168), (ox + 20, 184), (ox + 42, 220)]
        elif i == 1:
            pts = [(ox - 42, 220), (ox - 20, 184), (ox, 205), (ox + 20, 184), (ox + 42, 220)]
        else:
            pts = [(ox - 42, 220), (ox - 20, 184), (ox, 166), (ox + 20, 184), (ox + 42, 220)]
        for p, q in zip(pts, pts[1:]):
            cv.line(*p, *q, color=col, w=1.8)
    cv.text(W / 2, 250, "D>0 crosses x-axis; D=0 touches; D<0 misses real x-axis",
            size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ───────────────────────────── parabola and roots ───────────────────────────
def parabola_roots(spec):
    W, H = 452, 282
    cv = Canvas(W, H, seed=_seed(spec, 3105))
    cv.text(W / 2, 20, "roots are the x-intercepts of y = ax^2 + bx + c",
            size=9.8, weight=700, color=C["soft"])
    ox, oy, scale = 226, 204, 32
    cv.line(ox - 5 * scale, oy, ox + 5 * scale, oy, color=C["ink"], w=1.2)
    cv.line(ox, oy - 5 * scale, ox, oy + 1 * scale, color=C["ink"], w=1.2)
    # y=(x-1)(x-3)=x^2-4x+3, vertex at (2,-1)
    pts = []
    for i in range(-8, 25):
        x = i / 4
        y = (x - 1) * (x - 3)
        pts.append((ox + x * scale, oy - y * scale))
    for p, q in zip(pts, pts[1:]):
        cv.line(*p, *q, color=C["blue"], w=1.8)
    for x, label in ((1, "root 1"), (3, "root 2")):
        px, py = ox + x * scale, oy
        cv.dot(px, py, r=4.5, color=C["red"])
        cv.text(px, py + 19, label, size=8.2, weight=700, color=C["red"])
    vx, vy = ox + 2 * scale, oy + 1 * scale
    cv.dot(vx, vy, r=3.5, color=C["amber"])
    cv.text(vx + 8, vy + 4, "vertex (2,-1)", size=8, color=C["amber"])
    _card(cv, 52, 246, 348, 24, C["purple"], C["purple_bg"], sw=1.4)
    cv.text(226, 263, "y=(x-1)(x-3); roots x=1 and x=3", size=9.2,
            weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── root relationships ───────────────────────────
def root_relations(spec):
    a = int(spec.get("a", 2))
    b = int(spec.get("b", -7))
    c = int(spec.get("c", 3))
    sum_roots = -b / a
    product = c / a
    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 3106))
    cv.text(W / 2, 20, "roots and coefficients are linked without solving both roots",
            size=9.7, weight=700, color=C["soft"])
    _card(cv, 42, 46, 368, 36, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(226, 69, f"{a}x^2 + ({b})x + {c} = 0", size=13, weight=700, color=C["blue"])
    _card(cv, 46, 108, 166, 48, C["green"], C["green_bg"], sw=1.6)
    cv.text(129, 129, "alpha + beta", size=9.5, weight=700, color=C["green"])
    cv.text(129, 148, f"= -b/a = {_fmt(sum_roots)}", size=9.2, color=C["green"])
    _card(cv, 240, 108, 166, 48, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(323, 129, "alpha x beta", size=9.5, weight=700, color=C["amber"])
    cv.text(323, 148, f"= c/a = {_fmt(product)}", size=9.2, color=C["amber"])
    _card(cv, 78, 190, 296, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 210, "equation from roots r1,r2: x^2-(r1+r2)x+r1r2=0",
            size=8.8, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "for ax^2+bx+c=0, divide coefficients by a",
            size=8.5, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "quadratic-form": quadratic_form,
    "factor-roots": factor_roots,
    "formula-steps": formula_steps,
    "discriminant": discriminant,
    "parabola-roots": parabola_roots,
    "root-relations": root_relations,
}
