"""
series.py — figures for Chapter 8 (Number Series).

series-chain     : terms in boxes with the operation written on each arrow
series-diff      : the successive-difference ladder (1st, 2nd, 3rd row)
series-family    : classification of the common series families
series-alternate : two interleaved series drawn in two colours
wrong-number     : the odd term highlighted against the corrected value
ap-gp-growth     : AP versus GP plotted as bars so the shape is visible
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


def _nums(spec, key="terms", default="7,12,17,22,27"):
    raw = str(spec.get(key, default))
    out = []
    for t in raw.split(","):
        t = t.strip()
        if not t:
            continue
        out.append(t)
    return out


def _fmt(v):
    if isinstance(v, float) and abs(v - round(v)) < 1e-9:
        v = int(round(v))
    return str(v)


# ─────────────────────────── chain with labelled arrows ─────────────────────
def series_chain(spec):
    terms = _nums(spec)
    ops = _nums(spec, "ops", "")
    show_q = str(spec.get("ask", "yes")).lower() in ("yes", "1", "true")
    if show_q:
        terms = terms + ["?"]

    bw, bh, gap = 62, 40, 46
    W = 24 + len(terms) * bw + (len(terms) - 1) * gap + 24
    H = 128
    cv = Canvas(W, H, seed=_seed(spec, 801))
    y = 46

    for i, t in enumerate(terms):
        x = 24 + i * (bw + gap)
        last = (t == "?")
        col = C["red"] if last else C["blue"]
        bg = C["red_bg"] if last else C["blue_bg"]
        _card(cv, x, y, bw, bh, col, bg, sw=1.7 if last else 1.4)
        cv.text(x + bw / 2, y + 27, t, size=15, weight=700, color=col)
        cv.text(x + bw / 2, y + bh + 16, f"T{i+1}", size=8, color=C["soft"])

        if i < len(terms) - 1:
            ax, bx = x + bw + 4, x + bw + gap - 4
            cv.arrow(ax, y + bh / 2, bx, y + bh / 2, color=C["grey"], w=1.3)
            if i < len(ops):
                mid = (ax + bx) / 2
                _card(cv, mid - 21, y - 6, 42, 20, C["green"], "#ffffff",
                      r=5, sw=1.2)
                cv.text(mid, y + 8, ops[i], size=9.4, weight=700,
                        color=C["green"])

    cap = str(spec.get("note", ""))
    if cap:
        cv.text(W / 2, H - 12, cap, size=9, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── difference ladder ──────────────────────────────
def series_diff(spec):
    vals = [float(v) for v in _nums(spec, "terms", "6,11,21,36,56,81")]
    rows = int(spec.get("rows", 2))

    layers = [vals]
    for _ in range(rows):
        prev = layers[-1]
        if len(prev) < 2:
            break
        layers.append([prev[i + 1] - prev[i] for i in range(len(prev) - 1)])

    bw, gap = 58, 20
    step = bw + gap
    W = 30 + len(vals) * step + 76
    H = 46 + len(layers) * 60
    cv = Canvas(W, H, seed=_seed(spec, 802))

    palette = [(C["blue"], C["blue_bg"]), (C["amber"], C["amber_bg"]),
               (C["green"], C["green_bg"]), (C["purple"], C["purple_bg"])]
    labels = ["series", "1st difference", "2nd difference", "3rd difference"]

    for li, layer in enumerate(layers):
        col, bg = palette[li % len(palette)]
        y = 40 + li * 60
        offset = 30 + li * step / 2
        cv.text(14, y + 18, "", size=8)
        for i, v in enumerate(layer):
            x = offset + i * step
            _card(cv, x, y, bw, 30, col, bg, sw=1.4)
            cv.text(x + bw / 2, y + 20, _fmt(v), size=12, weight=700, color=col)
            if li + 1 < len(layers):
                cv.line(x + bw / 2, y + 32, x + bw / 2 + step / 2 - 4,
                        y + 56, color=C["grey"], w=1.0)
                if i + 1 < len(layer):
                    cv.line(x + bw + gap + bw / 2, y + 32,
                            x + bw / 2 + step / 2 + 4, y + 56,
                            color=C["grey"], w=1.0)
        cv.text(W - 8, y + 20, labels[li] if li < len(labels) else "",
                size=8.2, anchor="end", color=C["soft"])

    last = layers[-1]
    same = len(set(_fmt(v) for v in last)) == 1 and len(last) > 1
    msg = (f"row is constant at {_fmt(last[0])}  ->  the rule is fixed"
           if same else "keep taking differences until a row repeats")
    cv.text(W / 2, 18, msg, size=9.6, weight=700,
            color=C["green"] if same else C["soft"])
    return cv.svg()


# ─────────────────────────── family of series ───────────────────────────────
def series_family(spec):
    fams = [
        ("ADD / SUBTRACT", "7, 12, 17, 22", "same gap each step", C["blue"], C["blue_bg"]),
        ("MULTIPLY / DIVIDE", "3, 6, 12, 24", "same ratio each step", C["green"], C["green_bg"]),
        ("SQUARE BASED", "2, 5, 10, 17", "n\u00b2 + 1", C["amber"], C["amber_bg"]),
        ("CUBE BASED", "3, 10, 29, 66", "n\u00b3 + 2", C["purple"], C["purple_bg"]),
        ("MIXED  xa + b", "5, 11, 23, 47", "x2 + 1 each step", C["red"], C["red_bg"]),
        ("TWO INTERLEAVED", "2, 8, 5, 11", "alternate terms", C["teal"], C["teal_bg"]),
        ("GROWING GAP", "6, 11, 21, 36", "gap 5, 10, 15", C["pink"], C["pink_bg"]),
        ("SPECIAL LISTS", "2, 3, 5, 7", "primes, factorials", C["ink"], "#f2f3f7"),
    ]
    cols, cw, ch, gx, gy = 2, 216, 50, 14, 10
    rows = (len(fams) + cols - 1) // cols
    W = 20 + cols * cw + (cols - 1) * gx + 20
    H = 34 + rows * (ch + gy)
    cv = Canvas(W, H, seed=_seed(spec, 803))
    cv.text(W / 2, 18, "the eight families that cover almost every question",
            size=10, weight=700, color=C["soft"])

    for i, (name, ex, note, col, bg) in enumerate(fams):
        r, c = divmod(i, cols)
        x = 20 + c * (cw + gx)
        y = 28 + r * (ch + gy)
        _card(cv, x, y, cw, ch, col, bg)
        cv.raw(f'<circle cx="{x+18}" cy="{y+ch/2}" r="12" fill="{col}"/>')
        cv.text(x + 18, y + ch / 2 + 4, str(i + 1), size=11, weight=700,
                color="#ffffff")
        cv.text(x + 36, y + 18, name, size=9.2, weight=700, color=col,
                anchor="start")
        cv.text(x + 36, y + 31, ex, size=9.6, weight=700, color=C["ink"],
                anchor="start")
        cv.text(x + 36, y + 43, note, size=7.8, color=C["soft"], anchor="start")
    return cv.svg()


# ─────────────────────────── two interleaved series ─────────────────────────
def series_alternate(spec):
    terms = _nums(spec, "terms", "2,8,5,11,8,14,11")
    bw, gap = 54, 18
    W = 30 + len(terms) * (bw + gap)
    H = 216
    cv = Canvas(W, H, seed=_seed(spec, 804))
    ymid = 112

    for i, t in enumerate(terms):
        x = 24 + i * (bw + gap)
        odd = (i % 2 == 0)
        col = C["blue"] if odd else C["red"]
        bg = C["blue_bg"] if odd else C["red_bg"]
        y = ymid - 46 if odd else ymid + 12
        _card(cv, x, y, bw, 34, col, bg)
        cv.text(x + bw / 2, y + 23, t, size=13.5, weight=700, color=col)
        cv.line(x + bw / 2, ymid - 4, x + bw / 2, ymid + 4, color=C["grey"],
                w=1.0)

    # linking arcs, drawn clear of the boxes
    for start, col in ((0, C["blue"]), (1, C["red"])):
        idx = list(range(start, len(terms), 2))
        for a, b in zip(idx, idx[1:]):
            xa = 24 + a * (bw + gap) + bw / 2
            xb = 24 + b * (bw + gap) + bw / 2
            if start == 0:
                y, sweep = ymid - 52, 1
            else:
                y, sweep = ymid + 54, 0
            r = (xb - xa) / 2
            cv.raw(f'<path d="M{xa} {y} A {r} {r*0.22} 0 0 {sweep} {xb} {y}" '
                   f'fill="none" stroke="{col}" stroke-width="1.3" '
                   f'stroke-dasharray="4 3"/>')

    cv.text(W / 2, 18, "odd places make one series, even places make another",
            size=9.6, weight=700, color=C["soft"])
    cv.text(22, ymid - 40, "A", size=10.5, weight=700, color=C["blue"],
            anchor="end")
    cv.text(22, ymid + 34, "B", size=10.5, weight=700, color=C["red"],
            anchor="end")
    cv.text(W / 2, H - 6, "solve each colour on its own",
            size=8.6, color=C["ink"])
    return cv.svg()


# ─────────────────────────── wrong number spotting ──────────────────────────
def wrong_number(spec):
    terms = _nums(spec, "terms", "2,6,12,20,30,44,56")
    bad = int(spec.get("index", 6))          # 1-based position of wrong term
    right = str(spec.get("correct", "42"))

    bw, gap = 60, 16
    W = 28 + len(terms) * (bw + gap)
    H = 176
    cv = Canvas(W, H, seed=_seed(spec, 805))
    y = 52

    for i, t in enumerate(terms):
        x = 22 + i * (bw + gap)
        wrong = (i + 1 == bad)
        col = C["red"] if wrong else C["blue"]
        bg = C["red_bg"] if wrong else C["blue_bg"]
        _card(cv, x, y, bw, 36, col, bg, sw=2.0 if wrong else 1.3)
        cv.text(x + bw / 2, y + 25, t, size=14, weight=700, color=col)
        if wrong:
            cv.line(x + 6, y + 6, x + bw - 6, y + 30, color=C["red"], w=1.8)
            cv.arrow(x + bw / 2, y + 42, x + bw / 2, y + 62, color=C["green"],
                     w=1.4)
            _card(cv, x - 6, y + 64, bw + 12, 30, C["green"], C["green_bg"],
                  sw=1.7)
            cv.text(x + bw / 2, y + 85, right, size=13.5, weight=700,
                    color=C["green"])

    cv.text(W / 2, 22, "find the term that breaks the rule",
            size=10, weight=700, color=C["soft"])
    note = str(spec.get("note", "every other term follows the pattern"))
    cv.text(W / 2, H - 12, note, size=8.8, weight=700, color=C["ink"])
    return cv.svg()


# ─────────────────────────── AP vs GP growth ────────────────────────────────
def ap_gp_growth(spec):
    n = int(spec.get("n", 6))
    a1, d = float(spec.get("a", 3)), float(spec.get("d", 3))
    g1, r = float(spec.get("g", 3)), float(spec.get("r", 2))

    ap = [a1 + i * d for i in range(n)]
    gp = [g1 * r ** i for i in range(n)]
    top = max(max(ap), max(gp))

    W, H = 452, 252
    cv = Canvas(W, H, seed=_seed(spec, 806))
    base = H - 46
    plot = 132
    bw = 15
    slot = (W - 70) / n

    for i in range(n):
        x = 44 + i * slot
        ha = ap[i] / top * plot
        hg = gp[i] / top * plot
        cv.raw(f'<rect x="{x}" y="{base-ha:.1f}" width="{bw}" height="{ha:.1f}" '
               f'rx="3" fill="{C["blue_bg"]}" stroke="{C["blue"]}" '
               f'stroke-width="1.3"/>')
        cv.raw(f'<rect x="{x+bw+4}" y="{base-hg:.1f}" width="{bw}" '
               f'height="{hg:.1f}" rx="3" fill="{C["red_bg"]}" '
               f'stroke="{C["red"]}" stroke-width="1.3"/>')
        cv.text(x + bw / 2, base - ha - 5, _fmt(ap[i]), size=7.6,
                color=C["blue"], weight=700)
        cv.text(x + bw + 4 + bw / 2, base - hg - 5, _fmt(gp[i]), size=7.6,
                color=C["red"], weight=700)
        cv.text(x + bw + 2, base + 15, f"T{i+1}", size=7.8, color=C["soft"])

    cv.line(36, base, W - 20, base, color=C["ink"], w=1.5)

    _card(cv, 44, 22, 168, 26, C["blue"], C["blue_bg"], r=5, sw=1.3)
    cv.text(128, 39, f"AP  a={_fmt(a1)} , d={_fmt(d)}  (adds)", size=9,
            weight=700, color=C["blue"])
    _card(cv, 226, 22, 182, 26, C["red"], C["red_bg"], r=5, sw=1.3)
    cv.text(317, 39, f"GP  a={_fmt(g1)} , r={_fmt(r)}  (multiplies)", size=9,
            weight=700, color=C["red"])

    cv.text(W / 2, H - 10,
            "an AP climbs like a staircase, a GP shoots up",
            size=9, weight=700, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "series-chain": series_chain,
    "series-diff": series_diff,
    "series-family": series_family,
    "series-alternate": series_alternate,
    "wrong-number": wrong_number,
    "ap-gp-growth": ap_gp_growth,
}
