"""
identities.py — figures for Chapter 28 (Algebraic Identities).

square-sum       : area decomposition for (a+b)^2
square-difference: visual structure of (a-b)^2
difference-squares: product (a+b)(a-b) and a^2-b^2
cube-identity    : the four terms of a cube expansion
three-variable   : the symmetric a^3+b^3+c^3 identity
mental-square    : use a nearby base to square a number quickly
"""
from .sketch import Canvas, C


def _seed(spec, default=2800):
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


# ───────────────────────────── (a+b)^2 area ────────────────────────────────
def square_sum(spec):
    a = float(spec.get("a", 3))
    b = float(spec.get("b", 2))
    total = a + b
    W, H = 452, 278
    cv = Canvas(W, H, seed=_seed(spec, 2801))
    cv.text(W / 2, 20, "the big square is split into four familiar areas",
            size=10, weight=700, color=C["soft"])

    x0, y0, side = 56, 48, 170
    scale = side / total
    aw, bw = a * scale, b * scale
    # Four area pieces of a square of side a+b.
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{aw:.2f}" height="{aw:.2f}" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.5"/>')
    cv.raw(f'<rect x="{x0+aw:.2f}" y="{y0}" width="{bw:.2f}" height="{aw:.2f}" '
           f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.5"/>')
    cv.raw(f'<rect x="{x0}" y="{y0+aw:.2f}" width="{aw:.2f}" height="{bw:.2f}" '
           f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.5"/>')
    cv.raw(f'<rect x="{x0+aw:.2f}" y="{y0+aw:.2f}" width="{bw:.2f}" height="{bw:.2f}" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.5"/>')
    cv.text(x0 + aw / 2, y0 + aw / 2 + 5, "a^2", size=12, weight=700, color=C["blue"])
    cv.text(x0 + aw + bw / 2, y0 + aw / 2 + 5, "ab", size=10, weight=700, color=C["green"])
    cv.text(x0 + aw / 2, y0 + aw + bw / 2 + 5, "ab", size=10, weight=700, color=C["green"])
    cv.text(x0 + aw + bw / 2, y0 + aw + bw / 2 + 5, "b^2", size=10, weight=700, color=C["amber"])
    cv.text(x0 + side / 2, y0 - 12, f"a + b = {_fmt(total)}", size=8.8, weight=700, color=C["purple"])
    cv.text(x0 - 14, y0 + side / 2, f"a+b", size=8.8, anchor="end", weight=700, color=C["purple"])

    _card(cv, 270, 68, 150, 34, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(345, 90, "(a+b)^2", size=12, weight=700, color=C["purple"])
    cv.text(345, 124, "= a^2 + ab + ab + b^2", size=9.2, weight=700, color=C["ink"])
    _card(cv, 266, 148, 158, 38, C["green"], C["green_bg"], sw=1.7)
    cv.text(345, 172, "= a^2 + 2ab + b^2", size=10.2, weight=700, color=C["green"])
    cv.text(W / 2, 220, f"for a={_fmt(a)}, b={_fmt(b)}:  ({_fmt(total)})^2 = {_fmt(total*total)}",
            size=9.2, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "identity comes from area, not memorisation alone",
            size=8.7, color=C["soft"])
    return cv.svg()


# ───────────────────────────── (a-b)^2 ──────────────────────────────────────
def square_difference(spec):
    a = float(spec.get("a", 5))
    b = float(spec.get("b", 2))
    value = (a - b) ** 2

    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 2802))
    cv.text(W / 2, 20, "subtracting a length creates two negative strips and b^2",
            size=9.8, weight=700, color=C["soft"])

    x0, y0, side = 54, 50, 150
    scale = side / a
    remain = (a - b) * scale
    cut = b * scale
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{remain:.2f}" height="{remain:.2f}" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.6"/>')
    cv.raw(f'<rect x="{x0+remain:.2f}" y="{y0}" width="{cut:.2f}" height="{remain:.2f}" '
           f'fill="{C["red_bg"]}" stroke="{C["red"]}" stroke-width="1.3"/>')
    cv.raw(f'<rect x="{x0}" y="{y0+remain:.2f}" width="{remain:.2f}" height="{cut:.2f}" '
           f'fill="{C["red_bg"]}" stroke="{C["red"]}" stroke-width="1.3"/>')
    cv.raw(f'<rect x="{x0+remain:.2f}" y="{y0+remain:.2f}" width="{cut:.2f}" height="{cut:.2f}" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.3"/>')
    cv.text(x0 + remain / 2, y0 + remain / 2 + 5, "a^2", size=12, weight=700, color=C["blue"])
    cv.text(x0 + remain + cut / 2, y0 + remain / 2 + 5, "-ab", size=9, weight=700, color=C["red"])
    cv.text(x0 + remain / 2, y0 + remain + cut / 2 + 4, "-ab", size=9, weight=700, color=C["red"])
    cv.text(x0 + remain + cut / 2, y0 + remain + cut / 2 + 4, "b^2", size=9, weight=700, color=C["amber"])

    _card(cv, 264, 58, 158, 36, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(343, 81, "(a-b)^2", size=12, weight=700, color=C["purple"])
    _card(cv, 258, 116, 170, 38, C["green"], C["green_bg"], sw=1.7)
    cv.text(343, 140, "= a^2 - 2ab + b^2", size=10.3, weight=700, color=C["green"])
    cv.text(343, 182, f"({ _fmt(a) }-{_fmt(b)})^2 = {_fmt(value)}",
            size=9.3, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "the middle term is negative twice ab",
            size=8.8, color=C["soft"])
    return cv.svg()


# ───────────────────────────── difference of squares ────────────────────────
def difference_squares(spec):
    a = float(spec.get("a", 7))
    b = float(spec.get("b", 3))
    left = (a + b) * (a - b)
    right = a * a - b * b

    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 2803))
    cv.text(W / 2, 20, "conjugate factors cancel the middle terms",
            size=10.1, weight=700, color=C["soft"])

    _card(cv, 32, 52, 178, 42, C["blue"], C["blue_bg"], sw=1.7)
    cv.text(121, 70, "(a+b)(a-b)", size=12, weight=700, color=C["blue"])
    cv.text(121, 86, "= a^2 - ab + ab - b^2", size=8.9, color=C["blue"])
    cv.arrow(214, 73, 238, 73, color=C["grey"], w=1.3)
    _card(cv, 244, 52, 176, 42, C["green"], C["green_bg"], sw=1.7)
    cv.text(332, 70, "a^2 - b^2", size=12, weight=700, color=C["green"])
    cv.text(332, 86, "middle terms cancel", size=8.7, color=C["green"])

    rows = [("a+b", _fmt(a + b), C["blue"]), ("a-b", _fmt(a - b), C["red"]),
            ("product", _fmt(left), C["purple"]), ("a^2-b^2", _fmt(right), C["amber"])]
    for i, (lab, value, col) in enumerate(rows):
        x = 52 + (i % 2) * 190
        y = 128 + (i // 2) * 44
        _card(cv, x, y, 160, 30, col, "#ffffff", r=5, sw=1.2)
        cv.text(x + 12, y + 20, lab, size=8.8, anchor="start", color=C["soft"])
        cv.text(x + 148, y + 20, value, size=9.6, anchor="end", weight=700, color=col)
    cv.text(W / 2, H - 8, f"({_fmt(a)}+{_fmt(b)})({_fmt(a)}-{_fmt(b)}) = {_fmt(right)}",
            size=9, weight=700, color=C["ink"])
    return cv.svg()


# ───────────────────────────── cube expansion ───────────────────────────────
def cube_identity(spec):
    a = float(spec.get("a", 2))
    b = float(spec.get("b", 1))
    value = (a + b) ** 3

    W, H = 452, 262
    cv = Canvas(W, H, seed=_seed(spec, 2804))
    cv.text(W / 2, 20, "the cube expansion has four terms",
            size=10.5, weight=700, color=C["soft"])

    terms = [("a^3", a ** 3, C["blue"], C["blue_bg"]),
             ("3a^2b", 3 * a * a * b, C["green"], C["green_bg"]),
             ("3ab^2", 3 * a * b * b, C["amber"], C["amber_bg"]),
             ("b^3", b ** 3, C["red"], C["red_bg"])]
    for i, (lab, val, col, bg) in enumerate(terms):
        x = 34 + (i % 2) * 204
        y = 48 + (i // 2) * 52
        _card(cv, x, y, 184, 38, col, bg, sw=1.5)
        cv.text(x + 66, y + 24, lab, size=10.2, weight=700, color=col)
        cv.text(x + 170, y + 24, _fmt(val), size=8.7, anchor="end", color=col)

    _card(cv, 48, 164, 356, 38, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 188, "(a+b)^3 = a^3 + 3a^2b + 3ab^2 + b^3",
            size=9.5, weight=700, color=C["purple"])
    cv.text(W / 2, 226, f"for a={_fmt(a)}, b={_fmt(b)}: value = {_fmt(value)}",
            size=9.2, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "coefficients 1, 3, 3, 1 follow the symmetric pattern",
            size=8.6, color=C["soft"])
    return cv.svg()


# ───────────────────────────── three-variable identity ──────────────────────
def three_variable(spec):
    a = float(spec.get("a", 1))
    b = float(spec.get("b", 2))
    c = float(spec.get("c", -3))
    left = a ** 3 + b ** 3 + c ** 3 - 3 * a * b * c
    right = (a + b + c) * (a * a + b * b + c * c - a * b - b * c - c * a)

    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 2805))
    cv.text(W / 2, 20, "the symmetric three-variable identity has a useful condition",
            size=9.7, weight=700, color=C["soft"])

    vals = [("a", a, C["blue"], C["blue_bg"]),
            ("b", b, C["green"], C["green_bg"]),
            ("c", c, C["red"], C["red_bg"])]
    for i, (lab, val, col, bg) in enumerate(vals):
        x = 44 + i * 134
        _card(cv, x, 48, 112, 44, col, bg, sw=1.5)
        cv.text(x + 56, 67, lab, size=12, weight=700, color=col)
        cv.text(x + 56, 84, f"= {_fmt(val)}", size=9, color=col)

    _card(cv, 38, 112, 376, 42, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 130, "a^3+b^3+c^3-3abc", size=11, weight=700, color=C["purple"])
    cv.text(226, 146, "= (a+b+c)(a^2+b^2+c^2-ab-bc-ca)", size=8.7, color=C["purple"])
    _card(cv, 62, 178, 328, 34, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 200, f"a+b+c = {_fmt(a+b+c)}; both sides = {_fmt(left)}",
            size=9.2, weight=700, color=C["amber"])
    cv.text(W / 2, 236, "if a+b+c = 0, then a^3+b^3+c^3 = 3abc",
            size=8.9, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "use the condition before expanding everything",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── nearby-base square ───────────────────────────
def mental_square(spec):
    n = int(spec.get("n", 103))
    base = int(spec.get("base", 100))
    d = n - base
    value = n * n
    sign = "+" if d >= 0 else "-"
    absd = abs(d)

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2806))
    cv.text(W / 2, 20, "choose a nearby base and apply (a+b)^2",
            size=10.3, weight=700, color=C["soft"])

    _card(cv, 54, 46, 344, 36, C["blue"], C["blue_bg"], sw=1.7)
    cv.text(226, 69, f"{n} = {base} {sign} {absd}", size=13, weight=700, color=C["blue"])
    _card(cv, 46, 104, 360, 34, C["green"], C["green_bg"], sw=1.6)
    cv.text(226, 126, f"{n}^2 = ({base} {sign} {absd})^2",
            size=10.5, weight=700, color=C["green"])
    _card(cv, 42, 158, 368, 34, C["amber"], C["amber_bg"], sw=1.6)
    expanded = f"= {base**2} { '+' if d >= 0 else '-' } {2*base*absd} + {absd**2}"
    cv.text(226, 180, expanded, size=10.2, weight=700, color=C["amber"])
    _card(cv, 92, 210, 268, 24, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 227, f"= {value}", size=11, weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "square-sum": square_sum,
    "square-difference": square_difference,
    "difference-squares": difference_squares,
    "cube-identity": cube_identity,
    "three-variable": three_variable,
    "mental-square": mental_square,
}
