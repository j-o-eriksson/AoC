import sys
from pathlib import Path

from utils import Vec2, load_grid

vs = [Vec2(-1, 0), Vec2(0, 1), Vec2(1, 0), Vec2(0, -1)]


def part1(grid, start):
    vi = 0
    v = vs[vi]
    p = start
    visited = {(start, vi)}

    while True:
        grid[p] = "E"

        if p + v not in grid:
            return False, grid

        if grid[p + v] == "#":
            vi = (vi + 1) % 4
            v = vs[vi]
        else:
            p += v

        if (p, vi) in visited:
            return True, grid
        visited.add((p, vi))


def part2(grid: dict, start: Vec2, obstacle: Vec2):
    grid[obstacle] = "#"
    is_infinite, _ = part1(grid, start)
    return is_infinite


grid, _ = load_grid(Path(sys.argv[1]).read_text())
[start] = [k for k, v in grid.items() if v == "^"]

_, g1 = part1(grid.copy(), start)
print(sum(v == "E" for v in g1.values()))

os = [o for o, v in g1.items() if v == "E"]
print(sum(part2(grid.copy(), start, o) for o in os))
