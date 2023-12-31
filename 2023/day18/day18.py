# AoC 2023 day 18
import sys


def parse(line, part1=True):
    directions = {"L": (0, -1), "U": (-1, 0), "R": (0, 1), "D": (1, 0)}
    a, b, c = line.split()
    if part1:
        return directions[a], int(b)
    else:
        m = {"0": "R", "1": "D", "2": "L", "3": "U"}
        return directions[m[c[-2]]], int(c[2:-2], 16)


def walk(start, steps):
    r, c = start
    path = [(r, c)]
    for (dr, dc), s in steps:
        r += s * dr
        c += s * dc
        path.append((r, c))
    return path


def area(path, border_length):
    area = sum(r1 * c2 - r2 * c1 for (r1, c1), (r2, c2) in zip(path, path[1:])) / 2
    return int(abs(area) + 0.5 * border_length) + 1


lines = open(sys.argv[1]).read().splitlines()

# part 1
steps = [parse(l, part1=True) for l in lines]
path = walk((0, 0), steps)
print(area(path, sum(s for _, s in steps)))

# part 2
steps = [parse(l, part1=False) for l in lines]
path = walk((0, 0), steps)
print(area(path, sum(s for _, s in steps)))
