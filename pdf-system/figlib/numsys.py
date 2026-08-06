"""
numsys.py — figures for Chapter 1 (Number System).

number-tree      : the classification hierarchy (real -> rational -> ... )
place-value      : Indian vs International place-value chart
number-line-ext  : an annotated number line showing integer classes
prime-sieve      : 1..100 grid with primes highlighted
divisibility-web : quick visual of the divisibility family
"""
import math
from .sketch import Canvas, C


def _seed(spec, d=7):
    s = spec.get("seed", d)
    try:
        return int(s)
    except Exception:
        return sum(ord(c) for c in str(s))


def _box(cv, x, y, w, h, label, sub=None, col=None, bg=None, fs=10.5):
    col = col or C["blue"]
    bg = bg or C["blue_bg"]
    cv.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="7" '
           f'fill="{bg}" stroke="{col}" stroke-width="1.5"/>')
    if sub:
        cv.text(x + w / 2, y + h / 2 - 2, label, size=fs, weight=700, color=col)
        cv.text(x + w / 2, y + h / 2 + 11, sub, size=7.8, color=C["soft"])
    else:
        cv.text(x + w / 2, y + h / 2 + 4, label, size=fs, weight=700, color=col)


def _elbow(cv, x1, y1, x2, y2, col=None):
    """vertical-then-horizontal-then-vertical connector"""
    col = col or C["grey"]
    mid = (y1 + y2) / 2
    for a in ((x1, y1, x1, mid), (x1, mid, x2, mid), (x2, mid, x2, y2)):
        cv.raw(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{a[2]:.1f}" '
               f'y2="{a[3]:.1f}" stroke="{col}" stroke-width="1.2"/>')


# ────────────────────────── number classification tree ──────────────────────
def number_tree(spec):
    W, H = 470, 300
    cv = Canvas(W, H, seed=_seed(spec, 301))
    bw, bh = 108, 34

    # level 0
    _box(cv, (W - 150) / 2, 8, 150, bh, "REAL  (R)", None, C["purple"], C["purple_bg"], 11.5)
    # level 1
    y1 = 78
    _box(cv, 52, y1, 150, bh, "RATIONAL  (Q)", "p/q ,  q != 0", C["blue"], C["blue_bg"])
    _box(cv, 268, y1, 150, bh, "IRRATIONAL", "sqrt2 , pi , e", C["red"], C["red_bg"])
    _elbow(cv, W / 2, 42, 127, y1)
    _elbow(cv, W / 2, 42, 343, y1)

    # level 2
    y2 = 150
    _box(cv, 14, y2, 104, bh, "INTEGERS", "... -2,-1,0,1,2 ...", C["green"], C["green_bg"], 9.6)
    _box(cv, 132, y2, 104, bh, "FRACTIONS", "3/4 , -5/7", C["teal"], C["teal_bg"], 9.6)
    _elbow(cv, 127, y1 + bh, 66, y2)
    _elbow(cv, 127, y1 + bh, 184, y2)

    # level 3
    y3 = 222
    _box(cv, 8, y3, 96, bh, "WHOLE", "0,1,2,3 ...", C["amber"], C["amber_bg"], 9.6)
    _box(cv, 118, y3, 96, bh, "NEGATIVE", "-1,-2,-3 ...", C["amber"], C["amber_bg"], 9.6)
    _elbow(cv, 66, y2 + bh, 56, y3)
    _elbow(cv, 66, y2 + bh, 166, y3)

    # level 4
    y4 = 270
    _box(cv, 8, y4, 96, 26, "NATURAL  1,2,3", None, C["ink"], "#f2f5fa", 8.8)
    _elbow(cv, 56, y3 + bh, 56, y4)

    cv.text(343, y1 + bh + 24, "cannot be written as p/q", size=8.6, color=C["soft"])
    cv.text(343, y1 + bh + 38, "non-terminating, non-repeating", size=8.6, color=C["soft"])
    return cv.svg()


# ────────────────────────── place value chart ──────────────────────────
def place_value(spec):
    """Indian vs International place value for one number."""
    num = str(spec.get("number", "6543210"))
    num = num.replace(",", "")[:9]
    n = len(num)

    ind = ["इकाई", "दहाई", "सैकड़ा", "हज़ार", "दस हज़ार",
           "लाख", "दस लाख", "करोड़", "दस करोड़"]
    itl = ["Ones", "Tens", "Hundreds", "Thousands", "Ten Thousands",
           "Hundred Th.", "Millions", "Ten Millions", "Hundred M."]
    # Devanagari cannot be drawn inside SVG text (matras detach), so use
    # transliterated Latin for the Indian row.
    ind_lat = ["Ikai", "Dahai", "Saikda", "Hazar", "Das Hazar",
               "Lakh", "Das Lakh", "Karod", "Das Karod"]

    cw = 52
    W = cw * n + 96
    H = 150
    cv = Canvas(W, H, seed=_seed(spec, 303))
    x0 = 88

    cv.text(80, 40, "Digit", size=9.4, anchor="end", weight=700, color=C["ink"])
    cv.text(80, 74, "Indian", size=9.4, anchor="end", weight=700, color=C["blue"])
    cv.text(80, 112, "Intl.", size=9.4, anchor="end", weight=700, color=C["green"])

    for i, ch in enumerate(num):
        x = x0 + i * cw
        pos = n - 1 - i                     # 0 = ones
        # digit cell
        cv.raw(f'<rect x="{x}" y="18" width="{cw-4}" height="30" rx="4" '
               f'fill="#fff" stroke="{C["ink"]}" stroke-width="1.4"/>')
        cv.text(x + (cw - 4) / 2, 40, ch, size=16, weight=700, color=C["ink"])
        # indian
        cv.raw(f'<rect x="{x}" y="54" width="{cw-4}" height="28" rx="4" '
               f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.1"/>')
        cv.text(x + (cw - 4) / 2, 72, ind_lat[pos], size=7.0, color=C["blue"])
        # international
        cv.raw(f'<rect x="{x}" y="88" width="{cw-4}" height="28" rx="4" '
               f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.1"/>')
        cv.text(x + (cw - 4) / 2, 106, itl[pos], size=6.6, color=C["green"])

    # comma grouping guides
    cv.text(W / 2, H - 18, f"Indian:  {_group_indian(num)}", size=9.6,
            color=C["blue"], weight=700)
    cv.text(W / 2, H - 4, f"International:  {_group_intl(num)}", size=9.6,
            color=C["green"], weight=700)
    return cv.svg()


def _group_indian(s):
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    out = []
    while len(head) > 2:
        out.insert(0, head[-2:])
        head = head[:-2]
    if head:
        out.insert(0, head)
    return ",".join(out) + "," + tail


def _group_intl(s):
    out = []
    while len(s) > 3:
        out.insert(0, s[-3:])
        s = s[:-3]
    if s:
        out.insert(0, s)
    return ",".join(out)


# ────────────────────────── annotated number line ──────────────────────────
def number_line_ext(spec):
    lo = int(spec.get("min", -5))
    hi = int(spec.get("max", 5))
    W, H = 430, 132
    cv = Canvas(W, H, seed=_seed(spec, 305))
    y = 66
    x0, x1 = 34, W - 34
    n = hi - lo
    step = (x1 - x0) / n

    cv.line(x0 - 6, y, x1 + 6, y, color=C["ink"], w=1.7)
    cv.arrow(x1 - 12, y, x1 + 10, y, color=C["ink"], w=1.5)
    cv.arrow(x0 + 12, y, x0 - 10, y, color=C["ink"], w=1.5)

    for i in range(n + 1):
        v = lo + i
        px = x0 + i * step
        big = (v == 0)
        cv.line(px, y - (9 if big else 6), px, y + (9 if big else 6),
                color=C["ink"], w=1.5 if big else 1.0)
        cv.text(px, y + 24, str(v), size=9.6,
                color=C["ink"] if big else C["soft"],
                weight=700 if big else 400)

    # zone labels
    cv.raw(f'<rect x="{x0-4}" y="{y-40}" width="{5*step+4}" height="20" rx="5" '
           f'fill="{C["red_bg"]}" stroke="{C["red"]}" stroke-width="1.1"/>')
    cv.text(x0 + 2.5 * step, y - 26, "negative integers", size=8.6, color=C["red"])

    cv.raw(f'<rect x="{x0+5*step}" y="{y-40}" width="{5*step+8}" height="20" rx="5" '
           f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.1"/>')
    cv.text(x0 + 7.5 * step, y - 26, "natural numbers", size=8.6, color=C["green"])

    cv.dot(x0 + 5 * step, y, r=4.2, color=C["blue"])
    cv.text(x0 + 5 * step, y + 44, "zero: neither +ve nor -ve", size=8.8,
            color=C["blue"], weight=700)
    cv.text(W / 2, H - 6, "whole = 0 together with the naturals", size=8.6,
            color=C["soft"])
    return cv.svg()


# ────────────────────────── prime sieve grid ──────────────────────────
def prime_sieve(spec):
    upto = int(spec.get("upto", 100))
    cols = 10
    rows = (upto + cols - 1) // cols
    cell = 27
    W = cols * cell + 26
    H = rows * cell + 62
    cv = Canvas(W, H, seed=_seed(spec, 307))

    def is_prime(k):
        if k < 2:
            return False
        for d in range(2, int(k ** 0.5) + 1):
            if k % d == 0:
                return False
        return True

    primes = 0
    for k in range(1, upto + 1):
        r, c = (k - 1) // cols, (k - 1) % cols
        x, y = 13 + c * cell, 12 + r * cell
        if is_prime(k):
            primes += 1
            fill, stroke, tcol, wt = C["green_bg"], C["green"], C["green"], 700
        elif k == 1:
            fill, stroke, tcol, wt = C["amber_bg"], C["amber"], C["amber"], 700
        else:
            fill, stroke, tcol, wt = "#ffffff", "#dbe1ec", C["soft"], 400
        cv.raw(f'<rect x="{x}" y="{y}" width="{cell-3}" height="{cell-3}" rx="3.5" '
               f'fill="{fill}" stroke="{stroke}" stroke-width="1.1"/>')
        cv.text(x + (cell - 3) / 2, y + (cell - 3) / 2 + 4, str(k),
                size=8.6, color=tcol, weight=wt)

    # legend on two lines so nothing runs past the viewBox
    yb = 12 + rows * cell + 10
    cv.raw(f'<rect x="14" y="{yb}" width="11" height="11" rx="2.5" '
           f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.1"/>')
    cv.text(30, yb + 9.5, f"prime  ({primes} of {upto})", size=8.4,
            anchor="start", color=C["green"], weight=700)
    yb2 = yb + 16
    cv.raw(f'<rect x="14" y="{yb2}" width="11" height="11" rx="2.5" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.1"/>')
    cv.text(30, yb2 + 9.5, "1 = neither prime nor composite", size=8.4,
            anchor="start", color=C["amber"], weight=700)
    return cv.svg()


# ────────────────────────── divisibility quick map ──────────────────────────
def divisibility_map(spec):
    W, H = 440, 190
    cv = Canvas(W, H, seed=_seed(spec, 309))
    items = [
        ("2", "last digit even", C["blue"]),
        ("3", "digit sum / 3", C["green"]),
        ("4", "last TWO digits", C["amber"]),
        ("5", "ends 0 or 5", C["purple"]),
        ("6", "by 2 AND 3", C["teal"]),
        ("8", "last THREE digits", C["pink"]),
        ("9", "digit sum / 9", C["red"]),
        ("11", "alt sum diff", C["blue"]),
    ]
    bw, bh = 100, 40
    for i, (n, rule, col) in enumerate(items):
        r, c = i // 4, i % 4
        x = 10 + c * (bw + 6)
        y = 14 + r * (bh + 16)
        cv.raw(f'<rect x="{x}" y="{y}" width="{bw}" height="{bh}" rx="7" '
               f'fill="#ffffff" stroke="{col}" stroke-width="1.5"/>')
        cv.raw(f'<circle cx="{x+18}" cy="{y+bh/2}" r="13" fill="{col}"/>')
        cv.text(x + 18, y + bh / 2 + 5, n, size=12.5, weight=700, color="#ffffff")
        cv.text(x + 36, y + bh / 2 + 4, rule, size=7.8, anchor="start",
                color=C["ink"])
    cv.text(W / 2, H - 34, "7 : double the last digit, subtract from the rest",
            size=8.8, color=C["soft"])
    cv.text(W / 2, H - 18, "12 : divisible by 3 AND 4      15 : by 3 AND 5",
            size=8.8, color=C["soft"])
    cv.text(W / 2, H - 4, "a perfect square never ends in 2, 3, 7 or 8",
            size=9, color=C["red"], weight=700)
    return cv.svg()


# ────────────────────────── factor tree ──────────────────────────
_SUP = {"0":"\u2070","1":"\u00b9","2":"\u00b2","3":"\u00b3","4":"\u2074",
        "5":"\u2075","6":"\u2076","7":"\u2077","8":"\u2078","9":"\u2079"}


def _sup(n):
    return "".join(_SUP[c] for c in str(n))


def factor_tree(spec):
    """Prime factorisation as a branching tree.

    The tree steps right each level, so the canvas width is computed from
    the depth — otherwise deep trees (360 needs 5 splits) run off the edge.
    """
    n = int(spec.get("number", 360))

    def split(m):
        d = 2
        while d * d <= m:
            if m % d == 0:
                return d, m // d
            d += 1
        return None, None

    chain = []
    cur = n
    while True:
        pr, co = split(cur)
        if pr is None:
            break
        chain.append((cur, pr, co))
        cur = co
    depth = len(chain)

    dx, dy = 42, 52                      # horizontal / vertical step
    left_pad, right_pad = 58, 44
    W = int(left_pad + depth * dx + right_pad)
    H = 44 + depth * dy + 26
    cv = Canvas(W, H, seed=_seed(spec, 311))

    def node(x, y, val, prime=False):
        r = 16 if val < 100 else 19
        col = C["red"] if prime else C["blue"]
        bg = C["red_bg"] if prime else C["blue_bg"]
        cv.circle(x, y, r, color=col, w=1.6, fill=bg)
        fs = 10.5 if val < 1000 else 8.6
        cv.text(x, y + 4.5, str(val), size=fs, weight=700, color=col)

    cx, y = left_pad, 30
    node(cx, y, n)
    for i, (val, pr, co) in enumerate(chain):
        ny = y + dy
        lx, rx = cx - 30, cx + dx
        cv.line(cx, y + 17, lx, ny - 16, color=C["grey"], w=1.2)
        cv.line(cx, y + 17, rx, ny - 16, color=C["grey"], w=1.2)
        node(lx, ny, pr, prime=True)
        node(rx, ny, co, prime=(i == len(chain) - 1))
        cx, y = rx, ny

    from collections import Counter
    primes = [c[1] for c in chain] + ([chain[-1][2]] if chain else [n])
    cnt = Counter(primes)
    expr = " \u00d7 ".join(f"{p}{_sup(e)}" if e > 1 else str(p)
                            for p, e in sorted(cnt.items()))
    cv.text(W / 2, H - 8, f"{n} = {expr}", size=11.5, weight=700,
            color=C["green"])
    return cv.svg()


# ────────────────────────── factor-count visual ──────────────────────────
def factor_count(spec):
    """Show how (e1+1)(e2+1)... gives the number of factors."""
    n = int(spec.get("number", 360))
    f = {}
    m, d = n, 2
    while d * d <= m:
        while m % d == 0:
            f[d] = f.get(d, 0) + 1
            m //= d
        d += 1
    if m > 1:
        f[m] = f.get(m, 0) + 1

    items = sorted(f.items())
    W, H = 340, 158
    cv = Canvas(W, H, seed=_seed(spec, 313))
    bw = 74
    x0 = (W - len(items) * (bw + 10)) / 2

    total = 1
    for i, (p, e) in enumerate(items):
        x = x0 + i * (bw + 10)
        cv.raw(f'<rect x="{x}" y="26" width="{bw}" height="46" rx="7" '
               f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.5"/>')
        cv.text(x + bw / 2, 48, f"{p}{_sup(e)}", size=14, weight=700,
                color=C["blue"])
        cv.text(x + bw / 2, 64, f"power = {e}", size=7.4, color=C["soft"])
        # arrow down to (e+1)
        cv.arrow(x + bw / 2, 76, x + bw / 2, 96, color=C["grey"], w=1.2)
        cv.raw(f'<rect x="{x+14}" y="98" width="{bw-28}" height="26" rx="6" '
               f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.4"/>')
        cv.text(x + bw / 2, 116, f"{e}+1 = {e+1}", size=9.2, weight=700,
                color=C["green"])
        total *= (e + 1)
        if i < len(items) - 1:
            cv.text(x + bw + 5, 116, "x", size=11, color=C["soft"])

    cv.text(W / 2, 14, f"n = {n}", size=11.5, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, f"total factors = {total}", size=11.5,
            weight=700, color=C["red"])
    return cv.svg()


# ────────────────────────── LCM / HCF venn ──────────────────────────
def lcm_hcf_venn(spec):
    """Two numbers as prime-power sets: overlap = HCF, whole = LCM."""
    a = int(spec.get("a", 12))
    b = int(spec.get("b", 18))

    def pf(n):
        f, d = {}, 2
        while d * d <= n:
            while n % d == 0:
                f[d] = f.get(d, 0) + 1
                n //= d
            d += 1
        if n > 1:
            f[n] = f.get(n, 0) + 1
        return f

    fa, fb = pf(a), pf(b)
    common = {p: min(fa.get(p, 0), fb.get(p, 0)) for p in set(fa) & set(fb)}
    onlya = {p: fa[p] - common.get(p, 0) for p in fa if fa[p] - common.get(p, 0) > 0}
    onlyb = {p: fb[p] - common.get(p, 0) for p in fb if fb[p] - common.get(p, 0) > 0}

    def flat(d):
        out = []
        for p in sorted(d):
            out += [str(p)] * d[p]
        return out

    W, H = 340, 208
    cv = Canvas(W, H, seed=_seed(spec, 315))
    r = 66
    c1, c2 = (118, 96), (222, 96)
    cv.circle(*c1, r, color=C["blue"], w=1.7, fill=C["blue_bg"])
    cv.circle(*c2, r, color=C["green"], w=1.7, fill=C["green_bg"])

    cv.text(c1[0] - 34, 22, f"{a}", size=13, weight=700, color=C["blue"])
    cv.text(c2[0] + 34, 22, f"{b}", size=13, weight=700, color=C["green"])

    def stack(cx, items, col):
        if not items:
            cv.text(cx, 96, "-", size=11, color=col)
            return
        for i, t in enumerate(items):
            cv.text(cx, 82 + i * 17, t, size=12, weight=700, color=col)

    stack(80, flat(onlya), C["blue"])
    stack(170, flat(common), C["red"])
    stack(262, flat(onlyb), C["green"])

    hcf = 1
    for p, e in common.items():
        hcf *= p ** e
    import math as _m
    lcmv = a * b // _m.gcd(a, b)

    cv.text(170, 176, f"HCF = {hcf}   (only the overlap)", size=10,
            weight=700, color=C["red"])
    cv.text(170, 194, f"LCM = {lcmv}   (everything, each taken once)",
            size=10, weight=700, color=C["purple"])
    return cv.svg()


# ────────────────────────── euclid division ladder ──────────────────────────
def euclid_ladder(spec):
    """Successive-division method for HCF."""
    a = int(spec.get("a", 1517))
    b = int(spec.get("b", 902))
    if b > a:
        a, b = b, a
    steps = []
    x, y = a, b
    while y:
        steps.append((x, y, x // y, x % y))
        x, y = y, x % y
    hcf = x

    W = 330
    H = 46 + len(steps) * 30 + 30
    cv = Canvas(W, H, seed=_seed(spec, 317))
    cv.text(W / 2, 20, f"HCF of {a} and {b}", size=11.5, weight=700,
            color=C["ink"])
    for i, (dv, dr, q, rem) in enumerate(steps):
        y0 = 40 + i * 30
        last = (rem == 0)
        col = C["green"] if last else C["blue"]
        bg = C["green_bg"] if last else "#ffffff"
        cv.raw(f'<rect x="18" y="{y0}" width="{W-36}" height="24" rx="5" '
               f'fill="{bg}" stroke="{col}" stroke-width="1.3"/>')
        cv.text(30, y0 + 16, f"{dv}  =  {dr} x {q}  +  {rem}", size=10.5,
                anchor="start", color=col, weight=700 if last else 400)
        if last:
            cv.text(W - 30, y0 + 16, "remainder 0", size=8.4, anchor="end",
                    color=C["green"])
    cv.text(W / 2, H - 10, f"last divisor = HCF = {hcf}", size=11.5,
            weight=700, color=C["red"])
    return cv.svg()


# ────────────────────────── fraction comparison bars ──────────────────────────
def fraction_compare(spec):
    """Two or more fractions drawn as shaded bars of equal width."""
    items = spec.get("fracs", ["3/5", "2/3", "7/10"])
    if isinstance(items, str):
        items = [items]
    pairs = []
    for it in items:
        try:
            n, d = str(it).split("/")
            pairs.append((int(n), int(d)))
        except Exception:
            continue

    barw, barh, gap = 230, 30, 16
    W = barw + 120
    H = 26 + len(pairs) * (barh + gap)
    cv = Canvas(W, H, seed=_seed(spec, 319))
    cols = [C["blue"], C["green"], C["amber"], C["purple"], C["teal"]]
    bgs = [C["blue_bg"], C["green_bg"], C["amber_bg"], C["purple_bg"], C["teal_bg"]]

    for i, (n, d) in enumerate(pairs):
        y = 18 + i * (barh + gap)
        col, bg = cols[i % 5], bgs[i % 5]
        cv.text(34, y + barh / 2 + 5, f"{n}/{d}", size=12, weight=700,
                color=col, anchor="end")
        seg = barw / d
        for k in range(d):
            fill = bg if k < n else "#ffffff"
            cv.raw(f'<rect x="{44 + k*seg:.1f}" y="{y}" width="{seg-1:.1f}" '
                   f'height="{barh}" fill="{fill}" stroke="{col}" '
                   f'stroke-width="1.1"/>')
        cv.text(44 + barw + 10, y + barh / 2 + 5, f"{n/d:.3f}", size=9.4,
                anchor="start", color=C["soft"])
    return cv.svg()


# ────────────────────────── decimal place chart ──────────────────────────
def decimal_places(spec):
    """Show what each digit after the point is worth."""
    num = str(spec.get("number", "3.407"))
    if "." not in num:
        num += ".0"
    ip, fp = num.split(".")
    fp = fp[:4]

    cw = 56
    cells = list(ip) + ["."] + list(fp)
    W = cw * len(cells) + 60
    H = 132
    cv = Canvas(W, H, seed=_seed(spec, 321))
    names_int = ["Ones", "Tens", "Hundreds", "Thousands"]
    names_frac = ["Tenths", "Hundredths", "Thousandths", "Ten-thou."]
    vals_frac = ["1/10", "1/100", "1/1000", "1/10000"]

    x = 30
    for idx, ch in enumerate(cells):
        if ch == ".":
            cv.text(x + 8, 52, ".", size=22, weight=700, color=C["red"])
            x += 18
            continue
        if idx < len(ip):
            lbl = names_int[len(ip) - 1 - idx]
            sub = ""
            col, bg = C["blue"], C["blue_bg"]
        else:
            k = idx - len(ip) - 1
            lbl = names_frac[k]
            sub = vals_frac[k]
            col, bg = C["green"], C["green_bg"]
        cv.raw(f'<rect x="{x}" y="24" width="{cw-6}" height="34" rx="5" '
               f'fill="#ffffff" stroke="{C["ink"]}" stroke-width="1.4"/>')
        cv.text(x + (cw - 6) / 2, 48, ch, size=17, weight=700, color=C["ink"])
        cv.raw(f'<rect x="{x}" y="64" width="{cw-6}" height="30" rx="5" '
               f'fill="{bg}" stroke="{col}" stroke-width="1.1"/>')
        cv.text(x + (cw - 6) / 2, 78, lbl, size=6.6, color=col)
        if sub:
            cv.text(x + (cw - 6) / 2, 89, sub, size=7.2, weight=700, color=col)
        x += cw

    cv.text(W / 2, H - 10, "each step right = one-tenth of the step before",
            size=9, color=C["soft"])
    return cv.svg()


# ────────────────────────── BODMAS order ladder ──────────────────────────
def bodmas_order(spec):
    """The six BODMAS stages as a descending ladder."""
    rows = [
        ("B", "Bracket", "( )  { }  [ ]", C["red"], C["red_bg"]),
        ("O", "Of / Order", "of , power", C["amber"], C["amber_bg"]),
        ("D", "Division", "\u00f7", C["green"], C["green_bg"]),
        ("M", "Multiplication", "\u00d7", C["green"], C["green_bg"]),
        ("A", "Addition", "+", C["blue"], C["blue_bg"]),
        ("S", "Subtraction", "\u2212", C["blue"], C["blue_bg"]),
    ]
    W, H = 340, 40 + len(rows) * 34 + 26
    cv = Canvas(W, H, seed=_seed(spec, 323))
    cv.text(W / 2, 20, "order of operations", size=10.5, color=C["soft"])
    for i, (ltr, name, sym, col, bg) in enumerate(rows):
        y = 30 + i * 34
        x = 20 + i * 6                       # slight stagger = ladder feel
        cv.raw(f'<rect x="{x}" y="{y}" width="{W-2*x}" height="27" rx="6" '
               f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>')
        cv.raw(f'<circle cx="{x+18}" cy="{y+13.5}" r="11" fill="{col}"/>')
        cv.text(x + 18, y + 18, ltr, size=12.5, weight=700, color="#ffffff")
        cv.text(x + 36, y + 18, name, size=9.6, anchor="start", color=col,
                weight=700)
        cv.text(W - x - 12, y + 18, sym, size=10.5, anchor="end", color=C["ink"])
    cv.text(W / 2, H - 8, "D and M rank equally - work left to right",
            size=8.6, color=C["red"], weight=700)
    return cv.svg()


# ────────────────────────── approximation rounding ──────────────────────────
def approx_round(spec):
    """Show messy value -> clean value -> answer."""
    pairs = spec.get("pairs", ["249.9=250", "15.02=15"])
    if isinstance(pairs, str):
        pairs = [pairs]
    ans = str(spec.get("answer", "3750"))
    op = str(spec.get("op", "x"))

    W = 320
    H = 44 + len(pairs) * 38 + 44
    cv = Canvas(W, H, seed=_seed(spec, 325))
    cv.text(W / 2, 20, "round first, then calculate", size=9.6, color=C["soft"])
    for i, pr in enumerate(pairs):
        try:
            raw, clean = str(pr).split("=")
        except ValueError:
            continue
        y = 32 + i * 38
        cv.raw(f'<rect x="18" y="{y}" width="118" height="28" rx="6" '
               f'fill="#ffffff" stroke="{C["grey"]}" stroke-width="1.3" '
               f'stroke-dasharray="4 3"/>')
        cv.text(77, y + 19, raw, size=11.5, color=C["soft"])
        cv.arrow(142, y + 14, 178, y + 14, color=C["red"], w=1.4)
        cv.raw(f'<rect x="184" y="{y}" width="118" height="28" rx="6" '
               f'fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.5"/>')
        cv.text(243, y + 19, clean, size=12.5, weight=700, color=C["green"])
    yb = 32 + len(pairs) * 38 + 4
    cv.raw(f'<rect x="60" y="{yb}" width="200" height="30" rx="7" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.6"/>')
    cv.text(160, yb + 20, f"answer {op} {ans}", size=12, weight=700,
            color=C["amber"])
    return cv.svg()


REGISTRY = {
    "bodmas-order": bodmas_order,
    "approx-round": approx_round,
    "fraction-compare": fraction_compare,
    "decimal-places": decimal_places,
    "lcm-hcf-venn": lcm_hcf_venn,
    "euclid-ladder": euclid_ladder,
    "factor-tree": factor_tree,
    "factor-count": factor_count,
    "number-tree": number_tree,
    "place-value": place_value,
    "number-line-ext": number_line_ext,
    "prime-sieve": prime_sieve,
    "divisibility-map": divisibility_map,
}
