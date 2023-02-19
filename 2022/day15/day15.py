# AoC 2022 day 15
import re
import sys

import tqdm  # type: ignore


def _parse(line):
    sx, sy, bx, by = [int(x) for x in re.findall("-*[0-9]+", line)]
    dist = abs(sx - bx) + abs(sy - by)
    return (sx, sy), dist


def find_gaps(data, y):
    rs = []
    for (sx, sy), dist in data:
        dy = abs(sy - y)
        if dy <= dist:
            dx = dist - dy
            rs.append((sx - dx, sx + dx))

    rs = sorted(rs)
    rs = merge_lines(rs[0], rs[1:])

    if len(rs) > 1:
        print(4000000 * (rs[0][1] + 1) + y)
        print(f"gap: {rs} at y={y}")
    return rs


def merge_lines(line, lines):
    if lines == []:
        return [line]

    head, *tail = lines
    l1, r1 = line
    l2, r2 = head

    if r1 + 1 >= l2:
        return merge_lines((l1, max(r1, r2)), tail)

    return [line] + merge_lines(head, tail)


data = [_parse(line) for line in open(sys.argv[1]).read().splitlines()]

# part 1
[(xmin, xmax)] = find_gaps(data, 2000000)
print(xmax - xmin)


# part 2
for y in tqdm.tqdm(range(4000000)):
    find_gaps(data, y)
