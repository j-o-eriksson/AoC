from itertools import combinations

from utils import Vec2, load_file, load_grid


def find_pairs(grid: dict):
    s = {v for v in grid.values() if v != "."}
    out = {}
    for c in s:
        gs = [k for k, v in grid.items() if v == c]
        out[c] = list(combinations(gs, 2))
    return out


def antinodes1(a: Vec2, b: Vec2, bounds: Vec2):
    d = a - b
    return [an for an in [a + d, b - d] if an in bounds]


def antinodes2(a: Vec2, b: Vec2, bounds: Vec2):
    d = a - b

    out = [a, b]
    for i in range(1000000):
        ai = a + d * i
        bi = b - d * i
        if ai in bounds:
            out.append(ai)
        if bi in bounds:
            out.append(bi)

        if ai not in bounds and bi not in bounds:
            break

    return out


def count(g: dict, bounds: Vec2, f):
    p = find_pairs(g)
    return len({a for combs in p.values() for a, b in combs for a in f(a, b, bounds)})


s = load_file()
grid, dim = load_grid(s)
print(count(grid, dim, antinodes1))
print(count(grid, dim, antinodes2))
