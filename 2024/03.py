import sys
from pathlib import Path

BIG = 1000000000000


def mul(s: str) -> int:
    ss = s.split(",")
    if len(ss) == 2 and ss[0].isnumeric() and ss[1].isnumeric():
        return int(ss[0]) * int(ss[1])
    return 0


def _x(s: str, token: str):
    i = s.find(token)
    return i if i != -1 else BIG


def nxt(s: str) -> list[tuple[int, str, int]]:
    tokens = ["mul(", ")", "do()", "don't()"]
    return [(_x(s, t), t, len(t)) for t in tokens]


def stupid(s: str, enable: bool):
    ts = nxt(s)
    i, t, n = min(ts)

    if t == ")":
        c = mul(s[:i]) if enable else 0
        return c, s[i + n :], enable

    for i, t, n in sorted(ts):
        if t == "do()":
            enable = True
        # elif t == "don't()":
        #     enable = False
        elif t == "mul(":
            return stupid(s[i + n :], enable)

    return 0, "", False


def parse2(s: str) -> int:
    start = _x(s, "mul(") + 4
    s = s[start:]
    enable = True

    count = 0
    while True:
        c, s, enable = stupid(s, enable)
        count += c

        if s == "":
            break

    return count


count = parse2(Path(sys.argv[1]).read_text())
print(count)
