import sys
from collections import Counter

NORTH = [(-1, -1), (-1, 0), (-1, 1)]
SOUTH = [(1, -1), (1, 0), (1, 1)]
WEST = [(-1, -1), (0, -1), (1, -1)]
EAST = [(-1, 1), (0, 1), (1, 1)]
FULL = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def scan(elves, r, c, scan_order):
    if not any((r + dr, c + dc) in elves for dr, dc in FULL):
        return None

    for direction in scan_order:
        if not any((r + dr, c + dc) in elves for dr, dc in direction):
            return r + direction[1][0], c + direction[1][1]

    return None


def visualize(elves):
    print("--------------")
    rs = [r for r, _ in elves]
    cs = [c for _, c in elves]
    min_r, max_r = min(rs) - 2, max(rs) + 3
    min_c, max_c = min(cs) - 2, max(cs) + 3

    for r in range(max_r - min_r):
        print(
            "".join(
                [
                    "#" if (r + min_r, c + min_c) in elves else "."
                    for c in range(max_c - min_c)
                ]
            )
        )



ls = [list(line.strip()) for line in open(sys.argv[1]).readlines()]
elves = {(r, c) for r, row in enumerate(ls) for c, val in enumerate(row) if val == "#"}


# simulate
order = [NORTH, SOUTH, WEST, EAST]
i = 0
while True:
    moved = False
    # first half
    propositions = []
    for elf in elves:
        proposition = scan(elves, *elf, order)
        if proposition is not None:
            propositions.append((elf, proposition))

    # second half
    counts = Counter([p for _, p in propositions])
    for elf, proposition in propositions:
        if counts[proposition] == 1:
            elves.remove(elf)
            elves.add(proposition)
            moved = True

    order = order[1:] + order[:1]
    i += 1

    if not moved:
        break


xs = [c for _, c in elves]
ys = [r for r, _ in elves]

visualize(elves)
print((max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves))
print(i)



