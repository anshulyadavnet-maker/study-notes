"""figlib — code-generated sketchy SVG figures for the notes pipeline."""
from . import geometry, geometry2, charts, nonverbal, numsys, surds, roots, series, cyclic, wordprob, percent, ratio, average, unitary, profit, interest, compound, partner, mixture, ages, timework, pipes, wages, icons

REGISTRY = {}
for _m in (geometry, geometry2, charts, nonverbal, numsys, surds, roots, series, cyclic, wordprob, percent, ratio, average, unitary, profit, interest, compound, partner, mixture, ages, timework, pipes, wages):
    REGISTRY.update(_m.REGISTRY)


def render(spec):
    t = spec.get("type")
    if t not in REGISTRY:
        raise KeyError(f"unknown figure type {t!r}. known: {sorted(REGISTRY)}")
    return REGISTRY[t](spec)
