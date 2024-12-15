from dataclasses import dataclass
from pathlib import Path
from sys import argv


@dataclass
class Vec2:
    r: int
    c: int

    def __add__(self, other):
        return Vec2(self.r + other.r, self.c + other.c)

    def __sub__(self, other):
        return Vec2(self.r - other.r, self.c - other.c)

    def __mul__(self, s: int):
        return Vec2(self.r * s, self.c * s)

    def __contains__(self, other):
        return 0 <= other.r < self.r and 0 <= other.c < self.c

    def __hash__(self) -> int:
        return hash((self.r, self.c))


def dir4():
    return [Vec2(-1, 0), Vec2(0, 1), Vec2(1, 0), Vec2(0, -1)]


def load_grid(s: str, f=lambda x: x):
    g = {
        Vec2(r, c): f(x) for r, l in enumerate(s.splitlines()) for c, x in enumerate(l)
    }
    n = max(p.r for p in g.keys()) + 1
    m = max(p.c for p in g.keys()) + 1
    return g, Vec2(n, m)


def printgrid(g, dim: Vec2):
    g2 = [["." for _ in range(dim.c)] for _ in range(dim.r)]
    for k, v in g.items():
        g2[k.r][k.c] = v
    s = "\n".join("".join(l) for l in g2)
    print(s)


def load_file():
    return Path(argv[1]).read_text()
