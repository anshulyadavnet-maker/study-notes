"""
nonverbal.py — non-verbal reasoning figures (Part E).

Mirror / water images, paper folding & punched holes, embedded figures,
figure matrices & series, cube nets, space visualisation.

Latin + numerals only inside SVG (Canvas.text enforces this).
"""
import math
from .sketch import Canvas, C


def _seed(spec, d=7):
    s = spec.get("seed", d)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


# ══════════════════════════════════════════════════════════
#  shape primitives used by series / analogy / matrix
# ══════════════════════════════════════════════════════════
def _shape(cv, kind, cx, cy, r, rot=0.0, color=None, fill=None, w=1.6):
    col = color or C["ink"]
    if kind == "circle":
        cv.circle(cx, cy, r, color=col, w=w, fill=fill)
    elif kind == "square":
        pts = [(cx + r * math.cos(rot + a), cy + r * math.sin(rot + a))
               for a in (math.pi*0.25, math.pi*0.75, math.pi*1.25, math.pi*1.75)]
        cv.polygon(pts, color=col, w=w, fill=fill)
    elif kind == "triangle":
        pts = [(cx + r * math.cos(rot - math.pi/2 + i*2*math.pi/3),
                cy + r * math.sin(rot - math.pi/2 + i*2*math.pi/3)) for i in range(3)]
        cv.polygon(pts, color=col, w=w, fill=fill)
    elif kind == "pentagon":
        pts = [(cx + r*math.cos(rot - math.pi/2 + i*2*math.pi/5),
                cy + r*math.sin(rot - math.pi/2 + i*2*math.pi/5)) for i in range(5)]
        cv.polygon(pts, color=col, w=w, fill=fill)
    elif kind == "diamond":
        pts = [(cx, cy - r), (cx + r*0.72, cy), (cx, cy + r), (cx - r*0.72, cy)]
        cv.polygon(pts, color=col, w=w, fill=fill)
    elif kind == "arrow":
        cv.arrow(cx - r*math.cos(rot), cy - r*math.sin(rot),
                 cx + r*math.cos(rot), cy + r*math.sin(rot), color=col, w=w)
    elif kind == "line":
        cv.line(cx - r*math.cos(rot), cy - r*math.sin(rot),
                cx + r*math.cos(rot), cy + r*math.sin(rot), color=col, w=w)
    elif kind == "L":
        # rotate the two arms about (cx, cy) so the series visibly turns
        def rp(px, py):
            ca, sa = math.cos(rot), math.sin(rot)
            return (cx + px*ca - py*sa, cy + px*sa + py*ca)
        a = rp(-r*0.6, -r*0.6); b = rp(-r*0.6, r*0.6); c = rp(r*0.6, r*0.6)
        cv.line(*a, *b, color=col, w=w)
        cv.line(*b, *c, color=col, w=w)
    elif kind == "flag":
        def rp(px, py):
            ca, sa = math.cos(rot), math.sin(rot)
            return (cx + px*ca - py*sa, cy + px*sa + py*ca)
        p0 = rp(-r*0.5, r*0.8); p1 = rp(-r*0.5, -r*0.8); p2 = rp(r*0.7, -r*0.35)
        cv.line(*p0, *p1, color=col, w=w)
        cv.polygon([p1, p2, rp(-r*0.5, r*0.05)], color=col, w=w, fill=fill)


def _dots(cv, n, cx, cy, r, color=None):
    col = color or C["red"]
    if n <= 0:
        return
    if n == 1:
        cv.dot(cx, cy, r=2.6, color=col); return
    for i in range(n):
        a = -math.pi/2 + i * 2*math.pi/n
        cv.dot(cx + r*0.45*math.cos(a), cy + r*0.45*math.sin(a), r=2.4, color=col)


def _panel(cv, x, y, s, label=None, dashed=False, color=None):
    col = color or "#c8d0e0"
    cv.raw(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="5" '
           f'fill="#ffffff" stroke="{col}" stroke-width="1.2"'
           f'{" stroke-dasharray=\'4 3\'" if dashed else ""}/>')
    if label:
        cv.text(x + s/2, y + s + 13, label, size=9.5, color=C["soft"])


# ══════════════════════════════════════════════════════════
#  1. MIRROR / WATER IMAGE
# ══════════════════════════════════════════════════════════
# --- stroke-drawn capital letters (7-segment style, mirror-safe) ----------
# WeasyPrint's SVG <text> does not survive scale(-1,1) reliably, so mirrored
# words are drawn as line segments. Coordinates are on a 0..1 box.
_GLYPH = {
    "A": [(0,1,.5,0),(.5,0,1,1),(.25,.55,.75,.55)],
    "B": [(0,0,0,1),(0,0,.75,.15),(.75,.15,0,.5),(0,.5,.8,.72),(.8,.72,0,1)],
    "C": [(1,.15,.5,0),(.5,0,0,.35),(0,.35,0,.65),(0,.65,.5,1),(.5,1,1,.85)],
    "D": [(0,0,0,1),(0,0,.7,.2),(.7,.2,.7,.8),(.7,.8,0,1)],
    "E": [(0,0,0,1),(0,0,.85,0),(0,.5,.7,.5),(0,1,.85,1)],
    "F": [(0,0,0,1),(0,0,.85,0),(0,.5,.7,.5)],
    "G": [(1,.15,.5,0),(.5,0,0,.35),(0,.35,0,.65),(0,.65,.5,1),(.5,1,1,.8),(1,.8,1,.55),(1,.55,.55,.55)],
    "H": [(0,0,0,1),(1,0,1,1),(0,.5,1,.5)],
    "I": [(.5,0,.5,1),(.2,0,.8,0),(.2,1,.8,1)],
    "J": [(.8,0,.8,.8),(.8,.8,.4,1),(.4,1,.05,.75)],
    "K": [(0,0,0,1),(0,.5,.9,0),(0,.5,.9,1)],
    "L": [(0,0,0,1),(0,1,.85,1)],
    "M": [(0,1,0,0),(0,0,.5,.55),(.5,.55,1,0),(1,0,1,1)],
    "N": [(0,1,0,0),(0,0,1,1),(1,1,1,0)],
    "O": [(.5,0,0,.35),(0,.35,0,.65),(0,.65,.5,1),(.5,1,1,.65),(1,.65,1,.35),(1,.35,.5,0)],
    "P": [(0,1,0,0),(0,0,.8,.18),(.8,.18,0,.45)],
    "Q": [(.5,0,0,.35),(0,.35,0,.65),(0,.65,.5,1),(.5,1,1,.65),(1,.65,1,.35),(1,.35,.5,0),(.6,.7,1,1.05)],
    "R": [(0,1,0,0),(0,0,.8,.18),(.8,.18,0,.45),(.25,.45,.95,1)],
    "S": [(.95,.12,.4,0),(.4,0,.05,.28),(.05,.28,.9,.68),(.9,.68,.6,1),(.6,1,.05,.85)],
    "T": [(0,0,1,0),(.5,0,.5,1)],
    "U": [(0,0,0,.7),(0,.7,.5,1),(.5,1,1,.7),(1,.7,1,0)],
    "V": [(0,0,.5,1),(.5,1,1,0)],
    "W": [(0,0,.22,1),(.22,1,.5,.35),(.5,.35,.78,1),(.78,1,1,0)],
    "X": [(0,0,1,1),(1,0,0,1)],
    "Y": [(0,0,.5,.5),(1,0,.5,.5),(.5,.5,.5,1)],
    "Z": [(0,0,1,0),(1,0,0,1),(0,1,1,1)],
    "0": [(.5,0,0,.35),(0,.35,0,.65),(0,.65,.5,1),(.5,1,1,.65),(1,.65,1,.35),(1,.35,.5,0)],
    "1": [(.25,.18,.55,0),(.55,0,.55,1),(.2,1,.9,1)],
    "3": [(.05,.05,.75,.05),(.75,.05,.35,.45),(.35,.45,.85,.7),(.85,.7,.4,1),(.4,1,.05,.85)],
    "8": [(.5,0,.1,.22),(.1,.22,.5,.45),(.5,.45,.9,.22),(.9,.22,.5,0),(.5,.45,.08,.72),(.08,.72,.5,1),(.5,1,.92,.72),(.92,.72,.5,.45)],
    " ": [],
}


def _draw_word(cv, txt, cx, cy, h, color, flip_x=False, flip_y=False, w=2.4):
    """Draw a word as stroked segments; safely mirrorable."""
    txt = str(txt).upper()
    cw = h * 0.62
    gap = h * 0.20
    total = len(txt) * cw + (len(txt) - 1) * gap
    x0 = cx - total / 2
    for i, ch in enumerate(txt):
        segs = _GLYPH.get(ch)
        if segs is None:
            segs = _GLYPH["O"]
        bx = x0 + i * (cw + gap)
        for (ax, ay, bx2, by2) in segs:
            X1 = bx + (1 - ax if flip_x else ax) * cw
            X2 = bx + (1 - bx2 if flip_x else bx2) * cw
            Y1 = cy + ((1 - ay) if flip_y else ay) * h - h / 2
            Y2 = cy + ((1 - by2) if flip_y else by2) * h - h / 2
            cv.raw(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" '
                   f'y2="{Y2:.1f}" stroke="{color}" stroke-width="{w}" '
                   f'stroke-linecap="round"/>')
    return total


def mirror_image(spec):
    """text ; kind: mirror | water — letters drawn as strokes, always render."""
    txt = str(spec.get("text", "PRAB")).upper()
    kind = spec.get("kind", "mirror")
    h = 30
    est = len(txt) * (h * 0.82) + 40

    if kind == "mirror":
        W = int(2 * est + 30); H = 126
        axis = W / 2.0
        cv = Canvas(W, H, seed=_seed(spec, 111))
        _draw_word(cv, txt, axis - est / 2, 54, h, C["ink"])
        cv.raw(f'<line x1="{axis}" y1="14" x2="{axis}" y2="{H-40}" '
               f'stroke="{C["red"]}" stroke-width="1.6" stroke-dasharray="5 4"/>')
        _draw_word(cv, txt[::-1], axis + est / 2, 54, h, C["blue"], flip_x=True)
        cv.text(W / 2, H - 14, "mirror line — left-right flip", size=9,
                color=C["red"])
    else:
        W = int(est + 70); H = 158
        axis = 78.0
        cx = W / 2.0
        cv = Canvas(W, H, seed=_seed(spec, 111))
        _draw_word(cv, txt, cx, 46, h, C["ink"])
        cv.raw(f'<line x1="22" y1="{axis}" x2="{W-22}" y2="{axis}" '
               f'stroke="{C["red"]}" stroke-width="1.6" stroke-dasharray="5 4"/>')
        _draw_word(cv, txt, cx, 2 * axis - 46, h, C["blue"], flip_y=True)
        cv.text(W / 2, H - 8, "water line — up-down flip", size=9, color=C["red"])
    return cv.svg()


def symmetry_chart(spec):
    """kind: mirror | water | both — letters that stay unchanged"""
    kind = spec.get("kind", "mirror")
    sets = {
        "mirror": ("A H I M O T U V W X Y", "unchanged in MIRROR (vertical symmetry)", C["blue"]),
        "water":  ("B C D E H I K O X", "unchanged in WATER (horizontal symmetry)", C["green"]),
        "both":   ("H I O X", "unchanged in BOTH", C["purple"]),
    }
    letters, note, col = sets.get(kind, sets["mirror"])
    ls = letters.split()
    W = 42 * len(ls) + 30
    H = 108
    cv = Canvas(W, H, seed=_seed(spec, 113))
    for i, ch in enumerate(ls):
        x = 24 + i * 42
        cv.raw(f'<rect x="{x-16}" y="26" width="34" height="38" rx="6" '
               f'fill="{C["blue_bg"] if kind=="mirror" else C["green_bg"] if kind=="water" else C["purple_bg"]}" '
               f'stroke="{col}" stroke-width="1.3"/>')
        cv.text(x + 1, 54, ch, size=19, weight=700, color=col)
    cv.text(W/2, 86, note, size=9.6, color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  2. PAPER FOLDING / PUNCHED HOLES
# ══════════════════════════════════════════════════════════
def paper_fold(spec):
    """folds: 1|2 — shows sheet, fold(s), punch, and the opened result."""
    folds = int(spec.get("folds", 2))
    s = 60                      # panel size
    gap = 24
    # widths of the four steps (step 3 is half-size when folded twice)
    w3 = s / 2 if folds >= 2 else s
    widths = [s, s, w3, s]
    W = int(sum(widths) + gap * 3 + 32)
    H = 132
    cv = Canvas(W, H, seed=_seed(spec, 117))
    y = 20
    x = 16

    # 1 — full sheet
    _panel(cv, x, y, s, "1. sheet")
    x += s + gap

    # 2 — first fold (bottom half up)
    cv.raw(f'<rect x="{x}" y="{y+s/2}" width="{s}" height="{s/2}" rx="4" '
           f'fill="#ffffff" stroke="#c8d0e0" stroke-width="1.2"/>')
    cv.raw(f'<rect x="{x}" y="{y}" width="{s}" height="{s/2}" rx="4" '
           f'fill="#eef3fb" stroke="#c8d0e0" stroke-width="1" '
           f'stroke-dasharray="3 3"/>')
    cv.arrow(x + s/2, y + 7, x + s/2, y + s/2 - 5, color=C["red"], w=1.3)
    cv.text(x + s/2, y + s + 13, "2. fold", size=9, color=C["soft"])
    x += s + gap

    # 3 — folded (again) + punch
    if folds >= 2:
        cv.raw(f'<rect x="{x}" y="{y+s/2}" width="{s/2}" height="{s/2}" rx="4" '
               f'fill="#ffffff" stroke="#c8d0e0" stroke-width="1.2"/>')
        hx, hy = x + s*0.16, y + s*0.76
        cv.text(x + s/4, y + s + 13, "3. punch", size=9, color=C["soft"])
    else:
        cv.raw(f'<rect x="{x}" y="{y+s/2}" width="{s}" height="{s/2}" rx="4" '
               f'fill="#ffffff" stroke="#c8d0e0" stroke-width="1.2"/>')
        hx, hy = x + s*0.3, y + s*0.76
        cv.text(x + s/2, y + s + 13, "3. punch", size=9, color=C["soft"])
    cv.circle(hx, hy, 4.6, color=C["red"], w=1.4, fill="#ffe3e3")
    x += w3 + gap

    # 4 — opened
    _panel(cv, x, y, s)
    cv.raw(f'<line x1="{x}" y1="{y+s/2}" x2="{x+s}" y2="{y+s/2}" '
           f'stroke="#dbe2ee" stroke-width="1" stroke-dasharray="3 3"/>')
    if folds >= 2:
        cv.raw(f'<line x1="{x+s/2}" y1="{y}" x2="{x+s/2}" y2="{y+s}" '
               f'stroke="#dbe2ee" stroke-width="1" stroke-dasharray="3 3"/>')
        spots = [(0.16, 0.76), (0.84, 0.76), (0.16, 0.24), (0.84, 0.24)]
    else:
        spots = [(0.30, 0.76), (0.30, 0.24)]
    for dx, dy in spots:
        cv.circle(x + s*dx, y + s*dy, 4.6, color=C["red"], w=1.4, fill="#ffe3e3")
    cv.text(x + s/2, y + s + 13, f"4. open = {len(spots)}", size=9,
            color=C["red"], weight=600)
    cv.text(W/2, H - 6, "holes double with every fold", size=8.8,
            color=C["soft"])
    return cv.svg()


def holes_formula(spec):
    """visual table: folds -> holes = 2^n"""
    W, H = 300, 118
    cv = Canvas(W, H, seed=_seed(spec, 119))
    for i in range(4):
        x = 22 + i * 70
        cv.raw(f'<rect x="{x}" y="20" width="52" height="46" rx="6" '
               f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.3"/>')
        cv.text(x + 26, 40, f"{i+1} fold" if i == 0 else f"{i+1} folds",
                size=9, color=C["soft"])
        cv.text(x + 26, 58, f"{2**(i+1)}", size=16, weight=700, color=C["amber"])
    cv.text(W/2, 88, "holes = 2 ^ (number of folds)", size=10.5,
            color=C["ink"], weight=600)
    cv.text(W/2, 104, "punch ON a fold line does NOT double", size=9,
            color=C["red"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  3. EMBEDDED FIGURE
# ══════════════════════════════════════════════════════════
def embedded(spec):
    W, H = 300, 150
    cv = Canvas(W, H, seed=_seed(spec, 127))
    # target shape
    _panel(cv, 16, 24, 76, "question figure")
    tri = [(30, 84), (78, 84), (54, 42)]
    cv.polygon(tri, color=C["red"], w=2.0)

    # complex figure containing it
    ox, oy, s = 140, 24, 76
    _panel(cv, ox, oy, s, "find it here")
    cv.rect(ox + 8, oy + 8, s - 16, s - 16, color=C["ink"], w=1.2)
    cv.line(ox + 8, oy + s - 8, ox + s - 8, oy + s - 8, color=C["ink"], w=1.2)
    cv.line(ox + 8, oy + 8, ox + s - 8, oy + s - 8, color=C["ink"], w=1.1)
    cv.line(ox + s - 8, oy + 8, ox + 8, oy + s - 8, color=C["ink"], w=1.1)
    # highlighted embedded triangle
    tri2 = [(ox + 14, oy + 60), (ox + 62, oy + 60), (ox + 38, oy + 18)]
    cv.polygon(tri2, color=C["red"], w=2.0)
    cv.text(232, 132, "the shape keeps its size and angle", size=9,
            color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  4. FIGURE SERIES (rotation / count)
# ══════════════════════════════════════════════════════════
def figure_series(spec):
    """shape, rotate (deg per step), dots (start), steps, question(bool)"""
    shape = spec.get("shape", "L")
    rot = float(spec.get("rotate", 90))
    dots0 = int(spec.get("dots", 0))
    ddot = int(spec.get("dot_step", 0))
    steps = int(spec.get("steps", 4))
    W = 76 * steps + 40
    H = 118
    cv = Canvas(W, H, seed=_seed(spec, 131))
    for i in range(steps):
        x = 20 + i * 76
        last = (i == steps - 1) and spec.get("question", True)
        _panel(cv, x, 18, 62, chr(65 + i) if not last else "?", dashed=last)
        if last:
            cv.text(x + 31, 56, "?", size=26, weight=700, color=C["grey"])
        else:
            _shape(cv, shape, x + 31, 49, 20,
                   rot=math.radians(rot * i), color=C["blue"], w=1.8)
            if dots0 or ddot:
                _dots(cv, dots0 + ddot * i, x + 31, 49, 20)
    return cv.svg()


def figure_analogy(spec):
    """A : B :: C : ?  with a stated transformation"""
    shape = spec.get("shape", "triangle")
    rot = float(spec.get("rotate", 180))
    W, H = 330, 122
    cv = Canvas(W, H, seed=_seed(spec, 137))
    xs = [16, 100, 200, 284]
    _panel(cv, xs[0], 18, 62, "A")
    _shape(cv, shape, xs[0]+31, 49, 20, color=C["blue"], w=1.8)
    _dots(cv, 1, xs[0]+31, 49, 20)
    cv.text(xs[0]+74, 54, ":", size=17, color=C["soft"])

    _panel(cv, xs[1], 18, 62, "B")
    _shape(cv, shape, xs[1]+31, 49, 20, rot=math.radians(rot), color=C["blue"], w=1.8)
    _dots(cv, 2, xs[1]+31, 49, 20)
    cv.text(xs[1]+80, 54, "::", size=16, color=C["soft"])

    _panel(cv, xs[2], 18, 62, "C")
    _shape(cv, spec.get("shape2", "square"), xs[2]+31, 49, 20, color=C["green"], w=1.8)
    _dots(cv, 3, xs[2]+31, 49, 20)
    cv.text(xs[2]+74, 54, ":", size=17, color=C["soft"])

    _panel(cv, xs[3], 18, 62, "?", dashed=True)
    cv.text(xs[3]+31, 58, "?", size=26, weight=700, color=C["grey"])
    cv.text(W/2, 112, f"rule: rotate {int(rot)} deg  +  add one dot",
            size=9.2, color=C["red"], weight=600)
    return cv.svg()


def odd_one_out(spec):
    """four figures, one differs"""
    W, H = 320, 118
    cv = Canvas(W, H, seed=_seed(spec, 139))
    kinds = spec.get("shapes", ["triangle", "square", "pentagon", "circle"])
    odd = int(spec.get("odd", 3))
    for i, k in enumerate(kinds[:4]):
        x = 18 + i * 76
        _panel(cv, x, 16, 62, f"({chr(97+i)})")
        _shape(cv, k, x + 31, 47, 20,
               color=C["red"] if i == odd else C["blue"], w=1.8)
    cv.text(W/2, 108, spec.get("note", ""), size=9.2, color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  5. FIGURE MATRIX 3x3
# ══════════════════════════════════════════════════════════
def figure_matrix(spec):
    W, H = 250, 262
    cv = Canvas(W, H, seed=_seed(spec, 149))
    s = 66
    ox, oy = 24, 18
    shapes = ["circle", "square", "triangle"]
    for r in range(3):
        for c in range(3):
            x, y = ox + c*(s+6), oy + r*(s+6)
            last = (r == 2 and c == 2)
            _panel(cv, x, y, s, dashed=last)
            if last:
                cv.text(x+s/2, y+s/2+9, "?", size=25, weight=700, color=C["grey"])
            else:
                _shape(cv, shapes[c], x+s/2, y+s/2, 19, color=C["blue"], w=1.7)
                _dots(cv, r+1, x+s/2, y+s/2, 19)
    cv.text(W/2, H-8, "rule: shape by column, dots by row", size=9.4,
            color=C["red"], weight=600)
    return cv.svg()


def number_matrix(spec):
    """rows: [[a,b,c],[...],[...]] with last cell '?'"""
    rows = spec.get("rows", [[4, 5, 20], [3, 6, 18], [7, 8, "?"]])
    W, H = 230, 200
    cv = Canvas(W, H, seed=_seed(spec, 151))
    cw, ch = 62, 46
    ox, oy = 20, 18
    for r, row in enumerate(rows[:3]):
        for c, v in enumerate(list(row)[:3]):
            x, y = ox + c*(cw+2), oy + r*(ch+2)
            isq = str(v) == "?"
            cv.raw(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="5" '
                   f'fill="{"#f3f6fc" if c==2 else "#ffffff"}" '
                   f'stroke="{C["blue"] if not isq else C["grey"]}" stroke-width="1.3"'
                   f'{" stroke-dasharray=\'4 3\'" if isq else ""}/>')
            cv.text(x+cw/2, y+ch/2+6, str(v), size=15,
                    weight=700 if c == 2 else 400,
                    color=C["grey"] if isq else (C["purple"] if c == 2 else C["ink"]))
    cv.text(W/2, H-10, spec.get("note", "check row-wise first"), size=9.3,
            color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  6. CUBE NET
# ══════════════════════════════════════════════════════════
def cube_net(spec):
    """cross net with labelled faces; opposite pairs proven by folding"""
    W, H = 260, 236
    s = 50
    cv = Canvas(W, H, seed=_seed(spec, 157))
    labs = spec.get("labels", ["A", "B", "C", "D", "E", "F"])
    ox, oy = 46, 16
    cells = {
        labs[0]: (ox + s, oy),                 # top of cross
        labs[1]: (ox, oy + s),
        labs[2]: (ox + s, oy + s),
        labs[3]: (ox + 2*s, oy + s),
        labs[4]: (ox + 3*s, oy + s),
        labs[5]: (ox + s, oy + 2*s),
    }
    for lab, (x, y) in cells.items():
        cv.raw(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" '
               f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.5"/>')
        cv.text(x + s/2, y + s/2 + 6, lab, size=16, weight=700, color=C["blue"])
    cv.text(W/2, oy + 3*s + 22, "opposite pairs:", size=9.6, color=C["soft"])
    cv.text(W/2, oy + 3*s + 38,
            f"{labs[1]}-{labs[3]}   {labs[2]}-{labs[4]}   {labs[0]}-{labs[5]}",
            size=11, weight=700, color=C["red"])
    cv.text(W/2, oy + 3*s + 53, "(one gap apart in a straight strip)",
            size=8.8, color=C["soft"])
    return cv.svg()


def painted_cube(spec):
    """n x n x n painted cube with the four counts"""
    n = int(spec.get("n", 4))
    W, H = 300, 196
    cv = Canvas(W, H, seed=_seed(spec, 163))
    # isometric stack
    s = 96; d = 34
    ox, oy = 24, 40
    f = [(ox, oy+d), (ox+s, oy+d), (ox+s, oy+d+s), (ox, oy+d+s)]
    cv.polygon(f, color=C["teal"], w=1.7, fill=C["teal_bg"])
    top = [(ox, oy+d), (ox+d, oy), (ox+s+d, oy), (ox+s, oy+d)]
    cv.polygon(top, color=C["teal"], w=1.5, fill="#f0fbfc")
    side = [(ox+s, oy+d), (ox+s+d, oy), (ox+s+d, oy+s), (ox+s, oy+d+s)]
    cv.polygon(side, color=C["teal"], w=1.5, fill="#e2f4f6")
    for i in range(1, n):
        t = i / n
        cv.line(ox + s*t, oy+d, ox + s*t, oy+d+s, color=C["teal"], w=0.8)
        cv.line(ox, oy+d+s*t, ox+s, oy+d+s*t, color=C["teal"], w=0.8)
    cv.text(ox + s/2 + d/2, oy + d + s + 22, f"n = {n}", size=11,
            weight=700, color=C["teal"])
    # counts
    tx = ox + s + d + 20
    rows = [("3 faces (corners)", 8, C["red"]),
            ("2 faces (edges)", 12*(n-2), C["amber"]),
            ("1 face", 6*(n-2)**2, C["blue"]),
            ("0 face (inside)", (n-2)**3, C["green"])]
    for i, (lab, val, col) in enumerate(rows):
        y = oy + 8 + i*30
        cv.text(tx, y, lab, size=9.2, anchor="start", color=C["soft"])
        cv.text(tx, y + 15, str(val), size=15, anchor="start", weight=700, color=col)
    cv.text(W/2, H-6, f"total = {n**3}", size=9.4, color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  7. COUNTING FIGURES
# ══════════════════════════════════════════════════════════
def count_figures(spec):
    """kind: square-diagonals | grid"""
    kind = spec.get("kind", "square-diagonals")
    W, H = 250, 168
    cv = Canvas(W, H, seed=_seed(spec, 167))
    if kind == "square-diagonals":
        s = 110; ox, oy = (W-s)/2, 22
        cv.rect(ox, oy, s, s, color=C["blue"], w=1.8, fill=C["blue_bg"])
        cv.line(ox, oy, ox+s, oy+s, color=C["red"], w=1.5)
        cv.line(ox+s, oy, ox, oy+s, color=C["red"], w=1.5)
        cv.text(W/2, oy+s+24, "triangles = 8", size=12, weight=700, color=C["red"])
        cv.text(W/2, oy+s+40, "4 small + 4 large", size=9.2, color=C["soft"])
    else:
        n = int(spec.get("grid", 3))
        s = 108; ox, oy = (W-s)/2, 18
        cell = s/n
        for i in range(n+1):
            cv.line(ox+i*cell, oy, ox+i*cell, oy+s, color=C["blue"], w=1.3)
            cv.line(ox, oy+i*cell, ox+s, oy+i*cell, color=C["blue"], w=1.3)
        rects = (n*(n+1)//2)**2
        squares = sum((n-k)*(n-k) for k in range(n))
        cv.text(W/2, oy+s+22, f"{n} x {n} grid", size=10, color=C["soft"])
        cv.text(W/2, oy+s+38, f"rectangles = {rects}   squares = {squares}",
                size=10.5, weight=700, color=C["red"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  8. FAMILY TREE / DIRECTION / SEATING (verbal-support)
# ══════════════════════════════════════════════════════════
def family_tree(spec):
    W, H = 300, 190
    cv = Canvas(W, H, seed=_seed(spec, 173))
    def node(x, y, lab, male=True, col=None):
        c = col or (C["blue"] if male else C["pink"])
        if male:
            cv.raw(f'<rect x="{x-16}" y="{y-14}" width="32" height="28" rx="4" '
                   f'fill="{C["blue_bg"]}" stroke="{c}" stroke-width="1.5"/>')
        else:
            cv.circle(x, y, 16, color=c, w=1.5, fill=C["pink_bg"])
        cv.text(x, y+5, lab, size=11.5, weight=700, color=c)
    node(96, 34, "D", True); node(196, 34, "C", False)
    cv.raw(f'<line x1="112" y1="34" x2="180" y2="34" stroke="{C["ink"]}" '
           f'stroke-width="1.6"/>')
    cv.raw(f'<line x1="112" y1="30" x2="180" y2="30" stroke="{C["ink"]}" '
           f'stroke-width="1.6"/>')
    cv.line(146, 40, 146, 84, color=C["ink"], w=1.3)
    cv.line(76, 84, 216, 84, color=C["ink"], w=1.3)
    cv.line(76, 84, 76, 104, color=C["ink"], w=1.3)
    cv.line(216, 84, 216, 104, color=C["ink"], w=1.3)
    node(76, 120, "A", True); node(216, 120, "B", False)
    cv.text(150, 168, "= marriage      | descent      A, B are siblings",
            size=9, color=C["soft"])
    cv.text(46, 34, "male", size=8.6, color=C["blue"], anchor="start")
    cv.text(238, 34, "female", size=8.6, color=C["pink"], anchor="start")
    return cv.svg()


def direction_path(spec):
    """moves: [N:10, E:5, S:10] — draws the path and the resultant"""
    moves = spec.get("moves", ["N:10", "E:5", "S:10"])
    if isinstance(moves, str):
        moves = [moves]
    W, H = 280, 226
    cv = Canvas(W, H, seed=_seed(spec, 179))
    # compass
    cx, cy = 34, 40
    cv.line(cx, cy-16, cx, cy+16, color=C["grey"], w=1.0)
    cv.line(cx-16, cy, cx+16, cy, color=C["grey"], w=1.0)
    for lab, dx, dy in (("N",0,-20),("S",0,24),("E",22,4),("W",-22,4)):
        cv.text(cx+dx, cy+dy, lab, size=8.6, color=C["grey"])
    D = {"N": (0,-1), "S": (0,1), "E": (1,0), "W": (-1,0)}
    pts = [(140.0, 150.0)]
    sc = 5.2
    for mv in moves:
        try:
            d, v = str(mv).split(":"); v = float(v)
        except Exception:
            continue
        dx, dy = D.get(d.strip().upper(), (0,0))
        x, y = pts[-1]
        pts.append((x + dx*v*sc, y + dy*v*sc))
    for i in range(len(pts)-1):
        cv.arrow(*pts[i], *pts[i+1], color=C["blue"], w=1.7)
        mx, my = (pts[i][0]+pts[i+1][0])/2, (pts[i][1]+pts[i+1][1])/2
        cv.text(mx+10, my-4, str(moves[i]).replace(":", " "), size=8.8,
                color=C["blue"], anchor="start")
    cv.dot(*pts[0], r=3.4, color=C["green"])
    cv.text(pts[0][0]-6, pts[0][1]+16, "start", size=9, color=C["green"],
            anchor="end")
    cv.dot(*pts[-1], r=3.4, color=C["red"])
    cv.text(pts[-1][0]+8, pts[-1][1]-8, "end", size=9, color=C["red"],
            anchor="start")
    if len(pts) > 2:
        cv.line(*pts[0], *pts[-1], color=C["red"], w=1.4, dash="5 3")
        dx = (pts[-1][0]-pts[0][0])/sc; dy = (pts[-1][1]-pts[0][1])/sc
        dist = math.hypot(dx, dy)
        cv.text(W/2, H-8, f"shortest distance = {dist:.0f} units", size=9.6,
                color=C["red"], weight=600)
    return cv.svg()


def seating(spec):
    """kind: circular | linear ; n people ; facing"""
    kind = spec.get("kind", "circular")
    n = int(spec.get("n", 6))
    facing = spec.get("facing", "centre")
    W, H = 250, 232
    cv = Canvas(W, H, seed=_seed(spec, 181))
    if kind == "circular":
        cx, cy, r = 125, 106, 74
        cv.circle(cx, cy, r, color="#dbe2ee", w=1.2)
        for i in range(n):
            a = -math.pi/2 + i*2*math.pi/n
            x, y = cx + r*math.cos(a), cy + r*math.sin(a)
            cv.circle(x, y, 15, color=C["blue"], w=1.5, fill=C["blue_bg"])
            cv.text(x, y+5, chr(65+i), size=11.5, weight=700, color=C["blue"])
            # facing arrow
            if facing == "centre":
                ix, iy = cx + (r-28)*math.cos(a), cy + (r-28)*math.sin(a)
                cv.arrow(x - 13*math.cos(a), y - 13*math.sin(a), ix, iy,
                         color=C["red"], w=1.1)
            else:
                ox_, oy_ = cx + (r+26)*math.cos(a), cy + (r+26)*math.sin(a)
                cv.arrow(x + 13*math.cos(a), y + 13*math.sin(a), ox_, oy_,
                         color=C["red"], w=1.1)
        note = ("facing CENTRE: anticlockwise = LEFT"
                if facing == "centre" else
                "facing OUTSIDE: clockwise = LEFT")
        cv.text(W/2, H-14, note, size=9.4, color=C["red"], weight=600)
    else:
        y = 96
        gap = 200/(n-1) if n > 1 else 0
        for i in range(n):
            x = 25 + i*gap
            cv.circle(x, y, 15, color=C["blue"], w=1.5, fill=C["blue_bg"])
            cv.text(x, y+5, chr(65+i), size=11.5, weight=700, color=C["blue"])
            cv.arrow(x, y+22, x, y+42, color=C["red"], w=1.1)
        cv.text(W/2, y+66, "all facing NORTH", size=9.6, color=C["red"],
                weight=600)
        cv.text(W/2, y+82, "your LEFT = picture left", size=9, color=C["soft"])
    return cv.svg()


REGISTRY = {
    "mirror-image": mirror_image,
    "symmetry-chart": symmetry_chart,
    "paper-fold": paper_fold,
    "holes-formula": holes_formula,
    "embedded": embedded,
    "figure-series": figure_series,
    "figure-analogy": figure_analogy,
    "odd-one-out": odd_one_out,
    "figure-matrix": figure_matrix,
    "number-matrix": number_matrix,
    "cube-net": cube_net,
    "painted-cube": painted_cube,
    "count-figures": count_figures,
    "family-tree": family_tree,
    "direction-path": direction_path,
    "seating": seating,
}


# ══════════════════════════════════════════════════════════
#  9. FIGURE COMPLETION  (36.2)
# ══════════════════════════════════════════════════════════
def figure_completion(spec):
    """A patterned square with one quadrant missing + four options."""
    W, H = 330, 176
    cv = Canvas(W, H, seed=_seed(spec, 191))
    s = 74
    ox, oy = 16, 20

    def pattern(px, py, size, skip_tr=False, variant=0):
        """draw hatch + border; variant changes the missing-piece content"""
        cv.raw(f'<rect x="{px}" y="{py}" width="{size}" height="{size}" rx="3" '
               f'fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.4"/>')
        h = size / 2
        # cross lines
        cv.line(px, py + h, px + size, py + h, color=C["ink"], w=1.1)
        cv.line(px + h, py, px + h, py + size, color=C["ink"], w=1.1)
        # quadrant fills: TL dots, BL diagonal, BR circle, TR = the answer
        cv.dot(px + h*0.5, py + h*0.5, r=2.6, color=C["blue"])
        cv.line(px + 5, py + size - 5, px + h - 5, py + h + 5,
                color=C["green"], w=1.3)
        cv.circle(px + h*1.5, py + h*1.5, h*0.28, color=C["amber"], w=1.3)
        if not skip_tr:
            if variant == 0:                      # correct: two dots
                cv.dot(px + h*1.3, py + h*0.4, r=2.4, color=C["blue"])
                cv.dot(px + h*1.7, py + h*0.7, r=2.4, color=C["blue"])
            elif variant == 1:                    # wrong: one dot
                cv.dot(px + h*1.5, py + h*0.5, r=2.4, color=C["blue"])
            elif variant == 2:                    # wrong: circle
                cv.circle(px + h*1.5, py + h*0.5, h*0.26, color=C["blue"], w=1.2)
            else:                                 # wrong: line
                cv.line(px + h*1.15, py + h*0.3, px + h*1.85, py + h*0.7,
                        color=C["blue"], w=1.3)

    # question figure with a gap
    pattern(ox, oy, s, skip_tr=True)
    hx, hy = ox + s/2, oy
    cv.raw(f'<rect x="{hx}" y="{hy}" width="{s/2}" height="{s/2}" '
           f'fill="#f3f5f9" stroke="{C["grey"]}" stroke-width="1.2" '
           f'stroke-dasharray="3 3"/>')
    cv.text(hx + s/4, hy + s/4 + 6, "?", size=17, weight=700, color=C["grey"])
    cv.text(ox + s/2, oy + s + 14, "question", size=9, color=C["soft"])

    # four options
    osz = 40
    for i in range(4):
        px = 128 + i * 50
        py = oy + 8
        cv.raw(f'<rect x="{px}" y="{py}" width="{osz}" height="{osz}" rx="3" '
               f'fill="#ffffff" stroke="{C["blue"] if i == 0 else "#c8d0e0"}" '
               f'stroke-width="{1.7 if i == 0 else 1.2}"/>')
        h = osz
        if i == 0:
            cv.dot(px + h*0.32, py + h*0.35, r=2.3, color=C["blue"])
            cv.dot(px + h*0.66, py + h*0.62, r=2.3, color=C["blue"])
        elif i == 1:
            cv.dot(px + h/2, py + h/2, r=2.3, color=C["blue"])
        elif i == 2:
            cv.circle(px + h/2, py + h/2, h*0.22, color=C["blue"], w=1.2)
        else:
            cv.line(px + h*0.24, py + h*0.3, px + h*0.76, py + h*0.7,
                    color=C["blue"], w=1.3)
        cv.text(px + osz/2, py + osz + 13, f"({chr(97+i)})", size=9,
                color=C["blue"] if i == 0 else C["soft"],
                weight=700 if i == 0 else 400)
    cv.text(W/2, H - 8, "match the lines and the pattern at the edges",
            size=8.8, color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  10. GROUPING OF IDENTICAL FIGURES  (36.3)
# ══════════════════════════════════════════════════════════
def grouping(spec):
    """six figures sorted into two logical groups"""
    W, H = 320, 168
    cv = Canvas(W, H, seed=_seed(spec, 193))
    g1 = ["triangle", "square", "pentagon"]     # closed, straight sides
    g2 = ["circle", "diamond", "circle"]        # curved / other
    cv.raw(f'<rect x="10" y="16" width="146" height="92" rx="9" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.4" '
           f'stroke-dasharray="5 4"/>')
    cv.raw(f'<rect x="164" y="16" width="146" height="92" rx="9" '
           f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.4" '
           f'stroke-dasharray="5 4"/>')
    for i, k in enumerate(g1):
        _shape(cv, k, 40 + i*44, 62, 17, color=C["blue"], w=1.6)
    for i, k in enumerate(g2):
        _shape(cv, k, 194 + i*44, 62, 17, color=C["green"], w=1.6)
    cv.text(83, 126, "group 1", size=10, weight=700, color=C["blue"])
    cv.text(237, 126, "group 2", size=10, weight=700, color=C["green"])
    cv.text(83, 142, "straight sides only", size=8.8, color=C["soft"])
    cv.text(237, 142, "has a curve / other", size=8.8, color=C["soft"])
    cv.text(W/2, 162, "sort by: sides, curves, shading, symmetry",
            size=8.8, color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  11. SPACE ORIENTATION  (38.2)
# ══════════════════════════════════════════════════════════
def space_orientation(spec):
    """same object seen from three sides — top / front / side views"""
    W, H = 320, 186
    cv = Canvas(W, H, seed=_seed(spec, 197))
    # isometric object (L-shaped block)
    ox, oy, u = 22, 44, 26
    d = 12
    base = [(ox, oy+2*u), (ox+2*u, oy+2*u), (ox+2*u, oy+u),
            (ox+u, oy+u), (ox+u, oy), (ox, oy)]
    cv.polygon(base, color=C["teal"], w=1.7, fill=C["teal_bg"])
    top = [(ox, oy), (ox+d, oy-d), (ox+u+d, oy-d), (ox+u, oy)]
    cv.polygon(top, color=C["teal"], w=1.4, fill="#f0fbfc")
    cv.text(ox+u, oy+2*u+18, "object", size=9.4, weight=600, color=C["teal"])

    views = [("top", [(0,0),(2,0),(2,1),(1,1),(1,2),(0,2)]),
             ("front", [(0,0),(2,0),(2,1),(0,1)]),
             ("side", [(0,0),(1,0),(1,2),(0,2)])]
    for i, (name, poly) in enumerate(views):
        bx, by, k = 128 + i*66, 46, 22
        pts = [(bx + x*k, by + y*k) for x, y in poly]
        cv.polygon(pts, color=C["blue"], w=1.6, fill=C["blue_bg"])
        cv.text(bx + k, by + 2*k + 18, name, size=9.4, color=C["blue"],
                weight=600)
    cv.text(W/2, H - 8, "pick one fixed reference corner, then re-draw",
            size=8.8, color=C["soft"])
    return cv.svg()


# ══════════════════════════════════════════════════════════
#  12. TRENDS  (38.4)
# ══════════════════════════════════════════════════════════
def trend(spec):
    """a quantity growing/shrinking/rotating step by step"""
    kind = spec.get("kind", "grow")
    steps = int(spec.get("steps", 4))
    W = 70*steps + 40
    H = 122
    cv = Canvas(W, H, seed=_seed(spec, 199))
    for i in range(steps):
        x = 20 + i*70
        last = (i == steps-1) and spec.get("question", True)
        _panel(cv, x, 16, 58, chr(65+i) if not last else "?", dashed=last)
        if last:
            cv.text(x+29, 54, "?", size=24, weight=700, color=C["grey"])
            continue
        if kind == "grow":
            r = 8 + i*4.5
            cv.circle(x+29, 45, r, color=C["blue"], w=1.6, fill=C["blue_bg"])
        elif kind == "shrink":
            r = 20 - i*4.5
            cv.circle(x+29, 45, r, color=C["amber"], w=1.6, fill=C["amber_bg"])
        else:                                    # fill level rising
            lv = (i+1)/steps
            cv.rect(x+14, 26, 30, 38, color=C["teal"], w=1.5)
            cv.raw(f'<rect x="{x+14}" y="{26+38*(1-lv)}" width="30" '
                   f'height="{38*lv:.1f}" fill="{C["teal_bg"]}"/>')
    cv.text(W/2, H-8, {"grow":"size increases by a fixed step",
                       "shrink":"size decreases by a fixed step",
                       "fill":"shaded part increases each step"}.get(kind,""),
            size=8.8, color=C["soft"])
    return cv.svg()


REGISTRY.update({
    "figure-completion": figure_completion,
    "grouping": grouping,
    "space-orientation": space_orientation,
    "trend": trend,
})
