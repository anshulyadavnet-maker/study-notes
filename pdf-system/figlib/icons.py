"""
icons.py — small inline SVG icons for headings, callouts and list items.

Usage in markdown:  :icon-bulb:  :icon-warn:  :icon-target:  :icon-cat:  :icon-dog: ...

Rendered as a ~1em inline SVG so icons sit on the text baseline.
Deliberately stroke-only: WeasyPrint's SVG support does not cover
filters or gradients reliably.
"""

_ICONS = {
    # ── concept / learning ──────────────────────────────────────────
    "bulb": ('<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.5.4.8 1 .8 1.6V16h5.4v-.5c0-.6.3-1.2.8-1.6A6 6 0 0 0 12 3z"/>', "#a8620a"),
    "target": ('<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1.3" fill="currentColor" stroke="none"/>', "#c02b3a"),
    "key": ('<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3.5M21 12v2.5"/>', "#127a4d"),
    "warn": ('<path d="M12 3.5 1.8 20.5h20.4L12 3.5z"/><path d="M12 10v4.5"/><circle cx="12" cy="17.4" r="1" fill="currentColor" stroke="none"/>', "#c02b3a"),
    "star": ('<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1-5.4-2.9-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>', "#6b3fa0"),
    "check": ('<circle cx="12" cy="12" r="9"/><path d="m7.8 12.3 2.9 2.9 5.5-5.9"/>', "#127a4d"),
    "cross": ('<circle cx="12" cy="12" r="9"/><path d="m8.5 8.5 7 7M15.5 8.5l-7 7"/>', "#c02b3a"),
    "cat": ('<path d="M5 9 4 3l5 3a7 7 0 0 1 6 0l5-3-1 6"/><path d="M5 9v4.2A7 7 0 0 0 12 20a7 7 0 0 0 7-6.8V9"/><circle cx="9" cy="12" r=".7" fill="currentColor" stroke="none"/><circle cx="15" cy="12" r=".7" fill="currentColor" stroke="none"/><path d="m11 15 1-1 1 1M12 15v1M8 14l-3-1M8 16l-3 1M16 14l3-1M16 16l3 1"/>', "#6b3fa0"),
    "dog": ('<path d="M6 8 3 4l1 9M18 8l3-4-1 9"/><path d="M6 9v4a6 6 0 0 0 12 0V9"/><circle cx="9" cy="12" r=".7" fill="currentColor" stroke="none"/><circle cx="15" cy="12" r=".7" fill="currentColor" stroke="none"/><path d="m10 15 2 1 2-1M12 16v2"/>', "#a8620a"),

    # ── maths specific ──────────────────────────────────────────────
    "calc": ('<rect x="4.5" y="2.5" width="15" height="19" rx="2"/><path d="M7.5 6.5h9M8 11h.01M12 11h.01M16 11h.01M8 14.5h.01M12 14.5h.01M16 14.5h.01"/>', "#1668c4"),
    "formula": ('<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9.5h4M9 12.5h6M7 15.5h3M15 8.5l3 3M18 8.5l-3 3"/>', "#127a4d"),
    "number": ('<path d="M8 3.5 6 20.5M16 3.5l-2 17M3.5 9h17M2.5 15h17"/>', "#1668c4"),
    "ruler": ('<rect x="2" y="8" width="20" height="8" rx="1.5"/><path d="M6 8v3M10 8v4M14 8v3M18 8v4"/>', "#0b6f78"),
    "clock": ('<circle cx="12" cy="12" r="9"/><path d="M12 7v5.3l3.4 2"/>', "#6b3fa0"),
    "chart": ('<path d="M4 20V4M4 20h16"/><rect x="7" y="12" width="3" height="5"/><rect x="12" y="8" width="3" height="9"/><rect x="17" y="14" width="3" height="3"/>', "#1668c4"),
    "pie": ('<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5v8.5h8.5"/>', "#b83280"),
    "divide": ('<circle cx="12" cy="12" r="9"/><path d="M8 12h8"/><circle cx="12" cy="8.6" r="1.1" fill="currentColor" stroke="none"/><circle cx="12" cy="15.4" r="1.1" fill="currentColor" stroke="none"/>', "#0b6f78"),
    "tree": ('<circle cx="12" cy="4.5" r="2.4"/><circle cx="6.5" cy="14" r="2.4"/><circle cx="17.5" cy="14" r="2.4"/><path d="M10.4 6.2 8 11.8M13.6 6.2 16 11.8"/>', "#127a4d"),

    # ── exam / study ────────────────────────────────────────────────
    "exam": ('<path d="M6 2.5h9l4 4v15H6z"/><path d="M15 2.5v4h4"/><path d="M9 12h7M9 15.5h7M9 8.5h3"/>', "#1668c4"),
    "book": ('<path d="M4 4.5C4 3.7 4.7 3 5.5 3H19v16H5.5C4.7 19 4 19.7 4 20.5z"/><path d="M4 20.5C4 19.7 4.7 19 5.5 19H19v2.5H5.5C4.7 21.5 4 20.8 4 20z"/>', "#6b3fa0"),
    "pencil": ('<path d="m4 20 1-4 11-11 3 3L8 19z"/><path d="m14.5 6.5 3 3"/>', "#a8620a"),
    "trophy": ('<path d="M8 3.5h8v5a4 4 0 0 1-8 0z"/><path d="M8 5H5v1.5A3 3 0 0 0 8 9.5M16 5h3v1.5a3 3 0 0 1-3 3"/><path d="M12 12.5v4M9 20.5h6"/>', "#a8620a"),
    "timer": ('<circle cx="12" cy="13.5" r="7.5"/><path d="M12 9.5v4l2.5 1.5M9.5 2.5h5M12 2.5v3"/>', "#c02b3a"),
    "list": ('<path d="M9 6.5h11M9 12h11M9 17.5h11"/><circle cx="5" cy="6.5" r="1.3" fill="currentColor" stroke="none"/><circle cx="5" cy="12" r="1.3" fill="currentColor" stroke="none"/><circle cx="5" cy="17.5" r="1.3" fill="currentColor" stroke="none"/>', "#4a5163"),
    "steps": ('<path d="M3 20h5v-5h5v-5h5V5"/><path d="M3 20h18"/>', "#0b6f78"),
    "brain": ('<path d="M12 5.5a3 3 0 0 0-5.6-1.4A2.8 2.8 0 0 0 4 9.3a3 3 0 0 0 .6 4.5A3 3 0 0 0 8 18.6a3 3 0 0 0 4 1.9z"/><path d="M12 5.5a3 3 0 0 1 5.6-1.4A2.8 2.8 0 0 1 20 9.3a3 3 0 0 1-.6 4.5 3 3 0 0 1-3.4 4.8 3 3 0 0 1-4 1.9z"/><path d="M12 5.5v14.9"/>', "#b83280"),
}


def render(name, size_em=1.0, color=None):
    """Return an inline <svg> for the named icon."""
    item = _ICONS.get(name)
    if item is None:
        return f'<span class="iconerr">:{name}:</span>'
    body, default = item
    col = color or default
    return (
        f'<svg class="ic" viewBox="0 0 24 24" '
        f'style="width:{size_em:.2f}em;height:{size_em:.2f}em" '
        f'fill="none" stroke="{col}" stroke-width="1.7" color="{col}" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'xmlns="http://www.w3.org/2000/svg">{body}</svg>'
    )


def available():
    return sorted(_ICONS)
