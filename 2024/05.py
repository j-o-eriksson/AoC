import sys
from collections import defaultdict
from functools import cmp_to_key
from pathlib import Path


def parse(s: str):
    a, b = s.split("\n\n")

    rules = defaultdict(list)
    for r in a.splitlines():
        c1, c2 = r.split("|")
        rules[int(c1)].append(int(c2))

    updates = [[int(x) for x in l.split(",")] for l in b.splitlines()]

    return rules, updates


def is_valid(update, rules):
    return reorder(update, rules) == update


def reorder(update, rules):
    cmp = lambda a, b: -1 if b in rules[a] else 1
    return sorted(update, key=cmp_to_key(cmp))


rules, updates = parse(Path(sys.argv[1]).read_text())
valid = [u for u in updates if is_valid(u, rules)]
print(sum(u[len(u) // 2] for u in valid))

invalid = [reorder(u, rules) for u in updates if not is_valid(u, rules)]
print(sum(u[len(u) // 2] for u in invalid))
