# AoC 2023 day 10
import sys

lines = open(sys.argv[1]).read().splitlines()
m = {(r, c): x for r, line in enumerate(lines) for c, x in enumerate(line)}

dirs = {(-1, 0), (0, -1), (1, 0), (0, 1)}
left, up, right, down = dirs
blocks = {
    "L": {right, up},
    "F": {right, down},
    "-": {left, right},
    "|": {up, down},
    "J": {left, up},
    "7": {left, down},
}


def walk(m):
    prev = next(p for p, x in m.items() if x == "S")
    curr = prev

    while True:
        r, c = curr
        for dr, dc in dirs:
            curr = (r + dr, c + dc)
            if curr != prev and curr in m and m[curr] != ".":
                break


walk(m)
