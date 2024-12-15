import sys
from pathlib import Path


def parse(s: str):
    ls = s.splitlines()
    return [[int(x) for x in l.split()] for l in ls]


def is_safe(ns) -> bool:
    ds = [a - b for a, b in zip(ns, ns[1:])]

    if not (all(d < 0 for d in ds) or all(d > 0 for d in ds)):
        return False

    return all(0 < abs(d) <= 3 for d in ds)


data = parse(Path(sys.argv[1]).read_text())
print(sum(is_safe(ns) for ns in data))
