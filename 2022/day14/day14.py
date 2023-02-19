# AoC 2022 day 14
import itertools
import sys


def _parse(line):
    return [(int(x), int(y)) for x, y in (ps.split(",") for ps in line.split(" -> "))]


def _get_rocks(rock_segment):
    out = []
    for (x0, y0), (x1, y1) in zip(rock_segment, rock_segment[1:]):
        rx = range(min(x0, x1), max(x0, x1) + 1)
        ry = range(min(y0, y1), max(y0, y1) + 1)
        out.extend([(x, y) for x, y in itertools.product(rx, ry)])
    return out


def get_next_pos(x, y, stuff, y_bottom):
    for next_pos in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
        if next_pos not in stuff and y + 1 < y_bottom:
            return False, next_pos
    return True, (x, y)


def run(rocks):
    rock_count = len(rocks)
    y_max = max(y for _, y in rocks)
    units = []
    while True:
        units.append((500, 0))
        for i in reversed(range(len(units))):
            pos = units[i]
            blocked, next_pos = get_next_pos(*pos, rocks, y_max + 2)
            if blocked:
                rocks.add(next_pos)
                _ = units.pop(i)
                if next_pos == (500, 0):
                    return len(rocks) - rock_count
            else:
                units[i] = next_pos
                # if next_pos[1] >= y_max:
                #     return len(rocks) - rock_count


rock_segments = [_parse(line) for line in open(sys.argv[1]).read().splitlines()]
rocks = {r for segment in rock_segments for r in _get_rocks(segment)}
print(run(rocks))
