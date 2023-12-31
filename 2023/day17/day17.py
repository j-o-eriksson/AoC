# AoC 2023 day 17
import sys
import typing

lines = open(sys.argv[1]).read().splitlines()
g = [list(map(int, r)) for r in lines]
rmax = len(g)
cmax = len(g[0])


class Data(typing.NamedTuple):
    r: int
    c: int
    dir: int
    steps: int
    cost: int


def _directions(d: Data) -> typing.List[typing.Tuple[typing.Tuple[int, int], int, int]]:
    ds = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # LTRB
    ii = [(d.dir - 1) % 4, (d.dir + 1) % 4]
    if d.steps == 3:
        return [(ds[i], i, 1) for i in ii]
    else:
        return [(ds[i], i, 1) for i in ii] + [(ds[d.dir], d.dir, d.steps + 1)]


def candidates(l: Data, visited) -> typing.List[Data]:
    return [
        Data(l.r + dr, l.c + dc, dir, steps, l.cost + g[l.r + dr][l.c + dc])
        for (dr, dc), dir, steps in _directions(l)
        if (l.r + dr, l.c + dc, dir, steps) not in visited
        and 0 <= l.r + dr < rmax
        and 0 <= l.c + dc < cmax
    ]


def pop(q, visited):
    while True:
        d = q.pop()
        if (d.r, d.c, d.dir, d.steps) not in visited:
            visited.add((d.r, d.c, d.dir, d.steps))
            return d


def explore(start, end):
    visited = set()
    q = [start]

    count = 0
    while True:
        count += 1
        d = pop(q, visited)
        q += candidates(d, visited)
        q.sort(key=lambda x: -x.cost)

        if (d.r, d.c) == end:
            print("count:", count, rmax * cmax)
            return d.cost


r0, c0 = 0, 0
print(explore(Data(r0, c0, dir=2, steps=0, cost=0), (rmax - 1, cmax - 1)))
