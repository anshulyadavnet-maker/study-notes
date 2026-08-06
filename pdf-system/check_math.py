#!/usr/bin/env python3
"""check_math.py — flag Devanagari inside $…$ / $$…$$ (renders as tofu)."""
import re, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
try:
    from figlib import mathtex
except Exception:
    mathtex = None
DEV = re.compile(r"[\u0900-\u097F]")
CODE = re.compile(r"(```.*?```|`[^`\n]*`)", re.S)
DISP = re.compile(r"\$\$(.+?)\$\$", re.S)
INLN = re.compile(r"(?<!\$)\$(?!\$)([^$\n]+?)(?<!\$)\$(?!\$)")
bad = 0
for f in sys.argv[1:]:
    txt = pathlib.Path(f).read_text(encoding="utf-8")
    for chunk in CODE.split(txt):
        if chunk.startswith("`"):
            continue
        for rx in (DISP, INLN):
            for m in rx.finditer(chunk):
                expr = m.group(1)
                if DEV.search(expr):
                    print(f"  {f}: Devanagari in math -> {expr[:60]!r}")
                    bad += 1
                elif mathtex is not None and "texerr" in mathtex.render(expr, rx is DISP):
                    print(f"  {f}: LaTeX not supported -> {expr[:60]!r}")
                    bad += 1
print("clean" if not bad else f"{bad} problem(s)")
sys.exit(1 if bad else 0)
