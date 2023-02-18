# AoC 2022 day 11
import math
import sys


class Monkey:
    def __init__(self, monkey_id, items, operation, divisor, a, b):
        self.id = monkey_id
        self.items = items
        self.op = operation
        self.divisor = divisor
        self.a = a
        self.b = b
        self.inspected = 0

    def apply_operation(self, val):
        a1, op, a2 = self.op
        x1 = val if a1 == "old" else int(a1)
        x2 = val if a2 == "old" else int(a2)
        if op == "+":
            return x1 + x2
        elif op == "*":
            return x1 * x2
        else:
            raise ValueError

    def next(self, mod):
        if not self.items:
            return []
        self.inspected += 1

        item = self.items[0]
        self.items = self.items[1:]

        worry = self.apply_operation(item)
        next_monkey = self.a if worry % self.divisor == 0 else self.b

        return [worry % mod, next_monkey]

    @staticmethod
    def from_string(monkey_str: str):
        lines = monkey_str.split("\n")

        monkey_id = int(lines[0].split()[1][:-1])
        items = [int(w) for w in lines[1].split(": ")[1].split(", ")]
        a1, op, a2 = lines[2].split(" = ")[1].split()
        divisor = int(lines[3].split()[-1])
        a = int(lines[4].split()[-1])
        b = int(lines[5].split()[-1])

        return Monkey(monkey_id, items, (a1, op, a2), divisor, a, b)


with open(sys.argv[1]) as f:
    monkeys = [Monkey.from_string(s) for s in f.read().split("\n\n")]

mod = math.prod(m.divisor for m in monkeys)
N = 10000
for _ in range(N):
    for monkey in monkeys:
        while True:
            res = monkey.next(mod)
            if res == []:
                break
            monkeys[res[1]].items.append(res[0])

# part 1, 2
xs = sorted([m.inspected for m in monkeys])
print(xs[-1] * xs[-2])
print([m.inspected for m in monkeys])
