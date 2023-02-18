# AoC 2022 day 22
import sys
import re


a, b = open(sys.argv[1]).read().split("\n\n")
rows = a.split("\n")

grid = dict(
    ((r, c), val)
    for r, row in enumerate(rows)
    for c, val in enumerate(row)
    if val in {".", "#"}
)

N = len(rows)
rbounds = dict(
    (i, (min(xs), max(xs)))
    for i, xs in enumerate([c for r, c in grid if r == i] for i in range(N))
)

M = max(b for _, b in rbounds.values()) + 1
cbounds = dict(
    (i, (min(ys), max(ys)))
    for i, ys in enumerate([r for r, c in grid if c == i] for i in range(M))
)

moves = re.findall("\d+|[LR]", b)

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0


def get_next(x, dx, bounds):
    x_min, x_max = bounds
    if x + dx > x_max:
        return x_min
    if x + dx < x_min:
        return x_max
    return x + dx


d = {"R": 1, "L": -1}
r = 0
c = rbounds[r][0]

for move in moves:
    if move.isalpha():
        direction = (direction + d[move]) % 4
    else:
        dr, dc = directions[direction]

        steps = int(move)
        for _ in range(steps):
            next_pos = (get_next(r, dr, cbounds[c]), get_next(c, dc, rbounds[r]))
            r, c = next_pos if grid[next_pos] == "." else (r, c)

# part 1
print(1000 * (r + 1) + 4 * (c + 1) + direction)
