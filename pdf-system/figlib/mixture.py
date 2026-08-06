"""
mixture.py — figures for Chapter 19 (Mixture & Alligation).

allig-cross      : the classic X, cheaper and dearer with the mean in the middle
allig-line       : the same idea on a number line, distances give the ratio
mixture-jar      : a jar showing milk and water bands before and after
replacement      : repeated remove-and-refill, milk falling each round
add-to-ratio     : how much water to add so the ratio becomes what is asked
two-vessels      : two jars poured together, the result sits between them
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


def _ratio(a, b):
    fa = Fraction(a).limit_denominator(1000)
    fb = Fraction(b).limit_denominator(1000)
    n = fa.numerator * fb.denominator
    d = fb.numerator * fa.denominator
    g = math.gcd(int(n), int(d)) or 1
    return int(n // g), int(d // g)


# ─────────────────────────── the alligation cross ───────────────────────────
def allig_cross(spec):
    c1 = float(spec.get("cheap", 20))
    c2 = float(spec.get("dear", 30))
    m = float(spec.get("mean", 24))
    d1 = c2 - m
    d2 = m - c1
    r1, r2 = _ratio(d1, d2)

    W, H = 420, 268
    cv = Canvas(W, H, seed=_seed(spec, 1901))
    cv.text(W / 2, 20, "cross-subtract, and the ratio falls out",
            size=10.6, weight=700, color=C["soft"])

    cx, cy = W / 2, 122
    dx, dy = 96, 52
    tl, tr = (cx - dx, cy - dy), (cx + dx, cy - dy)
    bl, br = (cx - dx, cy + dy), (cx + dx, cy + dy)

    cv.line(*tl, *br, color=C["blue"], w=1.5)
    cv.line(*tr, *bl, color=C["green"], w=1.5)

    for (px, py), val, lab, col, bg in (
            (tl, c1, "cheaper", C["blue"], C["blue_bg"]),
            (tr, c2, "dearer", C["green"], C["green_bg"])):
        _card(cv, px - 48, py - 20, 96, 40, col, bg, sw=1.7)
        cv.text(px, py + 6, _fmt(val), size=14, weight=700, color=col)
        cv.text(px, py - 28, lab, size=8.6, weight=700, color=C["soft"])

    _card(cv, cx - 48, cy - 18, 96, 36, C["amber"], C["amber_bg"], sw=1.8)
    cv.text(cx, cy + 6, _fmt(m), size=13.5, weight=700, color=C["amber"])
    cv.text(cx, cy + 32, "mean", size=8.6, weight=700, color=C["soft"])

    for (px, py), val, col, bg in ((bl, d1, C["green"], C["green_bg"]),
                                   (br, d2, C["blue"], C["blue_bg"])):
        _card(cv, px - 44, py - 18, 88, 36, col, bg, sw=1.5)
        cv.text(px, py + 5, _fmt(val), size=12.5, weight=700, color=col)

    cv.text(bl[0], bl[1] + 32, f"{_fmt(c2)} - {_fmt(m)}", size=8,
            color=C["soft"])
    cv.text(br[0], br[1] + 32, f"{_fmt(m)} - {_fmt(c1)}", size=8,
            color=C["soft"])

    _card(cv, (W - 260) / 2, 216, 260, 32, C["red"], C["red_bg"], sw=1.8)
    cv.text(W / 2, 237, f"cheaper : dearer = {r1} : {r2}", size=12,
            weight=700, color=C["red"])
    cv.text(W / 2, H - 6, "the bottom answer sits under the OPPOSITE top",
            size=8.4, color=C["soft"])
    return cv.svg()


# ─────────────────────────── the same idea on a line ────────────────────────
def allig_line(spec):
    c1 = float(spec.get("cheap", 20))
    c2 = float(spec.get("dear", 30))
    m = float(spec.get("mean", 24))
    d1 = m - c1
    d2 = c2 - m
    r1, r2 = _ratio(d2, d1)

    W, H = 452, 216
    cv = Canvas(W, H, seed=_seed(spec, 1902))
    cv.text(W / 2, 20, "the mean sits nearer to whichever side is heavier",
            size=10.4, weight=700, color=C["soft"])

    x0, x1 = 76, W - 76
    y = 104
    cv.line(x0 - 12, y, x1 + 12, y, color=C["ink"], w=1.6)

    def px(v):
        return x0 + (v - c1) / (c2 - c1) * (x1 - x0)

    for v, lab, col in ((c1, "cheaper", C["blue"]), (c2, "dearer", C["green"])):
        cv.line(px(v), y - 10, px(v), y + 10, color=col, w=1.8)
        cv.text(px(v), y + 28, _fmt(v), size=11, weight=700, color=col)
        cv.text(px(v), y + 42, lab, size=8.4, color=C["soft"])

    cv.dot(px(m), y, r=5.0, color=C["amber"])
    _card(cv, px(m) - 42, y - 46, 84, 26, C["amber"], C["amber_bg"], r=5,
          sw=1.5)
    cv.text(px(m), y - 28, f"mean {_fmt(m)}", size=9.4, weight=700,
            color=C["amber"])

    # distance braces
    cv.raw(f'<path d="M{px(c1)} {y+58} L{px(c1)} {y+66} L{px(m)} {y+66} '
           f'L{px(m)} {y+58}" fill="none" stroke="{C["blue"]}" '
           f'stroke-width="1.3"/>')
    cv.text((px(c1) + px(m)) / 2, y + 80, _fmt(d1), size=9.4, weight=700,
            color=C["blue"])
    cv.raw(f'<path d="M{px(m)} {y+58} L{px(m)} {y+66} L{px(c2)} {y+66} '
           f'L{px(c2)} {y+58}" fill="none" stroke="{C["green"]}" '
           f'stroke-width="1.3"/>')
    cv.text((px(m) + px(c2)) / 2, y + 80, _fmt(d2), size=9.4, weight=700,
            color=C["green"])

    cv.text(W / 2, H - 12, f"quantities are in the INVERSE ratio of these "
            f"gaps  =  {r1} : {r2}", size=9.4, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── a jar of milk and water ────────────────────────
def mixture_jar(spec):
    vol = float(spec.get("volume", 60))
    a = int(spec.get("a", 2))
    b = int(spec.get("b", 1))
    milk = vol * a / (a + b)
    water = vol - milk

    W, H = 400, 246
    cv = Canvas(W, H, seed=_seed(spec, 1903))
    cv.text(W / 2, 20, f"{_fmt(vol)} litres in the ratio {a} : {b}",
            size=10.6, weight=700, color=C["soft"])

    jw, jh = 104, 132
    jx, jy = (W - jw) / 2 - 68, 44

    def jar(x, milk_v, water_v, tag):
        tot = milk_v + water_v
        cv.raw(f'<rect x="{x}" y="{jy}" width="{jw}" height="{jh}" rx="8" '
               f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.8"/>')
        wh = jh * water_v / tot
        mh = jh - wh
        cv.raw(f'<rect x="{x+3}" y="{jy+3}" width="{jw-6}" height="{mh-3}" '
               f'rx="5" fill="{C["blue_bg"]}" stroke="{C["blue"]}" '
               f'stroke-width="1.2"/>')
        cv.raw(f'<rect x="{x+3}" y="{jy+mh}" width="{jw-6}" '
               f'height="{wh-3}" rx="5" fill="{C["teal_bg"]}" '
               f'stroke="{C["teal"]}" stroke-width="1.2"/>')
        cv.text(x + jw / 2, jy + mh / 2 + 4, f"milk {_fmt(milk_v)}",
                size=9.4, weight=700, color=C["blue"])
        cv.text(x + jw / 2, jy + mh + wh / 2 + 4, f"water {_fmt(water_v)}",
                size=9, weight=700, color=C["teal"])
        cv.text(x + jw / 2, jy + jh + 16, tag, size=9, weight=700,
                color=C["ink"])

    jar(jx, milk, water, f"{a} : {b}")

    rows = [("total", _fmt(vol), C["ink"]),
            ("milk = total x a/(a+b)", _fmt(milk), C["blue"]),
            ("water = total x b/(a+b)", _fmt(water), C["teal"]),
            ("milk %", f"{_fmt(round(milk/vol*100,2))}%", C["red"])]
    for i, (lab, val, col) in enumerate(rows):
        y = 56 + i * 30
        _card(cv, 210, y, 176, 24, col, "#ffffff", r=5, sw=1.2)
        cv.text(218, y + 16, lab, size=8, anchor="start", color=C["soft"])
        cv.text(378, y + 16, val, size=9.2, anchor="end", weight=700,
                color=col)

    cv.text(W / 2, H - 12, "always turn the ratio into actual litres first",
            size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── remove and refill ──────────────────────────────
def replacement(spec):
    vol = float(spec.get("volume", 50))
    out = float(spec.get("out", 10))
    n = int(spec.get("times", 2))
    k = (vol - out) / vol

    vals = [vol * k ** i for i in range(n + 1)]

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 1904))
    cv.text(W / 2, 20, f"take out {_fmt(out)} L, top up with water, "
            f"{n} times", size=10.4, weight=700, color=C["soft"])

    bw = 76
    gap = (W - 60 - (n + 1) * bw) / n if n else 0
    x0 = 30
    jh = 92
    jy = 44
    for i, v in enumerate(vals):
        x = x0 + i * (bw + gap)
        cv.raw(f'<rect x="{x}" y="{jy}" width="{bw}" height="{jh}" rx="6" '
               f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.5"/>')
        mh = jh * v / vol
        cv.raw(f'<rect x="{x+3}" y="{jy+jh-mh+3}" width="{bw-6}" '
               f'height="{mh-6}" rx="4" fill="{C["blue_bg"]}" '
               f'stroke="{C["blue"]}" stroke-width="1.2"/>')
        cv.text(x + bw / 2, jy + jh - mh / 2 + 4, _fmt(round(v, 2)),
                size=9.4, weight=700, color=C["blue"])
        if v < vol:
            cv.text(x + bw / 2, jy + (jh - mh) / 2 + 4,
                    _fmt(round(vol - v, 2)), size=8.4, weight=700,
                    color=C["teal"])
        cv.text(x + bw / 2, jy + jh + 15, "start" if i == 0 else f"after {i}",
                size=8.2, color=C["soft"])
        if i < n:
            cv.arrow(x + bw + 3, jy + jh / 2, x + bw + gap - 3, jy + jh / 2,
                     color=C["red"], w=1.3)

    _card(cv, 40, 168, 372, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 189, f"milk left = V (1 - out/V)^n = {_fmt(vol)} x "
            f"({_fmt(vol-out)}/{_fmt(vol)})^{n} = {_fmt(round(vals[-1],2))}",
            size=9.6, weight=700, color=C["purple"])
    cv.text(W / 2, 218, "the jar is always full, only the milk share falls",
            size=9, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "blue is milk, the empty top is water",
            size=8.4, color=C["soft"])
    return cv.svg()


# ─────────────────────────── add water to fix the ratio ─────────────────────
def add_to_ratio(spec):
    vol = float(spec.get("volume", 60))
    a1 = int(spec.get("a1", 7))
    b1 = int(spec.get("b1", 3))
    a2 = int(spec.get("a2", 7))
    b2 = int(spec.get("b2", 4))

    milk = vol * a1 / (a1 + b1)
    w_old = vol - milk
    w_new = milk * b2 / a2
    add = w_new - w_old

    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 1905))
    cv.text(W / 2, 20, "milk never changes, only water is poured in",
            size=10.6, weight=700, color=C["soft"])

    unit = 300 / (milk + w_new)
    x0 = 92

    for i, (mv, wv, extra, lab) in enumerate((
            (milk, w_old, 0, f"now  {a1} : {b1}"),
            (milk, w_old, add, f"want  {a2} : {b2}"))):
        y = 48 + i * 54
        _card(cv, x0, y, mv * unit, 34, C["blue"], C["blue_bg"], r=4, sw=1.5)
        cv.text(x0 + mv * unit / 2, y + 22, f"milk {_fmt(mv)}", size=9.6,
                weight=700, color=C["blue"])
        _card(cv, x0 + mv * unit, y, wv * unit, 34, C["teal"], C["teal_bg"],
              r=4, sw=1.4)
        cv.text(x0 + mv * unit + wv * unit / 2, y + 22, _fmt(wv), size=9,
                weight=700, color=C["teal"])
        if extra:
            _card(cv, x0 + (mv + wv) * unit, y, extra * unit, 34, C["red"],
                  C["red_bg"], r=4, sw=1.7)
            cv.text(x0 + (mv + wv) * unit + extra * unit / 2, y + 22,
                    f"+{_fmt(extra)}", size=9, weight=700, color=C["red"])
        cv.text(x0 - 10, y + 22, lab, size=8.6, anchor="end", weight=700,
                color=C["ink"])

    rows = [(f"milk stays at", _fmt(milk), C["blue"]),
            (f"water needed for {a2} : {b2}", _fmt(w_new), C["teal"]),
            ("so pour in", _fmt(add), C["red"])]
    for i, (lab, val, col) in enumerate(rows):
        y = 162 + i * 22
        cv.text(56, y, lab, size=8.8, anchor="start", color=C["soft"])
        cv.text(W - 46, y, val, size=9.4, anchor="end", weight=700, color=col)
    return cv.svg()


# ─────────────────────────── two vessels poured together ────────────────────
def two_vessels(spec):
    a1 = int(spec.get("a1", 7))
    b1 = int(spec.get("b1", 3))
    a2 = int(spec.get("a2", 4))
    b2 = int(spec.get("b2", 1))

    f1 = a1 / (a1 + b1)
    f2 = a2 / (a2 + b2)
    fm = (f1 + f2) / 2
    r1, r2 = _ratio(fm, 1 - fm)

    W, H = 452, 280
    cv = Canvas(W, H, seed=_seed(spec, 1906))
    cv.text(W / 2, 20, "equal amounts poured together, milk shares average",
            size=10.4, weight=700, color=C["soft"])

    jw, jh = 82, 104
    jy = 62
    xs = [58, 186, 314]
    labels = [f"A  {a1} : {b1}", f"B  {a2} : {b2}", f"mix  {r1} : {r2}"]
    fracs = [f1, f2, fm]
    cols = [C["blue"], C["green"], C["purple"]]

    for x, lab, fr, col in zip(xs, labels, fracs, cols):
        cv.raw(f'<rect x="{x}" y="{jy}" width="{jw}" height="{jh}" rx="7" '
               f'fill="{C["paper"]}" stroke="{C["ink"]}" stroke-width="1.6"/>')
        mh = jh * fr
        cv.raw(f'<rect x="{x+3}" y="{jy+3}" width="{jw-6}" height="{mh-3}" '
               f'rx="4" fill="{C["blue_bg"]}" stroke="{C["blue"]}" '
               f'stroke-width="1.1"/>')
        cv.raw(f'<rect x="{x+3}" y="{jy+mh}" width="{jw-6}" '
               f'height="{jh-mh-3}" rx="4" fill="{C["teal_bg"]}" '
               f'stroke="{C["teal"]}" stroke-width="1.1"/>')
        cv.text(x + jw / 2, jy + mh / 2 + 4,
                f"{_fmt(round(fr*100,1))}%", size=9.4, weight=700,
                color=C["blue"])
        cv.text(x + jw / 2, jy + mh + (jh - mh) / 2 + 4,
                f"{_fmt(round((1-fr)*100,1))}%", size=8.4, weight=700,
                color=C["teal"])
        cv.text(x + jw / 2, jy + jh + 16, lab, size=9, weight=700, color=col)

    # both jars pour in from above, arrows kept clear of the labels
    mid = xs[2] + jw / 2
    ytop = jy - 10
    for src in (xs[0] + jw / 2, xs[1] + jw / 2):
        cv.raw(f'<path d="M{src} {ytop} L{src} {ytop-14} L{mid} {ytop-14}" '
               f'fill="none" stroke="{C["grey"]}" stroke-width="1.3"/>')
    cv.arrow(mid, ytop - 14, mid, ytop - 2, color=C["grey"], w=1.3)

    _card(cv, 40, 216, 372, 30, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 236, f"milk fraction = ({_fmt(round(f1,3))} + "
            f"{_fmt(round(f2,3))}) / 2 = {_fmt(round(fm,3))}", size=9.6,
            weight=700, color=C["amber"])
    cv.text(W / 2, 264, "if the amounts are unequal, use the weighted "
            "average instead", size=8.8, weight=700, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "allig-cross": allig_cross,
    "allig-line": allig_line,
    "mixture-jar": mixture_jar,
    "replacement": replacement,
    "add-to-ratio": add_to_ratio,
    "two-vessels": two_vessels,
}
