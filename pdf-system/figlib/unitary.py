"""
unitary.py — figures for Chapter 14 (Unitary Method).

unitary-steps    : many -> one -> many, the three-step ladder
direct-inverse   : the two behaviours side by side, arrows up or down
proportion-table : the given / asked grid with the cross-multiply arrow
chain-rule       : the M D H / W boxes on both sides of one equation
man-days-grid    : work drawn as a rectangle of men x days, area constant
partial-work     : a work bar split into the done part and the remaining part
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


# ─────────────────────────── many, one, many ────────────────────────────────
def unitary_steps(spec):
    n1 = float(spec.get("n1", 5))
    v1 = float(spec.get("v1", 60))
    n2 = float(spec.get("n2", 8))
    unit = v1 / n1
    v2 = unit * n2
    item = str(spec.get("item", "pens"))

    W, H = 452, 220
    cv = Canvas(W, H, seed=_seed(spec, 1401))
    cv.text(W / 2, 20, "come down to one, then go up again",
            size=10.6, weight=700, color=C["soft"])

    one = item[:-1] if item.endswith("s") and len(item) > 2 else item
    boxes = [(f"{_fmt(n1)} {item}", f"cost {_fmt(v1)}", C["blue"], C["blue_bg"]),
             (f"1 {one}", f"cost {_fmt(unit)}", C["red"], C["red_bg"]),
             (f"{_fmt(n2)} {item}", f"cost {_fmt(v2)}", C["green"], C["green_bg"])]

    bw, gap = 118, 42
    x0 = (W - (3 * bw + 2 * gap)) / 2
    for i, (top, bot, col, bg) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        _card(cv, x, 44, bw, 58, col, bg, sw=1.8 if i == 1 else 1.5)
        cv.text(x + bw / 2, 68, top, size=11.5, weight=700, color=col)
        cv.text(x + bw / 2, 88, bot, size=10, weight=700, color=C["ink"])
        if i < 2:
            ax, bx = x + bw + 5, x + bw + gap - 5
            cv.arrow(ax, 73, bx, 73, color=C["grey"], w=1.4)
            lab = f"div {_fmt(n1)}" if i == 0 else f"mult {_fmt(n2)}"
            cv.text((ax + bx) / 2, 62, lab, size=8, weight=700,
                    color=C["amber"])

    cv.text(x0 + bw / 2, 118, "given", size=8.6, color=C["soft"])
    cv.text(x0 + bw + gap + bw / 2, 118, "the ONE step", size=8.6,
            weight=700, color=C["red"])
    cv.text(x0 + 2 * (bw + gap) + bw / 2, 118, "asked", size=8.6,
            color=C["soft"])

    _card(cv, 46, 138, 360, 32, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 159, f"{_fmt(v1)} / {_fmt(n1)} x {_fmt(n2)} = {_fmt(v2)}",
            size=11.5, weight=700, color=C["purple"])
    cv.text(W / 2, 190, "this middle step is the whole method",
            size=9.4, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "it works because one unit never changes",
            size=8.4, color=C["soft"])
    return cv.svg()


# ─────────────────────────── direct vs inverse ──────────────────────────────
def direct_inverse(spec):
    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 1402))
    cv.text(W / 2, 20, "ask first: do they move together or opposite?",
            size=10.6, weight=700, color=C["soft"])

    panels = [
        ("DIRECT", "more gives more", C["green"], C["green_bg"],
         ["5 pens cost 60", "10 pens cost 120"], "a / b = c / d", "up , up"),
        ("INVERSE", "more gives less", C["red"], C["red_bg"],
         ["6 men take 12 days", "12 men take 6 days"], "a x b = c x d",
         "up , down"),
    ]
    pw = 196
    for i, (name, tag, col, bg, rows, rule, arrows) in enumerate(panels):
        x = 24 + i * (pw + 12)
        _card(cv, x, 36, pw, 178, col, bg, sw=1.7)
        cv.text(x + pw / 2, 58, name, size=12.5, weight=700, color=col)
        cv.text(x + pw / 2, 74, tag, size=9, color=C["soft"])

        for j, r in enumerate(rows):
            _card(cv, x + 14, 86 + j * 30, pw - 28, 24, col, "#ffffff", r=5,
                  sw=1.1)
            cv.text(x + pw / 2, 102 + j * 30, r, size=9.4, weight=700,
                    color=C["ink"])

        # arrow pair
        ax = x + pw / 2
        cv.arrow(ax - 30, 172, ax - 30, 152, color=col, w=1.6)
        if i == 0:
            cv.arrow(ax + 30, 172, ax + 30, 152, color=col, w=1.6)
        else:
            cv.arrow(ax + 30, 152, ax + 30, 172, color=col, w=1.6)
        cv.text(ax, 186, arrows, size=8.6, weight=700, color=C["soft"])

        _card(cv, x + 24, 192, pw - 48, 22, col, "#ffffff", r=5, sw=1.2)
        cv.text(x + pw / 2, 207, rule, size=9.6, weight=700, color=col)
    return cv.svg()


# ─────────────────────────── the given / asked grid ─────────────────────────
def proportion_table(spec):
    a = _fmt(float(spec.get("a", 5)))
    b = _fmt(float(spec.get("b", 60)))
    c = _fmt(float(spec.get("c", 8)))
    kind = str(spec.get("kind", "direct")).lower()
    inverse = kind.startswith("inv")

    try:
        if inverse:
            d = Fraction(int(float(spec.get("a", 5))) * int(float(spec.get("b", 60))),
                         int(float(spec.get("c", 8))))
        else:
            d = Fraction(int(float(spec.get("b", 60))) * int(float(spec.get("c", 8))),
                         int(float(spec.get("a", 5))))
        dtxt = _fmt(d)
    except Exception:
        dtxt = "x"

    W, H = 400, 224
    cv = Canvas(W, H, seed=_seed(spec, 1403))
    cv.text(W / 2, 20, "write the given row, then the asked row",
            size=10.6, weight=700, color=C["soft"])

    cw, ch = 128, 42
    x0 = (W - 2 * cw) / 2
    heads = [str(spec.get("h1", "quantity")), str(spec.get("h2", "cost"))]
    for j, h in enumerate(heads):
        cv.text(x0 + j * cw + cw / 2, 46, h, size=9.4, weight=700,
                color=C["soft"])

    cells = [[a, b], [c, dtxt]]
    for i, row in enumerate(cells):
        for j, v in enumerate(row):
            x, y = x0 + j * cw, 54 + i * ch
            last = (i == 1 and j == 1)
            col = C["red"] if last else C["blue"]
            bg = C["red_bg"] if last else C["blue_bg"]
            _card(cv, x + 3, y, cw - 6, ch - 6, col, bg, r=5,
                  sw=1.8 if last else 1.3)
            cv.text(x + cw / 2, y + 24, v, size=13, weight=700, color=col)
        cv.text(x0 - 10, 54 + i * ch + 24, "given" if i == 0 else "asked",
                size=8.8, anchor="end", weight=700, color=C["ink"])

    # the arrow: straight down for direct, crossed for inverse
    y1, y2 = 54 + 20, 54 + ch + 20
    if inverse:
        cv.line(x0 + 18, y1, x0 + cw + cw - 18, y2, color=C["amber"], w=1.6)
        cv.line(x0 + cw + cw - 18, y1, x0 + 18, y2, color=C["amber"], w=1.6)
        note = f"inverse: multiply across  ->  {a} x {b} = {c} x {dtxt}"
    else:
        cv.line(x0 + 18, y1, x0 + 18, y2, color=C["amber"], w=1.5)
        cv.line(x0 + 2 * cw - 18, y1, x0 + 2 * cw - 18, y2, color=C["amber"],
                w=1.5)
        note = f"direct: cross multiply  ->  {a} x {dtxt} = {b} x {c}"

    _card(cv, 26, 152, W - 52, 32, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(W / 2, 173, note, size=9.6, weight=700, color=C["amber"])

    _card(cv, (W - 190) / 2, 188, 190, 28, C["green"], C["green_bg"], sw=1.7)
    cv.text(W / 2, 207, f"answer = {dtxt}", size=11.5, weight=700,
            color=C["green"])
    return cv.svg()


# ─────────────────────────── chain rule ─────────────────────────────────────
def chain_rule(spec):
    m1 = _fmt(float(spec.get("m1", 12)))
    d1 = _fmt(float(spec.get("d1", 10)))
    h1 = _fmt(float(spec.get("h1", 8)))
    m2 = _fmt(float(spec.get("m2", 16)))
    h2 = _fmt(float(spec.get("h2", 6)))
    try:
        ans = Fraction(int(float(spec.get("m1", 12))) *
                       int(float(spec.get("d1", 10))) *
                       int(float(spec.get("h1", 8))),
                       int(float(spec.get("m2", 16))) *
                       int(float(spec.get("h2", 6))))
        atxt = _fmt(ans)
    except Exception:
        atxt = "D"

    W, H = 452, 216
    cv = Canvas(W, H, seed=_seed(spec, 1404))
    cv.text(W / 2, 20, "everything that helps goes on top, work at the bottom",
            size=10.2, weight=700, color=C["soft"])

    y = 52
    bw, bh = 40, 34
    labels = ["M", "D", "H"]

    def group(x0, vals, col, bg, tag):
        for k, v in enumerate(vals):
            x = x0 + k * (bw + 8)
            _card(cv, x, y, bw, bh, col, bg, r=5, sw=1.4)
            cv.text(x + bw / 2, y + 23, v, size=12, weight=700, color=col)
            cv.text(x + bw / 2, y - 6, labels[k], size=8.4, weight=700,
                    color=C["soft"])
        gw = 3 * bw + 2 * 8
        cv.line(x0 - 4, y + bh + 8, x0 + gw + 4, y + bh + 8, color=C["ink"],
                w=1.6)
        _card(cv, x0 + gw / 2 - 26, y + bh + 12, 52, 24, C["ink"], "#f2f3f7",
              r=5, sw=1.2)
        cv.text(x0 + gw / 2, y + bh + 29, "W", size=11, weight=700,
                color=C["ink"])
        cv.text(x0 + gw / 2, y + bh + 52, tag, size=8.8, weight=700,
                color=col)
        return gw

    gw = group(56, [m1, d1, h1], C["blue"], C["blue_bg"], "first situation")
    cv.text(W / 2, y + 24, "=", size=20, weight=700, color=C["ink"])
    group(W - 56 - gw, [m2, atxt, h2], C["green"], C["green_bg"],
          "second situation")

    _card(cv, 40, 158, 372, 30, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 178, f"D = ({m1} x {d1} x {h1}) / ({m2} x {h2}) = {atxt} days",
            size=10.4, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "M men, D days, H hours per day, W amount of work",
            size=8.4, color=C["soft"])
    return cv.svg()


# ─────────────────────────── men x days as an area ──────────────────────────
def man_days_grid(spec):
    m1 = int(spec.get("m1", 6))
    d1 = int(spec.get("d1", 12))
    m2 = int(spec.get("m2", 8))
    total = m1 * d1
    d2 = Fraction(total, m2)

    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 1405))
    cv.text(W / 2, 20, f"the work is always {total} man-days",
            size=10.6, weight=700, color=C["soft"])

    cell = 12
    ox = 52
    mid = 92                                   # common centre line

    # first block
    oy1 = mid - m1 * cell / 2
    for r in range(m1):
        for c in range(d1):
            cv.raw(f'<rect x="{ox+c*cell}" y="{oy1+r*cell}" width="{cell}" '
                   f'height="{cell}" fill="{C["blue_bg"]}" '
                   f'stroke="{C["blue"]}" stroke-width="0.7"/>')
    cv.text(ox + d1 * cell / 2, oy1 + m1 * cell + 15, f"{d1} days", size=9,
            weight=700, color=C["blue"])
    cv.text(ox - 8, mid + 4, f"{m1} men", size=9, anchor="end",
            weight=700, color=C["blue"])

    # second block
    ox2 = ox + d1 * cell + 88
    oy2 = mid - m2 * cell / 2
    for r in range(m2):
        for c in range(int(d2)):
            cv.raw(f'<rect x="{ox2+c*cell}" y="{oy2+r*cell}" width="{cell}" '
                   f'height="{cell}" fill="{C["green_bg"]}" '
                   f'stroke="{C["green"]}" stroke-width="0.7"/>')
    cv.text(ox2 + int(d2) * cell / 2, oy2 + m2 * cell + 15,
            f"{_fmt(d2)} days", size=9, weight=700, color=C["green"])
    cv.text(ox2 + int(d2) * cell + 8, mid + 4, f"{m2} men", size=9,
            anchor="start", weight=700, color=C["green"])

    cv.text((ox + d1 * cell + ox2) / 2, mid + 7, "=", size=19, weight=700,
            color=C["ink"])

    _card(cv, 44, 176, 364, 32, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 197, f"{m1} x {d1} = {m2} x {_fmt(d2)} = {total}",
            size=11.5, weight=700, color=C["amber"])
    cv.text(W / 2, 226, "same number of squares, only the shape changes",
            size=9.2, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── partial work bar ───────────────────────────────
def partial_work(spec):
    m1 = int(spec.get("men", 24))
    d1 = int(spec.get("days", 40))
    after = int(spec.get("after", 10))
    change = int(spec.get("change", -4))

    total = m1 * d1
    done = m1 * after
    left = total - done
    m2 = m1 + change
    d2 = Fraction(left, m2)

    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 1406))
    cv.text(W / 2, 20, f"the job is {total} man-days, no matter who works",
            size=10.4, weight=700, color=C["soft"])

    bx, bw, by, bh = 40, W - 80, 44, 42
    dw = bw * done / total
    _card(cv, bx, by, dw, bh, C["blue"], C["blue_bg"], r=5, sw=1.6)
    cv.text(bx + dw / 2, by + 20, f"{done}", size=11.5, weight=700,
            color=C["blue"])
    cv.text(bx + dw / 2, by + 34, "done", size=8.4, color=C["soft"])

    _card(cv, bx + dw, by, bw - dw, bh, C["amber"], C["amber_bg"], r=5,
          sw=1.6)
    cv.text(bx + dw + (bw - dw) / 2, by + 20, f"{left}", size=11.5,
            weight=700, color=C["amber"])
    cv.text(bx + dw + (bw - dw) / 2, by + 34, "still left", size=8.4,
            color=C["soft"])

    cv.text(bx + dw / 2, by - 8, f"{m1} men x {after} days", size=8.6,
            weight=700, color=C["blue"])

    rows = [
        (f"whole job = {m1} x {d1}", f"{total} man-days", C["ink"], "#f2f3f7"),
        (f"first {after} days = {m1} x {after}", f"{done} man-days",
         C["blue"], C["blue_bg"]),
        ("so what remains", f"{left} man-days", C["amber"], C["amber_bg"]),
        (f"now {m2} men work", f"{left} / {m2} = {_fmt(d2)} days",
         C["green"], C["green_bg"]),
    ]
    for i, (lab, val, col, bg) in enumerate(rows):
        y = 104 + i * 28
        _card(cv, 40, y, 372, 24, col, bg, r=5, sw=1.2)
        cv.text(52, y + 16, lab, size=9, anchor="start", color=C["soft"])
        cv.text(400, y + 16, val, size=9.6, anchor="end", weight=700,
                color=col)

    cv.text(W / 2, H - 10, f"total time = {after} + {_fmt(d2)} = "
            f"{_fmt(after + d2)} days", size=10.4, weight=700, color=C["red"])
    return cv.svg()


REGISTRY = {
    "unitary-steps": unitary_steps,
    "direct-inverse": direct_inverse,
    "proportion-table": proportion_table,
    "chain-rule": chain_rule,
    "man-days-grid": man_days_grid,
    "partial-work": partial_work,
}
