"""
partner.py — figures for Chapter 18 (Partnership).

capital-share    : equal-time partnership, profit split straight by capital
capital-time     : the capital x time rectangles, area is what counts
join-later       : one partner enters after some months, shown on a timeline
withdraw-mid     : capital changes midway, the area splits into two blocks
working-sleeping : management share taken off the top, the rest split
profit-flow      : the four-step route from capitals to each partner's share
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


def _nums(spec, key, default):
    return [float(v) for v in str(spec.get(key, default)).split(",")
            if v.strip()]


COLS = [C["blue"], C["green"], C["amber"], C["purple"]]
BGS = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["purple_bg"]]
NAMES = ["A", "B", "C", "D"]


# ─────────────────────────── same time, split by capital ────────────────────
def capital_share(spec):
    caps = _nums(spec, "capitals", "5000,6000,9000")
    profit = float(spec.get("profit", 4000))
    tot = sum(caps)
    g = 0
    for c in caps:
        g = math.gcd(int(g), int(c))
    parts = [int(c // g) for c in caps]

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 1801))
    cv.text(W / 2, 20, "same time for everyone, so capital alone decides",
            size=10.4, weight=700, color=C["soft"])

    bx, bw = 40, W - 80

    # capital bar
    x = bx
    for i, c in enumerate(caps):
        w = bw * c / tot
        _card(cv, x, 44, w, 34, COLS[i % 4], BGS[i % 4], r=4, sw=1.5)
        cv.text(x + w / 2, 66, _fmt(c), size=10.4, weight=700,
                color=COLS[i % 4])
        cv.text(x + w / 2, 92, NAMES[i], size=10, weight=700, color=C["ink"])
        x += w
    cv.text(bx - 8, 66, "capital", size=8.6, anchor="end", weight=700,
            color=C["soft"])

    # profit bar, exactly the same proportions
    x = bx
    for i, c in enumerate(caps):
        w = bw * c / tot
        share = profit * c / tot
        _card(cv, x, 112, w, 34, COLS[i % 4], BGS[i % 4], r=4, sw=1.5)
        cv.text(x + w / 2, 134, _fmt(share), size=10.4, weight=700,
                color=COLS[i % 4])
        x += w
    cv.text(bx - 8, 134, "profit", size=8.6, anchor="end", weight=700,
            color=C["soft"])

    for i in range(len(caps) - 1):
        cx = bx + bw * sum(caps[:i + 1]) / tot
        cv.line(cx, 80, cx, 110, color=C["grey"], w=1.0, dash="3 3")

    _card(cv, 46, 166, 360, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(226, 186, f"profit ratio = capital ratio = "
            f"{' : '.join(str(p) for p in parts)}", size=10.4, weight=700,
            color=C["red"])
    cv.text(W / 2, 214, f"total profit {_fmt(profit)} split into "
            f"{sum(parts)} equal parts", size=9.2, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "the two bars are cut at exactly the same places",
            size=8.6, color=C["soft"])
    return cv.svg()


# ─────────────────────────── capital x time as area ─────────────────────────
def capital_time(spec):
    caps = _nums(spec, "capitals", "5000,6000,8000")
    times = _nums(spec, "months", "12,8,6")
    prods = [c * t for c, t in zip(caps, times)]
    g = 0
    for m in prods:
        g = math.gcd(int(g), int(m))
    parts = [int(m // g) for m in prods]

    W, H = 452, 272
    cv = Canvas(W, H, seed=_seed(spec, 1802))
    cv.text(W / 2, 20, "money x months, the area is what counts",
            size=10.6, weight=700, color=C["soft"])

    maxc = max(caps)
    maxt = max(times)
    hmax = 96
    wunit = 86 / maxt
    base = 168
    gap = 24
    xs = 66

    for i, (c, t) in enumerate(zip(caps, times)):
        h = c / maxc * hmax
        w = t * wunit
        cv.raw(f'<rect x="{xs}" y="{base-h:.1f}" width="{w:.1f}" '
               f'height="{h:.1f}" rx="3" fill="{BGS[i%4]}" '
               f'stroke="{COLS[i%4]}" stroke-width="1.5"/>')
        cv.text(xs + w / 2, base - h / 2 + 4, _fmt(prods[i]), size=8.6,
                weight=700, color=COLS[i % 4])
        cv.text(xs + w / 2, base + 14, f"{_fmt(t)} mo", size=8,
                color=C["soft"])
        cv.text(xs + w / 2, base - h - 8, _fmt(c), size=8.4, weight=700,
                color=COLS[i % 4])
        cv.text(xs + w / 2, base + 30, NAMES[i], size=10, weight=700,
                color=C["ink"])
        xs += w + gap

    cv.line(54, base, W - 30, base, color=C["ink"], w=1.5)

    _card(cv, 46, 208, 360, 30, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 228, "ratio = " + " : ".join(str(p) for p in parts),
            size=11, weight=700, color=C["amber"])
    cv.text(W / 2, 254, "a small sum for long can beat a big sum for short",
            size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── one partner joins later ────────────────────────
def join_later(spec):
    ca = float(spec.get("ca", 9000))
    cb = float(spec.get("cb", 12000))
    join = int(spec.get("join", 6))
    total = int(spec.get("total", 12))
    ma = ca * total
    mb = cb * (total - join)
    g = math.gcd(int(ma), int(mb))

    W, H = 452, 234
    cv = Canvas(W, H, seed=_seed(spec, 1803))
    cv.text(W / 2, 20, "count only the months each rupee actually stayed",
            size=10.4, weight=700, color=C["soft"])

    ox, ow = 74, 300
    mu = ow / total

    for m in range(total + 1):
        x = ox + m * mu
        if m % 2 == 0:
            cv.line(x, 40, x, 132, color=C["grey"], w=0.6, dash="2 3")
            cv.text(x, 148, str(m), size=7.6, color=C["soft"])
    cv.text(ox + ow / 2, 164, "months", size=8.6, color=C["soft"])

    _card(cv, ox, 46, ow, 32, C["blue"], C["blue_bg"], r=4, sw=1.5)
    cv.text(ox + ow / 2, 66, f"{_fmt(ca)} for {total} months", size=9.6,
            weight=700, color=C["blue"])
    cv.text(ox - 10, 66, "A", size=10.4, anchor="end", weight=700,
            color=C["blue"])

    bx = ox + join * mu
    _card(cv, bx, 92, ow - join * mu, 32, C["green"], C["green_bg"], r=4,
          sw=1.5)
    cv.text(bx + (ow - join * mu) / 2, 112,
            f"{_fmt(cb)} for {total-join} months", size=9.6, weight=700,
            color=C["green"])
    cv.text(ox - 10, 112, "B", size=10.4, anchor="end", weight=700,
            color=C["green"])
    cv.raw(f'<rect x="{ox}" y="92" width="{join*mu}" height="32" rx="4" '
           f'fill="none" stroke="{C["grey"]}" stroke-width="1.1" '
           f'stroke-dasharray="4 3"/>')
    cv.text(ox + join * mu / 2, 112, "not in yet", size=8, color=C["grey"])

    _card(cv, 40, 178, 178, 30, C["blue"], C["blue_bg"], sw=1.4)
    cv.text(129, 198, f"A: {_fmt(ca)} x {total} = {_fmt(ma)}", size=9.2,
            weight=700, color=C["blue"])
    _card(cv, 234, 178, 178, 30, C["green"], C["green_bg"], sw=1.4)
    cv.text(323, 198, f"B: {_fmt(cb)} x {total-join} = {_fmt(mb)}",
            size=9.2, weight=700, color=C["green"])

    cv.text(W / 2, 224, f"ratio = {int(ma//g)} : {int(mb//g)}", size=10.6,
            weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── capital changes midway ─────────────────────────
def withdraw_mid(spec):
    c1 = float(spec.get("c1", 6000))
    c2 = float(spec.get("c2", 4000))
    switch = int(spec.get("switch", 6))
    total = int(spec.get("total", 12))
    cb = float(spec.get("cb", 8000))

    ma = c1 * switch + c2 * (total - switch)
    mb = cb * total
    g = math.gcd(int(ma), int(mb))

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 1804))
    cv.text(W / 2, 20, "capital changed, so add the two blocks separately",
            size=10.4, weight=700, color=C["soft"])

    ox, ow = 74, 300
    mu = ow / total
    base = 132
    hmax = 76
    top = max(c1, c2, cb)

    # A, two blocks
    h1 = c1 / top * hmax
    h2 = c2 / top * hmax
    cv.raw(f'<rect x="{ox}" y="{base-h1:.1f}" width="{switch*mu:.1f}" '
           f'height="{h1:.1f}" rx="3" fill="{C["blue_bg"]}" '
           f'stroke="{C["blue"]}" stroke-width="1.5"/>')
    cv.text(ox + switch * mu / 2, base - h1 / 2 + 4, _fmt(c1), size=9,
            weight=700, color=C["blue"])
    cv.raw(f'<rect x="{ox+switch*mu:.1f}" y="{base-h2:.1f}" '
           f'width="{(total-switch)*mu:.1f}" height="{h2:.1f}" rx="3" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.5"/>')
    cv.text(ox + switch * mu + (total - switch) * mu / 2, base - h2 / 2 + 4,
            _fmt(c2), size=9, weight=700, color=C["blue"])

    cv.line(ox + switch * mu, base - h1 - 8, ox + switch * mu, base + 6,
            color=C["red"], w=1.5, dash="3 3")
    cv.text(ox + switch * mu, base - h1 - 13, f"month {switch}", size=8,
            weight=700, color=C["red"])

    cv.line(60, base, W - 30, base, color=C["ink"], w=1.5)
    cv.text(ox - 10, base - h1 / 2, "A", size=10.4, anchor="end",
            weight=700, color=C["blue"])
    for m in (0, switch, total):
        cv.text(ox + m * mu, base + 15, str(m), size=7.8, color=C["soft"])

    rows = [(f"A: {_fmt(c1)} x {switch} + {_fmt(c2)} x {total-switch}",
             _fmt(ma), C["blue"]),
            (f"B: {_fmt(cb)} x {total}", _fmt(mb), C["green"])]
    for i, (lab, val, col) in enumerate(rows):
        y = 160 + i * 28
        _card(cv, 40, y, 372, 24, col, "#ffffff", r=5, sw=1.2)
        cv.text(52, y + 16, lab, size=8.8, anchor="start", color=C["soft"])
        cv.text(400, y + 16, val, size=9.4, anchor="end", weight=700,
                color=col)

    cv.text(W / 2, 230, f"ratio = {int(ma//g)} : {int(mb//g)}", size=11,
            weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── working vs sleeping ────────────────────────────
def working_sleeping(spec):
    total = float(spec.get("profit", 8400))
    pct = float(spec.get("pct", 20))
    r1 = int(spec.get("r1", 3))
    r2 = int(spec.get("r2", 4))
    mg = total * pct / 100
    rest = total - mg
    s1 = rest * r1 / (r1 + r2)
    s2 = rest * r2 / (r1 + r2)

    W, H = 452, 256
    cv = Canvas(W, H, seed=_seed(spec, 1805))
    cv.text(W / 2, 20, "management fee comes off the top, first",
            size=10.6, weight=700, color=C["soft"])

    bx, bw = 48, W - 96
    _card(cv, bx, 42, bw, 30, C["ink"], "#f2f3f7", r=4, sw=1.5)
    cv.text(bx + bw / 2, 62, f"total profit {_fmt(total)}", size=10.4,
            weight=700, color=C["ink"])

    mw = bw * pct / 100
    _card(cv, bx, 88, mw, 34, C["red"], C["red_bg"], r=4, sw=1.6)
    cv.text(bx + mw / 2, 109, _fmt(mg), size=10, weight=700, color=C["red"])
    _card(cv, bx + mw, 88, bw - mw, 34, C["ink"], "#ffffff", r=4, sw=1.4)
    cv.text(bx + mw + (bw - mw) / 2, 109, f"rest {_fmt(rest)}", size=10,
            weight=700, color=C["ink"])
    cv.text(bx + mw / 2, 82, f"{_fmt(pct)}% for managing", size=7.6,
            weight=700, color=C["red"])

    rw = bw - mw
    w1 = rw * r1 / (r1 + r2)
    _card(cv, bx + mw, 132, w1, 34, C["blue"], C["blue_bg"], r=4, sw=1.5)
    cv.text(bx + mw + w1 / 2, 153, _fmt(s1), size=10, weight=700,
            color=C["blue"])
    _card(cv, bx + mw + w1, 132, rw - w1, 34, C["green"], C["green_bg"],
          r=4, sw=1.5)
    cv.text(bx + mw + w1 + (rw - w1) / 2, 153, _fmt(s2), size=10,
            weight=700, color=C["green"])
    cv.text(bx + mw + rw / 2, 172, f"capital ratio {r1} : {r2}", size=7.8,
            weight=700, color=C["soft"])

    _card(cv, 40, 192, 178, 32, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(129, 213, f"working: {_fmt(mg)} + {_fmt(s1)} = {_fmt(mg+s1)}",
            size=8.8, weight=700, color=C["blue"])
    _card(cv, 234, 192, 178, 32, C["green"], C["green_bg"], sw=1.5)
    cv.text(323, 213, f"sleeping: {_fmt(s2)}", size=9.4, weight=700,
            color=C["green"])
    cv.text(W / 2, 244, "only what is left after the fee follows the ratio",
            size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── the four-step route ────────────────────────────
def profit_flow(spec):
    W, H = 452, 200
    cv = Canvas(W, H, seed=_seed(spec, 1806))
    cv.text(W / 2, 20, "every partnership question walks this same road",
            size=10.4, weight=700, color=C["soft"])

    steps = [("capital x months", "for each partner", C["blue"], C["blue_bg"]),
             ("simplify the ratio", "divide by the HCF", C["green"],
              C["green_bg"]),
             ("count total parts", "add the ratio terms", C["amber"],
              C["amber_bg"]),
             ("one part x his terms", "that is his share", C["red"],
              C["red_bg"])]

    bw, gap = 98, 16
    x0 = (W - (4 * bw + 3 * gap)) / 2
    for i, (top, bot, col, bg) in enumerate(steps):
        x = x0 + i * (bw + gap)
        _card(cv, x, 46, bw, 62, col, bg, sw=1.6)
        cv.raw(f'<circle cx="{x+bw/2}" cy="{62}" r="11" fill="{col}"/>')
        cv.text(x + bw / 2, 66, str(i + 1), size=11, weight=700,
                color="#ffffff")
        cv.text(x + bw / 2, 88, top, size=8, weight=700, color=col)
        cv.text(x + bw / 2, 100, bot, size=7, color=C["soft"])
        if i < 3:
            cv.arrow(x + bw + 2, 77, x + bw + gap - 2, 77, color=C["grey"],
                     w=1.2)

    _card(cv, 46, 126, 360, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 146, "share = total profit x (his parts / total parts)",
            size=10.2, weight=700, color=C["purple"])
    cv.text(W / 2, 176, "if everyone stays the same months, step 1 is just "
            "the capitals", size=8.8, weight=700, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "capital-share": capital_share,
    "capital-time": capital_time,
    "join-later": join_later,
    "withdraw-mid": withdraw_mid,
    "working-sleeping": working_sleeping,
    "profit-flow": profit_flow,
}
