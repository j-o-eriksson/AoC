# AoC 2022 day 6
with open("input.txt") as f:
    input_string = f.read()

# n = 4 - 1
n = 14 - 1

for i in range(n + 1, len(input_string)):
    curr = input_string[i]
    prev = set(input_string[i - n : i])
    if curr not in prev and len(prev) == n:
        print(i)
        break
