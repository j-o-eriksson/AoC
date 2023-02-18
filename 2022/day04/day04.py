# AoC 2022 day 4
with open("input.txt") as f:
    input_string = f.read()


def _parse(line):
    a, b = line.split(",")
    return a.split("-"), b.split("-")


stuff = [_parse(line) for line in input_string.split()]

# part 1
def _contains(a, b):
    return int(a[0]) <= int(b[0]) and int(a[1]) >= int(b[1])


print(sum(_contains(a, b) or _contains(b, a) for a, b in stuff))

# part 2
def _no_overlap(a, b):
    return int(a[0]) > int(b[1]) or int(a[1]) < int(b[0])


print(len(stuff) - sum(_no_overlap(a, b) for a, b in stuff))
