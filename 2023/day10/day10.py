# AoC 2023 day 10
import sys


def walk(start, m, blocks):
    curr = start
    prev = start
    visited = []

    while True:
        visited.append(curr)
        r, c = curr
        opts = [(r + dr, c + dc) for dr, dc in blocks[m[curr]]]
        nxt = next(p for p in opts if p != prev)

        prev = curr
        curr = nxt
        if curr == start:
            break

    return visited


lines = open(sys.argv[1]).read().splitlines()
m = {(r, c): x for r, line in enumerate(lines) for c, x in enumerate(line)}

left, up, right, down = (0, -1), (-1, 0), (0, 1), (1, 0)
blocks = {
    "L": {right, up},
    "F": {right, down},
    "-": {left, right},
    "|": {up, down},
    "J": {left, up},
    "7": {left, down},
    "S": {right, up},  # hard coded
}


start = next(p for p, x in m.items() if x == "S")
path = walk(start, m, blocks)

# part 1
n = len(path) // 2
print(n, path[n])

# part 2


rmax = max(r for r, _ in path)
cmax = max(c for _, c in path)
grid = [[" " for _ in range(cmax + 1)] for _ in range(rmax + 1)]
for r, c in path:
    grid[r][c] = "O"
for r in grid:
    print("".join(r))
