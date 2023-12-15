# AoC 2023 day 15
import sys


def hash_1(s: str):
    h = 0
    for c in s:
        h += ord(c)
        h *= 17
        h = h % 256
    return h


inp = open(sys.argv[1]).read().strip().split(",")
print(sum(hash_1(s) for s in inp))
