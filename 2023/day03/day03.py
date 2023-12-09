# AoC 2023 day 3
import re
import math
import sys


def _parse(lines):
    digits = {}
    for r, line in enumerate(lines):
        for m in re.finditer(r"\d+", line):
            c = m.span()[0]
            digits[(r, c)] = m.group()

    symbols = {
        (r, c)
        for r, line in enumerate(lines)
        for c, x in enumerate(line)
        if x != "." and not x.isdigit()
    }
    return digits, symbols


def adjacent(num, r, c, symbols):
    ns = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    for dcc in range(len(num)):
        if any((r + dr, c + dc + dcc) in symbols for dr, dc in ns):
            return True
    return False


lines = open(sys.argv[1]).read().splitlines()
digits, symbols = _parse(lines)

# part 1
print(sum(int(d) for (r, c), d in digits.items() if adjacent(d, r, c, symbols)))


# part 2
def adj(gear, digit):
    gr, gc = gear
    r, c, val = digit
    return any((r - gr) ** 2 + (c + dcc - gc) ** 2 <= 2 for dcc in range(len(val)))


gears = {(r, c) for r, line in enumerate(lines) for c, x in enumerate(line) if x == "*"}

count = 0
for gear in gears:
    n = [int(d) for (r, c), d in digits.items() if adj(gear, (r, c, d))]
    if len(n) == 2:
        count += math.prod(n)
print(count)
