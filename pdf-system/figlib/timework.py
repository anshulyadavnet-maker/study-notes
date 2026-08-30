"""
timework.py — figures for Chapter 21 (Time & Work).

work-unit       : convert individual days into whole work units using an LCM
rate-table      : compare one-day work rates and the combined rate
progress-bar    : show work completed first by A and then by A+B together
efficiency-ratio: efficiency and time move in inverse ratios
men-days        : preserve the men x days x hours product
alternate-days  : track an alternating-work schedule day by day
"""
import math
from fractions import Fraction

from .sketch import Canvas, C


def _seed(spec, default=2100):
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


def _lcm(*values):
    out = 1
    for value in values:
        out = math.lcm(out, int(value))
    return out


# ───────────────────────────── LCM work units ───────────────────────────────
def work_unit(spec):
    a_days = int(spec.get("a_days", 12))
    b_days = int(spec.get("b_days", 18))
    total = _lcm(a_days, b_days)
    a_rate, b_rate = total // a_days, total // b_days
    together = a_rate + b_rate
    together_time = Fraction(total, together)

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2101))
    cv.text(W / 2, 20, "LCM turns fractional rates into whole work units",
            size=10.5, weight=700, color=C["soft"])

    _card(cv, 34, 38, 182, 48, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(125, 57, f"A alone: {a_days} days", size=10, weight=700,
            color=C["blue"])
    cv.text(125, 75, f"rate = {a_rate} units/day", size=9.2, color=C["blue"])

    _card(cv, 236, 38, 182, 48, C["green"], C["green_bg"], sw=1.6)
    cv.text(327, 57, f"B alone: {b_days} days", size=10, weight=700,
            color=C["green"])
    cv.text(327, 75, f"rate = {b_rate} units/day", size=9.2, color=C["green"])

    x0, y0, bw, bh = 44, 112, 364, 28
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{bw}" height="{bh}" rx="5" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    unit_w = bw / total
    for i in range(total):
        col = C["blue_bg"] if i < a_rate else C["green_bg"]
        stroke = C["blue"] if i < a_rate else C["green"]
        cv.raw(f'<rect x="{x0 + i * unit_w + 1:.2f}" y="{y0 + 1}" '
               f'width="{max(unit_w - 1, 0.5):.2f}" height="{bh - 2}" '
               f'fill="{col}" stroke="{stroke}" stroke-width="0.45"/>')
    cv.text(x0 + bw / 2, y0 + 19, f"total work = LCM({a_days}, {b_days}) = {total} units",
            size=9.6, weight=700, color=C["ink"])

    _card(cv, 44, 164, 364, 36, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 187, f"together = {total}/({a_rate}+{b_rate}) = "
            f"{_fmt(together_time)} days", size=10.4, weight=700,
            color=C["purple"])
    cv.text(W / 2, 224, "never add days; add one-day work rates",
            size=9.5, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "work = rate x time", size=9, color=C["soft"])
    return cv.svg()


# ───────────────────────────── rate comparison ──────────────────────────────
def rate_table(spec):
    a_days = int(spec.get("a_days", 12))
    b_days = int(spec.get("b_days", 18))
    c_days = spec.get("c_days")
    days = [a_days, b_days]
    labels = ["A", "B"]
    cols = [C["blue"], C["green"]]
    bgs = [C["blue_bg"], C["green_bg"]]
    if c_days not in (None, "", 0):
        days.append(int(c_days))
        labels.append("C")
        cols.append(C["amber"])
        bgs.append(C["amber_bg"])
    total = _lcm(*days)
    rates = [total // d for d in days]
    combined = sum(rates)
    together_time = Fraction(total, combined)

    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 2102))
    cv.text(W / 2, 20, "one-day work is the rate, not the number of days",
            size=10.3, weight=700, color=C["soft"])

    x0 = 34
    widths = [72, 112, 112, 88]
    headers = ["worker", "alone days", "one-day rate", "units"]
    xpos = [x0]
    for width in widths[:-1]:
        xpos.append(xpos[-1] + width)
    for x, width, head in zip(xpos, widths, headers):
        _card(cv, x, 36, width, 28, C["ink"], C["paper"], r=4, sw=1.2)
        cv.text(x + width / 2, 55, head, size=8.5, weight=700,
                color=C["ink"])

    for i, (lab, d, rate, col, bg) in enumerate(zip(labels, days, rates, cols, bgs)):
        y = 70 + i * 38
        vals = [lab, str(d), f"1/{d}", str(rate)]
        for j, (x, width, val) in enumerate(zip(xpos, widths, vals)):
            _card(cv, x, y, width, 30, col, bg if j == 0 else "#ffffff",
                  r=4, sw=1.2)
            cv.text(x + width / 2, y + 20, val, size=9.6,
                    weight=700 if j in (0, 3) else 400, color=col)

    bottom = 70 + len(days) * 38 + 10
    _card(cv, 34, bottom, 384, 34, C["purple"], C["purple_bg"], sw=1.7)
    rate_text = " + ".join(str(rate) for rate in rates)
    cv.text(226, bottom + 22, f"combined rate = {rate_text} = {combined} units/day  "
            f"-> time = {total}/{combined} = {_fmt(together_time)} days",
            size=9.2, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "the fastest possible combined time is less than every solo time",
            size=8.6, color=C["red"])
    return cv.svg()


# ───────────────────────────── partial completion ───────────────────────────
def progress_bar(spec):
    a_days = int(spec.get("a_days", 12))
    b_days = int(spec.get("b_days", 18))
    first_days = int(spec.get("first_days", 4))
    total = _lcm(a_days, b_days)
    a_rate, b_rate = total // a_days, total // b_days
    done = min(first_days * a_rate, total)
    remaining = total - done
    together_rate = a_rate + b_rate
    extra = Fraction(remaining, together_rate)
    total_time = first_days + extra

    W, H = 452, 256
    cv = Canvas(W, H, seed=_seed(spec, 2103))
    cv.text(W / 2, 20, "finish the remaining work at the new rate",
            size=10.5, weight=700, color=C["soft"])

    x0, bw, bh = 38, 376, 34
    cv.text(x0, 47, "whole job", size=8.8, anchor="start", weight=700,
            color=C["ink"])
    cv.raw(f'<rect x="{x0}" y="{56}" width="{bw}" height="{bh}" rx="5" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    done_w = bw * done / total if total else 0
    if done_w:
        cv.raw(f'<rect x="{x0+2}" y="58" width="{max(done_w-2,1):.2f}" '
               f'height="{bh-4}" rx="4" fill="{C["blue_bg"]}" '
               f'stroke="{C["blue"]}" stroke-width="1.2"/>')
    rem_w = bw - done_w
    if rem_w:
        cv.raw(f'<rect x="{x0 + done_w:.2f}" y="58" width="{max(rem_w-2,1):.2f}" '
               f'height="{bh-4}" rx="4" fill="{C["amber_bg"]}" '
               f'stroke="{C["amber"]}" stroke-width="1.2"/>')
    cv.text(x0 + done_w / 2, 79, f"done {done}", size=9, weight=700,
            color=C["blue"])
    cv.text(x0 + done_w + rem_w / 2, 79, f"left {remaining}", size=9,
            weight=700, color=C["amber"])

    rows = [
        (f"A works first", f"{first_days} days x {a_rate} = {done} units",
         C["blue"], C["blue_bg"]),
        ("A + B now", f"rate = {a_rate} + {b_rate} = {together_rate} units/day",
         C["green"], C["green_bg"]),
        ("time for balance", f"{remaining}/{together_rate} = {_fmt(extra)} days",
         C["amber"], C["amber_bg"]),
    ]
    for i, (lab, value, col, bg) in enumerate(rows):
        y = 108 + i * 34
        _card(cv, 38, y, 376, 27, col, bg, r=5, sw=1.3)
        cv.text(50, y + 18, lab, size=8.8, anchor="start", weight=700,
                color=col)
        cv.text(402, y + 18, value, size=8.8, anchor="end", color=col)

    _card(cv, 78, 214, 296, 30, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 234, f"total time = {first_days} + {_fmt(extra)} = {_fmt(total_time)} days",
            size=10, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── efficiency and time ──────────────────────────
def efficiency_ratio(spec):
    ea = int(spec.get("ea", 3))
    eb = int(spec.get("eb", 2))
    b_days = int(spec.get("b_days", 30))
    a_days = Fraction(b_days * eb, ea)
    total_units = _lcm(int(a_days), b_days)
    a_rate, b_rate = total_units // int(a_days), total_units // b_days
    together = Fraction(total_units, a_rate + b_rate)

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2104))
    cv.text(W / 2, 20, "efficiency and time are inverse ratios",
            size=10.5, weight=700, color=C["soft"])

    _card(cv, 34, 40, 182, 48, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(125, 58, f"A efficiency = {ea}", size=10.5, weight=700,
            color=C["blue"])
    cv.text(125, 76, f"A time = {_fmt(a_days)} days", size=9.6, color=C["blue"])

    _card(cv, 236, 40, 182, 48, C["green"], C["green_bg"], sw=1.6)
    cv.text(327, 58, f"B efficiency = {eb}", size=10.5, weight=700,
            color=C["green"])
    cv.text(327, 76, f"B time = {b_days} days", size=9.6, color=C["green"])

    cv.text(W / 2, 112, f"efficiency A : B = {ea} : {eb}", size=10,
            weight=700, color=C["ink"])
    cv.text(W / 2, 131, f"time A : B = {eb} : {ea}", size=10,
            weight=700, color=C["red"])

    # Two bars: the longer bar is the slower time.
    x0, y1, maxw = 82, 158, 288
    for y, value, lab, col, bg in ((y1, float(a_days), "A time", C["blue"], C["blue_bg"]),
                                    (y1 + 32, b_days, "B time", C["green"], C["green_bg"])):
        width = maxw * value / max(float(a_days), b_days)
        _card(cv, x0, y, width, 22, col, bg, r=4, sw=1.3)
        cv.text(x0 + width / 2, y + 15, f"{lab}  {_fmt(value)}", size=8.8,
                weight=700, color=col)

    _card(cv, 62, 222, 328, 24, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 239, f"together time = {_fmt(together)} days",
            size=9.5, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── men-days-hours product ───────────────────────
def men_days(spec):
    m1 = int(spec.get("m1", 12))
    d1 = int(spec.get("d1", 15))
    h1 = int(spec.get("h1", 8))
    m2 = int(spec.get("m2", 20))
    h2 = int(spec.get("h2", 6))
    d2 = Fraction(m1 * d1 * h1, m2 * h2)
    product = m1 * d1 * h1

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 2105))
    cv.text(W / 2, 20, "same work means the men x days x hours product stays fixed",
            size=9.9, weight=700, color=C["soft"])

    _card(cv, 32, 42, 184, 68, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(124, 61, f"old plan: {m1} men", size=9.5, weight=700,
            color=C["blue"])
    cv.text(124, 80, f"{d1} days x {h1} hours", size=9.5, color=C["blue"])
    cv.text(124, 99, f"work = {product} units", size=9.5, weight=700,
            color=C["blue"])

    _card(cv, 236, 42, 184, 68, C["green"], C["green_bg"], sw=1.6)
    cv.text(328, 61, f"new plan: {m2} men", size=9.5, weight=700,
            color=C["green"])
    cv.text(328, 80, f"x days x {h2} hours", size=9.5, color=C["green"])
    cv.text(328, 99, f"days = {_fmt(d2)}", size=9.5, weight=700,
            color=C["green"])

    cv.arrow(216, 76, 236, 76, color=C["grey"], w=1.3)
    _card(cv, 48, 136, 356, 34, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 158, f"{m1} x {d1} x {h1} = {m2} x d x {h2}",
            size=11, weight=700, color=C["amber"])
    _card(cv, 80, 184, 292, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 205, f"d = {product}/({m2} x {h2}) = {_fmt(d2)} days",
            size=9.8, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "more men or more hours means fewer days",
            size=8.8, color=C["red"])
    return cv.svg()


# ───────────────────────────── alternate-day schedule ───────────────────────
def alternate_days(spec):
    a_days = int(spec.get("a_days", 8))
    b_days = int(spec.get("b_days", 12))
    start = str(spec.get("start", "A")).upper()
    total = _lcm(a_days, b_days)
    rates = {"A": total // a_days, "B": total // b_days}
    order = [start, "B" if start == "A" else "A"]

    remaining = Fraction(total)
    rows = []
    day = 1
    index = 0
    while remaining > 0 and day <= 16:
        worker = order[index % 2]
        rate = rates[worker]
        used = min(remaining, Fraction(rate))
        part_day = used / rate
        rows.append((day, worker, used, part_day))
        remaining -= used
        day += 1
        index += 1

    W, H = 452, 276
    cv = Canvas(W, H, seed=_seed(spec, 2106))
    cv.text(W / 2, 20, "alternate the workers and stop when the remaining work is zero",
            size=9.8, weight=700, color=C["soft"])

    x0, y0, box_w, gap = 20, 52, 38, 6
    for i, (number, worker, used, part_day) in enumerate(rows[:10]):
        x = x0 + i * (box_w + gap)
        col = C["blue"] if worker == "A" else C["green"]
        bg = C["blue_bg"] if worker == "A" else C["green_bg"]
        _card(cv, x, y0, box_w, 56, col, bg, r=5, sw=1.3)
        cv.text(x + box_w / 2, y0 + 16, f"D{number} {worker}", size=8.8,
                weight=700, color=col)
        cv.text(x + box_w / 2, y0 + 35, f"+{_fmt(used)}", size=8.6,
                color=col)
        if part_day != 1:
            cv.text(x + box_w / 2, y0 + 48, f"{_fmt(part_day)} d", size=7.5,
                    weight=700, color=C["red"])
        if i < len(rows[:10]) - 1:
            cv.arrow(x + box_w + 1, y0 + 28, x + box_w + gap - 1, y0 + 28,
                     color=C["grey"], w=0.9)

    # A compact cumulative bar makes the stopping point obvious.
    bx, by, bw, bh = 42, 137, 368, 28
    cv.raw(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="5" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    cursor = bx
    for number, worker, used, _ in rows:
        width = bw * float(used) / total
        col = C["blue"] if worker == "A" else C["green"]
        bg = C["blue_bg"] if worker == "A" else C["green_bg"]
        cv.raw(f'<rect x="{cursor + 1:.2f}" y="{by + 1}" '
               f'width="{max(width - 1, 0.5):.2f}" height="{bh - 2}" '
               f'fill="{bg}" stroke="{col}" stroke-width="0.6"/>')
        cursor += width
    cv.text(bx + bw / 2, by + 19, f"total {total} units completed", size=9.2,
            weight=700, color=C["ink"])

    pair_rate = rates[order[0]] + rates[order[1]]
    full_pairs = total // pair_rate
    last = rows[-1] if rows else (0, "", 0, 0)
    last_note = f"last step: {last[1]} uses {_fmt(last[3])} day" if last[3] != 1 else "last step is a full day"
    _card(cv, 38, 184, 376, 34, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 206, f"2-day rate = {pair_rate}; full pairs = {full_pairs}; {last_note}",
            size=8.9, weight=700, color=C["purple"])
    _card(cv, 82, 230, 288, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 249, f"total time = {len(rows)-1} + {_fmt(rows[-1][3])} days",
            size=9.6, weight=700, color=C["amber"])
    return cv.svg()


REGISTRY = {
    "work-unit": work_unit,
    "rate-table": rate_table,
    "progress-bar": progress_bar,
    "efficiency-ratio": efficiency_ratio,
    "men-days": men_days,
    "alternate-days": alternate_days,
}
