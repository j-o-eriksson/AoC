# AoC 2022 day 3
with open("input.txt") as f:
    input_string = f.read()

stuff = [line for line in input_string.split()]

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
scores = {c: i + 1 for i, c in enumerate(letters)}


# part 1
def _split(line):
    n = len(line) // 2
    return line[:n], line[n:]


def _score_common(a, b):
    common = set(a).intersection(set(b))
    return scores[common.pop()]


print(sum(_score_common(*_split(line)) for line in stuff))


# part 2
def _score_group(a, b, c):
    common = set(a).intersection(set(b)).intersection(set(c))
    return scores[common.pop()]


print(sum(_score_group(*stuff[i : i + 3]) for i in range(0, len(stuff), 3)))
