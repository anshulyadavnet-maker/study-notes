"""
sketch.py — seeded hand-drawn (sketchy) SVG primitives.

Rough.js-inspired. Every stroke gets deterministic jitter derived from a seed,
so a figure looks identical on every rebuild (reproducible, never random).

HARD RULE: no Devanagari inside SVG <text>. WeasyPrint's SVG text path does not
compose Devanagari matras reliably. Hindi labels used by figures are emitted as
pre-shaped glyph outlines (SVG <path>) when a label is available in
`hindi_paths.py`; captions/body text remain the preferred place for Hindi.\n\n`Canvas.text()` keeps the no-Devanagari-`<text>` rule and uses the path-backed\nlabels for the small set of tested Hindi labels.
"""
import math
import random
import re

DEVANAGARI = re.compile(r"[\u0900-\u097F]")

# Single-stroke look. Set True for the sketchier double-stroke overlay.
DOUBLE_STROKE = False

# palette — mirrors style.css :root
C = {
    "ink":    "#1f2431",
    "soft":   "#4a5163",
    "blue":   "#1668c4", "blue_bg":   "#eaf3ff",
    "green":  "#127a4d", "green_bg":  "#e6f7ee",
    "amber":  "#a8620a", "amber_bg":  "#fff3dc",
    "red":    "#c02b3a", "red_bg":    "#ffecec",
    "purple": "#6b3fa0", "purple_bg": "#f3ecff",
    "teal":   "#0b6f78", "teal_bg":   "#e3f7f8",
    "pink":   "#b83280", "pink_bg":   "#fdecf6",
    "grey":   "#8b93a6", "paper":     "#fffdf7",
}


def n(v):
    """compact number"""
    return f"{v:.1f}".rstrip("0").rstrip(".")


class Sketch:
    """Generates wobbled path data."""

    def __init__(self, seed=1, roughness=1.0, bowing=1.0, maxrand=2.0):
        self.rng = random.Random(seed)
        self.roughness = roughness
        self.bowing = bowing
        self.maxrand = maxrand

    # ---- randomness helpers -------------------------------------------
    def _off(self, lo, hi, gain=1.0):
        return self.roughness * gain * (self.rng.random() * (hi - lo) + lo)

    def _o(self, x, gain=1.0):
        return self._off(-x, x, gain)

    # ---- line ----------------------------------------------------------
    def _line_d(self, x1, y1, x2, y2, overlay=False):
        lensq = (x1 - x2) ** 2 + (y1 - y2) ** 2
        length = math.sqrt(lensq)
        if length < 200:
            gain = 1.0
        elif length > 500:
            gain = 0.4
        else:
            gain = -0.0016668 * length + 1.233334

        offset = self.maxrand
        if offset * offset * 100 > max(lensq, 1e-6):
            offset = length / 10.0
        o = offset / 2.0 if overlay else offset

        diverge = 0.2 + self.rng.random() * 0.2
        mdx = self.bowing * self.maxrand * (y2 - y1) / 200.0
        mdy = self.bowing * self.maxrand * (x1 - x2) / 200.0
        mdx = self._o(mdx, gain)
        mdy = self._o(mdy, gain)

        sx = x1 + (self._o(o, gain) if not overlay else self._o(o, gain))
        sy = y1 + self._o(o, gain)
        ex = x2 + self._o(o, gain)
        ey = y2 + self._o(o, gain)

        c1x = mdx + x1 + (x2 - x1) * diverge + self._o(o, gain)
        c1y = mdy + y1 + (y2 - y1) * diverge + self._o(o, gain)
        c2x = mdx + x1 + 2 * (x2 - x1) * diverge + self._o(o, gain)
        c2y = mdy + y1 + 2 * (y2 - y1) * diverge + self._o(o, gain)

        return (f"M{n(sx)},{n(sy)} C{n(c1x)},{n(c1y)} "
                f"{n(c2x)},{n(c2y)} {n(ex)},{n(ey)}")

    # ---- smooth closed curve through points ----------------------------
    def _curve_d(self, pts, closed=True):
        """Catmull-Rom -> cubic bezier."""
        if len(pts) < 3:
            return ""
        p = list(pts)
        if closed:
            p = [pts[-1]] + list(pts) + [pts[0], pts[1]]
        else:
            p = [pts[0]] + list(pts) + [pts[-1]]
        d = f"M{n(p[1][0])},{n(p[1][1])}"
        for i in range(1, len(p) - 2):
            p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
            c1x = p1[0] + (p2[0] - p0[0]) / 6.0
            c1y = p1[1] + (p2[1] - p0[1]) / 6.0
            c2x = p2[0] - (p3[0] - p1[0]) / 6.0
            c2y = p2[1] - (p3[1] - p1[1]) / 6.0
            d += (f" C{n(c1x)},{n(c1y)} {n(c2x)},{n(c2y)} "
                  f"{n(p2[0])},{n(p2[1])}")
        if closed:
            d += " Z"
        return d

    def _ellipse_pts(self, cx, cy, rx, ry, steps=9, jitter=1.0):
        pts = []
        start = self._o(0.5) - math.pi / 2
        inc = 2 * math.pi / steps
        for i in range(steps):
            a = start + i * inc + self._o(0.06)
            r1 = rx + self._o(rx * 0.04 * jitter)
            r2 = ry + self._o(ry * 0.04 * jitter)
            pts.append((cx + r1 * math.cos(a), cy + r2 * math.sin(a)))
        return pts

    def _arc_pts(self, cx, cy, rx, ry, a0, a1, steps=None):
        span = a1 - a0
        steps = steps or max(4, int(abs(span) / 0.35) + 2)
        pts = []
        for i in range(steps + 1):
            a = a0 + span * i / steps
            r1 = rx + self._o(rx * 0.03)
            r2 = ry + self._o(ry * 0.03)
            pts.append((cx + r1 * math.cos(a), cy + r2 * math.sin(a)))
        return pts


class Canvas:
    """Accumulates SVG elements for one figure."""

    def __init__(self, w, h, seed=1, roughness=1.0):
        self.w, self.h = w, h
        self.sk = Sketch(seed=seed, roughness=roughness)
        self.parts = []
        self.defs = []
        self.uid = f"f{seed}"

    # ---------- raw ----------
    def raw(self, s):
        self.parts.append(s)

    # ---------- strokes ----------
    def line(self, x1, y1, x2, y2, color=None, w=1.6, dash=None, double=None):
        col = color or C["ink"]
        if double is None:
            double = DOUBLE_STROKE
        da = f' stroke-dasharray="{dash}"' if dash else ""
        self.raw(f'<path d="{self.sk._line_d(x1,y1,x2,y2)}" stroke="{col}" '
                 f'stroke-width="{w}" fill="none" stroke-linecap="round"{da}/>')
        if double:
            self.raw(f'<path d="{self.sk._line_d(x1,y1,x2,y2,overlay=True)}" '
                     f'stroke="{col}" stroke-width="{max(w*0.7,0.7)}" fill="none" '
                     f'opacity="0.55" stroke-linecap="round"{da}/>')

    def polygon(self, pts, color=None, w=1.6, fill=None, close=True, dash=None,
                double=None):
        if fill:
            d = "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + " Z"
            self.raw(f'<path d="{d}" fill="{fill}" stroke="none" opacity="0.9"/>')
        seq = list(pts) + ([pts[0]] if close else [])
        for i in range(len(seq) - 1):
            self.line(*seq[i], *seq[i + 1], color=color, w=w, dash=dash,
                      double=double)

    def rect(self, x, y, w_, h_, **kw):
        self.polygon([(x, y), (x + w_, y), (x + w_, y + h_), (x, y + h_)], **kw)

    def ellipse(self, cx, cy, rx, ry, color=None, w=1.6, fill=None, double=None):
        col = color or C["ink"]
        if double is None:
            double = DOUBLE_STROKE
        if fill:
            p = self.sk._ellipse_pts(cx, cy, rx, ry, jitter=0.4)
            self.raw(f'<path d="{self.sk._curve_d(p)}" fill="{fill}" '
                     f'stroke="none" opacity="0.9"/>')
        for k in range(2 if double else 1):
            p = self.sk._ellipse_pts(cx, cy, rx, ry)
            self.raw(f'<path d="{self.sk._curve_d(p)}" stroke="{col}" '
                     f'stroke-width="{w if k==0 else max(w*0.7,0.7)}" fill="none" '
                     f'opacity="{1 if k==0 else 0.5}" stroke-linecap="round"/>')

    def circle(self, cx, cy, r, **kw):
        self.ellipse(cx, cy, r, r, **kw)

    def arc(self, cx, cy, r, a0, a1, color=None, w=1.4, double=False):
        col = color or C["ink"]
        p = self.sk._arc_pts(cx, cy, r, r, a0, a1)
        self.raw(f'<path d="{self.sk._curve_d(p, closed=False)}" stroke="{col}" '
                 f'stroke-width="{w}" fill="none" stroke-linecap="round"/>')
        if double:
            p = self.sk._arc_pts(cx, cy, r, r, a0, a1)
            self.raw(f'<path d="{self.sk._curve_d(p, closed=False)}" '
                     f'stroke="{col}" stroke-width="{w*0.7}" fill="none" '
                     f'opacity="0.5" stroke-linecap="round"/>')

    # ---------- fills ----------
    def hachure(self, pts, color=None, gap=6, angle=45, w=0.9, opacity=0.5):
        """Scanline diagonal fill inside a polygon."""
        col = color or C["blue"]
        th = math.radians(angle)
        dx, dy = math.cos(th), math.sin(th)
        px, py = -dy, dx
        proj = [(x * px + y * py) for x, y in pts]
        lo, hi = min(proj), max(proj)
        segs = []
        t = lo + gap / 2
        while t < hi:
            hits = []
            for i in range(len(pts)):
                x1, y1 = pts[i]
                x2, y2 = pts[(i + 1) % len(pts)]
                d1 = x1 * px + y1 * py - t
                d2 = x2 * px + y2 * py - t
                if (d1 <= 0 <= d2) or (d2 <= 0 <= d1):
                    if abs(d1 - d2) > 1e-9:
                        u = d1 / (d1 - d2)
                        hits.append((x1 + u * (x2 - x1), y1 + u * (y2 - y1)))
            if len(hits) >= 2:
                hits.sort(key=lambda p: p[0] * dx + p[1] * dy)
                for k in range(0, len(hits) - 1, 2):
                    segs.append((hits[k], hits[k + 1]))
            t += gap
        for a, b in segs:
            self.raw(f'<path d="{self.sk._line_d(a[0],a[1],b[0],b[1])}" '
                     f'stroke="{col}" stroke-width="{w}" fill="none" '
                     f'opacity="{opacity}" stroke-linecap="round"/>')

    # ---------- decorations ----------
    def arrow(self, x1, y1, x2, y2, color=None, w=1.5):
        col = color or C["red"]
        mid = f"ar{self.uid}{len(self.defs)}"
        self.defs.append(
            f'<marker id="{mid}" markerWidth="9" markerHeight="7" refX="8" '
            f'refY="3.5" orient="auto"><path d="M0,0 L9,3.5 L0,7 z" '
            f'fill="{col}"/></marker>')
        self.raw(f'<path d="{self.sk._line_d(x1,y1,x2,y2)}" stroke="{col}" '
                 f'stroke-width="{w}" fill="none" stroke-linecap="round" '
                 f'marker-end="url(#{mid})"/>')

    def right_angle(self, vx, vy, p1, p2, size=11, color=None):
        """Small square marking a 90° angle at vertex v."""
        col = color or C["red"]
        def unit(p):
            dx, dy = p[0] - vx, p[1] - vy
            L = math.hypot(dx, dy) or 1
            return dx / L, dy / L
        u1, u2 = unit(p1), unit(p2)
        a = (vx + u1[0] * size, vy + u1[1] * size)
        b = (vx + u1[0] * size + u2[0] * size, vy + u1[1] * size + u2[1] * size)
        c = (vx + u2[0] * size, vy + u2[1] * size)
        self.line(*a, *b, color=col, w=1.2, double=False)
        self.line(*b, *c, color=col, w=1.2, double=False)

    def ticks(self, p1, p2, count=1, size=5, color=None, gap=3.5):
        """Equal-side tick marks at the midpoint of a segment."""
        col = color or C["purple"]
        mx, my = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        L = math.hypot(dx, dy) or 1
        ux, uy = dx / L, dy / L
        nx, ny = -uy, ux
        start = -(count - 1) * gap / 2
        for i in range(count):
            o = start + i * gap
            cx, cy = mx + ux * o, my + uy * o
            self.line(cx - nx * size / 2, cy - ny * size / 2,
                      cx + nx * size / 2, cy + ny * size / 2,
                      color=col, w=1.2, double=False)

    def dot(self, x, y, r=2.4, color=None):
        self.raw(f'<circle cx="{n(x)}" cy="{n(y)}" r="{n(r)}" '
                 f'fill="{color or C["ink"]}"/>')

    # ---------- text (Latin / numerals, plus tested Hindi path labels) ----------
    def text(self, x, y, s, size=10, color=None, anchor="middle", weight=None,
             italic=False):
        s = str(s)
        if DEVANAGARI.search(s):
            try:
                from . import hindi_paths
                self.raw(hindi_paths.render(
                    s, x, y, size=size, color=color or C["ink"], anchor=anchor
                ))
                return
            except (ImportError, KeyError) as exc:
                raise ValueError(
                    f"No pre-shaped Hindi SVG label is available for {s!r}; "
                    "put Hindi in the Markdown caption/body instead.") from exc
        esc = (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))
        fw = f' font-weight="{weight}"' if weight else ""
        fi = ' font-style="italic"' if italic else ""
        self.raw(f'<text x="{n(x)}" y="{n(y)}" font-size="{size}" '
                 f'text-anchor="{anchor}" fill="{color or C["ink"]}"{fw}{fi}>'
                 f'{esc}</text>')

    # ---------- output ----------
    def svg(self):
        defs = (f"<defs>{''.join(self.defs)}</defs>" if self.defs else "")
        return (f'<svg viewBox="0 0 {n(self.w)} {n(self.h)}" '
                f'width="{n(self.w)}" height="{n(self.h)}" '
                f'xmlns="http://www.w3.org/2000/svg" '
                f'class="figsvg">{defs}{"".join(self.parts)}</svg>')
