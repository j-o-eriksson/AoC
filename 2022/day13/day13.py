# AoC 2022 day 13
import functools
import sys


def read_element(chunk):
    stop = next(i for i, c in enumerate(chunk) if c in {"]", ","})
    return stop, int(chunk[:stop])


def read_list(chunk):
    l = []
    i = 0
    while i < len(chunk):
        c = chunk[i]

        if c == "]":
            break
        elif c == "[":
            n, sub = read_list(chunk[i + 1 :])
            l.append(sub)
            i += n + 2
        elif c == ",":
            i += 1
        else:
            n, elem = read_element(chunk[i:])
            l.append(elem)
            i += n

    return i, l


def compare(p1, p2):
    def _comp(a, b):
        return (a > b) - (a < b)

    if isinstance(p1, int) and isinstance(p2, int):
        return _comp(p1, p2)

    p1 = p1 if isinstance(p1, list) else [p1]
    p2 = p2 if isinstance(p2, list) else [p2]
    for a, b in zip(p1, p2):
        subcomp = compare(a, b)

        if subcomp != 0:
            return subcomp

    return _comp(len(p1), len(p2))


lines = open(sys.argv[1]).read().split("\n\n")

# part 1
pairs = [[read_list(p[1:])[1] for p in s.split()] for s in lines]
print(sum(i + 1 for i, (p1, p2) in enumerate(pairs) if compare(p1, p2) == -1))

# part2
pairs += [[[[2]], [[6]]]]
packets = sorted([p for pair in pairs for p in pair], key=functools.cmp_to_key(compare))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
