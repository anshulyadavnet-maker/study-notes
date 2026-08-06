"""
surds.py — figures for Chapter 6 (Indices & Surds).

power-anatomy    : base / exponent / value anatomy of a^n
index-laws       : the seven index laws as a labelled card grid
surd-line        : sqrt2, sqrt3, sqrt5 located on a number line
surd-spiral      : the geometric construction of sqrt2, sqrt3, sqrt4 ...
rationalise-flow : conjugate multiplication turning a surd denominator rational
surd-order       : comparing surds by raising to a common index
"""
import math
from .sketch import Canvas, C

_SUP = {"0": "\u2070", "1": "\u00b9", "2": "\u00b2", "3": "\u00b3", "4": "\u2074",
        "5": "\u2075", "6": "\u2076", "7": "\u2077", "8": "\u2078", "9": "\u2079",
        "-": "\u207b", "/": "\u141f"}


def _seed(spec, d=7):
    s = spec.get("seed", d)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


def _sup(v):
    return "".join(_SUP.get(c, c) for c in str(v))


def _card(cv, x, y, w, h, col, bg, r=7, sw=1.5):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
           f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


# ─────────────────────────── anatomy of a power ─────────────────────────────
def power_anatomy(spec):
    base = str(spec.get("base", 2))
    exp = str(spec.get("exp", 5))
    try:
        val = int(base) ** int(exp)
    except Exception:
        val = spec.get("value", "")

    W, H = 360, 196
    cv = Canvas(W, H, seed=_seed(spec, 601))

    cx = 150
    cv.text(cx, 78, base, size=54, weight=700, color=C["blue"])
    cv.text(cx + 42, 48, exp, size=28, weight=700, color=C["red"])

    # base callout
    cv.line(cx - 16, 92, cx - 60, 128, color=C["blue"], w=1.3)
    _card(cv, 18, 130, 108, 30, C["blue"], C["blue_bg"])
    cv.text(72, 143, "BASE", size=9.4, weight=700, color=C["blue"])
    cv.text(72, 154, "what repeats", size=7.4, color=C["soft"])

    # exponent callout
    cv.line(cx + 52, 40, cx + 104, 28, color=C["red"], w=1.3)
    _card(cv, 208, 14, 134, 30, C["red"], C["red_bg"])
    cv.text(275, 27, "EXPONENT / INDEX", size=8.6, weight=700, color=C["red"])
    cv.text(275, 38, "how many times", size=7.4, color=C["soft"])

    # expansion
    times = " x ".join([base] * min(int(exp) if exp.isdigit() else 3, 6))
    cv.line(cx + 60, 72, 208, 72, color=C["grey"], w=1.2)
    _card(cv, 196, 58, 150, 30, C["green"], C["green_bg"])
    cv.text(271, 78, times, size=10.5, weight=700, color=C["green"])

    # value
    _card(cv, 150, 168, 200, 24, C["amber"], C["amber_bg"], sw=1.4)
    cv.text(250, 185, f"value = {val}", size=11, weight=700, color=C["amber"])

    cv.text(72, 176, "read: " + base + " to the power " + exp, size=8.2,
            color=C["soft"], anchor="middle")
    return cv.svg()


# ─────────────────────────── the seven index laws ───────────────────────────
def index_laws(spec):
    laws = [
        ("a\u1d50 x a\u207f = a\u1d50\u207a\u207f", "2\u00b3 x 2\u2074 = 2\u2077", C["blue"], C["blue_bg"]),
        ("a\u1d50 / a\u207f = a\u1d50\u207b\u207f", "2\u2075 / 2\u00b2 = 2\u00b3", C["blue"], C["blue_bg"]),
        ("(a\u1d50)\u207f = a\u1d50\u207f", "(2\u00b3)\u00b2 = 2\u2076", C["green"], C["green_bg"]),
        ("(ab)\u207f = a\u207f b\u207f", "(2x3)\u00b2 = 4x9", C["green"], C["green_bg"]),
        ("(a/b)\u207f = a\u207f/b\u207f", "(2/3)\u00b2 = 4/9", C["green"], C["green_bg"]),
        ("a\u2070 = 1", "7\u2070 = 1  (a =/= 0)", C["amber"], C["amber_bg"]),
        ("a\u207b\u207f = 1/a\u207f", "2\u207b\u00b3 = 1/8", C["red"], C["red_bg"]),
        ("a^(m/n) = n-th root of a\u1d50", "16^(3/4) = 8", C["purple"], C["purple_bg"]),
    ]
    cols, cw, ch, gx, gy = 2, 218, 46, 14, 10
    rows = (len(laws) + cols - 1) // cols
    W = 20 + cols * cw + (cols - 1) * gx + 20
    H = 34 + rows * (ch + gy)
    cv = Canvas(W, H, seed=_seed(spec, 602))
    cv.text(W / 2, 18, "the eight index laws", size=10.5, color=C["soft"])

    for i, (rule, ex, col, bg) in enumerate(laws):
        r, c = divmod(i, cols)
        x = 20 + c * (cw + gx)
        y = 28 + r * (ch + gy)
        _card(cv, x, y, cw, ch, col, bg)
        cv.raw(f'<circle cx="{x+17}" cy="{y+ch/2}" r="11" fill="{col}"/>')
        cv.text(x + 17, y + ch / 2 + 4, str(i + 1), size=11, weight=700,
                color="#ffffff")
        cv.text(x + 34, y + 20, rule, size=10.2, weight=700, color=col,
                anchor="start")
        cv.text(x + 34, y + 35, ex, size=8.6, color=C["soft"], anchor="start")
    return cv.svg()


# ─────────────────────────── surds on a number line ─────────────────────────
def surd_line(spec):
    W, H = 460, 150
    cv = Canvas(W, H, seed=_seed(spec, 603))
    y = 92
    x0, x1 = 40, W - 34
    lo, hi = 0, 4
    step = (x1 - x0) / (hi - lo)

    cv.line(x0 - 8, y, x1 + 8, y, color=C["ink"], w=1.7)
    cv.arrow(x1 - 10, y, x1 + 12, y, color=C["ink"], w=1.5)

    for i in range(hi - lo + 1):
        px = x0 + i * step
        cv.line(px, y - 7, px, y + 7, color=C["ink"], w=1.4)
        cv.text(px, y + 22, str(lo + i), size=10, weight=700, color=C["ink"])

    marks = [(math.sqrt(2), "sqrt2", "1.414", C["blue"], -34),
             (math.sqrt(3), "sqrt3", "1.732", C["green"], -58),
             (math.sqrt(5), "sqrt5", "2.236", C["red"], -34),
             (math.sqrt(7), "sqrt7", "2.646", C["purple"], -58)]
    for v, lab, dec, col, dy in marks:
        px = x0 + v * step
        cv.line(px, y, px, y + dy, color=col, w=1.3, dash="3 3")
        cv.dot(px, y, r=3.6, color=col)
        _card(cv, px - 32, y + dy - 17, 64, 20, col, "#ffffff", r=5, sw=1.3)
        cv.text(px, y + dy - 3, f"{lab} = {dec}", size=8, weight=700, color=col)

    cv.text(W / 2, H - 8, "every surd sits between two consecutive integers",
            size=8.6, color=C["soft"])
    return cv.svg()


# ─────────────────────────── the square-root spiral ─────────────────────────
def surd_spiral(spec):
    """Right triangles stacked so each hypotenuse is sqrt(n)."""
    steps = int(spec.get("steps", 7))
    W, H = 380, 262
    cv = Canvas(W, H, seed=_seed(spec, 604))
    scale = 62.0
    ox, oy = 168, 200          # origin

    pts = [(1.0, 0.0)]
    for k in range(2, steps + 1):
        px, py = pts[-1]
        r = math.hypot(px, py)
        # unit perpendicular
        ux, uy = -py / r, px / r
        pts.append((px + ux, py + uy))

    def S(p):
        return (ox + p[0] * scale, oy - p[1] * scale)

    prev = (0.0, 0.0)
    for k, p in enumerate(pts, start=1):
        cv.line(*S((0, 0)), *S(p), color=C["blue"] if k == 1 else C["grey"],
                w=1.5 if k == 1 else 1.1)
        if k > 1:
            cv.line(*S(prev), *S(p), color=C["green"], w=1.3)
        prev = p

    # labels on the hypotenuses
    for k, p in enumerate(pts, start=1):
        mx, my = S((p[0] * 0.60, p[1] * 0.60))
        cv.text(mx, my, "sqrt" + str(k) if k > 1 else "1",
                size=8.8, weight=700,
                color=C["ink"] if k > 1 else C["blue"])

    cv.dot(*S((0, 0)), r=3.4, color=C["red"])
    cv.text(ox - 12, oy + 16, "O", size=10, weight=700, color=C["red"])
    cv.text(W / 2, 18, "square-root spiral", size=10.5, weight=700,
            color=C["soft"])
    cv.text(W / 2, H - 8, "each green side = 1 unit, so each hypotenuse grows to sqrt(n+1)",
            size=8.2, color=C["soft"])
    return cv.svg()


# ─────────────────────────── rationalising flow ─────────────────────────────
def rationalise_flow(spec):
    a = spec.get("a", "5")
    b = spec.get("b", "3")
    W, H = 460, 210
    cv = Canvas(W, H, seed=_seed(spec, 605))

    cv.text(W / 2, 18, "rationalising a two-term surd denominator",
            size=10.5, color=C["soft"])

    # step 1
    _card(cv, 24, 34, 122, 44, C["red"], C["red_bg"])
    cv.text(85, 50, "start", size=8, color=C["soft"])
    cv.text(85, 68, f"1 / (sqrt{a} - sqrt{b})", size=10.4, weight=700,
            color=C["red"])
    cv.arrow(150, 56, 186, 56, color=C["grey"], w=1.3)

    # step 2 - conjugate
    _card(cv, 190, 30, 150, 52, C["amber"], C["amber_bg"])
    cv.text(265, 48, "multiply top & bottom", size=8.2, color=C["soft"])
    cv.text(265, 68, f"by (sqrt{a} + sqrt{b})", size=10.4, weight=700,
            color=C["amber"])
    cv.text(265, 92, "the CONJUGATE", size=8.4, weight=700, color=C["amber"])
    cv.arrow(344, 56, 380, 56, color=C["grey"], w=1.3)

    # step 3 - identity
    _card(cv, 150, 112, 230, 40, C["blue"], C["blue_bg"])
    cv.text(265, 137, "(x - y)(x + y) = x\u00b2 - y\u00b2", size=12,
            weight=700, color=C["blue"])
    cv.text(384, 74, "why?", size=8.6, color=C["soft"])
    cv.line(390, 66, 330, 112, color=C["grey"], w=1.1, dash="3 3")

    # result
    try:
        d = int(a) - int(b)
    except Exception:
        d = "a - b"
    _card(cv, 60, 164, 340, 36, C["green"], C["green_bg"], sw=1.7)
    cv.text(230, 188, f"= (sqrt{a} + sqrt{b}) / {d}    -  denominator is rational",
            size=10, weight=700, color=C["green"])
    return cv.svg()


# ─────────────────────────── comparing surds ────────────────────────────────
def surd_order(spec):
    """Raise unlike-index surds to a common index and compare."""
    items = spec.get("items", "2:2,3:3,5:4")
    parsed = []
    for chunk in str(items).split(","):
        num, idx = chunk.split(":")
        parsed.append((int(num.strip()), int(idx.strip())))

    L = 1
    for _, idx in parsed:
        L = L * idx // math.gcd(L, idx)

    rows = [(nu, idx, nu ** (L // idx)) for nu, idx in parsed]
    ranked = sorted(rows, key=lambda r: r[2])

    W = 380
    H = 60 + len(rows) * 34 + 34
    cv = Canvas(W, H, seed=_seed(spec, 606))
    cv.text(W / 2, 18, f"common index = LCM of the roots = {L}",
            size=9.6, weight=700, color=C["soft"])

    hx = [22, 130, 250]
    cv.text(hx[0] + 44, 40, "surd", size=8.8, color=C["soft"])
    cv.text(hx[1] + 50, 40, f"raise to power {L}", size=8.8, color=C["soft"])
    cv.text(hx[2] + 50, 40, "compare", size=8.8, color=C["soft"])

    for i, (nu, idx, val) in enumerate(rows):
        y = 48 + i * 34
        _card(cv, hx[0], y, 92, 27, C["blue"], C["blue_bg"], r=6, sw=1.3)
        cv.text(hx[0] + 46, y + 18, f"{idx}-root of {nu}", size=9,
                weight=700, color=C["blue"])
        cv.arrow(hx[0] + 96, y + 13, hx[1] - 4, y + 13, color=C["grey"], w=1.1)
        _card(cv, hx[1], y, 100, 27, C["amber"], C["amber_bg"], r=6, sw=1.3)
        cv.text(hx[1] + 50, y + 18, f"{nu}^{L//idx} = {val}", size=9.4,
                weight=700, color=C["amber"])
        rank = ranked.index((nu, idx, val)) + 1
        _card(cv, hx[2], y, 100, 27, C["green"], C["green_bg"], r=6, sw=1.3)
        cv.text(hx[2] + 50, y + 18, f"rank {rank}", size=9.4, weight=700,
                color=C["green"])

    order = "  <  ".join(f"{idx}-root {nu}" for nu, idx, _ in ranked)
    cv.text(W / 2, H - 10, order, size=8.8, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "power-anatomy": power_anatomy,
    "index-laws": index_laws,
    "surd-line": surd_line,
    "surd-spiral": surd_spiral,
    "rationalise-flow": rationalise_flow,
    "surd-order": surd_order,
}
