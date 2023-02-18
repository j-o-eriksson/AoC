# AoC 2022 day 17
import sys

s1 = [(0, 0), (1, 0), (2, 0), (3, 0)]
s2 = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
s3 = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
s4 = [(0, 0), (0, 1), (0, 2), (0, 3)]
s5 = [(0, 0), (1, 0), (0, 1), (1, 1)]
shapes = [s1, s2, s3, s4, s5]


WIDTH = 7
move_map = {"<": -1, ">": 1}
moves = [move_map[c] for c in open(sys.argv[1]).read().strip()]


def move(shape, dx, dy):
    return [(x + dx, y + dy) for x, y in shape]


def possible(shape, stuff):
    if any(p in stuff for p in shape):
        return False

    xs = [x for x, _ in shape]
    if min(xs) < 0 or max(xs) >= WIDTH:
        return False

    if min(y for _, y in shape) < 0:
        return False

    return True


def visualize(stuff, top):
    for y in reversed(range(top)):
        s = "".join(["#" if (x, y) in stuff else "." for x in range(WIDTH)])
        print(f"|{s}|")
    print("+-------+")


def simulate(n):
    stuff = set()  # type: ignore
    top = 3
    j = 0
    shape = move(shapes[j], dx=2, dy=3)
    i = 0
    while j < n:
        dx = moves[i % len(moves)]
        i += 1

        shapex = move(shape, dx=dx, dy=0)
        if possible(shapex, stuff):
            shape = shapex

        shapey = move(shape, dx=0, dy=-1)
        if possible(shapey, stuff):
            shape = shapey
        else:
            for p in shape:
                stuff.add(p)
            top = max(top, 4 + max(y for _, y in shape))

            j += 1
            shape = move(shapes[j % len(shapes)], dx=2, dy=top)

    visualize(stuff, top)
    return top - 3


# part 1
print(simulate(2022))

# part 2
# find i % len(moves) == 0 and surface-shape combo already seen
