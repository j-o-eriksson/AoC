# AoC 2023 day 14
import copy
import itertools
import sys

rows = open(sys.argv[1]).read().splitlines()
m = {".": 0, "O": 1, "#": 2}
g = [[m[ch] for ch in row] for row in rows]
rmax = len(g)
cmax = len(g[0])


def printt():
    for r, row in enumerate(g):
        print(r, "".join(m2[x] for x in row))
    print()


def nxt(r, c, dr, dc):
    while True:
        r += dr
        c += dc
        valid = 0 <= r < rmax and 0 <= c < cmax and g[r][c] == 0
        if not valid:
            return r - dr, c - dc


def shuffle(rrange, crange, dr, dc):
    for r, c in itertools.product(rrange, crange):
        if g[r][c] == 1:
            r1, c1 = nxt(r, c, dr, dc)
            g[r][c] = 0
            g[r1][c1] = 1

def load():
    load = 0
    for r, row in enumerate(g):
        print(r, "".join(m2[x] for x in row))
        load += (len(g) - r) * sum(1 for x in row if x == 1)
    return load


m2 = {v: k for k, v in m.items()}

# part 1
shuffle(range(1, rmax), range(cmax), -1, 0)
print(load())


# part 2
def cycle(n):
    for _ in range(n):
        ds = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        shuffle(range(1, rmax), range(cmax), *ds[0])
        shuffle(range(rmax), range(1, cmax), *ds[1])
        shuffle(reversed(range(rmax - 1)), range(cmax), *ds[2])
        shuffle(range(rmax), reversed(range(cmax - 1)), *ds[3])


def find_cycle():
    gs = [copy.deepcopy(g)]
    for i1 in range(1000000000):
        cycle(1)
        i0 = next((i for i, gi in enumerate(gs) if gi == g), -1)
        gs.append(copy.deepcopy(g))
        if i0 != -1:
            return i0, i1
    return -1, -1


i0, i1 = find_cycle()
repeat = i1 - i0 + 1

big = 1000000000
remaining = (big - i0) % repeat
cycle(remaining)
print(load())
