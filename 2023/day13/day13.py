# AoC 2023 day 13
import sys


def parse(pattern: str):
    rows = [list(r) for r in pattern.splitlines()]
    cols = [[r[c] for r in rows] for c in range(len(rows[0]))]
    return rows, cols


def find_reflection_line(lines):
    return [i for i in range(len(lines) - 1) if lines[i] == lines[i + 1]]


def is_valid(lines, i):
    n = len(lines)
    return all(lines[i - j] != lines[i + j + 1] for j in range(min(i, n - i)))


patterns = [parse(p) for p in open(sys.argv[1]).read().split("\n\n")]

# part 1
for rp, cp in patterns:
    print("row:", find_reflection_line(rp))
    print("col:", find_reflection_line(cp))
    print()
