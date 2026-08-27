"""
wages.py — figures for Chapter 23 (Work & Wages).

work-wage-bars  : work contributions become proportional wage shares
efficiency-time : compare efficiency x time for two workers
men-hours       : men x days x hours as the work contribution
piecework       : pieces x rate per piece
 group-contribution: three workers' contribution units and wage ratio
wage-check      : split a fixed total wage and verify the sum
"""
from fractions import Fraction

from .sketch import Canvas, C


def _seed(spec, default=2300):
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
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _ratio(values):
    vals = [Fraction(v).limit_denominator(1000) for v in values]
    den = 1
    for v in vals:
        den = den * v.denominator
    nums = [int(v.numerator * (den // v.denominator)) for v in vals]
    import math
    g = 0
    for n in nums:
        g = math.gcd(g, abs(n))
    g = g or 1
    return [n // g for n in nums]


# ───────────────────────────── two work contributions ───────────────────────
def work_wage_bars(spec):
    a_work = float(spec.get("a_work", 12))
    b_work = float(spec.get("b_work", 8))
    total_wage = float(spec.get("total_wage", 1500))
    total = a_work + b_work
    a_wage = total_wage * a_work / total
    b_wage = total_wage * b_work / total

    W, H = 452, 260
    cv = Canvas(W, H, seed=_seed(spec, 2301))
    cv.text(W / 2, 20, "wage follows contribution, not merely clock time",
            size=10.3, weight=700, color=C["soft"])

    rows = [
        ("A work", a_work, a_wage, C["blue"], C["blue_bg"]),
        ("B work", b_work, b_wage, C["green"], C["green_bg"]),
    ]
    max_work = max(a_work, b_work) or 1
    for i, (lab, work, wage, col, bg) in enumerate(rows):
        y = 48 + i * 54
        cv.text(42, y + 16, lab, size=9, anchor="start", weight=700,
                color=col)
        width = 210 * work / max_work
        _card(cv, 102, y, width, 28, col, bg, r=4, sw=1.4)
        cv.text(102 + width / 2, y + 19, f"{_fmt(work)} units", size=9,
                weight=700, color=col)
        cv.text(326, y + 18, f"wage = {_fmt(wage)}", size=9.5,
                anchor="start", weight=700, color=col)

    _card(cv, 44, 166, 364, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 188, f"work ratio = {_fmt(a_work)} : {_fmt(b_work)}  ->  "
            f"wages = {_fmt(a_wage)} : {_fmt(b_wage)}",
            size=9.5, weight=700, color=C["purple"])
    _card(cv, 72, 214, 308, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 233, f"total wage = {_fmt(a_wage + b_wage)}",
            size=9.5, weight=700, color=C["amber"])
    return cv.svg()


# ───────────────────────────── efficiency x time ────────────────────────────
def efficiency_time(spec):
    ea = float(spec.get("ea", 3))
    ta = float(spec.get("ta", 4))
    eb = float(spec.get("eb", 2))
    tb = float(spec.get("tb", 6))
    wa, wb = ea * ta, eb * tb
    ratio = _ratio([wa, wb])

    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 2302))
    cv.text(W / 2, 20, "work contribution = efficiency x time",
            size=10.5, weight=700, color=C["soft"])

    for x, lab, e, t, work, col, bg in (
            (32, "A", ea, ta, wa, C["blue"], C["blue_bg"]),
            (236, "B", eb, tb, wb, C["green"], C["green_bg"])):
        _card(cv, x, 42, 184, 76, col, bg, sw=1.6)
        cv.text(x + 92, 62, f"worker {lab}", size=10, weight=700, color=col)
        cv.text(x + 92, 82, f"efficiency = {_fmt(e)}", size=8.8, color=col)
        cv.text(x + 92, 101, f"time = {_fmt(t)} days", size=8.8, color=col)
        cv.text(x + 92, 140, f"work = { _fmt(work) } units", size=9.5,
                weight=700, color=col)
        width = 140 * work / max(wa, wb, 1)
        _card(cv, x + 22, 154, width, 24, col, bg, r=4, sw=1.3)

    _card(cv, 62, 204, 328, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 225, f"work ratio A:B = {ratio[0]}:{ratio[1]}", size=10.2,
            weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── men x days x hours ───────────────────────────
def men_hours(spec):
    m1 = int(spec.get("m1", 4))
    d1 = int(spec.get("d1", 6))
    h1 = int(spec.get("h1", 8))
    m2 = int(spec.get("m2", 6))
    d2 = int(spec.get("d2", 4))
    h2 = int(spec.get("h2", 8))
    w1 = m1 * d1 * h1
    w2 = m2 * d2 * h2
    ratio = _ratio([w1, w2])

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 2303))
    cv.text(W / 2, 20, "for equal-efficiency workers, men x days x hours is work",
            size=9.8, weight=700, color=C["soft"])

    for x, lab, m, d, h, work, col, bg in (
            (32, "group A", m1, d1, h1, w1, C["blue"], C["blue_bg"]),
            (236, "group B", m2, d2, h2, w2, C["green"], C["green_bg"])):
        _card(cv, x, 42, 184, 72, col, bg, sw=1.6)
        cv.text(x + 92, 61, lab, size=9.8, weight=700, color=col)
        cv.text(x + 92, 81, f"{m} men x {d} days", size=8.8, color=col)
        cv.text(x + 92, 99, f"x {h} hours = {work}", size=8.8, color=col)
        width = 142 * work / max(w1, w2, 1)
        _card(cv, x + 21, 142, width, 24, col, bg, r=4, sw=1.3)
        cv.text(x + 21 + width / 2, 158, f"{work} man-hours", size=8.3,
                weight=700, color=col)

    _card(cv, 54, 190, 344, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 211, f"wage ratio = work ratio = {ratio[0]}:{ratio[1]}",
            size=9.8, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "only when worker efficiencies are equal",
            size=8.7, color=C["red"])
    return cv.svg()


# ───────────────────────────── piecework ────────────────────────────────────
def piecework(spec):
    units_a = float(spec.get("units_a", 120))
    rate_a = float(spec.get("rate_a", 5))
    units_b = float(spec.get("units_b", 80))
    rate_b = float(spec.get("rate_b", 7.5))
    wage_a, wage_b = units_a * rate_a, units_b * rate_b

    W, H = 452, 248
    cv = Canvas(W, H, seed=_seed(spec, 2304))
    cv.text(W / 2, 20, "piecework wage = pieces completed x rate per piece",
            size=9.9, weight=700, color=C["soft"])

    rows = [("A", units_a, rate_a, wage_a, C["blue"], C["blue_bg"]),
            ("B", units_b, rate_b, wage_b, C["green"], C["green_bg"])]
    for i, (lab, units, rate, wage, col, bg) in enumerate(rows):
        y = 48 + i * 54
        _card(cv, 30, y, 392, 42, col, bg, sw=1.5)
        cv.text(52, y + 17, lab, size=10, anchor="start", weight=700, color=col)
        cv.text(106, y + 17, f"{_fmt(units)} pieces", size=8.8, anchor="start", color=col)
        cv.text(230, y + 17, f"x {_fmt(rate)} per piece", size=8.8, anchor="start", color=col)
        cv.text(398, y + 17, f"= {_fmt(wage)}", size=9.4, anchor="end", weight=700, color=col)
        width = 300 * wage / max(wage_a, wage_b, 1)
        _card(cv, 74, y + 26, width, 9, col, "#ffffff", r=3, sw=0.9)

    _card(cv, 72, 174, 308, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 195, f"A wage : B wage = {_fmt(wage_a)} : {_fmt(wage_b)}",
            size=9.7, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "a higher piece rate can balance fewer pieces",
            size=8.6, color=C["ink"])
    return cv.svg()


# ───────────────────────────── three-worker contribution ────────────────────
def group_contribution(spec):
    e1, t1 = float(spec.get("e1", 2)), float(spec.get("t1", 6))
    e2, t2 = float(spec.get("e2", 1)), float(spec.get("t2", 8))
    e3, t3 = float(spec.get("e3", 3)), float(spec.get("t3", 4))
    works = [e1 * t1, e2 * t2, e3 * t3]
    ratio = _ratio(works)
    total = sum(works)

    W, H = 452, 282
    cv = Canvas(W, H, seed=_seed(spec, 2305))
    cv.text(W / 2, 20, "each worker gets credit for actual contribution",
            size=10.2, weight=700, color=C["soft"])

    vals = [("A", e1, t1, works[0], C["blue"], C["blue_bg"]),
            ("B", e2, t2, works[1], C["green"], C["green_bg"]),
            ("C", e3, t3, works[2], C["amber"], C["amber_bg"])]
    max_work = max(works) or 1
    for i, (lab, eff, time, work, col, bg) in enumerate(vals):
        y = 44 + i * 44
        cv.text(38, y + 18, lab, size=10, weight=700, color=col)
        cv.text(66, y + 18, f"{_fmt(eff)} x {_fmt(time)}", size=8.8,
                anchor="start", color=col)
        width = 210 * work / max_work
        _card(cv, 168, y, width, 28, col, bg, r=4, sw=1.3)
        cv.text(168 + width / 2, y + 19, f"{_fmt(work)} units", size=8.8,
                weight=700, color=col)
        cv.text(404, y + 18, f"{ratio[i]}/{sum(ratio)} of wage", size=8.2,
                anchor="end", color=col)

    _card(cv, 48, 190, 356, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 212, f"work ratio = {ratio[0]} : {ratio[1]} : {ratio[2]}  "
            f"(total { _fmt(total) })", size=9.3, weight=700,
            color=C["purple"])
    cv.text(W / 2, H - 8, "divide total wages in this same ratio",
            size=8.8, color=C["ink"])
    return cv.svg()


# ───────────────────────────── fixed wage check ─────────────────────────────
def wage_check(spec):
    total_wage = float(spec.get("total_wage", 4500))
    a_work = float(spec.get("a_work", 3))
    b_work = float(spec.get("b_work", 2))
    total_work = a_work + b_work
    a_wage = total_wage * a_work / total_work
    b_wage = total_wage * b_work / total_work

    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 2306))
    cv.text(W / 2, 20, "share = total wage x personal work / total work",
            size=9.8, weight=700, color=C["soft"])

    _card(cv, 48, 44, 356, 34, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 66, f"total wage = {_fmt(total_wage)}   |   total work = {_fmt(total_work)}",
            size=9.6, weight=700, color=C["amber"])

    for i, (lab, work, wage, col, bg) in enumerate((
            ("A", a_work, a_wage, C["blue"], C["blue_bg"]),
            ("B", b_work, b_wage, C["green"], C["green_bg"]))):
        y = 98 + i * 42
        _card(cv, 48, y, 356, 30, col, bg, r=5, sw=1.3)
        cv.text(64, y + 20, f"{lab}: { _fmt(work) }/{_fmt(total_work)} x {_fmt(total_wage)}",
                size=8.8, anchor="start", color=col)
        cv.text(388, y + 20, f"= {_fmt(wage)}", size=9.4, anchor="end",
                weight=700, color=col)

    _card(cv, 94, 190, 264, 26, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 208, f"check: {_fmt(a_wage)} + {_fmt(b_wage)} = {_fmt(total_wage)}",
            size=9, weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "work-wage-bars": work_wage_bars,
    "efficiency-time": efficiency_time,
    "men-hours": men_hours,
    "piecework": piecework,
    "group-contribution": group_contribution,
    "wage-check": wage_check,
}
