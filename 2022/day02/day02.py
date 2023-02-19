# AoC 2022 day 2
import itertools
from collections import defaultdict

m1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}
m2 = [0, 3, 6]
o1 = ["A", "B", "C"]
o2 = ["X", "Y", "Z"]
m = {
    f"{o1[i]}{o2[(i + j - 1) % 3]}": m2[j]
    for i, j in itertools.product(range(3), range(3))
}


with open("input.txt") as f:
    s = f.read()

stuff = [line.replace(" ", "") for line in s.split("\n") if line]
print(sum(m1[s[1]] + m[s] for s in stuff))

# part 2
p2s = defaultdict(list)

map_letter = {"X": "A", "Y": "B", "Z": "C"}
for k, v in m.items():
    p2s[v].append(k[0] + map_letter[k[1]])

move_to_score = {"A": 1, "B": 2, "C": 3}
outcome_to_score = {"X": 0, "Y": 3, "Z": 6}

score = 0
for line in stuff:
    opponent, outcome = tuple(line)
    outcome_score = outcome_to_score[outcome]
    [move] = [ss[1] for ss in p2s[outcome_score] if ss[0] == opponent]
    score += outcome_score + move_to_score[move]
print(score)
