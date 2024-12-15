from utils import Vec2, dir4, load_file, load_grid


def explore(g: dict, start: tuple[Vec2, int]):
    vs = dir4()
    trail = [start]
    out = []

    while True:
        p, x = trail[-1]
        if x == 9:
            out.append(p)
            return out

        pps = [(p + v, g[p + v]) for v in vs if g.get(p + v, 1337) - x == 1]

        if len(pps) > 0:
            trail.append(pps.pop())
            for pp in pps:
                out += explore(g, pp)
        else:
            return out


def part1(g: dict):
    trailheads = [(p, x) for p, x in g.items() if x == 0]
    return sum(len(set(explore(g, t))) for t in trailheads)


def part2(g: dict):
    trailheads = [(p, x) for p, x in g.items() if x == 0]
    return sum(len(explore(g, t)) for t in trailheads)


data = load_file()
g, _ = load_grid(data, int)
print(part1(g))
print(part2(g))
