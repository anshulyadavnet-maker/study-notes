"""
trains.py — figures for Chapter 25 (Problems on Trains).

train-pole          : a train covers only its own length past a fixed pole
train-platform      : train length plus platform length
 two-trains         : combined lengths divided by relative speed
moving-person       : train speed relative to a moving person
train-data          : derive speed and train length from two crossing times
crossing-table      : compare pole, platform and bridge crossing distances
"""
from .sketch import Canvas, C


def _seed(spec, default=2500):
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
    value = float(value)
    if abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def _ms(kmh):
    return kmh * 5 / 18


# ───────────────────────────── fixed pole / person ──────────────────────────
def train_pole(spec):
    length = float(spec.get("length", 180))
    speed_kmh = float(spec.get("speed_kmh", 54))
    speed = _ms(speed_kmh)
    seconds = length / speed if speed else 0

    W, H = 452, 244
    cv = Canvas(W, H, seed=_seed(spec, 2501))
    cv.text(W / 2, 20, "past a fixed pole, the train covers only its own length",
            size=9.9, weight=700, color=C["soft"])

    x0, y0, tw = 54, 62, 226
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{tw}" height="40" rx="6" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.7"/>')
    cv.text(x0 + tw / 2, y0 + 25, f"train length = {_fmt(length)} m", size=10,
            weight=700, color=C["blue"])
    px = x0 + tw + 62
    cv.raw(f'<line x1="{px}" y1="{y0-12}" x2="{px}" y2="{y0+54}" '
           f'stroke="{C["red"]}" stroke-width="2"/>')
    cv.text(px, y0 + 71, "fixed pole", size=8.5, weight=700, color=C["red"])
    cv.arrow(x0 + 18, y0 + 62, x0 + tw - 18, y0 + 62, color=C["green"], w=1.4)
    cv.text(x0 + tw / 2, y0 + 80, f"speed = {_fmt(speed)} m/s", size=8.8,
            weight=700, color=C["green"])

    _card(cv, 58, 148, 336, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 170, f"time = length/speed = {_fmt(length)}/{_fmt(speed)} = {_fmt(seconds)} s",
            size=9.5, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "pole length = 0", size=8.9, color=C["ink"])
    return cv.svg()


# ───────────────────────────── platform / bridge ────────────────────────────
def train_platform(spec):
    length = float(spec.get("length", 150))
    platform = float(spec.get("platform", 250))
    speed_kmh = float(spec.get("speed_kmh", 72))
    speed = _ms(speed_kmh)
    distance = length + platform
    seconds = distance / speed if speed else 0

    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 2502))
    cv.text(W / 2, 20, "to clear a platform, the whole train must leave it",
            size=10.2, weight=700, color=C["soft"])

    x0, y0, tw, pw = 32, 60, 142, 226
    cv.raw(f'<rect x="{x0}" y="{y0}" width="{tw}" height="38" rx="6" '
           f'fill="{C["blue_bg"]}" stroke="{C["blue"]}" stroke-width="1.7"/>')
    cv.text(x0 + tw / 2, y0 + 24, f"train {_fmt(length)} m", size=9.2,
            weight=700, color=C["blue"])
    cv.raw(f'<rect x="{x0+tw}" y="{y0+8}" width="{pw}" height="22" rx="4" '
           f'fill="{C["amber_bg"]}" stroke="{C["amber"]}" stroke-width="1.5"/>')
    cv.text(x0 + tw + pw / 2, y0 + 23, f"platform {_fmt(platform)} m", size=8.8,
            weight=700, color=C["amber"])
    cv.arrow(52, y0 + 62, 384, y0 + 62, color=C["green"], w=1.4)
    cv.text(218, y0 + 80, f"distance = {_fmt(length)} + {_fmt(platform)} = {_fmt(distance)} m",
            size=8.8, weight=700, color=C["green"])

    _card(cv, 48, 148, 356, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 170, f"speed = {_fmt(speed)} m/s; time = {_fmt(distance)}/{_fmt(speed)} = {_fmt(seconds)} s",
            size=9.0, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "bridge and tunnel use the same L + object formula",
            size=8.7, color=C["ink"])
    return cv.svg()


# ───────────────────────────── two trains ───────────────────────────────────
def two_trains(spec):
    l1 = float(spec.get("l1", 100))
    l2 = float(spec.get("l2", 200))
    s1 = float(spec.get("s1", 54))
    s2 = float(spec.get("s2", 36))
    direction = str(spec.get("direction", "opposite")).lower()
    opposite = direction not in ("same", "same-direction", "same direction")
    relative_kmh = s1 + s2 if opposite else abs(s1 - s2)
    relative = _ms(relative_kmh)
    distance = l1 + l2
    seconds = distance / relative if relative else 0
    label = "opposite" if opposite else "same direction"
    sign = "+" if opposite else "-"

    W, H = 452, 270
    cv = Canvas(W, H, seed=_seed(spec, 2503))
    cv.text(W / 2, 20, "both trains must pass completely: add their lengths",
            size=9.9, weight=700, color=C["soft"])

    y1, y2 = 62, 112
    cv.raw(f'<rect x="42" y="{y1}" width="150" height="32" rx="5" fill="{C["blue_bg"]}" '
           f'stroke="{C["blue"]}" stroke-width="1.6"/>')
    cv.text(117, y1 + 21, f"A: {_fmt(l1)} m, {_fmt(s1)} km/h", size=8.6,
            weight=700, color=C["blue"])
    cv.raw(f'<rect x="260" y="{y2}" width="150" height="32" rx="5" fill="{C["green_bg"]}" '
           f'stroke="{C["green"]}" stroke-width="1.6"/>')
    cv.text(335, y2 + 21, f"B: {_fmt(l2)} m, {_fmt(s2)} km/h", size=8.6,
            weight=700, color=C["green"])
    if opposite:
        cv.arrow(202, y1 + 16, 252, y1 + 16, color=C["blue"], w=1.4)
        cv.arrow(250, y2 + 16, 200, y2 + 16, color=C["green"], w=1.4)
    else:
        cv.arrow(202, y1 + 16, 252, y1 + 16, color=C["blue"], w=1.4)
        cv.arrow(260, y2 + 16, 310, y2 + 16, color=C["green"], w=1.4)

    _card(cv, 44, 164, 364, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 186, f"distance = {_fmt(l1)} + {_fmt(l2)} = {_fmt(distance)} m",
            size=9.6, weight=700, color=C["purple"])
    _card(cv, 44, 212, 364, 30, C["amber"], C["amber_bg"], sw=1.6)
    cv.text(226, 232, f"{label}: relative = {_fmt(s1)} {sign} {_fmt(s2)} = {_fmt(relative_kmh)} km/h; time = {_fmt(seconds)} s",
            size=8.8, weight=700, color=C["amber"])
    return cv.svg()


# ───────────────────────────── moving person ────────────────────────────────
def moving_person(spec):
    length = float(spec.get("length", 200))
    train_kmh = float(spec.get("train_kmh", 72))
    person_kmh = float(spec.get("person_kmh", 18))
    direction = str(spec.get("direction", "same")).lower()
    same = direction in ("same", "same-direction", "same direction")
    relative_kmh = abs(train_kmh - person_kmh) if same else train_kmh + person_kmh
    relative = _ms(relative_kmh)
    seconds = length / relative if relative else 0
    label = "same direction" if same else "opposite direction"
    sign = "-" if same else "+"

    W, H = 452, 246
    cv = Canvas(W, H, seed=_seed(spec, 2504))
    cv.text(W / 2, 20, "train passes a moving person at relative speed",
            size=10.1, weight=700, color=C["soft"])

    y = 72
    cv.raw(f'<rect x="42" y="{y}" width="220" height="38" rx="6" fill="{C["blue_bg"]}" '
           f'stroke="{C["blue"]}" stroke-width="1.7"/>')
    cv.text(152, y + 24, f"train {_fmt(train_kmh)} km/h", size=10, weight=700,
            color=C["blue"])
    cv.arrow(64, y + 56, 220, y + 56, color=C["blue"], w=1.5)
    cv.raw(f'<circle cx="{326}" cy="{y+20}" r="10" fill="{C["green_bg"]}" stroke="{C["green"]}" stroke-width="1.6"/>')
    cv.text(326, y + 24, "P", size=9, weight=700, color=C["green"])
    if same:
        cv.arrow(344, y + 56, 392, y + 56, color=C["green"], w=1.3)
    else:
        cv.arrow(392, y + 56, 344, y + 56, color=C["green"], w=1.3)
    cv.text(326, y - 10, f"person {_fmt(person_kmh)} km/h", size=8.5,
            weight=700, color=C["green"])

    _card(cv, 46, 148, 360, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 170, f"{label}: relative = { _fmt(train_kmh) } {sign} { _fmt(person_kmh) } = {_fmt(relative_kmh)} km/h",
            size=9.2, weight=700, color=C["purple"])
    _card(cv, 94, 196, 264, 28, C["amber"], C["amber_bg"], sw=1.5)
    cv.text(226, 215, f"time = {_fmt(length)}/{_fmt(relative)} = {_fmt(seconds)} s",
            size=9.4, weight=700, color=C["amber"])
    return cv.svg()


# ───────────────────────────── derive speed and length ──────────────────────
def train_data(spec):
    platform = float(spec.get("platform", 200))
    pole_seconds = float(spec.get("pole_seconds", 20))
    platform_seconds = float(spec.get("platform_seconds", 30))
    speed = platform / (platform_seconds - pole_seconds) if platform_seconds != pole_seconds else 0
    length = speed * pole_seconds
    speed_kmh = speed * 18 / 5

    W, H = 452, 258
    cv = Canvas(W, H, seed=_seed(spec, 2505))
    cv.text(W / 2, 20, "two crossing times reveal both speed and train length",
            size=9.8, weight=700, color=C["soft"])

    rows = [
        ("pole", f"distance L; time { _fmt(pole_seconds) } s", C["blue"], C["blue_bg"]),
        ("platform", f"distance L + { _fmt(platform) }; time { _fmt(platform_seconds) } s", C["amber"], C["amber_bg"]),
    ]
    for i, (lab, text, col, bg) in enumerate(rows):
        y = 46 + i * 42
        _card(cv, 38, y, 376, 30, col, bg, r=5, sw=1.3)
        cv.text(52, y + 20, lab, size=9, anchor="start", weight=700, color=col)
        cv.text(400, y + 20, text, size=8.6, anchor="end", color=col)

    _card(cv, 44, 140, 364, 34, C["purple"], C["purple_bg"], sw=1.7)
    cv.text(226, 162, f"speed = { _fmt(platform) }/({_fmt(platform_seconds)}-{_fmt(pole_seconds)}) = {_fmt(speed)} m/s",
            size=9.1, weight=700, color=C["purple"])
    _card(cv, 54, 188, 344, 30, C["green"], C["green_bg"], sw=1.6)
    cv.text(226, 208, f"length = {_fmt(speed)} x {_fmt(pole_seconds)} = {_fmt(length)} m = {_fmt(speed_kmh)} km/h",
            size=8.9, weight=700, color=C["green"])
    cv.text(W / 2, H - 8, "platform time - pole time gives platform length / speed",
            size=8.5, color=C["ink"])
    return cv.svg()


# ───────────────────────────── compare crossing objects ─────────────────────
def crossing_table(spec):
    length = float(spec.get("length", 180))
    platform = float(spec.get("platform", 270))
    speed_kmh = float(spec.get("speed_kmh", 54))
    speed = _ms(speed_kmh)
    pole_time = length / speed if speed else 0
    platform_time = (length + platform) / speed if speed else 0
    bridge = float(spec.get("bridge", 420))
    bridge_time = (length + bridge) / speed if speed else 0

    W, H = 452, 260
    cv = Canvas(W, H, seed=_seed(spec, 2506))
    cv.text(W / 2, 20, "the object ahead changes the distance to be covered",
            size=10, weight=700, color=C["soft"])

    rows = [
        ("pole", length, pole_time, C["blue"], C["blue_bg"]),
        ("platform", length + platform, platform_time, C["amber"], C["amber_bg"]),
        ("bridge", length + bridge, bridge_time, C["green"], C["green_bg"]),
    ]
    for i, (lab, distance, time, col, bg) in enumerate(rows):
        y = 48 + i * 42
        _card(cv, 38, y, 376, 30, col, bg, r=5, sw=1.3)
        cv.text(54, y + 20, lab, size=9, anchor="start", weight=700, color=col)
        cv.text(220, y + 20, f"distance {_fmt(distance)} m", size=8.7, color=col)
        cv.text(400, y + 20, f"time {_fmt(time)} s", size=8.7, anchor="end", weight=700, color=col)

    _card(cv, 56, 184, 340, 32, C["purple"], C["purple_bg"], sw=1.6)
    cv.text(226, 205, f"speed = {_fmt(speed)} m/s = {_fmt(speed_kmh)} km/h",
            size=9.5, weight=700, color=C["purple"])
    cv.text(W / 2, H - 8, "pole = L; platform = L+P; bridge = L+B",
            size=9, color=C["ink"])
    return cv.svg()


REGISTRY = {
    "train-pole": train_pole,
    "train-platform": train_platform,
    "two-trains": two_trains,
    "moving-person": moving_person,
    "train-data": train_data,
    "crossing-table": crossing_table,
}
