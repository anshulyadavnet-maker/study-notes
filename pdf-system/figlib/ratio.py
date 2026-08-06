"""
ratio.py — figures for Chapter 12 (Ratio & Proportion).

ratio-bar        : a total split into ratio parts, each part labelled
ratio-parts      : why a:b means "a parts and b parts", with one part sized
ratio-chain      : a:b and b:c joined into a:b:c by matching the common term
proportion-cross : the cross-multiplication rule drawn as an X
mean-third-prop  : mean / third / fourth proportional on one card row
ratio-change     : adding the same number to both terms moves the ratio
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


def _parts(spec, key="ratio", default="3,4"):
    return [int(v.strip()) for v in str(spec.get(key, default))
            .replace(":", ",").split(",") if v.strip()]


def _fmt(v):
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return f"{v:.2f}".rstrip("0").rstrip(".")


# ─────────────────────────── total split into ratio ─────────────────────────
def ratio_bar(spec):
    parts = _parts(spec)
    total = float(spec.get("total", 1400))
    tp = sum(parts)
    unit = total / tp

    cols = [C["blue"], C["green"], C["amber"], C["red"], C["purple"]]
    bgs = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["red_bg"],
           C["purple_bg"]]

    W, H = 452, 208
    cv = Canvas(W, H, seed=_seed(spec, 1201))
    cv.text(W / 2, 20, f"{_fmt(total)} split in the ratio "
            f"{' : '.join(str(p) for p in parts)}",
            size=10.6, weight=700, color=C["soft"])

    bx, bw, by, bh = 36, W - 72, 46, 46
    x = bx
    for i, p in enumerate(parts):
        w = bw * p / tp
        col, bg = cols[i % len(cols)], bgs[i % len(bgs)]
        _card(cv, x, by, w, bh, col, bg, r=5, sw=1.6)
        cv.text(x + w / 2, by + 22, _fmt(p * unit), size=13, weight=700,
                color=col)
        cv.text(x + w / 2, by + 37, f"{p} parts", size=8.2, color=C["soft"])
        # tick marks for each single part
        for j in range(1, p):
            tx = x + bw * j / tp
            cv.line(tx, by + 4, tx, by + bh - 4, color=col, w=0.7,
                    dash="3 3")
        x += w

    # total brace
    cv.raw(f'<path d="M{bx} {by+bh+8} L{bx} {by+bh+16} L{bx+bw} {by+bh+16} '
           f'L{bx+bw} {by+bh+8}" fill="none" stroke="{C["grey"]}" '
           f'stroke-width="1.3"/>')
    cv.text(W / 2, by + bh + 32, f"total = {_fmt(total)}", size=9.6,
            weight=700, color=C["soft"])

    _card(cv, 40, 150, 176, 30, C["ink"], "#f2f3f7", sw=1.5)
    cv.text(128, 170, f"total parts = {tp}", size=10.4, weight=700,
            color=C["ink"])
    _card(cv, 236, 150, 176, 30, C["red"], C["red_bg"], sw=1.6)
    cv.text(324, 170, f"one part = {_fmt(unit)}", size=10.4, weight=700,
            color=C["red"])
    cv.text(W / 2, H - 8, "find one part first, then multiply",
            size=8.6, color=C["soft"])
    return cv.svg()


# ─────────────────────────── what a ratio means ─────────────────────────────
def ratio_parts(spec):
    parts = _parts(spec, "ratio", "2,3")
    a, b = parts[0], parts[1]

    W, H = 400, 216
    cv = Canvas(W, H, seed=_seed(spec, 1202))
    cv.text(W / 2, 20, f"{a} : {b} means {a} equal parts against {b}",
            size=10.5, weight=700, color=C["soft"])

    box = 34
    gap = 6
    y1, y2 = 46, 112

    for row, (n, col, bg, lab) in enumerate((
            (a, C["blue"], C["blue_bg"], "first"),
            (b, C["green"], C["green_bg"], "second"))):
        y = y1 if row == 0 else y2
        x0 = 92
        for i in range(n):
            x = x0 + i * (box + gap)
            _card(cv, x, y, box, box, col, bg, r=4, sw=1.5)
            cv.text(x + box / 2, y + 22, "1", size=11, weight=700, color=col)
        cv.text(x0 - 12, y + 22, lab, size=9, anchor="end", weight=700,
                color=col)
        cv.text(x0 + n * (box + gap) + 4, y + 22, f"= {n} parts", size=9,
                anchor="start", color=C["soft"])

    _card(cv, 60, 164, 280, 32, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(200, 185, f"every box is the same size, call it k", size=10,
            weight=700, color=C["amber"])
    cv.text(W / 2, H - 6, f"so the two amounts are {a}k and {b}k",
            size=9, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── joining a:b with b:c ───────────────────────────
def ratio_chain(spec):
    a, b1 = _parts(spec, "first", "2,3")
    b2, c = _parts(spec, "second", "4,5")

    la = a * b2
    lb = b1 * b2
    lc = b1 * c
    g = math.gcd(math.gcd(la, lb), lc)

    W, H = 452, 226
    cv = Canvas(W, H, seed=_seed(spec, 1203))
    cv.text(W / 2, 20, "make the shared term match, then read across",
            size=10.4, weight=700, color=C["soft"])

    _card(cv, 44, 38, 150, 40, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(119, 63, f"a : b = {a} : {b1}", size=12, weight=700,
            color=C["blue"])
    _card(cv, 258, 38, 150, 40, C["green"], C["green_bg"], sw=1.5)
    cv.text(333, 63, f"b : c = {b2} : {c}", size=12, weight=700,
            color=C["green"])

    cv.arrow(119, 82, 119, 104, color=C["grey"], w=1.2)
    cv.arrow(333, 82, 333, 104, color=C["grey"], w=1.2)
    cv.text(132, 98, f"x {b2}", size=9, weight=700, anchor="start",
            color=C["red"])
    cv.text(346, 98, f"x {b1}", size=9, weight=700, anchor="start",
            color=C["red"])

    _card(cv, 44, 108, 150, 38, C["blue"], "#ffffff", sw=1.3)
    cv.text(119, 132, f"{la} : {lb}", size=12.5, weight=700, color=C["blue"])
    _card(cv, 258, 108, 150, 38, C["green"], "#ffffff", sw=1.3)
    cv.text(333, 132, f"{lb} : {lc}", size=12.5, weight=700, color=C["green"])

    cv.line(198, 127, 254, 127, color=C["red"], w=1.2, dash="3 3")
    cv.text(226, 118, f"b = {lb}", size=9.2, weight=700, color=C["red"])

    _card(cv, (W - 300) / 2, 162, 300, 34, C["purple"], C["purple_bg"],
          sw=1.8)
    cv.text(W / 2, 184, f"a : b : c = {la} : {lb} : {lc}", size=13,
            weight=700, color=C["purple"])
    if g > 1:
        cv.text(W / 2, H - 10, f"divide by {g}  ->  "
                f"{la//g} : {lb//g} : {lc//g}", size=9.4, weight=700,
                color=C["ink"])
    return cv.svg()


# ─────────────────────────── cross multiplication ───────────────────────────
def proportion_cross(spec):
    a = int(spec.get("a", 3))
    b = int(spec.get("b", 4))
    c = int(spec.get("c", 9))
    d = int(spec.get("d", 12))

    W, H = 400, 258
    cv = Canvas(W, H, seed=_seed(spec, 1204))
    cv.text(W / 2, 18, "in a proportion the cross products match",
            size=10.5, weight=700, color=C["soft"])

    cx, cy = W / 2, 112
    dx, dy = 82, 40
    pts = {"a": (cx - dx, cy - dy), "b": (cx + dx, cy - dy),
           "c": (cx - dx, cy + dy), "d": (cx + dx, cy + dy)}
    vals = {"a": a, "b": b, "c": c, "d": d}
    cols = {"a": C["blue"], "b": C["red"], "c": C["red"], "d": C["blue"]}

    # the two crossing lines, drawn first so circles sit on top
    cv.line(*pts["a"], *pts["d"], color=C["blue"], w=1.6)
    cv.line(*pts["b"], *pts["c"], color=C["red"], w=1.6)

    for kk, (px, py) in pts.items():
        cv.circle(px, py, 23, color=cols[kk], fill=C["paper"], w=1.8)
        cv.text(px, py + 6, str(vals[kk]), size=15, weight=700,
                color=cols[kk])

    cv.text(cx, cy - dy + 6, f"{a} : {b}", size=10, weight=700,
            color=C["soft"])
    cv.text(cx, cy + dy + 6, f"{c} : {d}", size=10, weight=700,
            color=C["soft"])

    _card(cv, 30, 192, 160, 32, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(110, 213, f"a x d = {a*d}", size=11, weight=700, color=C["blue"])
    _card(cv, 210, 192, 160, 32, C["red"], C["red_bg"], sw=1.5)
    cv.text(290, 213, f"b x c = {b*c}", size=11, weight=700, color=C["red"])

    ok = (a * d == b * c)
    cv.text(W / 2, H - 10,
            "equal, so the four numbers are in proportion" if ok
            else "not equal, so they are NOT in proportion",
            size=9.2, weight=700,
            color=C["green"] if ok else C["red"])
    return cv.svg()


# ─────────────────────────── mean / third / fourth ──────────────────────────
def mean_third_prop(spec):
    a = int(spec.get("a", 4))
    b = int(spec.get("b", 16))
    mean = math.isqrt(a * b)
    third = Fraction(b * b, a)
    c = int(spec.get("c", 6))
    fourth = Fraction(b * c, a)

    rows = [
        ("MEAN proportional", f"{a} : x = x : {b}", "x\u00b2 = ab",
         f"x = {mean}" if mean * mean == a * b else f"x = sqrt({a*b})",
         C["blue"], C["blue_bg"]),
        ("THIRD proportional", f"{a} : {b} = {b} : x", "x = b\u00b2/a",
         f"x = {third}", C["green"], C["green_bg"]),
        ("FOURTH proportional", f"{a} : {b} = {c} : x", "x = bc/a",
         f"x = {fourth}", C["amber"], C["amber_bg"]),
    ]

    W = 452
    H = 36 + len(rows) * 52 + 10
    cv = Canvas(W, H, seed=_seed(spec, 1205))
    cv.text(W / 2, 18, "three names, one idea: fill the missing slot",
            size=10.2, weight=700, color=C["soft"])

    for i, (name, setup, rule, ans, col, bg) in enumerate(rows):
        y = 28 + i * 52
        _card(cv, 22, y, 408, 42, col, bg, sw=1.5)
        cv.text(34, y + 18, name, size=9.4, weight=700, anchor="start",
                color=col)
        cv.text(34, y + 33, setup, size=10.6, weight=700, anchor="start",
                color=C["ink"])
        cv.raw(f'<rect x="222" y="{y+8}" width="94" height="26" rx="5" '
               f'fill="{C["paper"]}" stroke="{col}" stroke-width="1.1"/>')
        cv.text(269, y + 26, rule, size=10, weight=700, color=col)
        cv.raw(f'<rect x="328" y="{y+8}" width="92" height="26" rx="5" '
               f'fill="#ffffff" stroke="{C["red"]}" stroke-width="1.3"/>')
        cv.text(374, y + 26, ans, size=10.6, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── adding to both terms ───────────────────────────
def ratio_change(spec):
    a, b = _parts(spec, "ratio", "3,4")
    add = int(spec.get("add", 6))
    k = int(spec.get("k", 6))

    n1, n2 = a * k, b * k
    m1, m2 = n1 + add, n2 + add
    g = math.gcd(m1, m2)

    W, H = 452, 248
    cv = Canvas(W, H, seed=_seed(spec, 1206))
    cv.text(W / 2, 20, f"adding {add} to both terms does NOT keep the ratio",
            size=10.4, weight=700, color=C["soft"])

    sc = 300 / max(m1, m2)
    x0 = 96

    for row, (v, extra, lab, col, bg) in enumerate((
            (n1, 0, f"{a}k", C["blue"], C["blue_bg"]),
            (n2, 0, f"{b}k", C["blue"], C["blue_bg"]))):
        y = 42 + row * 40
        _card(cv, x0, y, v * sc, 28, col, bg, r=4, sw=1.4)
        cv.text(x0 + v * sc / 2, y + 19, str(v), size=11, weight=700,
                color=col)
        cv.text(x0 - 10, y + 19, lab, size=9.6, anchor="end", weight=700,
                color=C["ink"])

    cv.text(x0 + 320, 61, f"{a} : {b}", size=10.4, anchor="start",
            weight=700, color=C["blue"])

    for row, (v, lab, col, bg) in enumerate((
            (n1, "+" + str(add), C["blue"], C["blue_bg"]),
            (n2, "+" + str(add), C["blue"], C["blue_bg"]))):
        y = 130 + row * 40
        _card(cv, x0, y, v * sc, 28, col, bg, r=4, sw=1.4)
        cv.text(x0 + v * sc / 2, y + 19, str(v), size=11, weight=700,
                color=col)
        _card(cv, x0 + v * sc, y, add * sc, 28, C["green"], C["green_bg"],
              r=4, sw=1.4)
        cv.text(x0 + v * sc + add * sc / 2, y + 19, lab, size=9,
                weight=700, color=C["green"])
        cv.text(x0 - 10, y + 19, str(v + add), size=9.6, anchor="end",
                weight=700, color=C["ink"])

    cv.text(x0 + 320, 149, f"{m1//g} : {m2//g}", size=10.4, anchor="start",
            weight=700, color=C["red"])

    _card(cv, (W - 340) / 2, 212, 340, 28, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(W / 2, 231, f"{a} : {b}  becomes  {m1} : {m2}  =  "
            f"{m1//g} : {m2//g}", size=10.4, weight=700, color=C["amber"])
    return cv.svg()


REGISTRY = {
    "ratio-bar": ratio_bar,
    "ratio-parts": ratio_parts,
    "ratio-chain": ratio_chain,
    "proportion-cross": proportion_cross,
    "mean-third-prop": mean_third_prop,
    "ratio-change": ratio_change,
}
