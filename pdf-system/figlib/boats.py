"""
boats.py — figures for Chapter 26 (Boats & Streams).

speed-components : still-water boat speed combined with stream speed
up-downstream     : compare downstream and upstream speeds
round-trip        : equal-distance downstream and upstream journey
floating-object   : a raft or floating object moves with the stream
boat-data         : derive still-water and current speeds from two speeds
meeting-boats     : two boats moving toward one another on a river
"""
from fractions import Fraction

from .sketch import Canvas, C


def _seed(spec, default=2600):
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


# ───────────────────────────── speed components ──────────────────────────────
def speed_components(spec):
    still = float(spec.get("still", 12))
    current = float(spec.get("current", 3))
    down = still + current
    up = still - current

    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 2601))
    cv.text(W / 2, 20, "the stream adds downstream and subtracts upstream",
            size=9.9, weight=700, color=C["soft"])

    _card(cv, 38, 44, 176, 48, C["blue"], C["blue_bg"], sw=1.6)
    cv.text(126, 63, f"still water = {_fmt(still)} km/h", size=9.5,
            weight=700, color=C["blue"])
    cv.text(126, 81, "boat's own speed", size=8.7, color=C["blue"])

    _card(cv, 238, 44, 176, 48, C["green"], C["green_bg"], sw=1.6)
    cv.text(326, 63, f"stream = {_fmt(current)} km/h", size=9.5,
            weight=700, color=C["green"])
    cv.text(326, 81, "water's speed", size=8.7, color=C["green"])

    cv.arrow(126, 105, 216, 105, color=C["blue"], w=1.4)
    cv.arrow(326, 105, 236, 105, color=C["green"], w=1.4)
    _card(cv, 42, 128, 168, 48, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(126, 148, f"downstream = {_fmt(still)} + {_fmt(current)}", size=8.8,
            weight=700, color=C["purple"])
    cv.text(126, 166, f"= {_fmt(down)} km/h", size=9.4, weight=700, color=C["purple"])

    _card(cv, 242, 128, 168, 48, C["red"], C["red_bg"], sw=1.7)
    cv.text(326, 148, f"upstream = {_fmt(still)} - {_fmt(current)}", size=8.8,
            weight=700, color=C["red"])
    cv.text(326, 166, f"= {_fmt(up)} km/h", size=9.4, weight=700, color=C["red"])

    cv.text(W / 2, 210, "boat speed in still water must be greater than stream speed",
            size=8.8, weight=700, color=C["ink"])
    cv.text(W / 2, H - 8, "downstream is faster; upstream is slower",
            size=9, color=C["soft"])
    return cv.svg()


# ───────────────────────────── compare two effective speeds ──────────────────
def up_downstream(spec):
    down = float(spec.get("down", 15))
    up = float(spec.get("up", 9))
    still = (down + up) / 2
    current = (down - up) / 2

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2602))
    cv.text(W / 2, 20, "add the two effective speeds, subtract them, then halve",
            size=9.8, weight=700, color=C["soft"])

    for y, lab, value, col, bg, arrow_dir in ((54, "downstream", down, C["blue"], C["blue_bg"], 1),
                                                (100, "upstream", up, C["red"], C["red_bg"], -1)):
        _card(cv, 48, y, 356, 32, col, bg, r=5, sw=1.4)
        cv.text(66, y + 21, lab, size=9, anchor="start", weight=700, color=col)
        if arrow_dir > 0:
            cv.arrow(172, y + 16, 260, y + 16, color=col, w=1.2)
        else:
            cv.arrow(260, y + 16, 172, y + 16, color=col, w=1.2)
        cv.text(390, y + 21, f"{_fmt(value)} km/h", size=9.6, anchor="end",
                weight=700, color=col)

    _card(cv, 68, 154, 316, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 176, f"still-water speed = ({_fmt(down)} + {_fmt(up)})/2 = {_fmt(still)}",
            size=9.3, weight=700, color=C["purple"])
    _card(cv, 86, 202, 280, 26, C["green"], C["green_bg"], sw=1.5)
    cv.text(226, 220, f"stream speed = ({_fmt(down)} - {_fmt(up)})/2 = {_fmt(current)}",
            size=9.1, weight=700, color=C["green"])
    return cv.svg()


# ───────────────────────────── equal-distance round trip ────────────────────
def round_trip(spec):
    distance = float(spec.get("distance", 120))
    down = float(spec.get("down", 15))
    up = float(spec.get("up", 9))
    down_time = distance / down if down else 0
    up_time = distance / up if up else 0
    total_time = down_time + up_time
    average = 2 * down * up / (down + up) if down + up else 0

    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 2603))
    cv.text(W / 2, 20, "downstream and upstream distances are equal",
            size=10.2, weight=700, color=C["soft"])

    for y, lab, speed, time, col, bg, direction in ((52, "downstream", down, down_time, C["blue"], C["blue_bg"], 1),
                                                      (102, "upstream", up, up_time, C["red"], C["red_bg"], -1)):
        _card(cv, 38, y, 376, 34, col, bg, r=5, sw=1.4)
        cv.text(54, y + 22, lab, size=8.9, anchor="start", weight=700, color=col)
        if direction > 0:
            cv.arrow(140, y + 17, 264, y + 17, color=col, w=1.3)
        else:
            cv.arrow(264, y + 17, 140, y + 17, color=col, w=1.3)
        cv.text(398, y + 22, f"{_fmt(distance)} km / {_fmt(speed)} = {_fmt(time)} h",
                size=8.5, anchor="end", color=col)

    _card(cv, 48, 158, 356, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 180, f"total time = {_fmt(total_time)} h; average = {_fmt(average)} km/h",
            size=9.4, weight=700, color=C["purple"])
    _card(cv, 86, 208, 280, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 227, f"average = 2({_fmt(down)})({_fmt(up)})/({_fmt(down)}+{_fmt(up)})",
            size=8.8, weight=700, color=C["amber"])
    cv.text(W / 2, H - 8, "equal distance does not mean arithmetic average",
            size=8.7, color=C["red"])
    return cv.svg()


# ───────────────────────────── floating object / raft ───────────────────────
def floating_object(spec):
    current = float(spec.get("current", 4))
    distance = float(spec.get("distance", 120))
    time = distance / current if current else 0

    W, H = 452, 242
    cv = Canvas(W, H, seed=_seed(spec, 2604))
    cv.text(W / 2, 20, "a floating object has no own speed: it follows the stream",
            size=9.8, weight=700, color=C["soft"])

    y = 76
    cv.line(46, y, 406, y, color=C["ink"], w=1.5)
    cv.arrow(70, y, 376, y, color=C["blue"], w=1.7)
    cv.raw(f'<path d="M190 {y-10} L210 {y+5} L252 {y+5} L272 {y-10} Z" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.6"/>')
    cv.text(231, y + 25, "raft", size=8.8, weight=700, color=C["amber"])
    cv.text(110, y - 17, "stream direction", size=8.7, weight=700, color=C["blue"])

    _card(cv, 46, 132, 360, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 154, f"raft speed = stream speed = {_fmt(current)} km/h",
            size=9.6, weight=700, color=C["purple"])
    _card(cv, 94, 182, 264, 28, C["green"], C["green_bg"], sw=1.5)
    cv.text(226, 201, f"time = {_fmt(distance)}/{_fmt(current)} = {_fmt(time)} h",
            size=9.3, weight=700, color=C["green"])
    cv.text(W / 2, H - 8, "still-water boat speed = 0 for a floating object",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── derive component speeds ──────────────────────
def boat_data(spec):
    down = float(spec.get("down", 18))
    up = float(spec.get("up", 10))
    still = (down + up) / 2
    current = (down - up) / 2

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2605))
    cv.text(W / 2, 20, "two effective speeds reveal boat and stream speeds",
            size=9.8, weight=700, color=C["soft"])

    rows = [("downstream", down, "+", C["blue"], C["blue_bg"]),
            ("upstream", up, "-", C["red"], C["red_bg"])]
    for i, (lab, value, sign, col, bg) in enumerate(rows):
        y = 48 + i * 40
        _card(cv, 44, y, 364, 30, col, bg, r=5, sw=1.3)
        cv.text(60, y + 20, lab, size=9, anchor="start", weight=700, color=col)
        cv.text(226, y + 20, f"boat {sign} stream = {_fmt(value)}", size=8.8,
                color=col)
        cv.text(394, y + 20, "km/h", size=8.7, anchor="end", weight=700, color=col)

    _card(cv, 52, 140, 348, 32, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 161, f"boat speed = ({_fmt(down)}+{_fmt(up)})/2 = {_fmt(still)} km/h",
            size=9.2, weight=700, color=C["purple"])
    _card(cv, 78, 186, 296, 28, C["green"], C["green_bg"], sw=1.5)
    cv.text(226, 205, f"stream speed = ({_fmt(down)}-{_fmt(up)})/2 = {_fmt(current)} km/h",
            size=9.1, weight=700, color=C["green"])
    return cv.svg()


# ───────────────────────────── two boats meeting ────────────────────────────
def meeting_boats(spec):
    distance = float(spec.get("distance", 120))
    down = float(spec.get("down", 15))
    up = float(spec.get("up", 9))
    relative = down + up
    time = distance / relative if relative else 0

    W, H = 452, 248
    cv = Canvas(W, H, seed=_seed(spec, 2606))
    cv.text(W / 2, 20, "boats moving toward one another close the gap at relative speed",
            size=9.6, weight=700, color=C["soft"])

    y = 82
    cv.line(48, y, 404, y, color=C["ink"], w=1.5)
    cv.arrow(86, y, 196, y, color=C["blue"], w=1.6)
    cv.arrow(366, y, 256, y, color=C["red"], w=1.6)
    cv.raw(f'<path d="M90 {y-11} L106 {y+5} L134 {y+5} L150 {y-11} Z" fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.5"/>')
    cv.raw(f'<path d="M302 {y-11} L318 {y+5} L346 {y+5} L362 {y-11} Z" fill="{C["red_bg"]}" stroke="{C["red"]}" stroke-width="1.5"/>')
    cv.text(120, y + 27, f"down { _fmt(down) } km/h", size=8.5, weight=700, color=C["blue"])
    cv.text(332, y + 27, f"up { _fmt(up) } km/h", size=8.5, weight=700, color=C["red"])

    _card(cv, 48, 144, 356, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 166, f"relative = {_fmt(down)} + {_fmt(up)} = {_fmt(relative)} km/h",
            size=9.4, weight=700, color=C["purple"])
    _card(cv, 90, 194, 272, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 213, f"meeting time = {_fmt(distance)}/{_fmt(relative)} = {_fmt(time)} h",
            size=9.1, weight=700, color=C["amber"])
    return cv.svg()


REGISTRY = {
    "speed-components": speed_components,
    "up-downstream": up_downstream,
    "round-trip": round_trip,
    "floating-object": floating_object,
    "boat-data": boat_data,
    "meeting-boats": meeting_boats,
}
