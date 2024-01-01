# AoC 2023 day 19
import sys


def parse(lines: str):
    rules, orders = lines.split("\n\n")

    rs = {}
    for rule in rules.splitlines():
        i = rule.find("{")  # }
        rs[rule[:i]] = rule[i + 1 : -1].split(",")

    os = [dict(v.split("=") for v in o[1:-1].split(",")) for o in orders.splitlines()]

    return rs, os


def process(rule, order, rules):
    for r in rule[:-1]:
        a, b = r.split(":")
        if _check(a, order):
            return _eval(b, order, rules)
    return _eval(rule[-1], order, rules)


def _eval(s, order, rules):
    if s == "A":
        return True
    elif s == "R":
        return False
    else:
        return process(rules[s], order, rules)


def _check(c, order):
    m = {"<": lambda a, b: int(a) < int(b), ">": lambda a, b: int(a) > int(b)}
    return m[c[1]](order[c[0]], c[2:])


rules, orders = parse(open(sys.argv[1]).read())
total = 0
for order in orders:
    if process(rules["in"], order, rules):
        total += sum(int(x) for x in order.values())
print(total)
