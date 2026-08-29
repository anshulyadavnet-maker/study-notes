"""
algebra.py — figures for Chapter 27 (Algebra Foundations & Polynomials).

algebra-parts     : terms, coefficients, powers and constant in an expression
like-terms        : combine coefficients of like terms
expression-tree   : an operation tree for a compound expression
polynomial-degree : polynomial terms arranged by descending degree
substitution      : evaluate a polynomial after substituting a value
 equation-balance : solve a simple linear equation by balanced operations
"""
from .sketch import Canvas, C


def _seed(spec, default=2700):
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


def _term(value, variable="x", power=1):
    value = float(value)
    if power == 0:
        return _fmt(value)
    if power == 1:
        if value == 1:
            return variable
        if value == -1:
            return "-" + variable
        return f"{_fmt(value)}{variable}"
    if value == 1:
        return f"{variable}^{power}"
    if value == -1:
        return f"-{variable}^{power}"
    return f"{_fmt(value)}{variable}^{power}"


# ───────────────────────────── parts of an expression ───────────────────────
def algebra_parts(spec):
    a = float(spec.get("a", 3))
    b = float(spec.get("b", -5))
    c = float(spec.get("c", 7))
    expression = f"{_term(a, 'x', 2)} {'+' if b >= 0 else '-'} {_term(abs(b), 'x', 1)} + {_fmt(c)}"

    W, H = 452, 264
    cv = Canvas(W, H, seed=_seed(spec, 2701))
    cv.text(W / 2, 20, "every algebraic expression is built from terms",
            size=10.3, weight=700, color=C["soft"])

    cards = [
        ("term 1", _term(a, "x", 2), "coefficient 3, power 2", C["blue"], C["blue_bg"]),
        ("term 2", _term(b, "x", 1), "coefficient -5, power 1", C["red"], C["red_bg"]),
        ("term 3", _fmt(c), "constant, power 0", C["green"], C["green_bg"]),
    ]
    for i, (lab, val, note, col, bg) in enumerate(cards):
        x = 30 + i * 142
        _card(cv, x, 48, 128, 70, col, bg, sw=1.6)
        cv.text(x + 64, 68, lab, size=8.8, weight=700, color=col)
        cv.text(x + 64, 94, val, size=14, weight=700, color=col)
        cv.text(x + 64, 133, note, size=7.8, color=C["soft"])

    _card(cv, 42, 164, 368, 38, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 188, expression, size=13, weight=700, color=C["purple"])
    cv.text(W / 2, 226, "coefficient x variable power; a number alone is a constant",
            size=8.8, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "terms are separated by + or - signs",
            size=8.7, color=C["soft"])
    return cv.svg()


# ───────────────────────────── combine like terms ───────────────────────────
def like_terms(spec):
    a = float(spec.get("a", 3))
    b = float(spec.get("b", 5))
    c = float(spec.get("c", -2))
    total = a + b + c

    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 2702))
    cv.text(W / 2, 20, "like terms have the same variable and the same power",
            size=9.9, weight=700, color=C["soft"])

    vals = [(a, C["blue"], C["blue_bg"]), (b, C["green"], C["green_bg"]),
            (c, C["red"], C["red_bg"])]
    x0 = 44
    for i, (value, col, bg) in enumerate(vals):
        x = x0 + i * 126
        _card(cv, x, 52, 100, 48, col, bg, sw=1.6)
        sign = "+" if value >= 0 and i else ("" if i == 0 else "-")
        cv.text(x + 50, 82, f"{sign}{_fmt(abs(value))}x", size=14,
                weight=700, color=col)
        if i < 2:
            cv.text(x + 112, 80, "+", size=13, weight=700, color=C["ink"])

    _card(cv, 78, 136, 296, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 158, f"({ _fmt(a) } + { _fmt(b) } - 2)x = {_fmt(total)}x",
            size=10.2, weight=700, color=C["purple"])
    cv.text(W / 2, 196, "add coefficients; keep the common x unchanged",
            size=9.1, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "unlike terms cannot be combined directly",
            size=8.8, color=C["red"])
    return cv.svg()


# ───────────────────────────── operation tree ───────────────────────────────
def expression_tree(spec):
    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2703))
    cv.text(W / 2, 20, "an expression can be evaluated from the inside out",
            size=10.1, weight=700, color=C["soft"])

    # Expression: 2x + 3(x - 1)
    _card(cv, 150, 40, 152, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 62, "2x + 3(x - 1)", size=12, weight=700, color=C["purple"])
    cv.line(196, 74, 128, 104, color=C["grey"], w=1.2)
    cv.line(256, 74, 324, 104, color=C["grey"], w=1.2)

    _card(cv, 56, 104, 144, 32, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(128, 125, "2x", size=11, weight=700, color=C["blue"])
    _card(cv, 252, 104, 144, 32, C["green"], C["green_bg"], sw=1.5)
    cv.text(324, 125, "3(x - 1)", size=11, weight=700, color=C["green"])
    cv.line(324, 136, 286, 166, color=C["grey"], w=1.1)
    cv.line(324, 136, 362, 166, color=C["grey"], w=1.1)
    _card(cv, 226, 166, 116, 30, C["amber"], C["amber_bg"], sw=1.4)
    cv.text(284, 186, "x - 1", size=10.5, weight=700, color=C["amber"])
    _card(cv, 352, 166, 58, 30, C["red"], C["red_bg"], sw=1.4)
    cv.text(381, 186, "3x", size=10.5, weight=700, color=C["red"])
    cv.text(W / 2, 220, "respect brackets before combining outside terms",
            size=8.9, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "inside-out evaluation prevents sign errors",
            size=8.6, color=C["soft"])
    return cv.svg()


# ───────────────────────────── polynomial degree ────────────────────────────
def polynomial_degree(spec):
    degree = int(spec.get("degree", 4))
    terms = [(degree, C["blue"], C["blue_bg"]),
             (max(degree - 1, 1), C["green"], C["green_bg"]),
             (0, C["amber"], C["amber_bg"])]

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2704))
    cv.text(W / 2, 20, "the degree is the highest power of the variable",
            size=10.2, weight=700, color=C["soft"])

    x0, y0, bw = 38, 54, 376
    for i, (power, col, bg) in enumerate(terms):
        y = y0 + i * 44
        _card(cv, x0, y, bw, 30, col, bg, r=5, sw=1.4)
        if power == 0:
            text = "constant term"
        else:
            text = f"term with x^{power}"
        cv.text(54, y + 20, text, size=9.2, anchor="start", weight=700, color=col)
        cv.text(396, y + 20, f"power {power}", size=9.2, anchor="end", color=col)

    _card(cv, 76, 198, 300, 28, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 217, f"highest power = {degree}  ->  degree {degree} polynomial",
            size=9.5, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── substitution ─────────────────────────────────
def substitution(spec):
    a = float(spec.get("a", 2))
    b = float(spec.get("b", -3))
    c = float(spec.get("c", 1))
    x = float(spec.get("x", 2))
    value = a * x * x + b * x + c

    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 2705))
    cv.text(W / 2, 20, "substitution: replace x everywhere, then calculate",
            size=10.2, weight=700, color=C["soft"])

    lines = [
        (f"P(x) = {_fmt(a)}x^2 - {_fmt(abs(b))}x + {_fmt(c)}", "given", C["blue"], C["blue_bg"]),
        (f"P({_fmt(x)}) = {_fmt(a)}({_fmt(x)})^2 - {_fmt(abs(b))}({_fmt(x)}) + {_fmt(c)}", "replace x", C["green"], C["green_bg"]),
        (f"= {_fmt(a*x*x)} - {_fmt(abs(b)*x)} + {_fmt(c)}", "powers first", C["amber"], C["amber_bg"]),
        (f"= {_fmt(value)}", "answer", C["purple"], C["purple_bg"]),
    ]
    for i, (text, note, col, bg) in enumerate(lines):
        y = 44 + i * 38
        _card(cv, 38, y, 316, 28, col, bg, r=5, sw=1.4)
        cv.text(48, y + 19, text, size=9.4, anchor="start", weight=700, color=col)
        cv.text(400, y + 19, note, size=8.4, anchor="end", color=C["soft"])
    cv.text(W / 2, H - 9, "same x-value must be used in every term",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── balance a simple equation ────────────────────
def equation_balance(spec):
    a = int(spec.get("a", 2))
    b = int(spec.get("b", 5))
    answer = int(spec.get("answer", 6))
    rhs = a * answer + b

    W, H = 420, 252
    cv = Canvas(W, H, seed=_seed(spec, 2706))
    cv.text(W / 2, 20, "do the same operation on both sides",
            size=10.4, weight=700, color=C["soft"])

    lines = [
        (f"{a}x + {b} = {rhs}", "given", C["blue"], C["blue_bg"]),
        (f"{a}x = {rhs} - {b}", f"subtract {b}", C["green"], C["green_bg"]),
        (f"{a}x = {a*answer}", "simplify", C["amber"], C["amber_bg"]),
        (f"x = {answer}", f"divide by {a}", C["purple"], C["purple_bg"]),
    ]
    for i, (text, note, col, bg) in enumerate(lines):
        y = 44 + i * 38
        _card(cv, 34, y, 206, 28, col, bg, r=5, sw=1.5)
        cv.text(137, y + 19, text, size=11.3, weight=700, color=col)
        cv.text(258, y + 19, note, size=8.6, anchor="start", color=C["soft"])
        if i < len(lines) - 1:
            cv.arrow(137, y + 30, 137, y + 36, color=C["grey"], w=1.1)
    _card(cv, 58, 210, 304, 26, C["red"], C["red_bg"], sw=1.5)
    cv.text(210, 228, "balance is preserved at every step", size=9.1,
            weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "algebra-parts": algebra_parts,
    "like-terms": like_terms,
    "expression-tree": expression_tree,
    "polynomial-degree": polynomial_degree,
    "substitution": substitution,
    "equation-balance": equation_balance,
}
