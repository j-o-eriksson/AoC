# AoC 2022 day 21
import sys

d = dict(line.strip().split(": ") for line in open(sys.argv[1]).readlines())

fs = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def evaluate(key):
    expr = d[key]
    if expr.isnumeric():
        return float(expr)

    a, op, b = expr.split()

    f = fs[op]
    return f(evaluate(a), evaluate(b))


# part 1
r1 = evaluate("root")
print(r1)


# part 2
fsi1 = {"+": fs["-"], "-": fs["+"], "*": fs["/"], "/": fs["*"]}
fsi2 = {
    "+": fs["-"],
    "-": lambda a, b: b - a,  # a = b - x -> x = b - a
    "*": fs["/"],
    "/": lambda a, b: b / a,  # a = b / x -> x = b / a
}


def find(key, searchkey):
    if key == searchkey:
        return True

    expr = d[key]
    if expr.isnumeric():
        return False

    a, _, b = expr.split()
    return find(a, searchkey) or find(b, searchkey)


def evaluate2(key, lvalue):
    if key == "humn":
        return lvalue

    expr = d[key]

    a, op, b = expr.split()
    sbranch, ebranch, fsi = (a, b, fsi1) if find(a, "humn") else (b, a, fsi2)

    f = fsi[op]
    return evaluate2(sbranch, f(lvalue, evaluate(ebranch)))


a, _, b = d["root"].split()
sbranch, ebranch = (a, b) if find(a, "humn") else (b, a)
r2 = evaluate2(sbranch, evaluate(ebranch))
print(r2)


# validate
d["humn"] = str(int(r2))
assert evaluate(a) == evaluate(b)
