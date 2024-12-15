import sys
from itertools import product
from pathlib import Path

from utils import Vec2, load_grid


def is_xmas_1(data: dict, p: Vec2, d: Vec2) -> bool:
    for x in "XMAS":
        if data.get(p, "Q") != x:
            return False
        p += d
    return True


def part1(data: dict) -> int:
    ds = set(Vec2(r, c) for r, c in product([-1, 0, 1], [-1, 0, 1])) - {Vec2(0, 0)}
    xs = [k for k, v in data.items() if v == "X"]
    return sum(is_xmas_1(data, p, d) for p in xs for d in ds)


def is_xmas_2(grid: dict, p: tuple[Vec2, Vec2, Vec2], p1: Vec2) -> bool:
    dp, v1, v2 = p
    p2 = p1 + dp

    for x in "MAS":
        if grid.get(p1, "Q") != x or grid.get(p2, "Q") != x:
            return False
        p1 += v1
        p2 += v2
    return True


def part2(grid: dict) -> int:
    # M.S  M.M  S.M  S.S
    # .A.  .A.  .A.  .A.
    # M.S  S.S  S.M  M.M
    ps = [
        (Vec2(2, 0), Vec2(1, 1), Vec2(-1, 1)),
        (Vec2(0, 2), Vec2(1, 1), Vec2(1, -1)),
        (Vec2(2, 0), Vec2(1, -1), Vec2(-1, -1)),
        (Vec2(0, 2), Vec2(-1, 1), Vec2(-1, -1)),
    ]
    ms = [k for k, v in grid.items() if v == "M"]
    return sum(is_xmas_2(grid, p, m) for p in ps for m in ms)


grid, _ = load_grid(Path(sys.argv[1]).read_text())
print(part1(grid))
print(part2(grid))
