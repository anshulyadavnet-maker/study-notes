"""
cyclic.py — figures for Chapter 9 (Unit Digit, Remainder & Cyclicity).

cycle-wheel      : the unit-digit cycle of one base drawn as a ring
cyclicity-table  : all ten digits with their cycle length
power-steps      : exponent -> divide by 4 -> remainder -> pick the digit
remainder-clock  : modulo arithmetic drawn as a clock face
negative-rem     : a remainder close to the divisor shown as a short backward step
successive-div   : the successive-division staircase, read back upward
"""
import math
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


def _cycle_of(d):
    seen, out = {}, []
    v = d % 10
    for p in range(1, 5):
        u = pow(d, p, 10)
        if u in seen:
            break
        seen[u] = p
        out.append(u)
    return out


# ─────────────────────────── one base as a wheel ────────────────────────────
def cycle_wheel(spec):
    base = int(spec.get("base", 2))
    cyc = _cycle_of(base)
    n = len(cyc)

    W, H = 320, 318
    cv = Canvas(W, H, seed=_seed(spec, 901))
    cx, cy, R = W / 2, 148, 76

    cv.text(W / 2, 22, f"unit digits of {base}, {base}\u00b2, {base}\u00b3, ...",
            size=10.5, weight=700, color=C["soft"])

    cols = [C["blue"], C["green"], C["amber"], C["red"]]
    pts = []
    for i in range(n):
        a = -math.pi / 2 + 2 * math.pi * i / n
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        pts.append((x, y))

    # connecting arcs
    for i in range(n):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % n]
        cv.arrow(x1 + (x2 - x1) * 0.26, y1 + (y2 - y1) * 0.26,
                 x1 + (x2 - x1) * 0.74, y1 + (y2 - y1) * 0.74,
                 color=C["grey"], w=1.3)

    for i, (x, y) in enumerate(pts):
        col = cols[i % len(cols)]
        cv.circle(x, y, 22, color=col, fill=C["paper"], w=1.8)
        cv.text(x, y + 6, str(cyc[i]), size=17, weight=700, color=col)
        ox = cx + (R + 34) * math.cos(-math.pi / 2 + 2 * math.pi * i / n)
        oy = cy + (R + 34) * math.sin(-math.pi / 2 + 2 * math.pi * i / n)
        cv.text(ox, oy + 4, f"{base}^{i+1}", size=8.6, color=C["soft"])

    _card(cv, (W - 200) / 2, H - 34, 200, 28, C["purple"], C["purple_bg"],
          sw=1.6)
    cv.text(W / 2, H - 14, f"cycle length = {n}", size=11.5, weight=700,
            color=C["purple"])
    return cv.svg()


# ─────────────────────────── all ten digits ─────────────────────────────────
def cyclicity_table(spec):
    W, H = 452, 226
    cv = Canvas(W, H, seed=_seed(spec, 902))
    cv.text(W / 2, 16, "every base repeats after at most four steps",
            size=10.2, weight=700, color=C["soft"])

    cw = 38
    x0 = W - 10 * cw - 18
    heads = ["power 1", "power 2", "power 3", "power 4"]
    for r, lab in enumerate(heads):
        cv.text(x0 - 8, 60 + r * 26, lab, size=8.4, anchor="end",
                color=C["soft"])
    cv.text(x0 - 8, 42, "digit", size=8.4, anchor="end", weight=700,
            color=C["ink"])
    cv.text(x0 - 8, 172, "cycle", size=8.4, anchor="end", weight=700,
            color=C["ink"])

    for d in range(10):
        x = x0 + d * cw
        cyc = _cycle_of(d)
        n = len(cyc)
        col = {1: C["green"], 2: C["amber"], 4: C["blue"]}.get(n, C["ink"])
        bg = {1: C["green_bg"], 2: C["amber_bg"], 4: C["blue_bg"]}.get(n, "#eee")

        _card(cv, x + 2, 28, cw - 4, 20, col, bg, r=4, sw=1.2)
        cv.text(x + cw / 2, 43, str(d), size=11.5, weight=700, color=col)

        for r in range(4):
            u = cyc[r % n]
            fade = (r >= n)
            cv.text(x + cw / 2, 64 + r * 26, str(u), size=12,
                    weight=400 if fade else 700,
                    color=C["grey"] if fade else C["ink"])

        _card(cv, x + 2, 158, cw - 4, 20, col, bg, r=4, sw=1.2)
        cv.text(x + cw / 2, 173, str(n), size=11.5, weight=700, color=col)

    for lab, col, txt in ((0, C["green"], "cycle 1 : 0 1 5 6"),
                          (1, C["amber"], "cycle 2 : 4 9"),
                          (2, C["blue"], "cycle 4 : 2 3 7 8")):
        x = 40 + lab * 128
        _card(cv, x, 190, 120, 24, col, "#ffffff", r=5, sw=1.3)
        cv.text(x + 60, 206, txt, size=8.4, weight=700, color=col)
    return cv.svg()


# ─────────────────────────── the four-step method ───────────────────────────
def power_steps(spec):
    base = int(spec.get("base", 7))
    exp = int(spec.get("exp", 105))
    cyc = _cycle_of(base)
    n = len(cyc)
    r = exp % n
    pick = cyc[(r - 1) % n]

    W, H = 452, 200
    cv = Canvas(W, H, seed=_seed(spec, 903))
    cv.text(W / 2, 20, f"unit digit of {base}^{exp}", size=11.5, weight=700,
            color=C["soft"])

    boxes = [
        (f"cycle of {base}", " , ".join(str(c) for c in cyc), C["blue"], C["blue_bg"]),
        (f"{exp} divided by {n}", f"remainder = {r}", C["amber"], C["amber_bg"]),
        ("pick that position", f"position {r if r else n} -> {pick}", C["green"], C["green_bg"]),
    ]
    bw, gap = 130, 24
    x = (W - (3 * bw + 2 * gap)) / 2
    for i, (title, val, col, bg) in enumerate(boxes):
        bx = x + i * (bw + gap)
        _card(cv, bx, 44, bw, 62, col, bg, sw=1.6)
        cv.text(bx + bw / 2, 66, title, size=8.6, color=C["soft"])
        cv.text(bx + bw / 2, 88, val, size=11, weight=700, color=col)
        if i < 2:
            cv.arrow(bx + bw + 3, 75, bx + bw + gap - 3, 75,
                     color=C["grey"], w=1.4)

    _card(cv, (W - 260) / 2, 122, 260, 32, C["purple"], C["purple_bg"], sw=1.8)
    cv.text(W / 2, 144, f"unit digit of {base}^{exp} = {pick}", size=12.5,
            weight=700, color=C["purple"])

    cv.text(W / 2, H - 14,
            f"remainder 0 means the LAST entry of the cycle, that is {cyc[-1]}",
            size=8.6, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── modulo as a clock ──────────────────────────────
def remainder_clock(spec):
    m = int(spec.get("mod", 7))
    n = int(spec.get("number", 100))
    r = n % m

    W, H = 320, 310
    cv = Canvas(W, H, seed=_seed(spec, 904))
    cx, cy, R = W / 2, 142, 78

    cv.text(W / 2, 20, f"counting in steps of {m}", size=10.5, weight=700,
            color=C["soft"])
    cv.circle(cx, cy, R, color=C["ink"], fill=C["paper"], w=1.7)

    for k in range(m):
        a = -math.pi / 2 + 2 * math.pi * k / m
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        hit = (k == r)
        col = C["red"] if hit else C["soft"]
        cv.dot(x, y, r=5.0 if hit else 3.0, color=col)
        lx, ly = cx + (R + 18) * math.cos(a), cy + (R + 18) * math.sin(a)
        cv.text(lx, ly + 4, str(k), size=10.5 if hit else 9.4,
                weight=700 if hit else 400, color=col)

    a = -math.pi / 2 + 2 * math.pi * r / m
    cv.arrow(cx, cy, cx + (R - 16) * math.cos(a), cy + (R - 16) * math.sin(a),
             color=C["red"], w=2.0)
    cv.dot(cx, cy, r=3.4, color=C["ink"])

    _card(cv, (W - 236) / 2, H - 36, 236, 30, C["red"], C["red_bg"], sw=1.7)
    cv.text(W / 2, H - 15, f"{n} leaves remainder {r} on {m}", size=11,
            weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── negative remainder ─────────────────────────────
def negative_rem(spec):
    m = int(spec.get("mod", 16))
    a = int(spec.get("base", 15))
    e = int(spec.get("exp", 23))
    short = a - m                     # e.g. -1

    W, H = 452, 194
    cv = Canvas(W, H, seed=_seed(spec, 905))
    y = 96
    cv.line(40, y, W - 40, y, color=C["ink"], w=1.6)
    cv.arrow(W - 54, y, W - 34, y, color=C["ink"], w=1.4)

    for k, val in enumerate([0, a, m]):
        x = 60 + k * (W - 150) / 2
        cv.line(x, y - 8, x, y + 8, color=C["ink"], w=1.4)
        cv.text(x, y + 24, str(val), size=11, weight=700, color=C["ink"])

    xa = 60 + (W - 150) / 2
    xm = 60 + (W - 150)
    cv.dot(xa, y, r=4.6, color=C["red"])
    cv.arrow(xa, y - 16, xm, y - 16, color=C["green"], w=1.4)
    cv.text((xa + xm) / 2, y - 24, f"only {m - a} short of {m}", size=9,
            weight=700, color=C["green"])

    _card(cv, 40, 20, 174, 32, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(127, 41, f"{a} = {m} - {m-a}", size=11, weight=700, color=C["blue"])
    _card(cv, 238, 20, 174, 32, C["red"], C["red_bg"], sw=1.5)
    cv.text(325, 41, f"so treat {a} as {short}", size=11, weight=700,
            color=C["red"])

    res = pow(a, e, m)
    sign = "+1" if e % 2 == 0 else "-1"
    _card(cv, (W - 330) / 2, H - 54, 330, 34, C["purple"], C["purple_bg"],
          sw=1.7)
    cv.text(W / 2, H - 32,
            f"({short})^{e} = {sign}  ->  {a}^{e} leaves {res} on {m}",
            size=10.5, weight=700, color=C["purple"])
    return cv.svg()


# ─────────────────────────── successive division ────────────────────────────
def successive_div(spec):
    """spec: divisors '5,4' and rems '3,2' -> smallest N."""
    divs = [int(v) for v in str(spec.get("divisors", "5,4")).split(",")]
    rems = [int(v) for v in str(spec.get("remainders", "3,2")).split(",")]

    # build upward: start from quotient 0 at the deepest step
    q = 0
    steps = []
    for d, r in zip(reversed(divs), reversed(rems)):
        n = d * q + r
        steps.append((d, q, r, n))
        q = n
    answer = steps[-1][3]

    W = 452
    H = 60 + len(steps) * 54 + 44
    cv = Canvas(W, H, seed=_seed(spec, 906))
    cv.text(W / 2, 20, "successive division: build the number back upward",
            size=10, weight=700, color=C["soft"])

    for i, (d, qq, r, n) in enumerate(steps):
        y = 36 + i * 54
        _card(cv, 30, y, 120, 40, C["blue"], C["blue_bg"], sw=1.4)
        cv.text(90, y + 18, f"divisor {d}", size=9, color=C["soft"])
        cv.text(90, y + 33, f"remainder {r}", size=10, weight=700,
                color=C["blue"])

        cv.arrow(154, y + 20, 190, y + 20, color=C["grey"], w=1.2)

        _card(cv, 194, y, 148, 40, C["amber"], C["amber_bg"], sw=1.4)
        cv.text(268, y + 26, f"{d} x {qq} + {r}", size=11.5, weight=700,
                color=C["amber"])

        cv.arrow(346, y + 20, 376, y + 20, color=C["grey"], w=1.2)

        _card(cv, 380, y, 60, 40, C["green"], C["green_bg"], sw=1.4)
        cv.text(410, y + 26, str(n), size=13, weight=700, color=C["green"])

        if i + 1 < len(steps):
            cv.raw(f'<path d="M410 {y+42} L410 {y+48} L268 {y+48} L268 {y+54}" '
                   f'fill="none" stroke="{C["grey"]}" stroke-width="1.1" '
                   f'stroke-dasharray="3 3"/>')
            cv.text(300, y + 46, "this becomes the next quotient", size=7.4,
                    anchor="start", color=C["soft"])

    _card(cv, (W - 270) / 2, H - 40, 270, 30, C["purple"], C["purple_bg"],
          sw=1.7)
    cv.text(W / 2, H - 19, f"smallest such number = {answer}", size=11.5,
            weight=700, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "cycle-wheel": cycle_wheel,
    "cyclicity-table": cyclicity_table,
    "power-steps": power_steps,
    "remainder-clock": remainder_clock,
    "negative-rem": negative_rem,
    "successive-div": successive_div,
}
