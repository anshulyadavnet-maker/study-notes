"""
interest.py — figures for Chapter 16 (Simple Interest).

si-blocks       : equal interest slabs stacked on the principal year by year
si-wheel        : the P, R, T, SI relation as a cover-one-to-find-it wheel
si-growth       : amount growing in a straight line, year on the x axis
si-doubling     : why doubling needs RT = 100, tripling RT = 200
two-amounts     : two known amounts, the gap gives one year's interest
split-principal : one sum split into two parts at different rates
"""
import math
from fractions import Fraction
from .sketch import Canvas, C


def _seed(spec, d=7):
    s = spec.get("seed", d)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


def _card(cv, x, y, w, h, col, bg, r=6, sw=1.4):
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
           f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>')


def _fmt(v):
    if isinstance(v, Fraction):
        return str(v.numerator) if v.denominator == 1 else \
            f"{v.numerator}/{v.denominator}"
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ─────────────────────────── equal slabs each year ──────────────────────────
def si_blocks(spec):
    p = float(spec.get("p", 5000))
    r = float(spec.get("r", 8))
    t = int(spec.get("t", 3))
    per = p * r / 100

    W, H = 452, 266
    cv = Canvas(W, H, seed=_seed(spec, 1601))
    cv.text(W / 2, 20, "every year adds exactly the same slab",
            size=10.6, weight=700, color=C["soft"])

    base = 196
    bw = 120
    x0 = 76
    ph = 62                       # principal drawn at a fixed height
    sh = 22                       # each interest slab

    _card(cv, x0, base - ph, bw, ph, C["blue"], C["blue_bg"], r=4, sw=1.7)
    cv.text(x0 + bw / 2, base - ph / 2 + 4, f"P = {_fmt(p)}", size=11,
            weight=700, color=C["blue"])
    for i in range(t):
        y = base - ph - (i + 1) * sh
        _card(cv, x0, y, bw, sh, C["green"], C["green_bg"], r=3, sw=1.4)
        cv.text(x0 + bw / 2, y + 15, _fmt(per), size=9.6, weight=700,
                color=C["green"])
        cv.text(x0 + bw + 10, y + 15, f"year {i+1}", size=8.4,
                anchor="start", color=C["soft"])

    cv.line(x0 - 8, base, x0 + bw + 8, base, color=C["ink"], w=1.5)

    rows = [(f"one year = {_fmt(p)} x {_fmt(r)} / 100", _fmt(per),
             C["green"], C["green_bg"]),
            (f"SI for {t} years = {_fmt(per)} x {t}", _fmt(t * per),
             C["amber"], C["amber_bg"]),
            ("amount = P + SI", _fmt(p + t * per), C["purple"],
             C["purple_bg"])]
    for i, (lab, val, col, bg) in enumerate(rows):
        y = 96 + i * 34
        _card(cv, 238, y, 190, 28, col, bg, r=5, sw=1.3)
        cv.text(248, y + 18, lab, size=8.2, anchor="start", color=C["soft"])
        cv.text(420, y + 18, val, size=9.6, anchor="end", weight=700,
                color=col)

    cv.text(W / 2, H - 28, f"amount after {t} years = {_fmt(p + t*per)}",
            size=10.4, weight=700, color=C["ink"])
    cv.text(W / 2, H - 10,
            "the slabs never grow, that is what makes it simple",
            size=8.8, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── the cover-one wheel ────────────────────────────
def si_wheel(spec):
    W, H = 400, 268
    cv = Canvas(W, H, seed=_seed(spec, 1602))
    cv.text(W / 2, 20, "cover the one you want, read off the rest",
            size=10.6, weight=700, color=C["soft"])

    cx, cy = W / 2, 108
    R = 60
    cv.circle(cx, cy, R, color=C["ink"], fill=C["paper"], w=1.7)
    cv.text(cx, cy - 16, "SI x 100", size=11.5, weight=700, color=C["red"])
    cv.line(cx - 44, cy - 4, cx + 44, cy - 4, color=C["ink"], w=1.6)
    cv.text(cx, cy + 18, "P  x  R  x  T", size=11.5, weight=700,
            color=C["blue"])

    outs = [("SI = PRT/100", C["red"], C["red_bg"]),
            ("P = SI x 100 / RT", C["blue"], C["blue_bg"]),
            ("R = SI x 100 / PT", C["green"], C["green_bg"]),
            ("T = SI x 100 / PR", C["amber"], C["amber_bg"])]
    for i, (txt, col, bg) in enumerate(outs):
        c, rr = divmod(i, 2)
        x = 26 + c * 190
        y = 202 + rr * 30
        _card(cv, x, y, 172, 26, col, bg, r=5, sw=1.3)
        cv.text(x + 86, y + 17, txt, size=9.4, weight=700, color=col)

    _card(cv, cx - 60, cy + R + 6, 120, 24, C["purple"],
          C["purple_bg"], r=5, sw=1.3)
    cv.text(cx, cy + R + 22, "A = P + SI", size=10.2, weight=700,
            color=C["purple"])
    return cv.svg()


# ─────────────────────────── straight-line growth ───────────────────────────
def si_growth(spec):
    p = float(spec.get("p", 4000))
    r = float(spec.get("r", 10))
    t = int(spec.get("t", 5))
    per = p * r / 100

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 1603))
    cv.text(W / 2, 20, "simple interest grows in a straight line",
            size=10.6, weight=700, color=C["soft"])

    ox, oy = 62, 168
    pw, ph = 316, 112
    top = (p + t * per) * 1.12

    cv.line(ox, oy, ox + pw, oy, color=C["ink"], w=1.5)
    cv.line(ox, oy, ox, oy - ph, color=C["ink"], w=1.5)

    def px(i):
        return ox + i * pw / t

    def py(v):
        return oy - v / top * ph

    # the principal baseline
    cv.line(ox, py(p), ox + pw, py(p), color=C["blue"], w=1.4, dash="4 3")
    cv.text(ox - 6, py(p) + 4, "P", size=9.4, anchor="end", weight=700,
            color=C["blue"])

    pts = [(px(i), py(p + i * per)) for i in range(t + 1)]
    for a, b in zip(pts, pts[1:]):
        cv.line(*a, *b, color=C["green"], w=2.0)
    for i, (x, y) in enumerate(pts):
        cv.dot(x, y, r=3.6, color=C["green"])
        cv.text(x, oy + 16, str(i), size=8.4, color=C["soft"])
        if i in (0, t):
            cv.text(x, y - 9, _fmt(p + i * per), size=8.6, weight=700,
                    color=C["green"])

    # one step highlighted
    cv.line(px(2), py(p + 2 * per), px(3), py(p + 2 * per), color=C["red"],
            w=1.2, dash="3 3")
    cv.line(px(3), py(p + 2 * per), px(3), py(p + 3 * per), color=C["red"],
            w=1.4)
    cv.text(px(3) + 6, (py(p + 2 * per) + py(p + 3 * per)) / 2 + 4,
            f"+{_fmt(per)}", size=8.4, anchor="start", weight=700,
            color=C["red"])

    cv.text(ox + pw + 16, oy + 16, "years", size=8.8,
            anchor="start", color=C["soft"])

    _card(cv, 40, 202, 182, 30, C["green"], C["green_bg"], sw=1.5)
    cv.text(131, 222, f"same step every year: {_fmt(per)}", size=9.2,
            weight=700, color=C["green"])
    _card(cv, 232, 202, 182, 30, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(323, 222, f"A = {_fmt(p)} + {_fmt(per)} x T", size=9.2,
            weight=700, color=C["blue"])
    return cv.svg()


# ─────────────────────────── doubling and tripling ──────────────────────────
def si_doubling(spec):
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 1604))
    cv.text(W / 2, 20, "how much interest must pile up?",
            size=10.6, weight=700, color=C["soft"])

    rows = [("becomes 2 times", 1, "R x T = 100", C["green"], C["green_bg"]),
            ("becomes 3 times", 2, "R x T = 200", C["amber"], C["amber_bg"]),
            ("becomes 4 times", 3, "R x T = 300", C["red"], C["red_bg"])]

    unit = 58
    x0 = 112
    for i, (lab, k, rule, col, bg) in enumerate(rows):
        y = 42 + i * 52
        _card(cv, x0, y, unit, 30, C["blue"], C["blue_bg"], r=4, sw=1.4)
        cv.text(x0 + unit / 2, y + 20, "P", size=11, weight=700,
                color=C["blue"])
        for j in range(k):
            _card(cv, x0 + (j + 1) * unit, y, unit, 30, col, bg, r=4, sw=1.3)
            cv.text(x0 + (j + 1) * unit + unit / 2, y + 20, "SI", size=10,
                    weight=700, color=col)
        cv.text(x0 - 10, y + 20, lab, size=8.8, anchor="end", weight=700,
                color=C["ink"])
        cv.text(x0 + (k + 1) * unit + 12, y + 20, rule, size=9.4,
                anchor="start", weight=700, color=col)

    _card(cv, 40, 200, 372, 28, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 219, "to become n times, the interest must equal "
            "(n - 1) x P", size=9.6, weight=700, color=C["purple"])
    return cv.svg()


# ─────────────────────────── two amounts, one gap ───────────────────────────
def two_amounts(spec):
    a1 = float(spec.get("a1", 4800))
    t1 = int(spec.get("t1", 2))
    a2 = float(spec.get("a2", 5600))
    t2 = int(spec.get("t2", 4))
    per = (a2 - a1) / (t2 - t1)
    p = a1 - t1 * per
    r = per * 100 / p

    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 1605))
    cv.text(W / 2, 20, "the gap between two amounts is pure interest",
            size=10.4, weight=700, color=C["soft"])

    unit = 268 / a2
    x0 = 96
    rows = [(p, 0, "principal", C["blue"], C["blue_bg"]),
            (a1, t1, f"after {t1} years", C["green"], C["green_bg"]),
            (a2, t2, f"after {t2} years", C["amber"], C["amber_bg"])]
    for i, (v, tt, lab, col, bg) in enumerate(rows):
        y = 42 + i * 40
        _card(cv, x0, y, v * unit, 30, col, bg, r=4, sw=1.5)
        cv.text(x0 + v * unit / 2, y + 20, _fmt(v), size=11, weight=700,
                color=col)
        cv.text(x0 - 10, y + 20, lab, size=8.6, anchor="end", weight=700,
                color=C["ink"])

    # the gap
    ya, yb = 82, 122
    cv.raw(f'<rect x="{x0+a1*unit}" y="{yb}" width="{(a2-a1)*unit}" '
           f'height="30" rx="3" fill="none" stroke="{C["red"]}" '
           f'stroke-width="1.5" stroke-dasharray="3 3"/>')
    cv.text(x0 + a1 * unit + (a2 - a1) * unit / 2 + 4, yb + 20,
            f"{_fmt(a2-a1)}", size=9, weight=700, color=C["red"])

    rows2 = [(f"{t2 - t1} years of interest", _fmt(a2 - a1), C["red"]),
             ("so one year gives", _fmt(per), C["green"]),
             (f"principal = {_fmt(a1)} - {t1} x {_fmt(per)}", _fmt(p),
              C["blue"]),
             ("rate", f"{_fmt(round(r,2))}%", C["purple"])]
    for i, (lab, val, col) in enumerate(rows2):
        y = 164 + i * 18
        cv.text(56, y, lab, size=8.6, anchor="start", color=C["soft"])
        cv.text(W - 46, y, val, size=9.2, anchor="end", weight=700, color=col)
    return cv.svg()


# ─────────────────────────── one sum, two rates ─────────────────────────────
def split_principal(spec):
    tot = float(spec.get("total", 2500))
    r1 = float(spec.get("r1", 6))
    r2 = float(spec.get("r2", 8))
    t = float(spec.get("t", 2))
    target = float(spec.get("si", 350))
    # x at r1, tot-x at r2
    x = (target * 100 / t - tot * r2) / (r1 - r2)
    y = tot - x

    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 1606))
    cv.text(W / 2, 20, "one sum, two rates, one total interest",
            size=10.6, weight=700, color=C["soft"])

    unit = 320 / tot
    x0 = 66
    _card(cv, x0, 42, tot * unit, 30, C["ink"], "#f2f3f7", r=4, sw=1.5)
    cv.text(x0 + tot * unit / 2, 62, f"total {_fmt(tot)}", size=10.4,
            weight=700, color=C["ink"])

    _card(cv, x0, 88, x * unit, 34, C["blue"], C["blue_bg"], r=4, sw=1.6)
    cv.text(x0 + x * unit / 2, 104, _fmt(x), size=11, weight=700,
            color=C["blue"])
    cv.text(x0 + x * unit / 2, 117, f"at {_fmt(r1)}%", size=8.4,
            color=C["soft"])

    _card(cv, x0 + x * unit, 88, y * unit, 34, C["green"], C["green_bg"],
          r=4, sw=1.6)
    cv.text(x0 + x * unit + y * unit / 2, 104, _fmt(y), size=11, weight=700,
            color=C["green"])
    cv.text(x0 + x * unit + y * unit / 2, 117, f"at {_fmt(r2)}%", size=8.4,
            color=C["soft"])

    i1 = x * r1 * t / 100
    i2 = y * r2 * t / 100
    _card(cv, 40, 140, 178, 30, C["blue"], C["blue_bg"], sw=1.4)
    cv.text(129, 160, f"interest {_fmt(i1)}", size=9.6, weight=700,
            color=C["blue"])
    _card(cv, 234, 140, 178, 30, C["green"], C["green_bg"], sw=1.4)
    cv.text(323, 160, f"interest {_fmt(i2)}", size=9.6, weight=700,
            color=C["green"])

    _card(cv, 60, 178, 332, 30, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 198, f"{_fmt(i1)} + {_fmt(i2)} = {_fmt(target)} in "
            f"{_fmt(t)} years", size=10.2, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "call one part x, the other becomes total - x",
            size=8.8, weight=700, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "si-blocks": si_blocks,
    "si-wheel": si_wheel,
    "si-growth": si_growth,
    "si-doubling": si_doubling,
    "two-amounts": two_amounts,
    "split-principal": split_principal,
}
