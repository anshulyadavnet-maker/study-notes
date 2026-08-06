"""
wordprob.py — figures for Chapter 10 (Number Word Problems).

digit-place      : why a two-digit number is 10T + U, drawn as place columns
reverse-digits   : N and its reverse side by side, with the 9(T-U) result
translate-table  : Hindi/English phrase -> algebraic symbol dictionary
consecutive-line : consecutive / even / odd runs marked on a number line
sum-diff-bars    : sum-and-difference solved as two bars
equation-steps   : an equation solved step by step, one operation per row
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


# ─────────────────────────── place value of a 2-digit number ────────────────
def digit_place(spec):
    n = int(spec.get("number", 36))
    T, U = n // 10, n % 10

    W, H = 420, 226
    cv = Canvas(W, H, seed=_seed(spec, 1001))
    cv.text(W / 2, 20, f"why {n} is written as 10T + U", size=10.5,
            weight=700, color=C["soft"])

    bw = 92
    x1, x2 = 88, 88 + bw + 40

    for x, lab, dig, mult, val, col, bg in (
            (x1, "tens digit  T", T, "x 10", T * 10, C["blue"], C["blue_bg"]),
            (x2, "units digit  U", U, "x 1", U, C["green"], C["green_bg"])):
        _card(cv, x, 34, bw, 44, col, bg, sw=1.7)
        cv.text(x + bw / 2, 66, str(dig), size=24, weight=700, color=col)
        cv.text(x + bw / 2, 92, lab, size=8.6, color=C["soft"])
        cv.arrow(x + bw / 2, 100, x + bw / 2, 122, color=C["grey"], w=1.2)
        _card(cv, x + 10, 124, bw - 20, 26, col, "#ffffff", r=5, sw=1.3)
        cv.text(x + bw / 2, 142, mult, size=9.6, weight=700, color=col)
        cv.arrow(x + bw / 2, 152, x + bw / 2, 168, color=C["grey"], w=1.2)
        cv.text(x + bw / 2, 182, str(val), size=14, weight=700, color=col)

    cv.text((x1 + bw + x2) / 2, 182, "+", size=16, weight=700, color=C["ink"])

    _card(cv, 84, 194, 250, 26, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(209, 212, f"10 x {T} + {U} = {n}", size=11.5, weight=700,
            color=C["purple"])
    return cv.svg()


# ─────────────────────────── number and its reverse ─────────────────────────
def reverse_digits(spec):
    n = int(spec.get("number", 36))
    T, U = n // 10, n % 10
    r = 10 * U + T

    W, H = 452, 210
    cv = Canvas(W, H, seed=_seed(spec, 1002))
    cv.text(W / 2, 20, "reversing swaps the two digits", size=10.5,
            weight=700, color=C["soft"])

    bw = 132
    x1, x2 = 52, W - 52 - bw

    for x, val, a, b, lab, col, bg in (
            (x1, n, T, U, "original  N", C["blue"], C["blue_bg"]),
            (x2, r, U, T, "reversed  R", C["red"], C["red_bg"])):
        _card(cv, x, 34, bw, 48, col, bg, sw=1.7)
        cv.text(x + bw / 2, 68, str(val), size=26, weight=700, color=col)
        cv.text(x + bw / 2, 96, lab, size=9, weight=700, color=C["soft"])
        cv.text(x + bw / 2, 112, f"= 10 x {a} + {b}", size=9.4, color=C["ink"])

    cv.arrow(x1 + bw + 8, 58, x2 - 8, 58, color=C["grey"], w=1.4)
    cv.text((x1 + bw + x2) / 2, 48, "swap", size=9, weight=700,
            color=C["grey"])

    _card(cv, 40, 130, 180, 30, C["green"], C["green_bg"], sw=1.5)
    cv.text(130, 150, f"R - N = 9 x (U - T)", size=10.6, weight=700,
            color=C["green"])
    _card(cv, 232, 130, 180, 30, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(322, 150, f"R + N = 11 x (T + U)", size=10.6, weight=700,
            color=C["amber"])

    cv.text(W / 2, 182, f"here  {r} - {n} = {r-n} = 9 x {U-T}"
            f"    and    {r} + {n} = {r+n} = 11 x {T+U}",
            size=9.2, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8,
            "so a difference always divides by 9, a sum always by 11",
            size=8.4, color=C["soft"])
    return cv.svg()


# ─────────────────────────── phrase to symbol table ─────────────────────────
def translate_table(spec):
    rows = [
        ("a number", "x", C["blue"]),
        ("twice / double", "2x", C["blue"]),
        ("three more than", "x + 3", C["green"]),
        ("five less than", "x - 5", C["green"]),
        ("half of", "x / 2", C["amber"]),
        ("one third of", "x / 3", C["amber"]),
        ("exceeds by 7", "x - y = 7", C["red"]),
        ("is / equals", "=", C["red"]),
        ("sum of the digits", "T + U", C["purple"]),
        ("the number itself", "10T + U", C["purple"]),
        ("reversed number", "10U + T", C["teal"]),
        ("consecutive", "x , x+1 , x+2", C["teal"]),
    ]
    cols, cw, ch, gx, gy = 2, 214, 30, 16, 8
    n = (len(rows) + cols - 1) // cols
    W = 20 + cols * cw + (cols - 1) * gx + 20
    H = 36 + n * (ch + gy)
    cv = Canvas(W, H, seed=_seed(spec, 1003))
    cv.text(W / 2, 18, "the phrase dictionary", size=10.5, weight=700,
            color=C["soft"])

    for i, (phrase, sym, col) in enumerate(rows):
        r, c = divmod(i, cols)
        x = 20 + c * (cw + gx)
        y = 28 + r * (ch + gy)
        _card(cv, x, y, cw, ch, col, "#ffffff", r=5, sw=1.2)
        cv.text(x + 9, y + 20, phrase, size=8.8, anchor="start",
                color=C["soft"])
        cv.raw(f'<rect x="{x+cw-84}" y="{y+4}" width="80" height="22" rx="4" '
               f'fill="{C["paper"]}" stroke="{col}" stroke-width="1.1"/>')
        cv.text(x + cw - 44, y + 20, sym, size=9.6, weight=700, color=col)
    return cv.svg()


# ─────────────────────────── consecutive runs ───────────────────────────────
def consecutive_line(spec):
    start = int(spec.get("start", 20))
    kind = str(spec.get("kind", "even")).lower()
    count = int(spec.get("count", 3))
    step = 2 if kind in ("even", "odd") else 1

    vals = [start + i * step for i in range(count)]
    lo, hi = vals[0] - 2, vals[-1] + 2

    W, H = 452, 176
    cv = Canvas(W, H, seed=_seed(spec, 1004))
    y = 92
    x0, x1 = 44, W - 44
    span = hi - lo
    sx = (x1 - x0) / span

    cv.line(x0 - 8, y, x1 + 8, y, color=C["ink"], w=1.6)
    cv.arrow(x1 - 8, y, x1 + 12, y, color=C["ink"], w=1.4)

    for v in range(lo, hi + 1):
        px = x0 + (v - lo) * sx
        on = v in vals
        cv.line(px, y - (8 if on else 5), px, y + (8 if on else 5),
                color=C["ink"] if on else C["grey"], w=1.5 if on else 1.0)
        cv.text(px, y + 24, str(v), size=9.4 if on else 8.2,
                weight=700 if on else 400,
                color=C["ink"] if on else C["grey"])
        if on:
            cv.dot(px, y, r=4.4, color=C["blue"])

    labels = ["x", f"x + {step}", f"x + {2*step}", f"x + {3*step}"]
    for i, v in enumerate(vals):
        px = x0 + (v - lo) * sx
        _card(cv, px - 27, y - 44, 54, 24, C["blue"], C["blue_bg"], r=5,
              sw=1.3)
        cv.text(px, y - 28, labels[i] if i < len(labels) else "...",
                size=9, weight=700, color=C["blue"])

    total = sum(vals)
    _card(cv, (W - 300) / 2, H - 44, 300, 30, C["green"], C["green_bg"],
          sw=1.6)
    mid = vals[len(vals) // 2]
    extra = f" = {count} x {mid}" if count % 2 else ""
    cv.text(W / 2, H - 24, f"sum = {' + '.join(str(v) for v in vals)}"
            f" = {total}{extra}", size=9.6, weight=700, color=C["green"])
    cv.text(W / 2, 20,
            f"{count} consecutive {kind} numbers, gap of {step}",
            size=10, weight=700, color=C["soft"])
    return cv.svg()


# ─────────────────────────── sum and difference bars ────────────────────────
def sum_diff_bars(spec):
    s = int(spec.get("sum", 25))
    d = int(spec.get("diff", 7))
    big, small = (s + d) // 2, (s - d) // 2

    W, H = 452, 214
    cv = Canvas(W, H, seed=_seed(spec, 1005))
    cv.text(W / 2, 20, f"sum {s} and difference {d}", size=10.5, weight=700,
            color=C["soft"])

    unit = (W - 130) / s
    x0 = 88

    # bar 1 - larger
    _card(cv, x0, 36, small * unit, 30, C["blue"], C["blue_bg"], r=4, sw=1.4)
    cv.text(x0 + small * unit / 2, 56, str(small), size=11, weight=700,
            color=C["blue"])
    _card(cv, x0 + small * unit, 36, d * unit, 30, C["red"], C["red_bg"], r=4,
          sw=1.4)
    cv.text(x0 + small * unit + d * unit / 2, 56, str(d), size=11, weight=700,
            color=C["red"])
    cv.text(x0 - 10, 56, "larger", size=9, anchor="end", weight=700,
            color=C["ink"])

    # bar 2 - smaller
    _card(cv, x0, 82, small * unit, 30, C["blue"], C["blue_bg"], r=4, sw=1.4)
    cv.text(x0 + small * unit / 2, 102, str(small), size=11, weight=700,
            color=C["blue"])
    cv.text(x0 - 10, 102, "smaller", size=9, anchor="end", weight=700,
            color=C["ink"])

    # total brace
    cv.raw(f'<path d="M{x0} 122 L{x0} 130 L{x0+s*unit} 130 L{x0+s*unit} 122" '
           f'fill="none" stroke="{C["grey"]}" stroke-width="1.3"/>')
    cv.text(x0 + s * unit / 2, 146, f"both bars together = {s}", size=9.4,
            weight=700, color=C["soft"])

    _card(cv, 26, 158, 196, 30, C["green"], C["green_bg"], sw=1.5)
    cv.text(124, 178, f"larger = (S + D)/2 = {big}", size=9.6, weight=700,
            color=C["green"])
    _card(cv, 230, 158, 196, 30, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(328, 178, f"smaller = (S - D)/2 = {small}", size=9.6, weight=700,
            color=C["amber"])
    cv.text(W / 2, H - 8, "remove the difference, split what is left in two",
            size=8.6, color=C["ink"])
    return cv.svg()


# ─────────────────────────── equation solved in steps ───────────────────────
def equation_steps(spec):
    lines = str(spec.get("lines",
                         "2x + 5 = 25|2x = 20|x = 10")).split("|")
    notes = str(spec.get("notes", "given|subtract 5|divide by 2")).split("|")

    W = 400
    H = 40 + len(lines) * 42 + 16
    cv = Canvas(W, H, seed=_seed(spec, 1006))
    cv.text(W / 2, 20, "one operation on each line", size=10, weight=700,
            color=C["soft"])

    for i, ln in enumerate(lines):
        y = 30 + i * 42
        last = (i == len(lines) - 1)
        col = C["green"] if last else C["blue"]
        bg = C["green_bg"] if last else C["blue_bg"]
        _card(cv, 30, y, 200, 32, col, bg, sw=1.8 if last else 1.3)
        cv.text(130, y + 21, ln.strip(), size=12, weight=700, color=col)
        if i < len(notes):
            cv.text(244, y + 21, notes[i].strip(), size=8.8, anchor="start",
                    color=C["soft"])
        if not last:
            cv.arrow(130, y + 34, 130, y + 40, color=C["grey"], w=1.2)
    return cv.svg()


REGISTRY = {
    "digit-place": digit_place,
    "reverse-digits": reverse_digits,
    "translate-table": translate_table,
    "consecutive-line": consecutive_line,
    "sum-diff-bars": sum_diff_bars,
    "equation-steps": equation_steps,
}
