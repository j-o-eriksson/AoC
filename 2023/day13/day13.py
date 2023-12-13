# AoC 2023 day 13
import sys


def parse(pattern: str):
    rows = [list(r) for r in pattern.splitlines()]
    cols = [[r[c] for r in rows] for c in range(len(rows[0]))]
    return rows, cols


def find_reflection_line(lines):
    candidates = [i for i in range(len(lines) - 1) if lines[i] == lines[i + 1]]
    return [c for c in candidates if is_valid(lines, c)]


def is_valid(lines, i):
    n = min(i + 1, len(lines) - i - 1)  # 01234 5678
    return all(lines[i - j] == lines[i + j + 1] for j in range(n))


patterns = [parse(p) for p in open(sys.argv[1]).read().split("\n\n")]

# part 1
count = 0
for rp, cp in patterns:
    a = find_reflection_line(rp)
    if a != []:
        count += 100 * (a[0] + 1)
    else:
        b = find_reflection_line(cp)
        count += b[0] + 1
print(count)
