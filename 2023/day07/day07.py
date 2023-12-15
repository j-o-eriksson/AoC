import sys
from typing import Counter

fs = {
    "five": lambda h: len(set(h)) == 1,
    "four": lambda h: {b for _, b in Counter(h).most_common()} == {4, 1},
    "house": lambda h: {b for _, b in Counter(h).most_common()} == {3, 2},
    "three": lambda h: Counter(h).most_common()[0][1] == 3,
    "twopair": lambda h: {b for _, b in Counter(h).most_common(2)} == {2, 2},
    "pair": lambda h: {b for _, b in Counter(h).most_common(2)} == {2, 1},
    "high": lambda _: True,
}


def test(hand):
    ss = ["five", "four", "house", "three", "twopair", "pair", "high"]
    return next(-i for i, s in enumerate(ss) if fs[s](hand))


hands = [
    (h, int(bet))
    for h, bet in (line.split() for line in open(sys.argv[1]).read().splitlines())
]

values = dict((str(i), i) for i in range(2, 10))
values |= {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

# part 1
ranks = [(test(hand),) + tuple(values[c] for c in hand) + (bet,) for hand, bet in hands]
print(sum(rank * h[-1] for rank, h in enumerate(sorted(ranks), 1)))


# part 2
def upgrade(hand: str):
    if "J" not in hand or hand == "JJJJJ":
        return hand

    c = Counter(hand)
    _ = c.pop("J")

    [(a, _)] = c.most_common(1)
    return hand.replace("J", a)


values["J"] = 1
ranks = [(test(upgrade(h)),) + tuple(values[c] for c in h) + (bet,) for h, bet in hands]
print(sum(rank * h[-1] for rank, h in enumerate(sorted(ranks), 1)))
