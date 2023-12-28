# AoC 2023 day 16
import sys

lines = open(sys.argv[1]).read().splitlines()

g = {(r, c): x for r, line in enumerate(lines) for c, x in enumerate(line)}
g = [[x for x in line] for line in lines]
rmax = len(g)
cmax = len(g[0])

dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # LTRB
mh = {"|": [-1, 1], "-": [0], "/": [-1], "\\": [1], ".": [0]}
mv = {"|": [0], "-": [-1, 1], "/": [1], "\\": [-1], ".": [0]}
ms = [mv, mh]


def walk2(r, c, d_idx, visited):
    path = []
    while True:
        dr, dc = dirs[d_idx]
        r += dr
        c += dc

        if not (0 <= r < rmax and 0 <= c < cmax) or d_idx in visited[r][c]:
            return [path]

        visited[r][c].add(d_idx)
        is_horizonal = dc != 0
        m = ms[is_horizonal]

        path.append((r, c))

        ds = m[g[r][c]]
        if len(ds) == 2:
            return [
                path,
                walk2(r, c, (d_idx + ds[0]) % 4, visited),
                walk2(r, c, (d_idx + ds[1]) % 4, visited),
            ]
        else:
            d_idx = (d_idx + ds[0]) % 4


# part 1
visited = [[set() for _ in range(cmax)] for _ in range(rmax)]
paths = walk2(0, -1, 2, visited)
print(sum(1 for r in visited for x in r if len(x) > 0))

# part 2
rightleft = [(r, c, d) for c, d in [(-1, 2), (cmax, 0)] for r in range(rmax)]
updown = [(r, c, d) for r, d in [(-1, 3), (rmax, 1)] for c in range(cmax)]
counts = []
for r, c, d in rightleft + updown:
    visited = [[set() for _ in range(cmax)] for _ in range(rmax)]
    paths = walk2(r, c, d, visited)
    counts.append(sum(1 for r in visited for x in r if len(x) > 0))
print(max(counts))
