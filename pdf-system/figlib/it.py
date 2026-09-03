"""Vector teaching figures for the SuperTET Information Technology notes.

All in-figure labels stay in Latin script (numbers, short words) so the SVG
remains reliable in WeasyPrint; Hindi explanations go in the Markdown caption
next to each block, exactly like the rest of figlib.
"""
import math

from .sketch import Canvas, C


def _seed(spec, default=8800):
    value = spec.get("seed", default)
    try:
        return int(value)
    except Exception:
        return sum(ord(ch) for ch in str(value))


def _box(cv, x, y, w, h, label, col, bg="#ffffff", size=8.4):
    cv.raw(
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" '
        f'fill="{bg}" stroke="{col}" stroke-width="1.4"/>'
    )
    cv.text(x + w / 2, y + h / 2 + 3, label, size=size, weight=700, color=col)


# ─────────────────────────── computer system ───────────────────────────
def computer_system(spec):
    """Classic block diagram: Input -> CPU <-> Output, with RAM & storage."""
    W, H = 452, 250
    cv = Canvas(W, H, seed=_seed(spec, 8801))
    cv.text(W / 2, 16, "computer system: devices, processor and memory work together",
            size=9.3, weight=700, color=C["soft"])
    # central CPU
    cv.raw('<rect x="164" y="92" width="124" height="52" rx="7" '
           'fill="#ffffff" stroke="#1668c4" stroke-width="1.8"/>')
    cv.text(226, 112, "CPU", size=10, weight=700, color="#1668c4")
    cv.text(226, 130, "(ALU + CU)", size=7.8, color="#5a6275")
    # input / output
    _box(cv, 40, 100, 88, 36, "Input", C["green"], bg="#e6f7ee")
    _box(cv, 324, 100, 88, 36, "Output", C["red"], bg="#ffecec")
    cv.arrow(130, 118, 160, 118, color=C["grey"], w=1.4)
    cv.arrow(292, 118, 322, 118, color=C["grey"], w=1.4)
    cv.text(145, 108, "data", size=7.4, color=C["grey"])
    cv.text(297, 108, "info", size=7.4, color=C["grey"])
    # RAM under CPU
    _box(cv, 176, 176, 100, 34, "RAM (volatile)", C["purple"], bg="#f3ecff")
    cv.arrow(226, 148, 226, 172, color=C["purple"], w=1.2)
    cv.arrow(226, 178, 226, 152, color=C["purple"], w=1.0)
    # secondary storage right of RAM
    _box(cv, 312, 176, 100, 34, "HDD / SSD", C["amber"], bg="#fff3dc")
    cv.arrow(280, 193, 308, 193, color=C["amber"], w=1.2)
    cv.arrow(312, 187, 284, 187, color=C["amber"], w=1.0)
    cv.text(226, 232, "RAM ↔ storage: programs/data move in and out of RAM",
            size=7.8, color=C["soft"])
    return cv.svg()


# ─────────────────────────── computer generations ───────────────────────────
def generations(spec):
    """Five ascending steps: vacuum tube -> transistor -> IC -> micro -> AI."""
    W, H = 452, 220
    cv = Canvas(W, H, seed=_seed(spec, 8802))
    cv.text(W / 2, 16, "generations rise in size and speed", size=9.3,
            weight=700, color=C["soft"])
    steps = [("1 Vacuum Tube", C["red"]), ("2 Transistor", C["amber"]),
             ("3 IC", C["green"]), ("4 Microprocessor", C["blue"]),
             ("5 AI", C["purple"])]
    x = 34
    for i, (lab, col) in enumerate(steps):
        w = 74 if i in (0, 1) else 72
        y = 168 - i * 27
        _box(cv, x, y, w, 26, lab, col, bg="#ffffff", size=7.6)
        if i < len(steps) - 1:
            cv.arrow(x + w + 2, y + 13, x + w + 16, y + 13, color=C["grey"], w=1.1)
            cv.line(x + w + 16, y + 13, x + w + 16, y - 14, color=C["grey"], w=1.1)
            cv.arrow(x + w + 16, y - 14, x + w + 24, y - 14, color=C["grey"], w=1.1)
        x += w + 26
    cv.text(W / 2, 204, "technology shrinks, speed and storage grow",
            size=8, color=C["soft"])
    return cv.svg()


# ─────────────────────────── memory hierarchy ───────────────────────────
def memory_hierarchy(spec):
    """Pyramid: registers -> cache -> RAM -> secondary storage."""
    W, H = 452, 236
    cv = Canvas(W, H, seed=_seed(spec, 8803))
    cv.text(W / 2, 16, "memory pyramid: higher = faster, costlier, smaller",
            size=9.3, weight=700, color=C["soft"])
    tiers = [(226, 36, 70, "Registers", C["red"]),
             (226, 78, 150, "Cache", C["amber"]),
             (226, 122, 250, "RAM (primary)", C["blue"]),
             (226, 176, 380, "HDD / SSD (secondary)", C["green"])]
    for cx, y, w, lab, col in tiers:
        cv.raw(f'<rect x="{cx - w/2}" y="{y}" width="{w}" height="40" rx="6" '
               f'fill="#ffffff" stroke="{col}" stroke-width="1.6"/>')
        cv.text(cx, y + 24, lab, size=8.8 if len(lab) < 16 else 8.2,
                weight=700, color=col)
    cv.text(150, 52, "fast", size=7.6, color=C["red"], anchor="end")
    cv.text(150, 196, "large", size=7.6, color=C["green"], anchor="end")
    return cv.svg()


# ─────────────────────────── software types ───────────────────────────
def software_tree(spec):
    """Software branches into System software and Application software."""
    W, H = 452, 240
    cv = Canvas(W, H, seed=_seed(spec, 8804))
    cv.text(W / 2, 16, "software: system runs the machine, applications do jobs",
            size=9.3, weight=700, color=C["soft"])
    _box(cv, 196, 34, 60, 30, "Software", C["ink"], bg="#eef1f6", size=8.6)
    cv.arrow(196, 64, 150, 86, color=C["grey"], w=1.0)
    cv.arrow(256, 64, 302, 86, color=C["grey"], w=1.0)
    # system panel
    _box(cv, 44, 88, 160, 28, "System software", C["blue"], bg="#eaf3ff", size=8.2)
    for i, t in enumerate(["OS", "Drivers", "Utilities"]):
        _box(cv, 40 + i * 60, 140, 56, 26, t, C["blue"], bg="#ffffff", size=7.6)
        cv.arrow(124, 118, 88 + i * 60 - 4, 138, color=C["blue"], w=0.9)
    # application panel
    _box(cv, 248, 88, 160, 28, "Application software", C["green"], bg="#e6f7ee", size=8.2)
    for i, t in enumerate(["Office", "Browser", "Games"]):
        _box(cv, 244 + i * 60, 140, 56, 26, t, C["green"], bg="#ffffff", size=7.6)
        cv.arrow(328, 118, 292 + i * 60 - 4, 138, color=C["green"], w=0.9)
    cv.text(W / 2, 202, "OS = system software that runs the whole computer",
            size=8.2, color=C["soft"])
    return cv.svg()


# ─────────────────────────── OS sandwich ───────────────────────────
def os_layer(spec):
    """User -> Application -> Operating System -> Hardware sandwich."""
    W, H = 452, 260
    cv = Canvas(W, H, seed=_seed(spec, 8805))
    cv.text(W / 2, 16, "OS sits between the user and the hardware",
            size=9.3, weight=700, color=C["soft"])
    rows = [("User", C["red"], 44), ("Application software", C["amber"], 96),
            ("Operating system", C["blue"], 148), ("Hardware", C["green"], 210)]
    for i, (lab, col, y) in enumerate(rows):
        w = 230
        cv.raw(f'<rect x="{226 - w/2}" y="{y}" width="{w}" height="38" rx="6" '
               f'fill="#ffffff" stroke="{col}" stroke-width="1.7"/>')
        cv.text(226, y + 23, lab, size=9.6, weight=700, color=col)
        if i < len(rows) - 1:
            gap_top = y + 38
            gap_bot = rows[i + 1][2]
            mid = (gap_top + gap_bot) / 2
            cv.arrow(219, gap_top + 2, 219, gap_bot - 2, color=C["grey"], w=1.1)
            cv.arrow(233, gap_bot - 2, 233, gap_top + 2, color=C["grey"], w=1.1)
    cv.text(226, 244, "user talks to hardware only through the OS",
            size=8.2, color=C["soft"])
    return cv.svg()


# ─────────────────────────── network topologies ───────────────────────────
def network_topology(spec):
    """Three small panels: star, bus and ring."""
    W, H = 452, 224
    cv = Canvas(W, H, seed=_seed(spec, 8806))
    cv.text(W / 2, 14, "network layouts: star | bus | ring", size=9.2,
            weight=700, color=C["soft"])

    def node(x, y, col=C["blue"]):
        cv.circle(x, y, 7, color=col, w=1.6, fill=C["blue_bg"] if col == C["blue"] else C["green_bg"])

    # star
    cv.text(86, 44, "Star", size=8.6, weight=700, color=C["blue"])
    cx, cy = 86, 128
    node(cx, cy)
    for a in (0, 90, 180, 270):
        x2 = cx + int(52 * math.cos(math.radians(a)))
        y2 = cy + int(44 * math.sin(math.radians(a)))
        cv.line(cx, cy, x2, y2, color=C["grey"], w=1.0)
        node(x2, y2, C["green"])
    # bus
    cv.text(226, 44, "Bus", size=8.6, weight=700, color=C["green"])
    cv.line(182, 128, 270, 128, color=C["blue"], w=2.0)
    for x in (196, 226, 256):
        cv.line(x, 128, x, 120, color=C["grey"], w=1.0)
        node(x, 116)
    # ring
    cv.text(374, 44, "Ring", size=8.6, weight=700, color=C["purple"])
    pts = [(336, 96), (412, 96), (412, 160), (336, 160)]
    for i in range(4):
        a, b = pts[i], pts[(i + 1) % 4]
        cv.line(a[0], a[1], b[0], b[1], color=C["purple"], w=1.6)
    for x, y in pts:
        node(x, y, C["purple"])
    cv.text(W / 2, 208, "school LAN is usually star-shaped (hub/switch in the middle)",
            size=8, color=C["soft"])
    return cv.svg()


# ─────────────────────────── email flow ───────────────────────────
def email_flow(spec):
    """Sender -> SMTP server -> Internet -> POP/IMAP server -> Receiver."""
    W, H = 452, 196
    cv = Canvas(W, H, seed=_seed(spec, 8807))
    cv.text(W / 2, 14, "email path: SMTP sends, POP3 / IMAP receive",
            size=9.3, weight=700, color=C["soft"])
    boxes = [("Sender", C["green"], 28, 62),
             ("Mail server", C["blue"], 108, 80),
             ("Internet", C["grey"], 206, 64),
             ("Mail server", C["blue"], 288, 80),
             ("Receiver", C["red"], 386, 62)]
    for lab, col, x, w in boxes:
        _box(cv, x, 58, w, 36, lab, col, bg="#ffffff", size=7.6)
    for (_, _, xa, wa), (_, _, xb, _) in zip(boxes, boxes[1:]):
        cv.arrow(xa + wa + 3, 76, xb - 4, 76, color=C["grey"], w=1.3)
    cv.text(76, 108, "SMTP", size=7.2, color=C["green"])
    cv.text(300, 108, "POP3 / IMAP", size=7.2, color=C["blue"])
    cv.text(226, 134, "sending uses SMTP; receiving uses POP3 / IMAP",
            size=7.9, color=C["soft"])
    return cv.svg()


# ─────────────────────────── client / server ───────────────────────────
def client_server(spec):
    """Browser (client) requests, web server responds."""
    W, H = 452, 172
    cv = Canvas(W, H, seed=_seed(spec, 8808))
    cv.text(W / 2, 14, "browsing the web: client asks, server answers",
            size=9.3, weight=700, color=C["soft"])
    _box(cv, 40, 66, 120, 40, "Browser (client)", C["green"], bg="#e6f7ee")
    _box(cv, 292, 66, 120, 40, "Web server", C["blue"], bg="#eaf3ff")
    cv.arrow(164, 86, 288, 86, color=C["green"], w=1.6)
    cv.arrow(288, 78, 164, 78, color=C["blue"], w=1.6)
    cv.text(226, 118, "request (ask for page)", size=7.4, color=C["green"])
    cv.text(226, 34, "response (page arrives)", size=7.4, color=C["blue"])
    return cv.svg()


# ─────────────────────────── malware fan ───────────────────────────
def malware_fan(spec):
    """Malware centre with five common kinds around it."""
    W, H = 452, 224
    cv = Canvas(W, H, seed=_seed(spec, 8809))
    cv.text(W / 2, 14, "malware = malicious software that harms a computer",
            size=9.3, weight=700, color=C["soft"])
    cv.circle(226, 116, 34, color=C["red"], w=2.0, fill="#ffecec")
    cv.text(226, 121, "Malware", size=9.2, weight=700, color=C["red"])
    kinds = [("Virus", 90), ("Worm", 45), ("Trojan", 0), ("Spyware", -45), ("Ransomware", -90)]
    for lab, deg in kinds:
        a = math.radians(90 + deg)
        x = 226 + int(108 * math.cos(a))
        y = 116 + int(74 * math.sin(a))
        cv.line(226 + int(40 * math.cos(a)), 116 + int(34 * math.sin(a)), x, y,
                color=C["grey"], w=0.9)
        w = 74 if len(lab) > 7 else 58
        _box(cv, x - w / 2, y - 13, w, 26, lab, C["purple"], bg="#ffffff", size=7.6)
    cv.text(W / 2, 208, "they attach, spread, hide or demand money - keep software updated",
            size=7.8, color=C["soft"])
    return cv.svg()


REGISTRY = {
    "it-computer-system": computer_system,
    "it-generations": generations,
    "it-memory-hierarchy": memory_hierarchy,
    "it-software-tree": software_tree,
    "it-os-layer": os_layer,
    "it-network-topology": network_topology,
    "it-email-flow": email_flow,
    "it-client-server": client_server,
    "it-malware-fan": malware_fan,
}
