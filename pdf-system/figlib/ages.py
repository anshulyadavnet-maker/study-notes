"""
ages.py — figures for Chapter 20 (Problems on Ages).

age-timeline    : past, present and future on one line, ages marked at each
age-gap         : the difference between two ages never changes
age-ratio-k     : ratio ages written as 4k and 5k, then the future condition
age-table       : the three-column past / present / future working table
age-equation    : one person, one condition, solved as a small equation
age-family      : a family average shifting when everyone grows n years
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


# ─────────────────────────── one line, three moments ────────────────────────
def age_timeline(spec):
    now = float(spec.get("age", 30))
    back = int(spec.get("back", 5))
    fwd = int(spec.get("forward", 5))

    W, H = 452, 210
    cv = Canvas(W, H, seed=_seed(spec, 2001))
    cv.text(W / 2, 20, "one line, three moments", size=10.6, weight=700,
            color=C["soft"])

    y = 104
    xs = [86, W / 2, W - 86]
    cv.line(40, y, W - 40, y, color=C["ink"], w=1.7)
    cv.arrow(W - 60, y, W - 34, y, color=C["ink"], w=1.4)

    marks = [(f"{back} years ago", now - back, C["blue"], C["blue_bg"]),
             ("today", now, C["green"], C["green_bg"]),
             (f"{fwd} years later", now + fwd, C["amber"], C["amber_bg"])]

    for x, (lab, val, col, bg) in zip(xs, marks):
        cv.line(x, y - 10, x, y + 10, color=col, w=1.8)
        _card(cv, x - 52, y - 52, 104, 34, col, bg, sw=1.6)
        cv.text(x, y - 30, f"age {_fmt(val)}", size=11, weight=700,
                color=col)
        cv.text(x, y + 28, lab, size=8.8, weight=700, color=C["soft"])

    cv.raw(f'<path d="M{xs[0]} {y+44} L{xs[0]} {y+52} L{xs[1]} {y+52} '
           f'L{xs[1]} {y+44}" fill="none" stroke="{C["grey"]}" '
           f'stroke-width="1.2"/>')
    cv.text((xs[0] + xs[1]) / 2, y + 66, f"+{back}", size=9, weight=700,
            color=C["grey"])
    cv.raw(f'<path d="M{xs[1]} {y+44} L{xs[1]} {y+52} L{xs[2]} {y+52} '
           f'L{xs[2]} {y+44}" fill="none" stroke="{C["grey"]}" '
           f'stroke-width="1.2"/>')
    cv.text((xs[1] + xs[2]) / 2, y + 66, f"+{fwd}", size=9, weight=700,
            color=C["grey"])

    cv.text(W / 2, H - 8, "past = x - t   |   future = x + t",
            size=9.6, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── the gap never changes ──────────────────────────
def age_gap(spec):
    a = float(spec.get("older", 40))
    b = float(spec.get("younger", 10))
    step = int(spec.get("step", 10))
    n = 3

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2002))
    cv.text(W / 2, 20, "both grow together, so the gap stays fixed",
            size=10.6, weight=700, color=C["soft"])

    top = a + (n - 1) * step
    unit = 210 / top
    x0 = 104
    for i in range(n):
        y = 44 + i * 54
        av, bv = a + i * step, b + i * step

        # younger on top
        _card(cv, x0, y, bv * unit, 22, C["green"], C["green_bg"], r=3,
              sw=1.3)
        cv.text(x0 + bv * unit / 2, y + 16, _fmt(bv), size=9, weight=700,
                color=C["green"])

        # older below: the matching part, then the gap part
        _card(cv, x0, y + 24, bv * unit, 22, C["blue"], C["blue_bg"], r=3,
              sw=1.3)
        cv.text(x0 + bv * unit / 2, y + 40, _fmt(bv), size=8.6, weight=700,
                color=C["blue"])
        _card(cv, x0 + bv * unit, y + 24, (av - bv) * unit, 22, C["red"],
              C["red_bg"], r=3, sw=1.5)
        cv.text(x0 + bv * unit + (av - bv) * unit / 2, y + 40,
                _fmt(av - bv), size=8.6, weight=700, color=C["red"])

        cv.text(x0 - 10, y + 18, _fmt(bv), size=8.6, anchor="end",
                weight=700, color=C["green"])
        cv.text(x0 - 10, y + 40, _fmt(av), size=8.6, anchor="end",
                weight=700, color=C["blue"])

        lab = "now" if i == 0 else f"after {i*step} yr"
        cv.text(x0 - 44, y + 30, lab, size=8.4, anchor="end", weight=700,
                color=C["ink"])
        cv.text(x0 + av * unit + 12, y + 30,
                f"ratio {_fmt(Fraction(int(av), int(bv)))}", size=8.4,
                anchor="start", weight=700, color=C["soft"])

    _card(cv, 40, 212, 372, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(226, 232, f"the gap is always {_fmt(a-b)}, but the ratio keeps "
            f"changing", size=9.6, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── ratio ages as 4k and 5k ────────────────────────
def age_ratio_k(spec):
    r1 = int(spec.get("r1", 4))
    r2 = int(spec.get("r2", 5))
    t = int(spec.get("after", 9))
    s1 = int(spec.get("s1", 5))
    s2 = int(spec.get("s2", 6))

    den = r1 * s2 - r2 * s1
    k = t * (s1 - s2) / den if den else 0
    a, b = r1 * k, r2 * k

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2003))
    cv.text(W / 2, 20, f"ratio {r1} : {r2} means the ages are {r1}k and "
            f"{r2}k", size=10.4, weight=700, color=C["soft"])

    unit = 240 / (r2 * k + t)
    x0 = 92

    rows = [(r1 * k, 0, f"{r1}k", C["blue"], C["blue_bg"]),
            (r2 * k, 0, f"{r2}k", C["green"], C["green_bg"]),
            (r1 * k, t, f"{r1}k + {t}", C["blue"], C["blue_bg"]),
            (r2 * k, t, f"{r2}k + {t}", C["green"], C["green_bg"])]
    for i, (base, extra, lab, col, bg) in enumerate(rows):
        y = 44 + i * 34 + (8 if i >= 2 else 0)
        _card(cv, x0, y, base * unit, 26, col, bg, r=3, sw=1.4)
        cv.text(x0 + base * unit / 2, y + 18, _fmt(base), size=9.4,
                weight=700, color=col)
        if extra:
            _card(cv, x0 + base * unit, y, extra * unit, 26, C["amber"],
                  C["amber_bg"], r=3, sw=1.4)
            cv.text(x0 + base * unit + extra * unit / 2, y + 18,
                    f"+{extra}", size=8.4, weight=700, color=C["amber"])
        cv.text(x0 - 10, y + 18, lab, size=8.6, anchor="end", weight=700,
                color=C["ink"])

    cv.text(x0 + 250, 78, "now", size=8.8, anchor="start", weight=700,
            color=C["soft"])
    cv.text(x0 + 250, 158, f"after {t} yr", size=8.8, anchor="start",
            weight=700, color=C["soft"])

    _card(cv, 40, 190, 372, 30, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 210, f"({r1}k + {t}) / ({r2}k + {t}) = {s1}/{s2}   ->   "
            f"k = {_fmt(k)}", size=10, weight=700, color=C["purple"])
    cv.text(W / 2, 234, f"so the ages are {_fmt(a)} and {_fmt(b)}",
            size=10, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── the working table ──────────────────────────────
def age_table(spec):
    back = int(spec.get("back", 5))
    fwd = int(spec.get("forward", 10))

    W, H = 452, 210
    cv = Canvas(W, H, seed=_seed(spec, 2004))
    cv.text(W / 2, 20, "make this table first, then read the condition",
            size=10.4, weight=700, color=C["soft"])

    cols = [(f"{back} years ago", C["blue"], C["blue_bg"]),
            ("now", C["green"], C["green_bg"]),
            (f"{fwd} years later", C["amber"], C["amber_bg"])]
    rows = [("first person", "x", f"x - {back}", "x", f"x + {fwd}"),
            ("second person", "y", f"y - {back}", "y", f"y + {fwd}")]

    cw = 116
    x0 = 96
    for j, (lab, col, bg) in enumerate(cols):
        x = x0 + j * cw
        cv.text(x + cw / 2, 46, lab, size=8.8, weight=700, color=col)

    for i, (who, _, past, now, fut) in enumerate(rows):
        y = 56 + i * 48
        cv.text(x0 - 10, y + 26, who, size=8.6, anchor="end", weight=700,
                color=C["ink"])
        for j, (val, (lab, col, bg)) in enumerate(zip((past, now, fut),
                                                      cols)):
            x = x0 + j * cw
            _card(cv, x + 4, y, cw - 8, 38, col, bg, r=5, sw=1.4)
            cv.text(x + cw / 2, y + 24, val, size=12, weight=700, color=col)

    _card(cv, 46, 158, 360, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(226, 178, "every condition becomes one equation from this table",
            size=9.6, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── one person, one condition ──────────────────────
def age_equation(spec):
    t = int(spec.get("t", 6))
    m = int(spec.get("times", 2))
    ans = m * t + t
    ans = (m * t + t) / (m - 1) if m != 1 else 0

    W, H = 400, 216
    cv = Canvas(W, H, seed=_seed(spec, 2005))
    cv.text(W / 2, 20, f"age {t} years later is {m} times age {t} "
            f"years ago", size=10.2, weight=700, color=C["soft"])

    lines = [(f"x + {t} = {m} (x - {t})", "write it down", C["blue"],
              C["blue_bg"]),
             (f"x + {t} = {m}x - {m*t}", "open the bracket", C["green"],
              C["green_bg"]),
             (f"{m*t + t} = {'' if m-1 == 1 else m-1}x",
              "collect the terms", C["amber"], C["amber_bg"]),
             (f"x = {_fmt(ans)}", "that is the age", C["red"], C["red_bg"])]

    for i, (eq, note, col, bg) in enumerate(lines):
        y = 42 + i * 38
        last = (i == len(lines) - 1)
        _card(cv, 40, y, 196, 30, col, bg, sw=1.8 if last else 1.3)
        cv.text(138, y + 20, eq, size=11.5, weight=700, color=col)
        cv.text(248, y + 20, note, size=8.4, anchor="start", color=C["soft"])
        if not last:
            cv.arrow(138, y + 32, 138, y + 38, color=C["grey"], w=1.1)

    cv.text(W / 2, H - 12, "one unknown, one condition, one line each",
            size=9, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── family average shifting ────────────────────────
def age_family(spec):
    n = int(spec.get("members", 5))
    avg = float(spec.get("avg", 20))
    back = int(spec.get("back", 5))

    tot_now = n * avg
    tot_back = tot_now - n * back

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2006))
    cv.text(W / 2, 20, f"{back} years ago EVERY member was {back} years "
            f"younger", size=10.4, weight=700, color=C["soft"])

    box = 34
    gap = 12
    x0 = (W - (n * box + (n - 1) * gap)) / 2
    for i in range(n):
        x = x0 + i * (box + gap)
        _card(cv, x, 44, box, box, C["blue"], C["blue_bg"], r=4, sw=1.4)
        cv.text(x + box / 2, 66, "-" + str(back), size=9, weight=700,
                color=C["blue"])
    cv.text(W / 2, 96, f"{n} members x {back} years = {_fmt(n*back)} years "
            f"less in total", size=9.4, weight=700, color=C["red"])

    rows = [("total age now", f"{n} x {_fmt(avg)} = {_fmt(tot_now)}",
             C["green"]),
            (f"drop for {back} years", f"{n} x {back} = {_fmt(n*back)}",
             C["red"]),
            (f"total {back} years ago", _fmt(tot_back), C["blue"]),
            (f"average {back} years ago", _fmt(tot_back / n), C["purple"])]
    for i, (lab, val, col) in enumerate(rows):
        y = 112 + i * 26
        _card(cv, 46, y, 360, 22, col, "#ffffff", r=5, sw=1.1)
        cv.text(58, y + 15, lab, size=8.6, anchor="start", color=C["soft"])
        cv.text(394, y + 15, val, size=9.2, anchor="end", weight=700,
                color=col)

    cv.text(W / 2, H - 12, "if the family size changed, count only who was "
            "there", size=8.8, weight=700, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "age-timeline": age_timeline,
    "age-gap": age_gap,
    "age-ratio-k": age_ratio_k,
    "age-table": age_table,
    "age-equation": age_equation,
    "age-family": age_family,
}
