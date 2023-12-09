# AoC 2023 day 9
import sys

import numpy as np


def extrapolate(values, f):
    # expand
    out = [values]
    while True:
        values = np.diff(values)
        out.append(values.tolist())
        if not values.any():
            break

    # extrapolate
    out[-1].append(0)
    for i in reversed(range(len(out) - 1)):
        f(out, i)

    return out


lines = open(sys.argv[1]).read().splitlines()
values = [list(map(int, line.split())) for line in lines]


def f1(out, i):
    out[i].append(out[i][-1] + out[i + 1][-1])


# part 1
explored = [extrapolate(v, f1) for v in values]
print(sum(v[0][-1] for v in explored))


def f2(out, i):
    out[i].insert(0, out[i][0] - out[i + 1][0])


# part 2
explored = [extrapolate(v, f2) for v in values]
print(sum(v[0][0] for v in explored))
