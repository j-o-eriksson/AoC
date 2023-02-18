# AoC 2022 day 5

import copy

with open("input.txt") as f:
    input_string = f.read()


def _parse_crate_line(s):
    ii = [1 + i * 4 for i in range(9)]
    return {i + 1: s[idx] for i, idx in enumerate(ii) if s[idx] != " "}


def _parse_move(s):
    ss = s.split()
    return int(ss[1]), int(ss[3]), int(ss[5])


crate_str, move_str = input_string.split("\n\n")
crate_lines = [_parse_crate_line(line) for line in crate_str.split("\n") if line]
crates = {
    i: list(reversed([c[i] for c in crate_lines[:-1] if i in c])) for i in range(1, 10)
}
moves = [_parse_move(line) for line in move_str.split("\n") if line]


def run_simulation(cratess, moves, apply_func):
    crates = copy.deepcopy(cratess)
    for move in moves:
        apply_func(crates, move)

    print("".join([crates[i][-1] for i in range(1, 10)]))


# part 1
def _apply_move_1(crates, move):
    n, src, dst = move
    for i in range(n):
        crates[dst].append(crates[src].pop())


run_simulation(crates, moves, _apply_move_1)


# part 2
def _apply_move_2(crates, move):
    n, src, dst = move
    stack = crates[src][-n:]
    crates[src] = crates[src][:-n]
    crates[dst] = crates[dst] + stack


run_simulation(crates, moves, _apply_move_2)
