# AoC 2022 day 10

with open("input.txt") as f:
    lines = f.read().splitlines()

val = 1
cycle = 1
ss = {}

n = 40
m = 6
screen = ["."] * n * m


def _update(screen, cycle, val):
    hor_pos = (cycle - 1) % n
    if val - 1 <= hor_pos <= val + 1:
        screen[cycle - 1] = "#"
    print(f"during cycle {cycle}: pixel at position {hor_pos}: {screen[cycle - 1]}")


for line in lines:
    if line == "noop":
        _update(screen, cycle, val)
        ss[cycle] = cycle * val
        cycle += 1
    else:
        print(f"start cycle {cycle}: begin executing {line}")
        for _ in range(2):
            _update(screen, cycle, val)
            ss[cycle] = cycle * val
            cycle += 1

        val += int(line.split()[1])
        print(f"finish executing {line} (Register X is now {val})")

# part 1
print(sum(ss[c] for c in [20, 60, 100, 140, 180, 220]))

# part 2
print("\n".join(["".join(screen[n * i : n * i + n]) for i in range(m)]))
