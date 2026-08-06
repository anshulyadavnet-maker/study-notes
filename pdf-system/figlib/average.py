"""
average.py — figures for Chapter 13 (Average).

average-level    : uneven bars levelled off to one common height
average-formula  : the three-way sum / count / average triangle
average-shift    : what happens to the average when one member joins
replace-member   : swapping one value changes the average by (new-old)/n
weighted-average : two groups combined, the result leans to the bigger group
harmonic-speed   : equal distance at two speeds, why it is not the plain mean
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


def _vals(spec, key="values", default="12,18,24,30,36"):
    return [float(v) for v in str(spec.get(key, default)).split(",")
            if v.strip()]


def _fmt(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ─────────────────────────── levelling the bars ─────────────────────────────
def average_level(spec):
    vals = _vals(spec)
    n = len(vals)
    avg = sum(vals) / n
    top = max(vals)

    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 1301))
    cv.text(W / 2, 20, "pour the tall ones into the short ones",
            size=10.6, weight=700, color=C["soft"])

    plot = 118
    base = 176
    slot = (W - 96) / n
    bw = min(slot - 14, 46)

    for i, v in enumerate(vals):
        x = 48 + i * slot + (slot - bw) / 2
        h = v / top * plot
        # the part below the average stays, the part above is the surplus
        ha = min(v, avg) / top * plot
        cv.raw(f'<rect x="{x}" y="{base-ha:.1f}" width="{bw}" '
               f'height="{ha:.1f}" rx="3" fill="{C["blue_bg"]}" '
               f'stroke="{C["blue"]}" stroke-width="1.3"/>')
        if v > avg:
            cv.raw(f'<rect x="{x}" y="{base-h:.1f}" width="{bw}" '
                   f'height="{(h-ha):.1f}" rx="3" fill="{C["green_bg"]}" '
                   f'stroke="{C["green"]}" stroke-width="1.3"/>')
        elif v < avg:
            cv.raw(f'<rect x="{x}" y="{base-avg/top*plot:.1f}" width="{bw}" '
                   f'height="{(avg-v)/top*plot:.1f}" rx="3" fill="none" '
                   f'stroke="{C["red"]}" stroke-width="1.2" '
                   f'stroke-dasharray="4 3"/>')
        cv.text(x + bw / 2, base - h - 6, _fmt(v), size=9, weight=700,
                color=C["ink"])
        cv.text(x + bw / 2, base + 15, f"T{i+1}", size=7.8, color=C["soft"])

    cv.line(36, base, W - 30, base, color=C["ink"], w=1.5)

    ay = base - avg / top * plot
    cv.line(36, ay, W - 30, ay, color=C["red"], w=1.7, dash="6 4")
    cv.text(W - 26, ay - 6, f"average {_fmt(avg)}", size=9.4, anchor="end",
            weight=700, color=C["red"])

    _card(cv, 40, 198, 178, 30, C["green"], C["green_bg"], sw=1.4)
    cv.text(129, 218, "surplus above the line", size=9.2, weight=700,
            color=C["green"])
    _card(cv, 234, 198, 178, 30, C["red"], C["red_bg"], sw=1.4)
    cv.text(323, 218, "deficit below the line", size=9.2, weight=700,
            color=C["red"])
    cv.text(W / 2, H - 6, "surplus and deficit always cancel exactly",
            size=8.6, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── the three-way relation ─────────────────────────
def average_formula(spec):
    total = float(spec.get("total", 120))
    n = float(spec.get("count", 5))
    avg = total / n

    W, H = 400, 236
    cv = Canvas(W, H, seed=_seed(spec, 1302))
    cv.text(W / 2, 20, "know any two, the third follows", size=10.6,
            weight=700, color=C["soft"])

    tri = [(W / 2, 44), (72, 150), (W - 72, 150)]
    cv.polygon(tri, color=C["grey"], w=1.4, fill=C["paper"])

    labels = [("TOTAL", _fmt(total), C["blue"], C["blue_bg"]),
              ("COUNT", _fmt(n), C["green"], C["green_bg"]),
              ("AVERAGE", _fmt(avg), C["red"], C["red_bg"])]
    for (px, py), (lab, val, col, bg) in zip(tri, labels):
        _card(cv, px - 56, py - 20, 112, 40, col, bg, sw=1.7)
        cv.text(px, py - 4, lab, size=8.4, weight=700, color=C["soft"])
        cv.text(px, py + 13, val, size=13, weight=700, color=col)

    _card(cv, 26, 196, 116, 30, C["red"], "#ffffff", r=5, sw=1.3)
    cv.text(84, 216, "avg = total / n", size=9.4, weight=700, color=C["red"])
    _card(cv, 148, 196, 116, 30, C["blue"], "#ffffff", r=5, sw=1.3)
    cv.text(206, 216, "total = avg x n", size=9.4, weight=700,
            color=C["blue"])
    _card(cv, 270, 196, 116, 30, C["green"], "#ffffff", r=5, sw=1.3)
    cv.text(328, 216, "n = total / avg", size=9.4, weight=700,
            color=C["green"])
    return cv.svg()


# ─────────────────────────── a new member joins ─────────────────────────────
def average_shift(spec):
    n = int(spec.get("count", 10))
    old = float(spec.get("old", 40))
    new_avg = float(spec.get("new_avg", 41))
    joiner = (n + 1) * new_avg - n * old
    d = new_avg - old

    W, H = 452, 226
    cv = Canvas(W, H, seed=_seed(spec, 1303))
    cv.text(W / 2, 20, "one new member pulls the whole average",
            size=10.6, weight=700, color=C["soft"])

    _card(cv, 34, 40, 172, 62, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(120, 62, f"{n} members", size=9.4, color=C["soft"])
    cv.text(120, 84, f"average {_fmt(old)}", size=12.5, weight=700,
            color=C["blue"])

    cv.arrow(212, 71, 244, 71, color=C["grey"], w=1.4)
    _card(cv, 248, 40, 172, 62, C["green"], C["green_bg"], sw=1.6)
    cv.text(334, 62, f"{n+1} members", size=9.4, color=C["soft"])
    cv.text(334, 84, f"average {_fmt(new_avg)}", size=12.5, weight=700,
            color=C["green"])

    cv.text(226, 62, "+1", size=9.4, weight=700, color=C["amber"])

    _card(cv, 56, 118, 340, 34, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 140, f"each of the {n} old members also gained "
            f"{_fmt(d)}", size=10, weight=700, color=C["amber"])

    _card(cv, 56, 160, 340, 30, C["ink"], "#f2f3f7", sw=1.4)
    cv.text(226, 180, f"so the joiner carries {_fmt(new_avg)} + "
            f"{n} x {_fmt(d)} = {_fmt(joiner)}", size=10, weight=700,
            color=C["ink"])

    _card(cv, (W - 260) / 2, 196, 260, 26, C["red"], C["red_bg"], sw=1.6)
    cv.text(W / 2, 214, f"new member = {_fmt(joiner)}", size=11.5,
            weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── one value replaced ─────────────────────────────
def replace_member(spec):
    n = int(spec.get("count", 8))
    out = float(spec.get("out", 65))
    d = float(spec.get("change", 2))
    inn = out + n * d

    W, H = 452, 214
    cv = Canvas(W, H, seed=_seed(spec, 1304))
    cv.text(W / 2, 20, f"one of the {n} is swapped, the count never changes",
            size=10.4, weight=700, color=C["soft"])

    box, gap = 34, 8
    x0 = (W - (n * box + (n - 1) * gap)) / 2
    y = 44
    for i in range(n):
        x = x0 + i * (box + gap)
        last = (i == n - 1)
        col = C["red"] if last else C["blue"]
        bg = C["red_bg"] if last else C["blue_bg"]
        _card(cv, x, y, box, box, col, bg, r=4, sw=1.8 if last else 1.2)
        if last:
            cv.line(x + 5, y + 5, x + box - 5, y + box - 5, color=C["red"],
                    w=1.6)

    lx = x0 + (n - 1) * (box + gap) + box / 2
    cv.arrow(lx, y + box + 4, lx, y + box + 22, color=C["green"], w=1.4)
    _card(cv, lx - 34, y + box + 24, 68, 26, C["green"], C["green_bg"], r=5,
          sw=1.5)
    cv.text(lx, y + box + 42, _fmt(inn), size=11, weight=700,
            color=C["green"])

    _card(cv, 30, 130, 190, 32, C["red"], C["red_bg"], sw=1.4)
    cv.text(125, 151, f"leaves: {_fmt(out)}", size=10.4, weight=700,
            color=C["red"])
    _card(cv, 234, 130, 190, 32, C["green"], C["green_bg"], sw=1.4)
    cv.text(329, 151, f"joins: {_fmt(inn)}", size=10.4, weight=700,
            color=C["green"])

    _card(cv, (W - 340) / 2, 172, 340, 30, C["purple"], C["purple_bg"],
          sw=1.7)
    cv.text(W / 2, 192, f"new = old + n x (change) = {_fmt(out)} + {n} x "
            f"{_fmt(d)} = {_fmt(inn)}", size=10.2, weight=700,
            color=C["purple"])
    return cv.svg()


# ─────────────────────────── two groups combined ────────────────────────────
def weighted_average(spec):
    n1 = float(spec.get("n1", 30))
    a1 = float(spec.get("a1", 42))
    n2 = float(spec.get("n2", 20))
    a2 = float(spec.get("a2", 36))
    comb = (n1 * a1 + n2 * a2) / (n1 + n2)

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 1305))
    cv.text(W / 2, 20, "the answer leans towards the bigger group",
            size=10.6, weight=700, color=C["soft"])

    lo, hi = min(a1, a2), max(a1, a2)
    pad = (hi - lo) * 0.35 if hi > lo else 1
    lo, hi = lo - pad, hi + pad
    x0, x1 = 60, W - 60
    y = 116

    def sx(v):
        return x0 + (v - lo) / (hi - lo) * (x1 - x0)

    cv.line(x0 - 10, y, x1 + 10, y, color=C["ink"], w=1.6)

    for v, nn, col, bg, lab in ((a1, n1, C["blue"], C["blue_bg"], "group A"),
                                (a2, n2, C["green"], C["green_bg"], "group B")):
        px = sx(v)
        r = 12 + 16 * (nn / max(n1, n2))
        cv.circle(px, y, r, color=col, fill=bg, w=1.7)
        cv.text(px, y + 5, _fmt(nn), size=11, weight=700, color=col)
        cv.text(px, y - r - 10, f"{lab}, avg {_fmt(v)}", size=8.8,
                weight=700, color=col)

    pc = sx(comb)
    cv.line(pc, y - 46, pc, y + 40, color=C["red"], w=1.8, dash="5 3")
    cv.dot(pc, y, r=4.4, color=C["red"])
    _card(cv, pc - 58, y + 42, 116, 26, C["red"], "#ffffff", r=5, sw=1.5)
    cv.text(pc, y + 60, f"combined {_fmt(comb)}", size=9.6, weight=700,
            color=C["red"])

    _card(cv, 40, 194, 372, 32, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 215, f"({_fmt(n1)} x {_fmt(a1)} + {_fmt(n2)} x {_fmt(a2)}) "
            f"/ {_fmt(n1+n2)} = {_fmt(comb)}", size=10.2, weight=700,
            color=C["amber"])
    cv.text(W / 2, H - 10, "never take the plain average of two averages",
            size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── average speed ──────────────────────────────────
def harmonic_speed(spec):
    u = float(spec.get("u", 40))
    v = float(spec.get("v", 60))
    hm = 2 * u * v / (u + v)
    am = (u + v) / 2
    d = float(spec.get("distance", 120))

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 1306))
    cv.text(W / 2, 20, "same distance each way, but not the same time",
            size=10.6, weight=700, color=C["soft"])

    y1, y2 = 46, 92
    bx, bw = 92, 250
    for y, sp, col, bg, lab in ((y1, u, C["blue"], C["blue_bg"], "going"),
                                (y2, v, C["green"], C["green_bg"], "coming")):
        _card(cv, bx, y, bw, 32, col, bg, r=5, sw=1.5)
        cv.text(bx + bw / 2, y + 21, f"{_fmt(d)} km at {_fmt(sp)} kmph",
                size=10, weight=700, color=col)
        cv.text(bx - 10, y + 21, lab, size=9, anchor="end", weight=700,
                color=C["ink"])
        cv.text(bx + bw + 10, y + 21, f"{_fmt(d/sp)} h", size=9.4,
                anchor="start", weight=700, color=C["soft"])

    _card(cv, 60, 138, 168, 32, C["red"], C["red_bg"], sw=1.5)
    cv.text(144, 159, f"plain mean {_fmt(am)}", size=10, weight=700,
            color=C["red"])
    cv.line(74, 159, 214, 159, color=C["red"], w=1.5)

    _card(cv, 240, 138, 168, 32, C["green"], C["green_bg"], sw=1.7)
    cv.text(324, 159, f"correct {_fmt(hm)}", size=10.4, weight=700,
            color=C["green"])

    _card(cv, 40, 180, 372, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 200, f"total {_fmt(2*d)} km in {_fmt(d/u + d/v)} h  =  "
            f"{_fmt(hm)} kmph", size=10.2, weight=700, color=C["purple"])

    cv.text(W / 2, 226, f"average speed = 2uv / (u + v)", size=10.6,
            weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "more time is spent at the slower speed, "
            "so the answer sits below the middle", size=8.4, color=C["soft"])
    return cv.svg()


REGISTRY = {
    "average-level": average_level,
    "average-formula": average_formula,
    "average-shift": average_shift,
    "replace-member": replace_member,
    "weighted-average": weighted_average,
    "harmonic-speed": harmonic_speed,
}
