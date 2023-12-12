import math
import re
import sys

ts, ds = open(sys.argv[1]).read().splitlines()
ts = [int(t) for t in re.findall(r"\d+", ts)]
ds = [int(d) for d in re.findall(r"\d+", ds)]

distss = [[i * (t - i) for i in range(t)] for t in ts]
print(math.prod(sum(1 for dist in dists if dist > d) for d, dists in zip(ds, distss)))

t = int("".join(str(t) for t in ts))
d = int("".join(str(d) for d in ds))
dists = [i * (t - i) for i in range(t)]
print(sum(1 for dist in dists if dist > d))
