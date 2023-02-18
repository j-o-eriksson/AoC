# AoC 2022 day 23
import sys
from collections import defaultdict


neighbors = [(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)]
moves = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}


def visualize(blizzards, n, m):
    d = defaultdict(list)
    for k, v in blizzards:
        d[k].append(v)

    for r in range(n):
        s = []
        for c in range(m):
            v = d.get((r, c), ["."])
            if len(v) == 1:
                s.append(v[0])
            else:
                s.append(str(len(v)))
        print("".join(s))
    print()


def explore(pos, stuff):
    (r, c), t = pos
    candidate_positions = [(r + dr, c + dc) for dr, dc in neighbors]
    c2 = {(p, t + 1) for p in candidate_positions if p not in stuff}
    return c2


def find_shortest_path(t, start, stop, stuffs):
    pos = (start, t)
    Q = explore(pos, stuffs[1])

    while pos[0] != stop:
        pos = min(Q, key=lambda x: x[1])
        Q.remove(pos)
        Q = Q.union(explore(pos, stuffs[(pos[1] + 1) % q]))

    return pos


lines = [list(line.strip()) for line in open(sys.argv[1]).readlines()]
n = len(lines)
m = len(lines[0])

grid = {(r, c): v for r, line in enumerate(lines) for c, v in enumerate(line)}
blizzard_states = [[(k, v) for k, v in grid.items() if v in {"<", ">", "^", "v"}]]
q = (n - 2) * (m - 2)
for i in range(q):
    bstate = []
    for (r, c), v in blizzard_states[i]:
        dr, dc = moves[v]
        rr = 1 + (r + dr - 1) % (n - 2)
        cc = 1 + (c + dc - 1) % (m - 2)
        bstate.append(((rr, cc), v))
    blizzard_states.append(bstate)
print(f"Pre-generated {q} blizzard states.")

start = (0, 1)
stop = (n - 1, m - 2)

walls = {k for k, v in grid.items() if v == "#"}
walls.add((start[0] - 1, start[1]))  # block upper exit
walls.add((stop[0] + 1, stop[1]))  # block bottom exit

stuffs = [walls.union({pos for pos, _ in bstate}) for bstate in blizzard_states]

# part 1
_, t0 = find_shortest_path(0, start, stop, stuffs)
print(f"Part 1: {t0}")

# part 2
_, t1 = find_shortest_path(t0, stop, start, stuffs)
print(f"Part 2: {t1 - t0}")
_, t2 = find_shortest_path(t1, start, stop, stuffs)
print(f"Part 2: {t0} + {t1 - t0} + {t2 - t1} = {t2}")
