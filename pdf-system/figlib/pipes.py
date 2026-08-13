"""
pipes.py — figures for Chapter 22 (Pipes & Cisterns).

tank-level       : a tank filling as a fraction of its capacity
rate-signs       : filling is positive, emptying is negative
net-rate         : signed LCM work units for several pipes
open-close       : a fill pipe and leak working together, then separately
capacity-litres  : convert litres per minute into tank time
efficiency       : pipe efficiency and filling time in inverse ratio
"""
import math
from fractions import Fraction

from .sketch import Canvas, C


def _seed(spec, default=2200):
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
    result = 1
    for value in values:
        result = math.lcm(result, int(value))
    return result


# ───────────────────────────── tank level ────────────────────────────────────
def tank_level(spec):
    fill_hours = int(spec.get("fill_hours", 12))
    hours = float(spec.get("hours", 5))
    fraction = min(max(hours / fill_hours, 0), 1)

    W, H = 420, 252
    cv = Canvas(W, H, seed=_seed(spec, 2201))
    cv.text(W / 2, 20, "a pipe adds the same fraction of the tank each hour",
            size=10.2, weight=700, color=C["soft"])

    x, y, tw, th = 148, 46, 124, 132
    cv.raw(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="8" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.8"/>')
    water_h = (th - 6) * fraction
    if water_h > 0:
        cv.raw(f'<rect x="{x+3}" y="{y+th-3-water_h:.2f}" width="{tw-6}" '
               f'height="{water_h:.2f}" rx="5" fill="{C["blue_bg"]}" '
               f'stroke="{C["blue"]}" stroke-width="1.3"/>')
    cv.text(x + tw / 2, y + 22, "FULL", size=9.2, weight=700, color=C["red"])
    cv.text(x + tw / 2, y + th - water_h / 2 + 4,
            f"{_fmt(Fraction(int(round(hours * 1000)), fill_hours * 1000))}",
            size=12, weight=700, color=C["blue"])
    cv.text(x + tw + 22, y + 10, "1", size=9, anchor="start", color=C["red"])
    cv.text(x + tw + 22, y + th, "0", size=9, anchor="start", color=C["soft"])

    rows = [
        ("full time", f"{fill_hours} h", C["blue"]),
        ("time open", f"{_fmt(hours)} h", C["green"]),
        ("tank filled", f"{_fmt(fraction * 100)}%", C["purple"]),
        ("one-hour rate", f"1/{fill_hours}", C["amber"]),
    ]
    for i, (lab, val, col) in enumerate(rows):
        yy = 54 + i * 30
        _card(cv, 24, yy, 104, 24, col, "#ffffff", r=5, sw=1.2)
        cv.text(76, yy + 16, lab, size=8.2, weight=700, color=col)
        cv.text(350, yy + 16, val, size=9.2, anchor="end", weight=700,
                color=col)
    cv.text(W / 2, H - 10, "fraction filled = hours open / full time",
            size=9, weight=700, color=C["ink"])
    return cv.svg()


# ───────────────────────────── positive and negative rates ──────────────────
def rate_signs(spec):
    in_hours = int(spec.get("in_hours", 12))
    out_hours = int(spec.get("out_hours", 18))
    net = Fraction(1, in_hours) - Fraction(1, out_hours)

    W, H = 452, 238
    cv = Canvas(W, H, seed=_seed(spec, 2202))
    cv.text(W / 2, 20, "fill is positive, emptying is negative",
            size=10.6, weight=700, color=C["soft"])

    _card(cv, 32, 42, 182, 58, C["blue"], C["blue_bg"], sw=1.7)
    cv.text(123, 62, f"inlet: fills in {in_hours} h", size=9.8, weight=700,
            color=C["blue"])
    cv.text(123, 83, f"rate = +1/{in_hours}", size=10, color=C["blue"])

    _card(cv, 238, 42, 182, 58, C["red"], C["red_bg"], sw=1.7)
    cv.text(329, 62, f"outlet: empties in {out_hours} h", size=9.4,
            weight=700, color=C["red"])
    cv.text(329, 83, f"rate = -1/{out_hours}", size=10, color=C["red"])

    cv.arrow(123, 112, 123, 136, color=C["blue"], w=1.4)
    cv.arrow(329, 112, 329, 136, color=C["red"], w=1.4)
    _card(cv, 68, 142, 316, 36, C["purple"], C["purple_bg"], sw=1.8)
    cv.text(226, 165, f"net rate = 1/{in_hours} - 1/{out_hours} = {_fmt(net)}",
            size=10.4, weight=700, color=C["purple"])
    cv.text(W / 2, 202, f"net is positive, so the tank rises; time = {_fmt(1/net)} h",
            size=9.2, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "never add an outlet rate", size=9, color=C["red"])
    return cv.svg()


# ───────────────────────────── signed LCM work units ─────────────────────────
def net_rate(spec):
    a_hours = int(spec.get("a_hours", 12))
    b_hours = int(spec.get("b_hours", 18))
    out_hours = int(spec.get("out_hours", 36))
    total = _lcm(a_hours, b_hours, out_hours)
    rates = [total // a_hours, total // b_hours, -(total // out_hours)]
    net_units = sum(rates)
    time = Fraction(total, net_units) if net_units > 0 else None

    W, H = 452, 276
    cv = Canvas(W, H, seed=_seed(spec, 2203))
    cv.text(W / 2, 20, "signed LCM units make several pipes easy to add",
            size=10.2, weight=700, color=C["soft"])

    labels = [f"A +{rates[0]}", f"B +{rates[1]}", f"outlet {rates[2]}"]
    cols = [C["blue"], C["green"], C["red"]]
    bgs = [C["blue_bg"], C["green_bg"], C["red_bg"]]
    days = [a_hours, b_hours, out_hours]
    for i, (lab, rate, day, col, bg) in enumerate(zip(labels, rates, days, cols, bgs)):
        x = 28 + i * 142
        _card(cv, x, 48, 126, 64, col, bg, sw=1.5)
        cv.text(x + 63, 68, lab, size=10.2, weight=700, color=col)
        cv.text(x + 63, 89, f"{day} h alone", size=8.7, color=col)
        cv.text(x + 63, 103, f"{abs(rate)} units/day", size=8.2, color=col)

    bx, by, bw, bh = 42, 132, 368, 32
    cv.raw(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="5" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    unit_w = bw / total
    positive_w = max(0, (rates[0] + rates[1]) * unit_w)
    negative_w = min(bw - positive_w, abs(rates[2]) * unit_w)
    if positive_w:
        cv.raw(f'<rect x="{bx+1}" y="{by+1}" width="{max(positive_w-1,1):.2f}" '
               f'height="{bh-2}" rx="4" fill="{C["green_bg"]}" '
               f'stroke="{C["green"]}" stroke-width="1.1"/>')
    if negative_w:
        cv.raw(f'<rect x="{bx+positive_w:.2f}" y="{by+1}" width="{max(negative_w-1,1):.2f}" '
               f'height="{bh-2}" rx="4" fill="{C["red_bg"]}" '
               f'stroke="{C["red"]}" stroke-width="1.1"/>')
    cv.text(bx + bw / 2, by + 21, f"total work = {total} units", size=9.4,
            weight=700, color=C["ink"])

    _card(cv, 50, 184, 352, 36, C["purple"], C["purple_bg"], sw=1.7)
    if time is None:
        formula = f"net = {rates[0]} + {rates[1]} - {abs(rates[2])} = {net_units}"
    else:
        formula = f"net = {rates[0]} + {rates[1]} - {abs(rates[2])} = {net_units}; time = {total}/{net_units} = {_fmt(time)} h"
    cv.text(226, 207, formula, size=9.1, weight=700, color=C["purple"])
    cv.text(W / 2, 246, "a negative net rate means the tank cannot fill while these pipes stay open",
            size=8.5, color=C["red"])
    cv.text(W / 2, H - 8, "outlet units are subtracted", size=9, color=C["soft"])
    return cv.svg()


# ───────────────────────────── open together, then close leak ───────────────
def open_close(spec):
    fill_hours = int(spec.get("fill_hours", 8))
    leak_hours = int(spec.get("leak_hours", 12))
    both_hours = int(spec.get("both_hours", 3))
    net = Fraction(1, fill_hours) - Fraction(1, leak_hours)
    done = both_hours * net
    remaining = 1 - done
    extra = remaining * fill_hours
    total_time = both_hours + extra

    W, H = 452, 272
    cv = Canvas(W, H, seed=_seed(spec, 2204))
    cv.text(W / 2, 20, "first use the net rate, then change the rate when the leak closes",
            size=9.7, weight=700, color=C["soft"])

    x0, y0, bw, bh = 38, 50, 376, 34
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{bw}" height="{bh}" rx="5" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
    done_w = bw * float(done)
    if done_w > 0:
        cv.raw(f'<rect x="{x0+1}" y="{y0+1}" width="{max(done_w-1,1):.2f}" '
               f'height="{bh-2}" rx="4" fill="{C["blue_bg"]}" '
               f'stroke="{C["blue"]}" stroke-width="1.2"/>')
    cv.raw(f'<rect x="{x0+done_w:.2f}" y="{y0+1}" width="{max(bw-done_w-1,1):.2f}" '
           f'height="{bh-2}" rx="4" fill="{C["amber_bg"]}" '
           f'stroke="{C["amber"]}" stroke-width="1.2"/>')
    cv.text(x0 + done_w / 2, y0 + 21, f"done {_fmt(done)}", size=9,
            weight=700, color=C["blue"])
    cv.text(x0 + done_w + (bw - done_w) / 2, y0 + 21,
            f"left {_fmt(remaining)}", size=9, weight=700, color=C["amber"])

    rows = [
        ("both open", f"{both_hours} h x (1/{fill_hours} - 1/{leak_hours}) = {_fmt(done)}",
         C["purple"], C["purple_bg"]),
        ("leak closed", f"remaining = {_fmt(remaining)} of tank",
         C["amber"], C["amber_bg"]),
        ("inlet alone", f"time = {_fmt(extra)} h more",
         C["green"], C["green_bg"]),
    ]
    for i, (lab, value, col, bg) in enumerate(rows):
        yy = 106 + i * 35
        _card(cv, 38, yy, 376, 28, col, bg, r=5, sw=1.3)
        cv.text(50, yy + 19, lab, size=8.8, anchor="start", weight=700,
                color=col)
        cv.text(402, yy + 19, value, size=8.6, anchor="end", color=col)

    _card(cv, 80, 218, 292, 30, C["red"], C["red_bg"], sw=1.7)
    cv.text(226, 238, f"total time = {both_hours} + {_fmt(extra)} = {_fmt(total_time)} h",
            size=9.8, weight=700, color=C["red"])
    cv.text(W / 2, H - 8, "the rate changes when a pipe is opened or closed",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── litre capacity ───────────────────────────────
def capacity_litres(spec):
    capacity = float(spec.get("capacity", 720))
    inlet = float(spec.get("inlet", 60))
    outlet = float(spec.get("outlet", 24))
    net = inlet - outlet
    minutes = capacity / net if net > 0 else 0

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2205))
    cv.text(W / 2, 20, "convert every rate to litres per minute first",
            size=10.3, weight=700, color=C["soft"])

    x, y, tw, th = 46, 54, 106, 126
    cv.raw(f'<rect x="{x}" y="{y}" width="{tw}" height="{th}" rx="8" '
           f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.8"/>')
    cv.raw(f'<rect x="{x+3}" y="{y+3}" width="{tw-6}" height="{th-6}" rx="5" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.2"/>')
    cv.text(x + tw / 2, y + th / 2 + 4, f"{_fmt(capacity)} L", size=12,
            weight=700, color=C["blue"])
    cv.text(x + tw / 2, y + th + 17, "full tank", size=8.8, weight=700,
            color=C["ink"])

    rows = [
        ("capacity", f"{_fmt(capacity)} L", C["blue"]),
        ("inlet", f"+{_fmt(inlet)} L/min", C["green"]),
        ("outlet", f"-{_fmt(outlet)} L/min", C["red"]),
        ("net rate", f"{_fmt(net)} L/min", C["purple"]),
        ("time", f"{_fmt(minutes)} min", C["amber"]),
    ]
    for i, (lab, value, col) in enumerate(rows):
        yy = 50 + i * 31
        _card(cv, 190, yy, 224, 25, col, "#ffffff", r=5, sw=1.2)
        cv.text(202, yy + 17, lab, size=8.4, anchor="start", color=C["soft"])
        cv.text(402, yy + 17, value, size=9.3, anchor="end", weight=700,
                color=col)
    _card(cv, 38, 204, 376, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 224, f"time = capacity / net rate = {_fmt(capacity)}/{_fmt(net)} = {_fmt(minutes)} min",
            size=9.3, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── efficiency and time ──────────────────────────
def efficiency(spec):
    ea = int(spec.get("ea", 3))
    eb = int(spec.get("eb", 2))
    b_hours = int(spec.get("b_hours", 30))
    a_hours = Fraction(b_hours * eb, ea)
    total = _lcm(int(a_hours), b_hours)
    rates = total // int(a_hours), total // b_hours
    together = Fraction(total, sum(rates))

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 2206))
    cv.text(W / 2, 20, "pipe efficiency and filling time are inverse",
            size=10.5, weight=700, color=C["soft"])

    _card(cv, 34, 40, 182, 52, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(125, 60, f"Pipe A efficiency = {ea}", size=9.8, weight=700,
            color=C["blue"])
    cv.text(125, 79, f"fills in {_fmt(a_hours)} h", size=9.5, color=C["blue"])

    _card(cv, 236, 40, 182, 52, C["green"], C["green_bg"], sw=1.6)
    cv.text(327, 60, f"Pipe B efficiency = {eb}", size=9.8, weight=700,
            color=C["green"])
    cv.text(327, 79, f"fills in {b_hours} h", size=9.5, color=C["green"])

    cv.text(W / 2, 119, f"efficiency A : B = {ea} : {eb}", size=10,
            weight=700, color=C["ink"])
    cv.text(W / 2, 138, f"time A : B = {eb} : {ea}", size=10,
            weight=700, color=C["red"])

    max_time = max(float(a_hours), b_hours)
    for yy, value, label, col, bg in ((164, float(a_hours), "A", C["blue"], C["blue_bg"]),
                                       (196, b_hours, "B", C["green"], C["green_bg"])):
        width = 270 * value / max_time
        _card(cv, 92, yy, width, 22, col, bg, r=4, sw=1.3)
        cv.text(92 + width / 2, yy + 15, f"{label}: {_fmt(value)} h", size=8.8,
                weight=700, color=col)

    _card(cv, 72, 226, 308, 24, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(226, 243, f"both pipes fill in {_fmt(together)} h",
            size=9.4, weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "tank-level": tank_level,
    "rate-signs": rate_signs,
    "net-rate": net_rate,
    "open-close": open_close,
    "capacity-litres": capacity_litres,
    "pipe-efficiency": efficiency,
}
