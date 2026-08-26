"""figlib — code-generated sketchy SVG figures for the notes pipeline."""
from . import geometry, geometry2, charts, nonverbal, numsys, surds, roots, series, cyclic, wordprob, percent, ratio, average, unitary, profit, interest, compound, partner, mixture, ages, timework, pipes, wages, speed, trains, boats, algebra, identities, factor, linear, quadratic, comparison, lines_angles, triangles, congruence, quadrilaterals, circles_tangents, mensuration2d, solids3d, prisms_pyramids, coordinate41, trig, trig_identities, heights, statistics, modern_math, ctet_math, icons

REGISTRY = {}
for _m in (geometry, geometry2, charts, nonverbal, numsys, surds, roots, series, cyclic, wordprob, percent, ratio, average, unitary, profit, interest, compound, partner, mixture, ages, timework, pipes, wages, speed, trains, boats, algebra, identities, factor, linear, quadratic, comparison, lines_angles, triangles, congruence, quadrilaterals, circles_tangents, mensuration2d, solids3d, prisms_pyramids, coordinate41, trig, trig_identities, heights, statistics, modern_math, ctet_math):
    REGISTRY.update(_m.REGISTRY)


def render(spec):
    t = spec.get("type")
    if t not in REGISTRY:
        raise KeyError(f"unknown figure type {t!r}. known: {sorted(REGISTRY)}")
    return REGISTRY[t](spec)
