# AoC 2023 day 2
import math
import sys


def _parse(line: str):
    a, bag = line.split(": ")

    def _p(item):
        count, color = item.split()
        return color, int(count)

    return int(a.split()[1]), [
        dict(_p(item) for item in cubeset.split(", ")) for cubeset in bag.split("; ")
    ]


lines = [_parse(l) for l in open(sys.argv[1]).read().splitlines()]
cubes = {"red": 12, "green": 13, "blue": 14}


# part 1
def _valid1(game):
    return all(all(cubes[k] >= v for k, v in cubeset.items()) for cubeset in game)


print(sum(game_id for game_id, game in lines if _valid1(game)))


# part 2
def _power(game):
    return math.prod(max(cubeset.get(color, 0) for cubeset in game) for color in cubes)


print(sum(_power(game) for _, game in lines))
