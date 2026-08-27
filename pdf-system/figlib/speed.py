"""
speed.py — figures for Chapter 24 (Speed, Time & Distance).

distance-triangle : the D = S x T relationship
unit-conversion   : km/h and m/s conversion factors
average-speed     : equal-distance journeys and weighted average
relative-speed    : same-direction difference and opposite-direction sum
train-crossing    : train length plus platform/pole distance
catch-up          : a faster object closing an initial lead
"""
from fractions import Fraction

from .sketch import Canvas, C


def _seed(spec, default=2400):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _card(cv, x, y, w, h, col, bg, r=6, sw=1.4):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" '
        f'fill="{bg}" stroke="{col}" stroke-width="{sw}"/>'
    )


def _fmt(value):
    if isinstance(value, Fraction):
        if value.denominator == 1:
            return str(value.numerator)
        return f"{value.numerator}/{value.denominator}"
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


# ───────────────────────────── distance-speed-time triangle ─────────────────
def distance_triangle(spec):
    distance = float(spec.get("distance", 150))
    speed = float(spec.get("speed", 60))
    time = distance / speed if speed else 0

    W, H = 420, 242
    cv = Canvas(W, H, seed=_seed(spec, 2401))
    cv.text(W / 2, 20, "distance = speed x time", size=10.8, weight=700,
            color=C["soft"])

    pts = [(W / 2, 45), (70, 174), (350, 174)]
    cv.polygon(pts, color=C["ink"], w=1.6, fill=C["paper"])
    cv.text(W / 2, 104, "D", size=25, weight=700, color=C["blue"])
    cv.text(126, 160, "S", size=22, weight=700, color=C["green"])
    cv.text(294, 160, "T", size=22, weight=700, color=C["amber"])
    cv.text(W / 2, 59, "cover", size=8.6, weight=700, color=C["soft"])
    cv.text(104, 194, "speed", size=8.6, weight=700, color=C["soft"])
    cv.text(316, 194, "time", size=8.6, weight=700, color=C["soft"])

    _card(cv, 48, 211, 324, 24, C["purple"], C["purple_bg"], sw=1.5)
    cv.text(210, 228, f"{_fmt(distance)} km = {_fmt(speed)} km/h x {_fmt(time)} h",
            size=9.1, weight=700, color=C["purple"])
    return cv.svg()


# ───────────────────────────── km/h and m/s conversion ──────────────────────
def unit_conversion(spec):
    kmh = float(spec.get("kmh", 72))
    ms = kmh * 5 / 18
    back = float(spec.get("ms", 15))
    back_kmh = back * 18 / 5

    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 2402))
    cv.text(W / 2, 20, "convert the unit before using distance and time",
            size=10.1, weight=700, color=C["soft"])

    _card(cv, 34, 44, 170, 58, C["blue"], C["blue_bg"], sw=1.7)
    cv.text(119, 65, f"{_fmt(kmh)} km/h", size=13, weight=700, color=C["blue"])
    cv.text(119, 87, f"x 5/18 = {_fmt(ms)} m/s", size=9.5, color=C["blue"])

    _card(cv, 248, 44, 170, 58, C["green"], C["green_bg"], sw=1.7)
    cv.text(333, 65, f"{_fmt(back)} m/s", size=13, weight=700, color=C["green"])
    cv.text(333, 87, f"x 18/5 = {_fmt(back_kmh)} km/h", size=9.5, color=C["green"])

    cv.arrow(204, 73, 248, 73, color=C["grey"], w=1.4)
    cv.arrow(248, 126, 204, 126, color=C["grey"], w=1.4)
    _card(cv, 56, 144, 340, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 165, "1 km/h = 5/18 m/s    |    1 m/s = 18/5 km/h",
            size=9.7, weight=700, color=C["purple"])
    cv.text(W / 2, H - 10, "5/18 for km/h -> m/s; 18/5 in the reverse direction",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── average speed ────────────────────────────────
def average_speed(spec):
    u = float(spec.get("u", 40))
    v = float(spec.get("v", 60))
    distance = float(spec.get("distance", 120))
    equal_avg = 2 * u * v / (u + v) if u + v else 0
    total_time = distance / u + distance / v if u and v else 0

    W, H = 452, 264
    cv = Canvas(W, H, seed=_seed(spec, 2403))
    cv.text(W / 2, 20, "average speed is total distance divided by total time",
            size=9.9, weight=700, color=C["soft"])

    x0, y0, bw, bh = 52, 48, 348, 28
    for i, (speed, col, bg, lab) in enumerate(((u, C["blue"], C["blue_bg"], "leg 1"),
                                                (v, C["green"], C["green_bg"], "leg 2"))):
        y = y0 + i * 48
        _card(cv, x0, y, bw, bh, col, bg, r=4, sw=1.4)
        cv.text(x0 + 58, y + 19, lab, size=8.8, weight=700, color=col)
        cv.text(x0 + 174, y + 19, f"{_fmt(distance)} km", size=8.8, color=col)
        cv.text(x0 + bw - 12, y + 19, f"at {_fmt(speed)} km/h", size=8.8,
                anchor="end", weight=700, color=col)

    _card(cv, 45, 154, 362, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 176, f"equal-distance average = 2uv/(u+v) = {_fmt(equal_avg)} km/h",
            size=9.4, weight=700, color=C["purple"])
    _card(cv, 74, 202, 304, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 221, f"total distance / time = {2*distance}/{_fmt(total_time)} = {_fmt(equal_avg)}",
            size=8.9, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "never take a simple average for equal distances",
            size=8.7, color=C["red"])
    return cv.svg()


# ───────────────────────────── relative speed ───────────────────────────────
def relative_speed(spec):
    s1 = float(spec.get("s1", 45))
    s2 = float(spec.get("s2", 55))
    direction = str(spec.get("direction", "opposite")).lower()
    opposite = direction not in ("same", "same-direction", "same direction")
    rel = s1 + s2 if opposite else abs(s1 - s2)
    label = "opposite directions" if opposite else "same direction"
    sign = "+" if opposite else "-"

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 2404))
    cv.text(W / 2, 20, "relative speed depends on the direction of motion",
            size=10.3, weight=700, color=C["soft"])

    y = 82
    cv.line(54, y, 398, y, color=C["ink"], w=1.5)
    cv.arrow(74, y, 176, y, color=C["blue"], w=1.6)
    if opposite:
        cv.arrow(378, y, 276, y, color=C["green"], w=1.6)
    else:
        cv.arrow(244, y + 32, 366, y + 32, color=C["green"], w=1.6)
    _card(cv, 46, 42, 124, 28, C["blue"], C["blue_bg"], r=4, sw=1.3)
    cv.text(108, 61, f"A: {_fmt(s1)} km/h", size=8.8, weight=700, color=C["blue"])
    _card(cv, 282, 42, 124, 28, C["green"], C["green_bg"], r=4, sw=1.3)
    cv.text(344, 61, f"B: {_fmt(s2)} km/h", size=8.8, weight=700, color=C["green"])

    _card(cv, 54, 146, 344, 36, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 169, f"{label}: relative speed = {_fmt(s1)} {sign} {_fmt(s2)} = {_fmt(rel)} km/h",
            size=9.5, weight=700, color=C["purple"])
    cv.text(W / 2, 210, "convert to m/s before using a metre distance and seconds",
            size=8.9, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "opposite -> add; same -> subtract",
            size=9, color=C["red"])
    return cv.svg()


# ───────────────────────────── train crossing ───────────────────────────────
def train_crossing(spec):
    train = float(spec.get("train", 180))
    platform = float(spec.get("platform", 0))
    speed_kmh = float(spec.get("speed_kmh", 54))
    speed_ms = speed_kmh * 5 / 18
    distance = train + platform
    seconds = distance / speed_ms if speed_ms else 0

    W, H = 452, 256
    cv = Canvas(W, H, seed=_seed(spec, 2405))
    cv.text(W / 2, 20, "crossing distance = train length + object length",
            size=10.1, weight=700, color=C["soft"])

    x0, y0 = 42, 66
    train_w = 190
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{train_w}" height="38" rx="6" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.7"/>')
    cv.text(x0 + train_w / 2, y0 + 24, f"train { _fmt(train) } m", size=10,
            weight=700, color=C["blue"])
    if platform:
        pw = 150
        cv.raw(f'<rect x="{x0 + train_w}" y="{y0 + 8}" width="{pw}" height="22" '
               f'rx="4" fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.4"/>')
        cv.text(x0 + train_w + pw / 2, y0 + 23, f"platform { _fmt(platform) } m",
                size=8.7, weight=700, color=C["amber"])
    else:
        cv.raw(f'<line x1="{x0 + train_w + 26}" y1="{y0 - 4}" x2="{x0 + train_w + 26}" y2="{y0 + 48}" '
               f'stroke="{C["red"]}" stroke-width="2"/>')
        cv.text(x0 + train_w + 26, y0 + 64, "pole", size=8.8, weight=700,
                color=C["red"])

    _card(cv, 48, 138, 356, 32, C["green"], C["green_bg"], sw=1.6)
    cv.text(226, 159, f"distance = {_fmt(distance)} m; speed = {_fmt(speed_ms)} m/s",
            size=9.4, weight=700, color=C["green"])
    _card(cv, 82, 188, 288, 30, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 208, f"time = { _fmt(distance) }/{_fmt(speed_ms)} = {_fmt(seconds)} s",
            size=9.8, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "a pole has zero length; a platform does not",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── catch-up / meeting ───────────────────────────
def catch_up(spec):
    lead = float(spec.get("lead", 30))
    fast = float(spec.get("fast", 60))
    slow = float(spec.get("slow", 45))
    relative = fast - slow
    hours = lead / relative if relative > 0 else 0

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 2406))
    cv.text(W / 2, 20, "catch-up time = initial lead / relative speed",
            size=10.2, weight=700, color=C["soft"])

    x0, y, scale = 60, 86, 5.0
    cv.line(x0, y, x0 + 330, y, color=C["ink"], w=1.5)
    cv.arrow(x0 + 20, y, x0 + 160, y, color=C["green"], w=1.6)
    cv.arrow(x0 + 112, y + 32, x0 + 260, y + 32, color=C["blue"], w=1.6)
    cv.dot(x0 + lead * scale, y, r=5, color=C["red"])
    cv.text(x0 + lead * scale, y - 15, f"lead {_fmt(lead)} km", size=8.8,
            weight=700, color=C["red"])
    cv.text(x0 + 90, y - 30, f"slow {_fmt(slow)} km/h", size=8.8,
            weight=700, color=C["green"])
    cv.text(x0 + 185, y + 52, f"fast {_fmt(fast)} km/h", size=8.8,
            weight=700, color=C["blue"])

    _card(cv, 56, 146, 340, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 168, f"relative = { _fmt(fast) } - { _fmt(slow) } = {_fmt(relative)} km/h",
            size=9.5, weight=700, color=C["purple"])
    _card(cv, 98, 196, 256, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 215, f"catch-up time = {_fmt(lead)}/{_fmt(relative)} = {_fmt(hours)} h",
            size=9.2, weight=700, color=C["amber"])
    return cv.svg()


REGISTRY = {
    "distance-triangle": distance_triangle,
    "unit-conversion": unit_conversion,
    "average-speed": average_speed,
    "relative-speed": relative_speed,
    "train-crossing": train_crossing,
    "catch-up": catch_up,
}
