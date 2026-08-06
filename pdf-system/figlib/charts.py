"""
charts.py — Venn diagrams, pie / bar / line charts, dice, clock.
Latin + numeral labels only (Devanagari goes in the caption).
"""
import math
from .sketch import Canvas, C


def _seed(spec, d=7):
    s = spec.get("seed", d)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


def _num(v):
    f = float(v)
    return str(int(f)) if f == int(f) else f"{f:g}"


# ───────────────────────── Venn ─────────────────────────
def venn(spec):
    """sets: 2 or 3 | labels | values (regions) | kind: overlap|subset|disjoint"""
    nsets = int(spec.get("sets", 2))
    kind = spec.get("kind", "overlap")
    labs = spec.get("labels", ["A", "B", "C"])
    vals = spec.get("values", [])
    if not isinstance(vals, list):
        vals = [vals]
    W, H = 300, 205
    cv = Canvas(W, H, seed=_seed(spec, 83))

    if nsets == 2:
        r = 66
        if kind == "disjoint":
            c1, c2 = (86, 100), (214, 100)
        elif kind == "subset":
            c1, c2 = (150, 100), (168, 100)
            r2 = 34
            cv.circle(*c1, r, color=C["blue"], w=1.8, fill=C["blue_bg"])
            cv.circle(*c2, r2, color=C["green"], w=1.7, fill=C["green_bg"])
            cv.text(150, 44, labs[0], size=11.5, color=C["blue"], weight=600)
            cv.text(168, 104, labs[1], size=11, color=C["green"], weight=600)
            cv.text(W / 2, H - 8, spec.get("note", ""), size=9.4, color=C["soft"])
            return cv.svg()
        else:
            c1, c2 = (112, 100), (188, 100)
        cv.circle(*c1, r, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.circle(*c2, r, color=C["green"], w=1.8, fill=C["green_bg"])
        cv.text(c1[0] - 20, 34, labs[0], size=12, color=C["blue"], weight=700)
        cv.text(c2[0] + 20, 34, labs[1], size=12, color=C["green"], weight=700)
        if vals:
            spots = [(c1[0] - 26, 106), (150, 106), (c2[0] + 26, 106)] \
                if kind != "disjoint" else [(c1[0], 106), None, (c2[0], 106)]
            for v, s in zip(vals, [p for p in spots if p]):
                cv.text(s[0], s[1], str(v), size=12, weight=700, color=C["ink"])
    else:
        r = 54
        c1, c2, c3 = (114, 84), (186, 84), (150, 142)
        for c, col, bg in ((c1, C["blue"], C["blue_bg"]),
                           (c2, C["green"], C["green_bg"]),
                           (c3, C["amber"], C["amber_bg"])):
            cv.circle(*c, r, color=col, w=1.7, fill=bg)
        cv.text(c1[0] - 34, 40, labs[0], size=11.5, color=C["blue"], weight=700)
        cv.text(c2[0] + 34, 40, labs[1], size=11.5, color=C["green"], weight=700)
        cv.text(c3[0], H - 22, labs[2], size=11.5, color=C["amber"], weight=700)
        if vals:
            spots = [(92, 78), (208, 78), (150, 162), (150, 74),
                     (118, 120), (182, 120), (150, 106)]
            for v, s in zip(vals, spots):
                cv.text(s[0], s[1], str(v), size=10.5, weight=700)
    cv.text(W / 2, H - 6, spec.get("note", ""), size=9.4, color=C["soft"])
    return cv.svg()


# ───────────────────────── pie ─────────────────────────
def pie(spec):
    labels = spec.get("labels", [])
    values = [float(v) for v in spec.get("values", [])]
    if not values:
        return "<svg/>"
    total = sum(values)
    W, H = 320, 232
    cx, cy, r = 108, 112, 84
    cv = Canvas(W, H, seed=_seed(spec, 89))
    cols = [C["blue"], C["green"], C["amber"], C["purple"], C["teal"], C["pink"]]
    bgs = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["purple_bg"],
           C["teal_bg"], C["pink_bg"]]
    a = -math.pi / 2
    for i, v in enumerate(values):
        sweep = 2 * math.pi * v / total
        steps = max(6, int(sweep / 0.2))
        arc = [(cx + r * math.cos(a + sweep * t / steps),
                cy + r * math.sin(a + sweep * t / steps))
               for t in range(steps + 1)]
        d = f"M{cx},{cy} L" + " L".join(f"{x:.1f},{y:.1f}" for x, y in arc) + " Z"
        cv.raw(f'<path d="{d}" fill="{bgs[i%6]}" stroke="none"/>')
        cv.line(cx, cy, arc[0][0], arc[0][1], color=cols[i % 6], w=1.4)
        mid = a + sweep / 2
        pct = v / total * 100
        if pct >= 6:
            cv.text(cx + r * 0.62 * math.cos(mid), cy + r * 0.62 * math.sin(mid) + 4,
                    f"{pct:.0f}%", size=10, weight=700, color=cols[i % 6])
        a += sweep
    cv.circle(cx, cy, r, color=C["ink"], w=1.7)
    # legend
    lx, ly = 210, 44
    for i, lab in enumerate(labels):
        cv.raw(f'<rect x="{lx}" y="{ly+i*22-9}" width="12" height="12" rx="2" '
               f'fill="{bgs[i%6]}" stroke="{cols[i%6]}" stroke-width="1.2"/>')
        deg = values[i] / total * 360
        cv.text(lx + 18, ly + i * 22 + 1, f"{lab} ({deg:.0f}°)", size=9.5,
                anchor="start", color=C["ink"])
    cv.text(W / 2, H - 6, spec.get("note", "1% = 3.6 degrees"), size=9.2,
            color=C["soft"])
    return cv.svg()


# ───────────────────────── bar ─────────────────────────
def bar(spec):
    labels = spec.get("labels", [])
    values = [float(v) for v in spec.get("values", [])]
    if not values:
        return "<svg/>"
    W, H = 320, 215
    ox, oy = 44, 162
    plot_w, plot_h = 252, 118
    mx = max(values) * 1.12
    cv = Canvas(W, H, seed=_seed(spec, 97))
    # axes + gridlines
    for i in range(5):
        gy = oy - plot_h * i / 4
        cv.raw(f'<line x1="{ox}" y1="{gy}" x2="{ox+plot_w}" y2="{gy}" '
               f'stroke="#e6eaf3" stroke-width="0.8"/>')
        cv.text(ox - 7, gy + 3.5, _num(round(mx * i / 4)), size=8.6,
                color=C["grey"], anchor="end")
    cv.line(ox, oy, ox + plot_w, oy, color=C["ink"], w=1.5)
    cv.line(ox, oy, ox, oy - plot_h, color=C["ink"], w=1.5)
    n = len(values)
    slot = plot_w / n
    bw = slot * 0.56
    cols = [C["blue"], C["green"], C["amber"], C["purple"], C["teal"], C["pink"]]
    bgs = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["purple_bg"],
           C["teal_bg"], C["pink_bg"]]
    for i, v in enumerate(values):
        h = plot_h * v / mx
        bx = ox + slot * i + (slot - bw) / 2
        cv.rect(bx, oy - h, bw, h, color=cols[i % 6], w=1.5, fill=bgs[i % 6])
        cv.text(bx + bw / 2, oy - h - 6, _num(v), size=9.2, weight=700,
                color=cols[i % 6])
        if i < len(labels):
            cv.text(bx + bw / 2, oy + 15, str(labels[i]), size=9, color=C["ink"])
    cv.text(W / 2, H - 5, spec.get("note", ""), size=9.2, color=C["soft"])
    return cv.svg()


# ───────────────────────── dice ─────────────────────────
PIPS = {
    1: [(0, 0)],
    2: [(-1, -1), (1, 1)],
    3: [(-1, -1), (0, 0), (1, 1)],
    4: [(-1, -1), (1, -1), (-1, 1), (1, 1)],
    5: [(-1, -1), (1, -1), (0, 0), (-1, 1), (1, 1)],
    6: [(-1, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (1, 1)],
}


def _die(cv, ox, oy, s, top, front, right):
    """isometric die: top face, front face, right face"""
    d = s * 0.42
    f = [(ox, oy + d), (ox + s, oy + d), (ox + s, oy + d + s), (ox, oy + d + s)]
    cv.polygon(f, color=C["ink"], w=1.6, fill="#ffffff")
    t = [(ox, oy + d), (ox + d, oy), (ox + s + d, oy), (ox + s, oy + d)]
    cv.polygon(t, color=C["ink"], w=1.5, fill="#f4f7fc")
    rg = [(ox + s, oy + d), (ox + s + d, oy), (ox + s + d, oy + s),
          (ox + s, oy + d + s)]
    cv.polygon(rg, color=C["ink"], w=1.5, fill="#e9eef7")
    # pips
    def pips(n, cx, cy, sp, col=C["ink"], rr=2.5):
        for px, py in PIPS.get(int(n), []):
            cv.dot(cx + px * sp, cy + py * sp, r=rr, color=col)
    pips(front, ox + s / 2, oy + d + s / 2, s * 0.24)
    pips(top, ox + s / 2 + d / 2, oy + d / 2, s * 0.2, rr=2.2)
    pips(right, ox + s + d / 2, oy + d / 2 + s / 2, s * 0.19, rr=2.1)


def dice(spec):
    """positions: [[top,front,right], ...] up to 3"""
    pos = spec.get("positions", [[1, 2, 3]])
    if pos and not isinstance(pos[0], (list, tuple)):
        pos = [pos]
    n = len(pos)
    W, H = 96 * n + 30, 140
    cv = Canvas(W, H, seed=_seed(spec, 101))
    for i, p in enumerate(pos):
        p = list(p) + [1, 1, 1]
        _die(cv, 22 + i * 96, 26, 52, p[0], p[1], p[2])
        cv.text(22 + i * 96 + 36, H - 12, f"({i+1})", size=9.5, color=C["soft"])
    return cv.svg()


# ───────────────────────── clock ─────────────────────────
def clock(spec):
    t = str(spec.get("time", "4:20"))
    try:
        hh, mm = [int(x) for x in t.split(":")]
    except Exception:
        hh, mm = 4, 20
    W, H = 220, 232
    cx, cy, r = 110, 108, 88
    cv = Canvas(W, H, seed=_seed(spec, 103))
    cv.circle(cx, cy, r, color=C["ink"], w=2.0, fill="#fffefa")
    for i in range(12):
        a = math.radians(i * 30 - 90)
        x1, y1 = cx + (r - 10) * math.cos(a), cy + (r - 10) * math.sin(a)
        x2, y2 = cx + r * math.cos(a), cy + r * math.sin(a)
        cv.raw(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
               f'stroke="{C["ink"]}" stroke-width="1.3"/>')
        nx, ny = cx + (r - 22) * math.cos(a), cy + (r - 22) * math.sin(a)
        cv.text(nx, ny + 4, str(12 if i == 0 else i), size=10, color=C["soft"])
    ma = math.radians(mm * 6 - 90)
    ha = math.radians((hh % 12) * 30 + mm * 0.5 - 90)
    cv.line(cx, cy, cx + r * 0.52 * math.cos(ha), cy + r * 0.52 * math.sin(ha),
            color=C["blue"], w=3.0)
    cv.line(cx, cy, cx + r * 0.76 * math.cos(ma), cy + r * 0.76 * math.sin(ma),
            color=C["red"], w=2.0)
    cv.dot(cx, cy, r=3.4)
    ang = abs(30 * (hh % 12) - 5.5 * mm)
    ang = min(ang, 360 - ang)
    cv.text(cx, H - 26, f"{hh}:{mm:02d}", size=12, weight=700, color=C["ink"])
    if spec.get("show_angle", True):
        cv.text(cx, H - 8, f"angle = |30H - 5.5M| = {_num(round(ang,1))} deg",
                size=9.4, color=C["purple"])
    return cv.svg()


REGISTRY = {
    "venn": venn,
    "pie": pie,
    "bar": bar,
    "dice": dice,
    "clock": clock,
}
