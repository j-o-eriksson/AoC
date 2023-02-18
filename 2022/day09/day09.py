# AoC 2022 day 9
import numpy as np

with open("input.txt") as f:
    lines = f.read().splitlines()

moves = {"L": [-1, 0], "R": [1, 0], "U": [0, -1], "D": [0, 1]}


def _next_tail(head, prev_tail):
    delta = head - prev_tail

    if any(np.abs(delta) > 1):
        return prev_tail + np.clip(delta, -1, 1)

    return prev_tail


N = 10
rope = [np.array([0, 0]) for _ in range(N)]
visited = {"x".join(str(p) for p in rope[-1])}

for line in lines:
    move, n = line.split()

    for _ in range(int(n)):
        rope[0] += moves[move]
        for i in range(1, N):
            rope[i] = _next_tail(rope[i - 1], rope[i])

        visited.add("x".join(str(p) for p in rope[-1]))

print(len(visited))

# grid = [["." for _ in range(40)] for _ in range(40)]
# for s in visited:
#     x, y = s.split("x")
#     grid[20 + int(y)][20 + int(x)] = "#"
