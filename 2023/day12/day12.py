# AoC 2023 day 12
import sys
from itertools import combinations


def parse(line: str):
    a, b = line.split()
    ls = list(map(int, b.split(",")))
    return a, ls


def valid(s, x):
    xs = [len(ss) for ss in s.split(".") if len(ss) > 0]
    return xs == x


def count1(s, x):
    n = [i for i, ch in enumerate(s) if ch == "?"]
    m = sum(x) - s.count("#")
    count = 0
    for y in combinations(n, m):
        d = [".", "#"]
        si = "".join(d[i in y] if ch == "?" else ch for i, ch in enumerate(s))
        if valid(si, x):
            count += 1
    return count


lines = open(sys.argv[1]).read().splitlines()
ls = [parse(l) for l in lines]

# part 1
print(sum(count1(*l) for l in ls))


count1("?###????????", [3, 2, 1])
