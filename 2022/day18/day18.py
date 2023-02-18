# AoC 2022 day 18
import sys

cubes = {tuple(int(x) for x in l.split(",")) for l in open(sys.argv[1]).readlines()}
sides = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

# part 1
count = sum(
    sum((x + dx, y + dy, z + dz) not in cubes for dx, dy, dz in sides)
    for x, y, z in cubes
)
print(count)
