"""
compound.py — figures for Chapter 17 (Compound Interest).

ci-stack        : each year's interest sits on top and itself earns next year
si-vs-ci        : the straight line and the curve drawn on one grid
ci-multiplier   : principal walked through the (1 + R/100) multipliers
ci-si-gap       : the extra piece that makes CI - SI, shown as one small block
compounding-freq: yearly vs half-yearly vs quarterly on the same principal
ci-doubling     : doubling twice gives four times, not double the time
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


# ─────────────────────────── interest on interest ───────────────────────────
def ci_stack(spec):
    p = float(spec.get("p", 10000))
    r = float(spec.get("r", 10))
    t = int(spec.get("t", 3))

    vals = [p]
    for _ in range(t):
        vals.append(vals[-1] * (1 + r / 100))
    ints = [vals[i + 1] - vals[i] for i in range(t)]

    W, H = 452, 272
    cv = Canvas(W, H, seed=_seed(spec, 1701))
    cv.text(W / 2, 20, "each year's interest joins the principal",
            size=10.6, weight=700, color=C["soft"])

    base = 200
    bw = 118
    x0 = 62
    ph = 58
    sh = 20

    _card(cv, x0, base - ph, bw, ph, C["blue"], C["blue_bg"], r=4, sw=1.7)
    cv.text(x0 + bw / 2, base - ph / 2 + 4, f"P = {_fmt(p)}", size=10.6,
            weight=700, color=C["blue"])

    cols = [C["green"], C["amber"], C["red"], C["purple"]]
    bgs = [C["green_bg"], C["amber_bg"], C["red_bg"], C["purple_bg"]]
    for i in range(t):
        y = base - ph - (i + 1) * sh
        col, bg = cols[i % 4], bgs[i % 4]
        _card(cv, x0, y, bw, sh, col, bg, r=3, sw=1.4)
        cv.text(x0 + bw / 2, y + 14, _fmt(round(ints[i], 2)), size=9,
                weight=700, color=col)
        cv.text(x0 + bw + 8, y + 14, f"year {i+1}", size=8,
                anchor="start", color=C["soft"])
    cv.line(x0 - 8, base, x0 + bw + 8, base, color=C["ink"], w=1.5)
    ytop = base - ph - t * sh
    cv.arrow(x0 - 16, base - ph - 4, x0 - 16, ytop + 4, color=C["red"],
             w=1.4)
    cv.text(x0 - 22, (base - ph + ytop) / 2, "each", size=7.4, anchor="end",
            weight=700, color=C["red"])
    cv.text(x0 - 22, (base - ph + ytop) / 2 + 10, "bigger", size=7.4,
            anchor="end", weight=700, color=C["red"])

    rows = [(f"year {i+1} interest", _fmt(round(ints[i], 2)),
             cols[i % 4]) for i in range(t)]
    for i, (lab, val, col) in enumerate(rows):
        y = 76 + i * 26
        _card(cv, 238, y, 190, 22, col, "#ffffff", r=4, sw=1.1)
        cv.text(248, y + 15, lab, size=8.4, anchor="start", color=C["soft"])
        cv.text(420, y + 15, val, size=9, anchor="end", weight=700, color=col)

    cv.text(W / 2, H - 30, f"amount = {_fmt(round(vals[-1],2))}",
            size=10.6, weight=700, color=C["ink"])
    cv.text(W / 2, H - 12, "the slabs keep growing, that is compounding",
            size=8.8, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── line versus curve ──────────────────────────────
def si_vs_ci(spec):
    p = float(spec.get("p", 10000))
    r = float(spec.get("r", 10))
    t = int(spec.get("t", 6))

    si = [p * (1 + r * i / 100) for i in range(t + 1)]
    ci = [p * (1 + r / 100) ** i for i in range(t + 1)]
    lo = p
    hi = ci[-1] + (ci[-1] - p) * 0.12

    W, H = 452, 264
    cv = Canvas(W, H, seed=_seed(spec, 1702))
    cv.text(W / 2, 20, "same rate, but one bends upward",
            size=10.6, weight=700, color=C["soft"])

    ox, oy = 74, 186
    pw, ph = 288, 134

    cv.line(ox, oy, ox + pw + 6, oy, color=C["ink"], w=1.5)
    cv.line(ox, oy, ox, oy - ph - 6, color=C["ink"], w=1.5)

    def px(i):
        return ox + i * pw / t

    def py(v):
        return oy - (v - lo) / (hi - lo) * ph

    # axis break, since the scale starts at P not zero
    cv.text(ox - 8, oy + 4, _fmt(p), size=8, anchor="end", color=C["soft"])
    for k in (0, 5):
        cv.line(ox - 5, oy - 8 + k, ox + 5, oy - 13 + k, color=C["ink"],
                w=1.0)

    for series, col, lab in ((si, C["blue"], "simple"),
                             (ci, C["green"], "compound")):
        pts = [(px(i), py(series[i])) for i in range(t + 1)]
        for a, b in zip(pts, pts[1:]):
            cv.line(*a, *b, color=col, w=2.0)
        for x, y in pts:
            cv.dot(x, y, r=3.0, color=col)

    cv.text(px(t) + 8, py(ci[t]) + 4, "compound", size=8.6, anchor="start",
            weight=700, color=C["green"])
    cv.text(px(t) + 8, py(si[t]) + 8, "simple", size=8.6, anchor="start",
            weight=700, color=C["blue"])

    for i in range(t + 1):
        cv.text(px(i), oy + 15, str(i), size=8.2, color=C["soft"])
    cv.text(ox + pw / 2, oy + 30, "years", size=8.8, color=C["soft"])

    # the widening gap, marked one step in from the right
    gi = t - 1
    cv.line(px(gi), py(si[gi]), px(gi), py(ci[gi]), color=C["red"], w=1.8)
    cv.line(px(gi) - 5, py(si[gi]), px(gi) + 5, py(si[gi]), color=C["red"],
            w=1.2)
    cv.line(px(gi) - 5, py(ci[gi]), px(gi) + 5, py(ci[gi]), color=C["red"],
            w=1.2)
    cv.text(px(gi) - 10, py(ci[gi]) - 6,
            f"gap {_fmt(round(ci[gi]-si[gi]))}", size=8.2, anchor="end",
            weight=700, color=C["red"])

    _card(cv, 40, 220, 372, 30, C["red"], C["red_bg"], sw=1.5)
    cv.text(226, 240, "the gap starts at zero and widens every year",
            size=9.6, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── the multiplier walk ────────────────────────────
def ci_multiplier(spec):
    p = float(spec.get("p", 10000))
    r = float(spec.get("r", 10))
    t = int(spec.get("t", 3))
    k = 1 + r / 100

    W, H = 452, 216
    cv = Canvas(W, H, seed=_seed(spec, 1703))
    cv.text(W / 2, 20, f"multiply by {_fmt(k)} once for every year",
            size=10.6, weight=700, color=C["soft"])

    n = t + 1
    bw = 78
    gap = (W - 60 - n * bw) / (n - 1)
    x0 = 30
    for i in range(n):
        x = x0 + i * (bw + gap)
        v = p * k ** i
        first = (i == 0)
        last = (i == n - 1)
        col = C["blue"] if first else (C["green"] if last else C["amber"])
        bg = C["blue_bg"] if first else (C["green_bg"] if last
                                         else C["amber_bg"])
        _card(cv, x, 48, bw, 50, col, bg, sw=1.8 if last else 1.4)
        cv.text(x + bw / 2, 78, _fmt(round(v, 2)), size=11, weight=700,
                color=col)
        cv.text(x + bw / 2, 110, "start" if first else f"year {i}",
                size=8.2, color=C["soft"])
        if i < n - 1:
            ax, bx = x + bw + 3, x + bw + gap - 3
            cv.arrow(ax, 73, bx, 73, color=C["grey"], w=1.3)
            cv.text((ax + bx) / 2, 64, f"x{_fmt(k)}", size=7.8, weight=700,
                    color=C["red"])

    _card(cv, 46, 130, 360, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 151, f"A = P (1 + R/100)^n = {_fmt(p)} x "
            f"{_fmt(k)}^{t} = {_fmt(round(p*k**t,2))}", size=10.2,
            weight=700, color=C["purple"])
    cv.text(W / 2, 180, f"CI = A - P = {_fmt(round(p*k**t - p,2))}",
            size=10, weight=700, color=C["ink"])
    cv.text(W / 2, H - 10, "never add the rate, always multiply",
            size=8.8, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── where CI - SI comes from ───────────────────────
def ci_si_gap(spec):
    p = float(spec.get("p", 5000))
    r = float(spec.get("r", 10))
    one = p * r / 100
    extra = one * r / 100

    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 1704))
    cv.text(W / 2, 20, "the extra bit is interest earned on interest",
            size=10.6, weight=700, color=C["soft"])

    unit = 250 / (p + 2 * one)
    x0 = 96

    # SI row
    _card(cv, x0, 44, p * unit, 30, C["blue"], C["blue_bg"], r=4, sw=1.4)
    cv.text(x0 + p * unit / 2, 64, f"P {_fmt(p)}", size=10, weight=700,
            color=C["blue"])
    for j in range(2):
        _card(cv, x0 + p * unit + j * one * unit, 44, one * unit, 30,
              C["green"], C["green_bg"], r=3, sw=1.3)
        cv.text(x0 + p * unit + (j + 0.5) * one * unit, 64, _fmt(one),
                size=8.6, weight=700, color=C["green"])
    cv.text(x0 - 10, 64, "simple", size=9, anchor="end", weight=700,
            color=C["ink"])

    # CI row
    y2 = 88
    _card(cv, x0, y2, p * unit, 30, C["blue"], C["blue_bg"], r=4, sw=1.4)
    cv.text(x0 + p * unit / 2, y2 + 20, f"P {_fmt(p)}", size=10, weight=700,
            color=C["blue"])
    for j in range(2):
        _card(cv, x0 + p * unit + j * one * unit, y2, one * unit, 30,
              C["green"], C["green_bg"], r=3, sw=1.3)
        cv.text(x0 + p * unit + (j + 0.5) * one * unit, y2 + 20, _fmt(one),
                size=8.6, weight=700, color=C["green"])
    ex = x0 + p * unit + 2 * one * unit
    _card(cv, ex, y2, max(extra * unit, 16), 30, C["red"], C["red_bg"], r=3,
          sw=1.8)
    cv.text(ex + max(extra * unit, 16) / 2, y2 + 20, _fmt(extra), size=8.4,
            weight=700, color=C["red"])
    cv.text(x0 - 10, y2 + 20, "compound", size=9, anchor="end", weight=700,
            color=C["ink"])

    cv.arrow(ex + 8, y2 - 8, ex + 8, y2 - 2, color=C["red"], w=1.3)
    cv.text(ex + 14, y2 - 12, f"{_fmt(r)}% of {_fmt(one)}", size=8,
            anchor="start", weight=700, color=C["red"])

    _card(cv, 40, 142, 372, 32, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 163, f"CI - SI (2 years) = P (R/100)\u00b2 = {_fmt(p)} x "
            f"({_fmt(r)}/100)\u00b2 = {_fmt(extra)}", size=10,
            weight=700, color=C["purple"])

    cv.text(W / 2, 194, "for 3 years the gap becomes "
            "P x R\u00b2 (300 + R) / 10\u2076", size=9.6, weight=700,
            color=C["ink"])
    cv.text(W / 2, H - 10, "first year they are equal, the gap opens later",
            size=8.6, color=C["soft"])
    return cv.svg()


# ─────────────────────────── compounding frequency ──────────────────────────
def compounding_freq(spec):
    p = float(spec.get("p", 10000))
    r = float(spec.get("r", 20))

    rows = [("yearly", 1, r), ("half-yearly", 2, r / 2),
            ("quarterly", 4, r / 4)]
    data = []
    for name, n, rr in rows:
        a = p * (1 + rr / 100) ** n
        data.append((name, n, rr, a))
    top = max(d[3] for d in data)

    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 1705))
    cv.text(W / 2, 20, f"{_fmt(p)} for one year at {_fmt(r)}% per annum",
            size=10.6, weight=700, color=C["soft"])

    unit = 240 / top
    x0 = 118
    cols = [C["blue"], C["amber"], C["green"]]
    bgs = [C["blue_bg"], C["amber_bg"], C["green_bg"]]
    for i, (name, n, rr, a) in enumerate(data):
        y = 46 + i * 46
        col, bg = cols[i], bgs[i]
        _card(cv, x0, y, a * unit, 32, col, bg, r=4, sw=1.5)
        cv.text(x0 + a * unit / 2, y + 21, _fmt(round(a, 2)), size=11,
                weight=700, color=col)
        cv.text(x0 - 10, y + 15, name, size=9, anchor="end", weight=700,
                color=C["ink"])
        cv.text(x0 - 10, y + 27, f"{_fmt(rr)}% x {n}", size=7.8,
                anchor="end", color=C["soft"])

    _card(cv, 30, 188, 392, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(226, 208, "more frequent compounding means more money",
            size=9.6, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "half-yearly: R/2 and 2n   |   quarterly: R/4 "
            "and 4n", size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── doubling under CI ──────────────────────────────
def ci_doubling(spec):
    t = int(spec.get("t", 5))

    W, H = 452, 218
    cv = Canvas(W, H, seed=_seed(spec, 1706))
    cv.text(W / 2, 20, f"if money doubles in {t} years",
            size=10.6, weight=700, color=C["soft"])

    stages = [(1, 0, "P", C["blue"], C["blue_bg"]),
              (2, t, "2P", C["green"], C["green_bg"]),
              (4, 2 * t, "4P", C["amber"], C["amber_bg"]),
              (8, 3 * t, "8P", C["red"], C["red_bg"])]

    bw, gap = 76, 30
    x0 = (W - (4 * bw + 3 * gap)) / 2
    for i, (mult, yrs, lab, col, bg) in enumerate(stages):
        x = x0 + i * (bw + gap)
        _card(cv, x, 48, bw, 48, col, bg, sw=1.7)
        cv.text(x + bw / 2, 78, lab, size=15, weight=700, color=col)
        cv.text(x + bw / 2, 110, f"{yrs} yr", size=9, weight=700,
                color=C["soft"])
        if i < 3:
            ax, bx = x + bw + 3, x + bw + gap - 3
            cv.arrow(ax, 72, bx, 72, color=C["grey"], w=1.4)
            cv.text((ax + bx) / 2, 62, "x2", size=8, weight=700,
                    color=C["red"])

    _card(cv, 40, 132, 372, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 152, f"to become 2^k times, the time is k x {t} years",
            size=10, weight=700, color=C["purple"])
    cv.text(W / 2, 182, "under simple interest 4 times would need "
            f"{3*t} years, not {2*t}", size=9.2, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "ci-stack": ci_stack,
    "si-vs-ci": si_vs_ci,
    "ci-multiplier": ci_multiplier,
    "ci-si-gap": ci_si_gap,
    "compounding-freq": compounding_freq,
    "ci-doubling": ci_doubling,
}
