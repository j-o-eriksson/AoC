from pathlib import Path
from sys import argv


def parse(s: str):
    ls = s.splitlines()
    out = []
    for l in ls:
        a, b = l.split(": ")
        out.append((int(a), [int(x) for x in b.split()]))
    return out


def f(t: int, v: int, vs: list[int]) -> bool:
    if vs == []:
        return v == t

    x, *xs = vs
    return f(t, int(f"{v}{x}"), xs) or f(t, max(v, 1) * x, xs) or f(t, v + x, xs)


data = parse(Path(argv[1]).read_text())
print(sum(x for x, xs in data if f(x, 0, xs)))
