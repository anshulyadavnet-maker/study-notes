"""
percent.py — figures for Chapter 11 (Percentage).

percent-grid      : a 10x10 grid with x squares shaded, so "per hundred" is literal
percent-forms     : the same value shown as percent, fraction, decimal, ratio
fraction-percent  : the must-learn fraction/percent conversion card wall
successive-change : two changes applied one after the other, base shifting
percent-reversal  : why "20% more" reverses to "16 2/3 % less"
price-consumption : price bar and consumption bar keeping the spend rectangle fixed
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
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ─────────────────────────── 100-square grid ────────────────────────────────
def percent_grid(spec):
    pct = int(spec.get("value", 25))
    W, H = 300, 322
    cv = Canvas(W, H, seed=_seed(spec, 1101))

    cell = 20
    gx = (W - 10 * cell) / 2
    gy = 46

    cv.text(W / 2, 22, f"{pct} out of every 100", size=11, weight=700,
            color=C["soft"])

    for r in range(10):
        for c in range(10):
            i = r * 10 + c
            on = i < pct
            x, y = gx + c * cell, gy + r * cell
            cv.raw(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" '
                   f'fill="{C["blue"] if on else C["paper"]}" '
                   f'stroke="{C["blue"] if on else C["grey"]}" '
                   f'stroke-width="{1.2 if on else 0.7}" '
                   f'fill-opacity="{0.82 if on else 1}"/>')

    gb = gy + 10 * cell
    cv.text(W / 2, gb + 18, "the same amount written three ways",
            size=8.6, color=C["soft"])
    _card(cv, 22, gb + 28, 116, 30, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(80, gb + 48, f"{pct}%", size=13, weight=700, color=C["blue"])

    f = Fraction(pct, 100)
    _card(cv, 148, gb + 28, 60, 30, C["green"], C["green_bg"], sw=1.5)
    cv.text(178, gb + 48, f"{f.numerator}/{f.denominator}", size=12,
            weight=700, color=C["green"])

    _card(cv, 216, gb + 28, 62, 30, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(247, gb + 48, _fmt(pct / 100), size=12, weight=700,
            color=C["amber"])
    return cv.svg()


# ─────────────────────────── four equivalent forms ──────────────────────────
def percent_forms(spec):
    pct = spec.get("value", 40)
    try:
        p = float(pct)
    except Exception:
        p = 40.0
    f = Fraction(int(round(p * 100)), 10000).limit_denominator(1000)

    W, H = 440, 168
    cv = Canvas(W, H, seed=_seed(spec, 1102))
    cv.text(W / 2, 20, "one quantity, four costumes", size=10.5, weight=700,
            color=C["soft"])

    items = [("percent", f"{_fmt(p)}%", C["blue"], C["blue_bg"]),
             ("fraction", f"{f.numerator}/{f.denominator}", C["green"], C["green_bg"]),
             ("decimal", _fmt(p / 100), C["amber"], C["amber_bg"]),
             ("ratio", f"{f.numerator} : {f.denominator}", C["purple"], C["purple_bg"])]

    bw, gap = 92, 20
    x0 = (W - (4 * bw + 3 * gap)) / 2
    for i, (lab, val, col, bg) in enumerate(items):
        x = x0 + i * (bw + gap)
        _card(cv, x, 40, bw, 56, col, bg, sw=1.7)
        cv.text(x + bw / 2, 72, val, size=14, weight=700, color=col)
        cv.text(x + bw / 2, 110, lab, size=9, weight=700, color=C["soft"])
        if i < 3:
            cv.text(x + bw + gap / 2, 72, "=", size=15, weight=700,
                    color=C["ink"])

    _card(cv, (W - 300) / 2, 126, 300, 28, C["red"], C["red_bg"], sw=1.5)
    cv.text(W / 2, 145, "remove the % sign, divide by 100", size=10.5,
            weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── conversion wall ────────────────────────────────
def fraction_percent(spec):
    rows = [
        ("1/2", "50%", C["blue"]), ("1/3", "33 1/3%", C["blue"]),
        ("1/4", "25%", C["green"]), ("1/5", "20%", C["green"]),
        ("1/6", "16 2/3%", C["amber"]), ("1/7", "14 2/7%", C["amber"]),
        ("1/8", "12 1/2%", C["red"]), ("1/9", "11 1/9%", C["red"]),
        ("1/10", "10%", C["purple"]), ("1/12", "8 1/3%", C["purple"]),
        ("1/16", "6 1/4%", C["teal"]), ("1/20", "5%", C["teal"]),
    ]
    cols, cw, ch, gx, gy = 4, 106, 44, 12, 10
    n = (len(rows) + cols - 1) // cols
    W = 18 + cols * cw + (cols - 1) * gx + 18
    H = 34 + n * (ch + gy) + 6
    cv = Canvas(W, H, seed=_seed(spec, 1103))
    cv.text(W / 2, 18, "learn these by heart, they save whole minutes",
            size=10, weight=700, color=C["soft"])

    for i, (fr, pc, col) in enumerate(rows):
        r, c = divmod(i, cols)
        x = 18 + c * (cw + gx)
        y = 28 + r * (ch + gy)
        _card(cv, x, y, cw, ch, col, "#ffffff", sw=1.4)
        cv.text(x + 25, y + 28, fr, size=13.5, weight=700, color=col)
        cv.text(x + 45, y + 27, "=", size=10, color=C["grey"])
        cv.text(x + cw - 27, y + 27, pc, size=10, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── successive change ──────────────────────────────
def successive_change(spec):
    a = float(spec.get("a", 20))
    b = float(spec.get("b", -20))
    base = float(spec.get("base", 100))

    v1 = base * (1 + a / 100)
    v2 = v1 * (1 + b / 100)
    net = v2 - base

    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 1104))
    cv.text(W / 2, 20, "the base moves after the first change", size=10.5,
            weight=700, color=C["soft"])

    stages = [(base, "start", C["ink"], "#f2f3f7"),
              (v1, f"{'+' if a>=0 else ''}{_fmt(a)}%",
               C["green"] if a >= 0 else C["red"],
               C["green_bg"] if a >= 0 else C["red_bg"]),
              (v2, f"{'+' if b>=0 else ''}{_fmt(b)}%",
               C["green"] if b >= 0 else C["red"],
               C["green_bg"] if b >= 0 else C["red_bg"])]

    bw, gap = 108, 40
    x0 = (W - (3 * bw + 2 * gap)) / 2
    for i, (val, lab, col, bg) in enumerate(stages):
        x = x0 + i * (bw + gap)
        _card(cv, x, 44, bw, 50, col, bg, sw=1.7)
        cv.text(x + bw / 2, 76, _fmt(val), size=18, weight=700, color=col)
        cv.text(x + bw / 2, 108, lab, size=9.4, weight=700, color=C["soft"])
        if i < 2:
            cv.arrow(x + bw + 5, 69, x + bw + gap - 5, 69, color=C["grey"],
                     w=1.4)

    # base annotations
    cv.text(x0 + bw / 2, 128, f"base = {_fmt(base)}", size=8.4,
            color=C["blue"])
    cv.text(x0 + bw + gap + bw / 2, 128, f"base = {_fmt(v1)}", size=8.4,
            weight=700, color=C["red"])
    cv.text(x0 + bw + gap + bw / 2, 140, "changed", size=8, weight=700,
            color=C["red"])

    _card(cv, 40, 156, 372, 32, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 177, f"net % = a + b + ab/100 = {_fmt(a)} "
            f"{'+' if b>=0 else '-'} {_fmt(abs(b))} "
            f"{'+' if a*b>=0 else '-'} {_fmt(abs(a*b)/100)} "
            f"= {_fmt(net/base*100)}", size=10, weight=700, color=C["amber"])

    col = C["green"] if net >= 0 else C["red"]
    _card(cv, (W - 250) / 2, 196, 250, 30, col,
          C["green_bg"] if net >= 0 else C["red_bg"], sw=1.7)
    cv.text(W / 2, 216, f"net change = {_fmt(net/base*100)}%"
            f"  ({'gain' if net >= 0 else 'loss'})", size=11.5, weight=700,
            color=col)
    return cv.svg()


# ─────────────────────────── the reversal asymmetry ─────────────────────────
def percent_reversal(spec):
    x = float(spec.get("value", 25))
    A = 100 + x
    back = x / A * 100

    W, H = 452, 214
    cv = Canvas(W, H, seed=_seed(spec, 1105))
    cv.text(W / 2, 20, "more and less are not mirror images", size=10.5,
            weight=700, color=C["soft"])

    unit = 260 / max(A, 100)
    x0 = 118
    yb, ya = 46, 96

    _card(cv, x0, ya, 100 * unit, 34, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(x0 + 100 * unit / 2, ya + 23, "B = 100", size=11, weight=700,
            color=C["blue"])
    cv.text(x0 - 10, ya + 23, "B", size=11, anchor="end", weight=700,
            color=C["ink"])

    _card(cv, x0, yb, 100 * unit, 34, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(x0 + 100 * unit / 2, yb + 23, "100", size=11, weight=700,
            color=C["blue"])
    _card(cv, x0 + 100 * unit, yb, x * unit, 34, C["green"], C["green_bg"],
          sw=1.5)
    cv.text(x0 + 100 * unit + x * unit / 2, yb + 23, f"+{_fmt(x)}", size=10,
            weight=700, color=C["green"])
    cv.text(x0 - 10, yb + 23, "A", size=11, anchor="end", weight=700,
            color=C["ink"])

    _card(cv, 26, 144, 194, 32, C["green"], C["green_bg"], sw=1.5)
    cv.text(123, 165, f"A is {_fmt(x)}% more than B", size=9.8, weight=700,
            color=C["green"])
    cv.text(123, 186, f"base is B = 100", size=8.4, color=C["soft"])

    _card(cv, 232, 144, 194, 32, C["red"], C["red_bg"], sw=1.5)
    frac = Fraction(int(round(x * 1000)), int(round(A * 1000)))
    cv.text(329, 165, f"B is {_fmt(back)}% less than A", size=9.8, weight=700,
            color=C["red"])
    cv.text(329, 186, f"base is A = {_fmt(A)}, so {frac.numerator}/"
            f"{frac.denominator} x 100", size=8.4, color=C["soft"])
    return cv.svg()


# ─────────────────────────── price vs consumption ───────────────────────────
def price_consumption(spec):
    x = float(spec.get("rise", 25))
    newp = 100 + x
    cut = x / newp * 100
    newc = 100 - cut

    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 1106))
    cv.text(W / 2, 20, "spend = price x quantity, keep the area fixed",
            size=10.4, weight=700, color=C["soft"])

    # two rectangles of equal area
    sc = 118 / 100
    hsc = 96 / newp

    x1, y1 = 56, 40
    w1, h1 = 100 * sc, 100 * hsc
    cv.raw(f'<rect x="{x1}" y="{y1 + (newp*hsc - h1)}" width="{w1}" '
           f'height="{h1}" rx="4" fill="{C["blue_bg"]}" '
           f'stroke="{C["blue"]}" stroke-width="1.6"/>')
    cv.text(x1 + w1 / 2, y1 + newp * hsc - h1 / 2 + 4, "spend", size=11,
            weight=700, color=C["blue"])
    cv.text(x1 + w1 / 2, y1 + newp * hsc + 18, "quantity 100", size=8.6,
            color=C["soft"])
    cv.text(x1 - 8, y1 + newp * hsc - h1 / 2, "price", size=8.6, anchor="end",
            color=C["soft"])
    cv.text(x1 - 8, y1 + newp * hsc - h1 / 2 + 12, "100", size=9,
            anchor="end", weight=700, color=C["blue"])

    x2 = 268
    w2, h2 = newc * sc, newp * hsc
    cv.raw(f'<rect x="{x2}" y="{y1}" width="{w2}" height="{h2}" rx="4" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.6"/>')
    cv.text(x2 + w2 / 2, y1 + h2 / 2 + 4, "spend", size=11, weight=700,
            color=C["amber"])
    cv.text(x2 + w2 / 2, y1 + h2 + 18, f"quantity {_fmt(newc)}", size=8.6,
            weight=700, color=C["red"])
    cv.text(x2 + w2 + 8, y1 + h2 / 2, "price", size=8.6, anchor="start",
            color=C["soft"])
    cv.text(x2 + w2 + 8, y1 + h2 / 2 + 12, _fmt(newp), size=9,
            anchor="start", weight=700, color=C["amber"])

    cv.arrow(x1 + w1 + 14, y1 + h2 / 2 + 10, x2 - 16, y1 + h2 / 2 + 10,
             color=C["grey"], w=1.4)
    cv.text((x1 + w1 + x2) / 2, y1 + h2 / 2 - 2,
            f"price +{_fmt(x)}%", size=8.8, weight=700, color=C["green"])

    _card(cv, 40, 188, 372, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(226, 208, f"so quantity must fall by {_fmt(x)}/{_fmt(newp)} "
            f"x 100 = {_fmt(cut)}%", size=10.4, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "both rectangles have exactly the same area",
            size=8.4, color=C["soft"])
    return cv.svg()


REGISTRY = {
    "percent-grid": percent_grid,
    "percent-forms": percent_forms,
    "fraction-percent": fraction_percent,
    "successive-change": successive_change,
    "percent-reversal": percent_reversal,
    "price-consumption": price_consumption,
}
