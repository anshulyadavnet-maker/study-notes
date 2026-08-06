"""
roots.py — figures for Chapter 7 (Square & Cube Roots).

square-dots     : 1, 4, 9, 16 drawn as literal square dot-arrays
sqrt-pairing    : how digits are paired from the decimal point outward
sqrt-longdiv    : the full long-division staircase for a chosen number
unit-square-map : unit digit -> unit digit of its square (2,3,7,8 impossible)
cuberoot-split  : the 3-digit split trick for cube roots
root-adjust     : least number to add / subtract to reach a perfect square
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


# ─────────────────────────── squares as dot arrays ──────────────────────────
def square_dots(spec):
    ns = [int(v) for v in str(spec.get("upto", 5)).split(",")] \
        if "," in str(spec.get("upto", 5)) else list(range(1, int(spec.get("upto", 5)) + 1))
    gap = 11
    pad = 26
    widths = [max(n * gap, 34) + pad for n in ns]
    W = 20 + sum(widths)
    H = 40 + max(ns) * gap + 40
    cv = Canvas(W, H, seed=_seed(spec, 701))
    cols = [C["blue"], C["green"], C["amber"], C["red"], C["purple"], C["teal"]]

    x = 16
    base = H - 46
    for i, n in enumerate(ns):
        col = cols[i % len(cols)]
        side = (n - 1) * gap
        x0 = x + (widths[i] - pad - side) / 2
        y0 = base - side
        if n > 1:
            cv.raw(f'<rect x="{x0-7}" y="{y0-7}" width="{side+14}" '
                   f'height="{side+14}" rx="4" fill="{C["paper"]}" '
                   f'stroke="{col}" stroke-width="1.2" stroke-dasharray="3 3"/>')
        for r in range(n):
            for c in range(n):
                cv.dot(x0 + c * gap, y0 + r * gap, r=3.2, color=col)
        cv.text(x + widths[i] / 2 - pad / 2, base + 22, f"{n}\u00b2 = {n*n}",
                size=10, weight=700, color=col)
        x += widths[i]

    cv.text(W / 2, 20, "a perfect square really is a square",
            size=10.5, weight=700, color=C["soft"])
    cv.text(W / 2, H - 8, "so its root is simply the side of that square",
            size=8.6, color=C["soft"])
    return cv.svg()


# ─────────────────────────── digit pairing ──────────────────────────────────
def sqrt_pairing(spec):
    num = str(spec.get("number", "174.24"))
    ip, _, fp = num.partition(".")
    W, H = 430, 172
    cv = Canvas(W, H, seed=_seed(spec, 702))
    cv.text(W / 2, 20, "pair the digits outward from the decimal point",
            size=10, weight=700, color=C["soft"])

    dw = 26
    total = len(ip) + (1 if fp else 0) + len(fp)
    x0 = (W - total * dw) / 2
    y = 56

    # integer part - pairs from the right
    ipad = ip if len(ip) % 2 == 0 else "0" + ip
    fpad = fp + ("0" if len(fp) % 2 else "") if fp else ""

    xs = []
    x = x0
    for ch in ip:
        _card(cv, x + 2, y, dw - 4, 30, C["ink"], "#ffffff", r=5, sw=1.2)
        cv.text(x + dw / 2, y + 21, ch, size=14, weight=700, color=C["ink"])
        xs.append(x)
        x += dw
    if fp:
        cv.text(x + 6, y + 24, ".", size=18, weight=700, color=C["red"])
        x += 12
        for ch in fp:
            _card(cv, x + 2, y, dw - 4, 30, C["ink"], "#ffffff", r=5, sw=1.2)
            cv.text(x + dw / 2, y + 21, ch, size=14, weight=700, color=C["ink"])
            xs.append(x)
            x += dw

    # brackets under integer pairs (right to left)
    nint = len(ip)
    i = nint
    k = 0
    while i > 0:
        lo = max(i - 2, 0)
        a = xs[lo] + 3
        b = xs[i - 1] + dw - 3
        cv.raw(f'<path d="M{a} {y+36} L{a} {y+44} L{b} {y+44} L{b} {y+36}" '
               f'fill="none" stroke="{C["blue"]}" stroke-width="1.5"/>')
        cv.text((a + b) / 2, y + 58, "pair", size=8, color=C["blue"])
        i -= 2
        k += 1
    if len(ip) % 2:
        cv.text(xs[0] + dw / 2, y - 8, "single", size=7.6, color=C["amber"])

    # brackets over decimal pairs (left to right)
    if fp:
        off = nint
        j = 0
        while j < len(fp):
            a = xs[off + j] + 3
            b = xs[off + min(j + 1, len(fp) - 1)] + dw - 3
            cv.raw(f'<path d="M{a} {y-6} L{a} {y-14} L{b} {y-14} L{b} {y-6}" '
                   f'fill="none" stroke="{C["green"]}" stroke-width="1.5"/>')
            j += 2

    cv.text(W / 2, H - 30,
            "integer side: pair from the RIGHT   |   decimal side: pair from the LEFT",
            size=8.6, weight=700, color=C["ink"])
    cv.text(W / 2, H - 12,
            "number of pairs = number of digits in the root",
            size=8.4, color=C["red"])
    return cv.svg()


# ─────────────────────────── long division staircase ────────────────────────
def sqrt_longdiv(spec):
    num = str(spec.get("number", "15129"))
    ip, _, fp = num.partition(".")
    if len(ip) % 2:
        ip = "0" + ip
    if fp and len(fp) % 2:
        fp = fp + "0"
    pairs = [ip[i:i + 2] for i in range(0, len(ip), 2)] + \
            [fp[i:i + 2] for i in range(0, len(fp), 2)]

    rows, rem, root = [], 0, 0
    for p in pairs:
        cur = rem * 100 + int(p)
        d = 0
        while (root * 20 + d + 1) * (d + 1) <= cur:
            d += 1
        div = root * 20 + d
        rows.append((p, cur, div, d, div * d, cur - div * d))
        rem = cur - div * d
        root = root * 10 + d

    W = 452
    H = 56 + len(rows) * 40 + 40
    cv = Canvas(W, H, seed=_seed(spec, 703))
    cv.text(W / 2, 20, f"long division: square root of {num}",
            size=10.5, weight=700, color=C["soft"])

    hx = [18, 116, 232, 350]
    heads = ["bring down", "working total", "divisor x digit", "remainder"]
    for i, h in enumerate(heads):
        cv.text(hx[i] + 44, 40, h, size=8.2, color=C["soft"])

    for i, (p, cur, div, d, prod, rm) in enumerate(rows):
        y = 48 + i * 40
        _card(cv, hx[0], y, 88, 30, C["grey"], "#ffffff")
        cv.text(hx[0] + 44, y + 20, p, size=11.5, weight=700, color=C["ink"])
        cv.arrow(hx[0] + 92, y + 15, hx[1] - 4, y + 15, color=C["grey"], w=1.1)

        _card(cv, hx[1], y, 106, 30, C["blue"], C["blue_bg"])
        cv.text(hx[1] + 53, y + 20, str(cur), size=11.5, weight=700,
                color=C["blue"])
        cv.arrow(hx[1] + 110, y + 15, hx[2] - 4, y + 15, color=C["grey"], w=1.1)

        _card(cv, hx[2], y, 110, 30, C["amber"], C["amber_bg"])
        cv.text(hx[2] + 55, y + 20, f"{div} x {d} = {prod}", size=10,
                weight=700, color=C["amber"])
        cv.arrow(hx[2] + 114, y + 15, hx[3] - 4, y + 15, color=C["grey"], w=1.1)

        _card(cv, hx[3], y, 84, 30, C["green"] if rm == 0 else C["red"],
              C["green_bg"] if rm == 0 else C["red_bg"])
        cv.text(hx[3] + 42, y + 20, str(rm), size=11.5, weight=700,
                color=C["green"] if rm == 0 else C["red"])

        # root digit badge on the far left margin
        cv.raw(f'<circle cx="{8}" cy="{y+15}" r="0"/>')

    digits = "".join(str(r[3]) for r in rows)
    if fp:
        digits = digits[:len(ip) // 2] + "." + digits[len(ip) // 2:]
    _card(cv, (W - 250) / 2, H - 36, 250, 28, C["purple"], C["purple_bg"],
          sw=1.7)
    cv.text(W / 2, H - 16, f"root = {digits.lstrip('0') or '0'}",
            size=12, weight=700, color=C["purple"])
    return cv.svg()


# ─────────────────────────── unit digit map ─────────────────────────────────
def unit_square_map(spec):
    W, H = 452, 176
    cv = Canvas(W, H, seed=_seed(spec, 704))
    cv.text(W / 2, 20, "unit digit of a number  ->  unit digit of its square",
            size=10, weight=700, color=C["soft"])

    cw = 41
    x0 = (W - 10 * cw) / 2
    for d in range(10):
        x = x0 + d * cw
        _card(cv, x + 2, 32, cw - 4, 28, C["blue"], C["blue_bg"], r=5, sw=1.2)
        cv.text(x + cw / 2, 51, str(d), size=13, weight=700, color=C["blue"])
        cv.arrow(x + cw / 2, 63, x + cw / 2, 80, color=C["grey"], w=1.0)
        u = (d * d) % 10
        _card(cv, x + 2, 82, cw - 4, 28, C["green"], C["green_bg"], r=5, sw=1.2)
        cv.text(x + cw / 2, 101, str(u), size=13, weight=700, color=C["green"])

    _card(cv, 24, 122, W - 48, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(W / 2, 142, "2 , 3 , 7 , 8 never appear -> such a number is NEVER a perfect square",
            size=8.8, weight=700, color=C["red"])
    cv.text(W / 2, H - 8,
            "also note 4 and 6 repeat, so the last digit alone cannot fix the root",
            size=8.2, color=C["soft"])
    return cv.svg()


# ─────────────────────────── cube-root split ────────────────────────────────
def cuberoot_split(spec):
    n = int(spec.get("number", 13824))
    s = str(n)
    last3 = s[-3:]
    rest = s[:-3] or "0"
    root = round(n ** (1 / 3))
    tens = root // 10
    unit = root % 10

    W, H = 452, 226
    cv = Canvas(W, H, seed=_seed(spec, 705))
    cv.text(W / 2, 20, f"cube root of {n}", size=11, weight=700, color=C["soft"])

    # split boxes
    _card(cv, 74, 34, 140, 42, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(144, 62, rest, size=17, weight=700, color=C["blue"])
    cv.text(144, 90, "the left part", size=8.4, color=C["soft"])

    _card(cv, 238, 34, 140, 42, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(308, 62, last3, size=17, weight=700, color=C["amber"])
    cv.text(308, 88, "last 3 digits", size=8.4, color=C["soft"])

    cv.line(226, 30, 226, 96, color=C["red"], w=1.6, dash="4 3")

    # rules
    cv.arrow(144, 100, 144, 126, color=C["grey"], w=1.2)
    _card(cv, 54, 128, 180, 44, C["blue"], "#ffffff", sw=1.3)
    cv.text(144, 146, f"largest cube <= {rest}", size=9, color=C["soft"])
    cv.text(144, 163, f"is {tens}\u00b3 = {tens**3}  ->  tens digit {tens}",
            size=9.4, weight=700, color=C["blue"])

    cv.arrow(308, 100, 308, 126, color=C["grey"], w=1.2)
    _card(cv, 238, 128, 180, 44, C["amber"], "#ffffff", sw=1.3)
    cv.text(328, 146, f"last digit of {last3} is {last3[-1]}", size=9,
            color=C["soft"])
    cv.text(328, 163, f"cube ending in {last3[-1]}  ->  unit digit {unit}",
            size=9.4, weight=700, color=C["amber"])

    _card(cv, 126, 184, 200, 32, C["green"], C["green_bg"], sw=1.7)
    cv.text(226, 206, f"cube root = {tens} | {unit} = {root}", size=12.5,
            weight=700, color=C["green"])
    return cv.svg()


# ─────────────────────────── add / subtract to a square ─────────────────────
def root_adjust(spec):
    n = int(spec.get("number", 5000))
    r = math.isqrt(n)
    lo, hi = r * r, (r + 1) ** 2

    W, H = 452, 172
    cv = Canvas(W, H, seed=_seed(spec, 706))
    y = 88
    cv.line(30, y, W - 30, y, color=C["ink"], w=1.7)
    cv.arrow(W - 44, y, W - 26, y, color=C["ink"], w=1.4)

    px = {lo: 82, n: 82 + (W - 164) * (n - lo) / (hi - lo), hi: W - 82}
    for val, col, lab in ((lo, C["green"], f"{r}\u00b2 = {lo}"),
                          (hi, C["blue"], f"{r+1}\u00b2 = {hi}")):
        x = px[val]
        cv.line(x, y - 9, x, y + 9, color=col, w=1.6)
        _card(cv, x - 48, y + 16, 96, 24, col, "#ffffff", r=5, sw=1.3)
        cv.text(x, y + 32, lab, size=9.6, weight=700, color=col)

    x = px[n]
    cv.dot(x, y, r=4.4, color=C["red"])
    _card(cv, x - 34, y - 44, 68, 24, C["red"], "#ffffff", r=5, sw=1.3)
    cv.text(x, y - 28, f"n = {n}", size=10, weight=700, color=C["red"])

    cv.arrow(x - 4, y - 6, px[lo] + 4, y - 6, color=C["green"], w=1.2)
    cv.text((x + px[lo]) / 2, y - 12, f"subtract {n - lo}", size=8.6,
            weight=700, color=C["green"])
    cv.arrow(x + 4, y - 6, px[hi] - 4, y - 6, color=C["blue"], w=1.2)
    cv.text((x + px[hi]) / 2, y - 12, f"add {hi - n}", size=8.6, weight=700,
            color=C["blue"])

    cv.text(W / 2, 22, "the nearest perfect squares on either side",
            size=10.2, weight=700, color=C["soft"])
    cv.text(W / 2, H - 10,
            f"least subtract = {n - lo}   |   least add = {hi - n}",
            size=9.4, weight=700, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "square-dots": square_dots,
    "sqrt-pairing": sqrt_pairing,
    "sqrt-longdiv": sqrt_longdiv,
    "unit-square-map": unit_square_map,
    "cuberoot-split": cuberoot_split,
    "root-adjust": root_adjust,
}
