"""
factor.py — figures for Chapter 29 (Factorisation).

common-factor     : pull out the numerical/variable common factor
grouping-factor   : group four terms into two common binomials
identity-factor   : reverse difference-of-squares identity
quadratic-split   : split the middle term using ac and b
substitution-factor: set y=x^2 before factoring an even polynomial
zero-product      : solve a factored equation through two branches
"""
from .sketch import Canvas, C


def _seed(spec, default=2900):
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


# ───────────────────────────── common factor ────────────────────────────────
def common_factor(spec):
    factor = int(spec.get("factor", 3))
    a = int(spec.get("a", 2))
    b = int(spec.get("b", 3))
    cv_a, cv_b = factor * a, factor * b

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2901))
    cv.text(W / 2, 20, "factorisation reverses distribution",
            size=10.4, weight=700, color=C["soft"])

    _card(cv, 38, 50, 164, 42, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(120, 75, f"{cv_a}x + {cv_b}", size=14, weight=700, color=C["blue"])
    cv.arrow(210, 71, 242, 71, color=C["grey"], w=1.3)
    _card(cv, 252, 50, 162, 42, C["green"], C["green_bg"], sw=1.6)
    cv.text(333, 75, f"{factor}({a}x + {b})", size=12, weight=700, color=C["green"])

    _card(cv, 50, 126, 352, 36, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 149, f"common factor = {factor}; divide each term by {factor}",
            size=9.8, weight=700, color=C["purple"])
    cv.text(W / 2, 194, f"{factor} x {a}x = {cv_a}x    |    {factor} x {b} = {cv_b}",
            size=9, color=C["ink"])
    cv.text(W / 2, H - 8, "the factor outside multiplies every term inside",
            size=8.8, color=C["soft"])
    return cv.svg()


# ───────────────────────────── grouping ──────────────────────────────────────
def grouping_factor(spec):
    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2902))
    cv.text(W / 2, 20, "group terms so the same binomial appears twice",
            size=9.9, weight=700, color=C["soft"])

    _card(cv, 34, 48, 384, 34, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(226, 70, "ax + ay + bx + by", size=13, weight=700, color=C["blue"])
    cv.line(226, 90, 226, 112, color=C["grey"], w=1.2)
    cv.line(226, 112, 132, 132, color=C["grey"], w=1.2)
    cv.line(226, 112, 320, 132, color=C["grey"], w=1.2)

    _card(cv, 40, 132, 184, 34, C["green"], C["green_bg"], sw=1.5)
    cv.text(132, 154, "a(x+y)", size=11.5, weight=700, color=C["green"])
    _card(cv, 228, 132, 184, 34, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(320, 154, "b(x+y)", size=11.5, weight=700, color=C["amber"])

    _card(cv, 78, 194, 296, 30, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 214, "(a+b)(x+y)", size=12, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "factor each pair, then factor the common bracket",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── difference of squares ────────────────────────
def identity_factor(spec):
    a = int(spec.get("a", 5))
    b = int(spec.get("b", 2))
    value = a * a - b * b

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2903))
    cv.text(W / 2, 20, "recognise a^2 - b^2 and reverse the identity",
            size=10.3, weight=700, color=C["soft"])

    _card(cv, 32, 50, 160, 40, C["blue"], C["blue_bg"], sw=1.7)
    cv.text(112, 75, f"x^2 - {_fmt(value)}", size=12, weight=700, color=C["blue"])
    cv.arrow(200, 70, 250, 70, color=C["grey"], w=1.3)
    _card(cv, 258, 50, 160, 40, C["green"], C["green_bg"], sw=1.7)
    cv.text(338, 75, f"(x-{a})(x+{a})", size=10.7, weight=700, color=C["green"])

    _card(cv, 46, 126, 360, 34, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 148, f"{_fmt(a)}^2 - {_fmt(b)}^2 = ({a}+{b})({a}-{b})",
            size=9.8, weight=700, color=C["purple"])
    _card(cv, 88, 178, 276, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 197, f"= {_fmt(a+b)} x {_fmt(a-b)} = {_fmt(value)}",
            size=9.5, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "difference of squares factors into conjugate brackets",
            size=8.6, color=C["ink"])
    return cv.svg()


# ───────────────────────────── split middle term ────────────────────────────
def quadratic_split(spec):
    a = int(spec.get("a", 2))
    b = int(spec.get("b", 7))
    c = int(spec.get("c", 3))
    ac = a * c
    # default example uses p=1,q=6; allow overrides for diagram clarity
    p = int(spec.get("p", 1))
    q = int(spec.get("q", 6))

    W, H = 452, 276
    cv = Canvas(W, H, seed=_seed(spec, 2904))
    cv.text(W / 2, 20, "split b into p+q, where pq = ac",
            size=10.3, weight=700, color=C["soft"])

    _card(cv, 42, 46, 368, 34, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(226, 68, f"{a}x^2 + {b}x + {c}", size=13, weight=700, color=C["blue"])
    _card(cv, 42, 96, 178, 46, C["green"], C["green_bg"], sw=1.5)
    cv.text(131, 116, f"ac = {a} x {c} = {ac}", size=9.7, weight=700, color=C["green"])
    cv.text(131, 133, f"p x q = {p} x {q} = {ac}", size=8.8, color=C["green"])
    _card(cv, 232, 96, 178, 46, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(321, 116, f"p + q = {p} + {q}", size=9.7, weight=700, color=C["amber"])
    cv.text(321, 133, f"= {b} = middle coefficient", size=8.5, color=C["amber"])

    _card(cv, 44, 168, 364, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 190, f"{a}x^2 + {p}x + {q}x + {c}", size=10.5, weight=700, color=C["purple"])
    _card(cv, 80, 218, 292, 28, C["red"], C["red_bg"], sw=1.5)
    cv.text(226, 237, f"= ({a}x+{p})(x+{c})", size=10, weight=700, color=C["red"])
    return cv.svg()


# ───────────────────────────── substitution factorisation ───────────────────
def substitution_factor(spec):
    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 2905))
    cv.text(W / 2, 20, "replace repeated powers by a temporary variable",
            size=9.9, weight=700, color=C["soft"])

    _card(cv, 42, 48, 368, 34, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(226, 70, "x^4 - 5x^2 + 4", size=13, weight=700, color=C["blue"])
    cv.arrow(226, 90, 226, 108, color=C["grey"], w=1.2)
    _card(cv, 54, 112, 154, 36, C["green"], C["green_bg"], sw=1.5)
    cv.text(131, 135, "let y = x^2", size=11, weight=700, color=C["green"])
    _card(cv, 244, 112, 154, 36, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(321, 135, "y^2 - 5y + 4", size=10.5, weight=700, color=C["amber"])
    _card(cv, 52, 174, 348, 32, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 195, "(y-1)(y-4) -> (x^2-1)(x^2-4)", size=9.3, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "substitute back, then factor each difference of squares",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── zero product ─────────────────────────────────
def zero_product(spec):
    r1 = int(spec.get("r1", 2))
    r2 = int(spec.get("r2", 3))
    W, H = 420, 258
    cv = Canvas(W, H, seed=_seed(spec, 2906))
    cv.text(W / 2, 20, "if a product is zero, at least one factor is zero",
            size=9.9, weight=700, color=C["soft"])

    _card(cv, 60, 48, 300, 34, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(210, 70, f"(x-{r1})(x-{r2}) = 0", size=12, weight=700, color=C["blue"])
    cv.line(210, 84, 130, 112, color=C["grey"], w=1.2)
    cv.line(210, 84, 290, 112, color=C["grey"], w=1.2)
    _card(cv, 48, 112, 164, 38, C["green"], C["green_bg"], sw=1.5)
    cv.text(130, 137, f"x-{r1}=0", size=11, weight=700, color=C["green"])
    _card(cv, 220, 112, 164, 38, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(302, 137, f"x-{r2}=0", size=11, weight=700, color=C["amber"])
    _card(cv, 62, 178, 296, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(210, 200, f"solutions: x={r1} or x={r2}", size=10.5, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "zero product property converts factors into solutions",
            size=8.6, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "common-factor": common_factor,
    "grouping-factor": grouping_factor,
    "identity-factor": identity_factor,
    "quadratic-split": quadratic_split,
    "substitution-factor": substitution_factor,
    "zero-product": zero_product,
}
