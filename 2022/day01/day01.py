# AoC 2022 day 1
with open("input.txt") as f:
    s = f.read()

d = [[int(e) for e in elf.split("\n") if len(e) > 0] for elf in s.split("\n\n")]

# part 1
ds = sorted([-sum(e) for e in d])
print(-ds[0])

# part 2
print(-sum(ds[:3]))

