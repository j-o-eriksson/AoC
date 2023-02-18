# AoC 2022 day 20
import sys


def mix(vals, n):
    indices = list(range(n))
    for i in range(n):
        i0 = indices.index(i)
        indices.pop(i0)

        j = (i0 + vals[i]) % (n - 1)
        indices.insert(j, i)

    return [vals[i] for i in indices]


vals = [int(line.strip()) for line in open(sys.argv[1]).readlines()]
n = len(vals)
vals = mix(vals, n)

i0 = vals.index(0)
print([vals[(i0 + 1000 * k) % n] for k in (1, 2, 3)])
