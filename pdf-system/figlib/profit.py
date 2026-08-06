"""
profit.py — figures for Chapter 15 (Profit, Loss & Discount).

price-ladder     : CP, MP and SP stacked so profit and discount are visible gaps
profit-loss-bar  : one bar showing CP with the profit or loss piece attached
mp-cp-sp         : the full chain MP -> discount -> SP -> profit -> CP
discount-chain   : two successive discounts applied one after the other
same-sp-trap     : two articles at the same SP, why it is always a loss
false-weight     : the shopkeeper's pan showing 900 g sold as 1 kg
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


# ─────────────────────────── the three prices stacked ───────────────────────
def price_ladder(spec):
    cp = float(spec.get("cp", 400))
    mp = float(spec.get("mp", 600))
    sp = float(spec.get("sp", 500))
    top = max(cp, mp, sp)

    W, H = 452, 274
    cv = Canvas(W, H, seed=_seed(spec, 1501))
    cv.text(W / 2, 20, "three prices, two gaps", size=10.6, weight=700,
            color=C["soft"])

    base = 182
    plot = 112
    bw = 72
    xs = [128, 244, 360]
    items = [("CP", cp, C["blue"], C["blue_bg"], "what it cost you"),
             ("MP", mp, C["amber"], C["amber_bg"], "printed on the tag"),
             ("SP", sp, C["green"], C["green_bg"], "what it sold for")]

    for x, (lab, v, col, bg, note) in zip(xs, items):
        h = v / top * plot
        _card(cv, x - bw / 2, base - h, bw, h, col, bg, r=5, sw=1.6)
        cv.text(x, base - h - 8, _fmt(v), size=11.5, weight=700, color=col)
        cv.text(x, base + 16, lab, size=11, weight=700, color=col)
        cv.text(x, base + 31, note, size=7.6, color=C["soft"])

    cv.line(66, base, W - 22, base, color=C["ink"], w=1.5)

    # discount gap : MP down to SP
    hm = base - mp / top * plot
    hs = base - sp / top * plot
    hc = base - cp / top * plot
    cv.line(244 + bw / 2, hm, 360 + bw / 2 + 8, hm, color=C["red"], w=1.1,
            dash="3 3")
    ax = 360 + bw / 2 + 4
    cv.arrow(ax, hm, ax, hs, color=C["red"], w=1.4)
    cv.text(ax + 6, (hm + hs) / 2 + 4, f"disc {_fmt(mp-sp)}", size=8.2,
            anchor="start", weight=700, color=C["red"])

    # profit gap : CP up to SP
    cv.line(128 - bw / 2 - 10, hc, 360 + bw / 2, hc, color=C["green"], w=1.1,
            dash="3 3")
    gx = 128 - bw / 2 - 6
    cv.arrow(gx, hc, gx, hs, color=C["green"], w=1.4)
    cv.text(gx - 6, (hc + hs) / 2 + 4, f"profit {_fmt(sp-cp)}", size=8.2,
            anchor="end", weight=700, color=C["green"])

    _card(cv, 40, 228, 182, 30, C["green"], C["green_bg"], sw=1.5)
    cv.text(131, 248, f"profit % = {_fmt(round((sp-cp)/cp*100,2))} (on CP)",
            size=9.2, weight=700, color=C["green"])
    _card(cv, 232, 228, 182, 30, C["red"], C["red_bg"], sw=1.5)
    cv.text(323, 248, f"discount % = {_fmt(round((mp-sp)/mp*100,2))} (on MP)",
            size=9.2, weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── profit or loss as a bar ────────────────────────
def profit_loss_bar(spec):
    cp = float(spec.get("cp", 100))
    pct = float(spec.get("pct", 25))
    gain = pct >= 0
    sp = cp * (1 + pct / 100)

    W, H = 452, 208
    cv = Canvas(W, H, seed=_seed(spec, 1502))
    cv.text(W / 2, 20, "the base is always CP, never SP", size=10.6,
            weight=700, color=C["soft"])

    unit = 300 / max(cp, sp)
    x0 = 96

    # CP bar
    _card(cv, x0, 44, cp * unit, 34, C["blue"], C["blue_bg"], r=4, sw=1.5)
    cv.text(x0 + cp * unit / 2, 65, f"CP {_fmt(cp)}", size=11, weight=700,
            color=C["blue"])
    cv.text(x0 - 10, 65, "cost", size=9, anchor="end", weight=700,
            color=C["ink"])

    # SP bar with the extra piece
    y2 = 94
    if gain:
        _card(cv, x0, y2, cp * unit, 34, C["blue"], C["blue_bg"], r=4, sw=1.5)
        cv.text(x0 + cp * unit / 2, y2 + 21, _fmt(cp), size=10.4, weight=700,
                color=C["blue"])
        _card(cv, x0 + cp * unit, y2, (sp - cp) * unit, 34, C["green"],
              C["green_bg"], r=4, sw=1.6)
        cv.text(x0 + cp * unit + (sp - cp) * unit / 2, y2 + 21,
                f"+{_fmt(sp-cp)}", size=10, weight=700, color=C["green"])
    else:
        _card(cv, x0, y2, sp * unit, 34, C["blue"], C["blue_bg"], r=4, sw=1.5)
        cv.text(x0 + sp * unit / 2, y2 + 21, _fmt(sp), size=10.4, weight=700,
                color=C["blue"])
        _card(cv, x0 + sp * unit, y2, (cp - sp) * unit, 34, C["red"],
              C["red_bg"], r=4, sw=1.6)
        cv.text(x0 + sp * unit + (cp - sp) * unit / 2, y2 + 21,
                f"-{_fmt(cp-sp)}", size=10, weight=700, color=C["red"])
    cv.text(x0 - 10, y2 + 21, "sold", size=9, anchor="end", weight=700,
            color=C["ink"])

    col = C["green"] if gain else C["red"]
    bg = C["green_bg"] if gain else C["red_bg"]
    word = "profit" if gain else "loss"

    _card(cv, 40, 144, 372, 30, col, bg, sw=1.6)
    cv.text(226, 164, f"{word} % = ({_fmt(abs(sp-cp))} / {_fmt(cp)}) x 100 "
            f"= {_fmt(abs(pct))}%", size=10.4, weight=700, color=col)
    cv.text(W / 2, H - 12, "divide by CP, always", size=9.2, weight=700,
            color=C["ink"])
    return cv.svg()


# ─────────────────────────── MP to SP to CP chain ───────────────────────────
def mp_cp_sp(spec):
    cp = float(spec.get("cp", 100))
    above = float(spec.get("above", 40))
    disc = float(spec.get("discount", 25))
    mp = cp * (1 + above / 100)
    sp = mp * (1 - disc / 100)
    prof = (sp - cp) / cp * 100

    W, H = 452, 222
    cv = Canvas(W, H, seed=_seed(spec, 1503))
    cv.text(W / 2, 20, "mark up from CP, then cut down to SP",
            size=10.6, weight=700, color=C["soft"])

    boxes = [("CP", _fmt(cp), C["blue"], C["blue_bg"]),
             ("MP", _fmt(mp), C["amber"], C["amber_bg"]),
             ("SP", _fmt(sp), C["green"], C["green_bg"])]
    bw, gap = 104, 56
    x0 = (W - (3 * bw + 2 * gap)) / 2
    for i, (lab, val, col, bg) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        _card(cv, x, 46, bw, 54, col, bg, sw=1.7)
        cv.text(x + bw / 2, 68, lab, size=9.4, weight=700, color=C["soft"])
        cv.text(x + bw / 2, 88, val, size=14, weight=700, color=col)
        if i < 2:
            ax, bx = x + bw + 5, x + bw + gap - 5
            cv.arrow(ax, 73, bx, 73, color=C["grey"], w=1.4)
            lab2 = f"+{_fmt(above)}%" if i == 0 else f"-{_fmt(disc)}%"
            col2 = C["amber"] if i == 0 else C["red"]
            cv.text((ax + bx) / 2, 62, lab2, size=9, weight=700, color=col2)

    cv.text(x0 + bw / 2, 118, "mark up on CP", size=8.2, color=C["soft"])
    cv.text(x0 + bw + gap + bw / 2, 118, "discount on MP", size=8.2,
            color=C["soft"])

    # the return arrow from SP back to CP
    cv.raw(f'<path d="M{x0+2*(bw+gap)+bw/2} 130 L{x0+2*(bw+gap)+bw/2} 146 '
           f'L{x0+bw/2} 146 L{x0+bw/2} 132" fill="none" '
           f'stroke="{C["green"]}" stroke-width="1.4" stroke-dasharray="4 3"/>')
    cv.text(W / 2, 158, f"profit measured back against CP", size=8.8,
            weight=700, color=C["green"])

    _card(cv, 46, 168, 360, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 188, f"SP = CP x {_fmt(1+above/100)} x {_fmt(1-disc/100)} "
            f"= {_fmt(sp/cp)} CP", size=10.2, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, f"so the profit is {_fmt(prof)}%", size=10,
            weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── two discounts in a row ─────────────────────────
def discount_chain(spec):
    mp = float(spec.get("mp", 2000))
    d1 = float(spec.get("d1", 20))
    d2 = float(spec.get("d2", 10))
    a = mp * (1 - d1 / 100)
    b = a * (1 - d2 / 100)
    single = (1 - (1 - d1 / 100) * (1 - d2 / 100)) * 100

    W, H = 452, 226
    cv = Canvas(W, H, seed=_seed(spec, 1504))
    cv.text(W / 2, 20, "the second cut is taken on the reduced price",
            size=10.6, weight=700, color=C["soft"])

    unit = 300 / mp
    x0 = 92
    rows = [(mp, "marked price", C["amber"], C["amber_bg"]),
            (a, f"after {_fmt(d1)}% off", C["blue"], C["blue_bg"]),
            (b, f"after {_fmt(d2)}% more", C["green"], C["green_bg"])]
    for i, (v, lab, col, bg) in enumerate(rows):
        y = 44 + i * 40
        _card(cv, x0, y, v * unit, 30, col, bg, r=4, sw=1.5)
        cv.text(x0 + v * unit / 2, y + 20, _fmt(v), size=11, weight=700,
                color=col)
        cv.text(x0 - 10, y + 20, lab, size=8.4, anchor="end", weight=700,
                color=C["ink"])
        if i > 0:
            prev = rows[i - 1][0]
            cv.raw(f'<rect x="{x0+v*unit}" y="{y}" width="{(prev-v)*unit}" '
                   f'height="30" rx="3" fill="none" stroke="{C["red"]}" '
                   f'stroke-width="1.2" stroke-dasharray="3 3"/>')
            cv.text(x0 + v * unit + (prev - v) * unit / 2, y + 20,
                    f"-{_fmt(prev-v)}", size=8.4, weight=700, color=C["red"])

    _card(cv, 40, 168, 178, 30, C["red"], C["red_bg"], sw=1.5)
    cv.text(129, 188, f"NOT {_fmt(d1+d2)}%", size=10.4, weight=700,
            color=C["red"])
    cv.line(64, 188, 194, 188, color=C["red"], w=1.5)

    _card(cv, 234, 168, 178, 30, C["green"], C["green_bg"], sw=1.7)
    cv.text(323, 188, f"single = {_fmt(single)}%", size=10.4, weight=700,
            color=C["green"])

    cv.text(W / 2, H - 10, f"a + b - ab/100 = {_fmt(d1)} + {_fmt(d2)} - "
            f"{_fmt(d1*d2/100)} = {_fmt(single)}", size=9.2, weight=700,
            color=C["ink"])
    return cv.svg()


# ─────────────────────────── same SP on two articles ────────────────────────
def same_sp_trap(spec):
    sp = float(spec.get("sp", 990))
    x = float(spec.get("pct", 10))
    cp1 = sp / (1 + x / 100)
    cp2 = sp / (1 - x / 100)
    tot_cp = cp1 + cp2
    loss = tot_cp - 2 * sp

    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 1505))
    cv.text(W / 2, 20, f"both sold at {_fmt(sp)}, one at +{_fmt(x)}%, "
            f"one at -{_fmt(x)}%", size=10.2, weight=700, color=C["soft"])

    unit = 150 / cp2
    x0 = 118
    rows = [(cp1, sp, f"+{_fmt(x)}%", C["green"], C["green_bg"], "article A"),
            (cp2, sp, f"-{_fmt(x)}%", C["red"], C["red_bg"], "article B")]
    for i, (c, s, tag, col, bg, lab) in enumerate(rows):
        y = 46 + i * 52
        _card(cv, x0, y, c * unit, 26, C["blue"], C["blue_bg"], r=4, sw=1.3)
        cv.text(x0 + c * unit / 2, y + 18, f"CP {_fmt(c)}", size=9.4,
                weight=700, color=C["blue"])
        _card(cv, x0, y + 26, s * unit, 22, col, bg, r=4, sw=1.4)
        cv.text(x0 + s * unit / 2, y + 42, f"SP {_fmt(s)}", size=9,
                weight=700, color=col)
        cv.text(x0 - 10, y + 26, lab, size=8.8, anchor="end", weight=700,
                color=C["ink"])
        cv.text(x0 + max(c, s) * unit + 10, y + 26, tag, size=9.4,
                anchor="start", weight=700, color=col)

    _card(cv, 40, 158, 178, 30, C["blue"], C["blue_bg"], sw=1.5)
    cv.text(129, 178, f"total CP = {_fmt(tot_cp)}", size=10, weight=700,
            color=C["blue"])
    _card(cv, 234, 158, 178, 30, C["green"], C["green_bg"], sw=1.5)
    cv.text(323, 178, f"total SP = {_fmt(2*sp)}", size=10, weight=700,
            color=C["green"])

    _card(cv, (W - 340) / 2, 196, 340, 32, C["red"], C["red_bg"], sw=1.8)
    cv.text(W / 2, 217, f"always a LOSS of x\u00b2/100 = "
            f"{_fmt(x*x/100)}%   (here {_fmt(loss)})", size=10.6,
            weight=700, color=C["red"])
    return cv.svg()


# ─────────────────────────── the false weight ───────────────────────────────
def false_weight(spec):
    w = float(spec.get("weight", 900))
    gain = (1000 - w) / w * 100

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 1506))
    cv.text(W / 2, 20, "he charges for 1000 g but hands over less",
            size=10.6, weight=700, color=C["soft"])

    unit = 260 / 1000
    x0 = 110
    _card(cv, x0, 46, 1000 * unit, 32, C["amber"], C["amber_bg"], r=4, sw=1.5)
    cv.text(x0 + 1000 * unit / 2, 67, "1000 g  (money taken)", size=10,
            weight=700, color=C["amber"])

    _card(cv, x0, 92, w * unit, 32, C["blue"], C["blue_bg"], r=4, sw=1.5)
    cv.text(x0 + w * unit / 2, 113, f"{_fmt(w)} g  (goods given)", size=9.6,
            weight=700, color=C["blue"])
    cv.raw(f'<rect x="{x0+w*unit}" y="92" width="{(1000-w)*unit}" '
           f'height="32" rx="3" fill="{C["green_bg"]}" '
           f'stroke="{C["green"]}" stroke-width="1.5"/>')
    cv.text(x0 + w * unit + (1000 - w) * unit / 2, 113, f"{_fmt(1000-w)}",
            size=9, weight=700, color=C["green"])

    cv.text(x0 + w * unit + (1000 - w) * unit / 2, 84, "free gain",
            size=8.2, weight=700, color=C["green"])

    _card(cv, 40, 146, 372, 32, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 167, f"gain % = (error / true weight) x 100 = "
            f"({_fmt(1000-w)} / {_fmt(w)}) x 100", size=10, weight=700,
            color=C["purple"])

    _card(cv, (W - 250) / 2, 186, 250, 30, C["green"], C["green_bg"], sw=1.8)
    cv.text(W / 2, 206, f"gain = {_fmt(round(gain,2))}%", size=12,
            weight=700, color=C["green"])
    cv.text(W / 2, H - 8, "the denominator is what he GAVE, not 1000",
            size=8.8, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "price-ladder": price_ladder,
    "profit-loss-bar": profit_loss_bar,
    "mp-cp-sp": mp_cp_sp,
    "discount-chain": discount_chain,
    "same-sp-trap": same_sp_trap,
    "false-weight": false_weight,
}
