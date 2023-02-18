# AoC 2022 day 8
import itertools

import numpy as np

with open("input.txt") as f:
    lines = f.read().splitlines()

grid = np.array([[int(x) for x in line] for line in lines])
n, m = grid.shape


# part 1
def is_visible(r, c):
    val = grid[r, c]

    # left
    if val > grid[r, :c].max():
        return True
    # right
    if val > grid[r, c + 1 :].max():
        return True
    # up
    if val > grid[:r, c].max():
        return True
    # down
    if val > grid[r + 1 :, c].max():
        return True

    return False


def _argmax(a):
    if np.all(np.invert(a)):
        return len(a)
    return np.argmax(a) + 1


def scenic_score(r, c):
    val = grid[r, c]

    ld = _argmax(val <= np.flip(grid[r, :c]))
    rd = _argmax(val <= grid[r, c + 1 :])
    ud = _argmax(val <= np.flip(grid[:r, c]))
    dd = _argmax(val <= grid[r + 1 :, c])

    return ld * rd * ud * dd


rn = range(1, n - 1)
rm = range(1, m - 1)

# part 1
count = sum(is_visible(r, c) for r, c in itertools.product(rn, rm))
print(count + 2 * (n + m) - 4)


# part 2
print(max(scenic_score(r, c) for r, c in itertools.product(rn, rm)))
