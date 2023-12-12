# AoC 2023 day 11
import itertools
import sys


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def more(e, g, idx):
    less = sum(1 for p in g if p[idx] < e)
    more = sum(1 for p in g if p[idx] > e)
    return less * more * (1000000 - 1)


lines = open(sys.argv[1]).read().splitlines()
g = {(r, c) for r, line in enumerate(lines) for c, x in enumerate(line) if x == "#"}
rmax = max(r for r, _ in g)
cmax = max(c for _, c in g)

# part 1
emptyrows = [r for r in range(rmax) if r not in {r for r, _ in g}]
emptycols = [c for c in range(cmax) if c not in {c for _, c in g}]
c1 = sum(dist(a, b) for a, b in itertools.combinations(g, 2))
c2 = sum(more(r, g, 0) for r in emptyrows)
c3 = sum(more(c, g, 1) for c in emptycols)
print(c1 + c2 + c3)
