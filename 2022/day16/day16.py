import time
import sys
import itertools

import scipy.sparse as ss
import numpy as np


def _parse(line):
    _, a, _, _, b, _, _, _, _, *cs = line.split()
    return a, (int(b[5:-1]), {c.strip(",") for c in cs})


def get_pairwise_distances(valves):
    V = sorted(valves.keys())
    n = len(V)

    g = np.zeros((n, n))
    for i, v in enumerate(V):
        _, U = valves[v]
        for u in U:
            g[i, V.index(u)] = 1

    # find shortest pairwise distances
    g = ss.csr_matrix(g)
    d = ss.csgraph.floyd_warshall(g, directed=False, unweighted=True)

    return {V[i]: {V[j]: int(d[i][j]) for j in range(n)} for i in range(n)}


valves_full = dict(_parse(line) for line in open(sys.argv[1]).readlines())
valves = {k: v for k, v in valves_full.items() if k == "AA" or v[0] > 0}
distances = get_pairwise_distances(valves_full)


def upper_bound(n, node, explored):
    return sum(
        max((n - distances[node][next_node] - 1) * f, 0)
        for next_node, (f, _) in valves.items()
        if next_node not in explored
    )


def maximum_flow_bounded(t0, node, flow, max_flow, explored):
    remaining = [v for v in valves if v not in explored]
    for next_node in remaining:
        t1 = t0 - distances[node][next_node] - 1
        if t1 < 1:
            continue

        f_n = flow + valves[next_node][0] * t1
        e_n = {*explored, next_node}

        if f_n + upper_bound(t1, next_node, e_n) > max_flow:
            f = maximum_flow_bounded(t1, next_node, f_n, max_flow, e_n)
            max_flow = max(f, max_flow)

    return max(max_flow, flow)


def maximum_flow_bounded2(t00, t01, node1, node2, flow, max_flow, explored):
    if t00 < 1 and t01 < 1:
        return max_flow

    remaining = [v for v in valves if v not in explored]
    for next1, next2 in itertools.permutations(remaining, 2):
        t10 = max(t00 - distances[node1][next1] - 1, 0)
        t11 = max(t01 - distances[node2][next2] - 1, 0)

        f_n = flow + valves[next1][0] * t10 + valves[next2][0] * t11
        e_n = {*explored, next1, next2}

        bound = max(upper_bound(t10, next1, e_n), upper_bound(t11, next2, e_n))
        if f_n + bound > max_flow:
            f = maximum_flow_bounded2(t10, t11, next1, next2, f_n, max_flow, e_n)
            max_flow = max(f, max_flow)

    return max(max_flow, flow)


# part 1
t0 = time.perf_counter_ns()
print(maximum_flow_bounded(30, "AA", 0, 0, {"AA"}))
t1 = time.perf_counter_ns()
print(f"elapsed: {(t1 - t0) / 1e6:0.2f}ms")

# part 2
t0 = time.perf_counter_ns()
print(maximum_flow_bounded2(26, 26, "AA", "AA", 0, 0, {"AA"}))
t1 = time.perf_counter_ns()
print(f"elapsed: {(t1 - t0) / 1e6:0.2f}ms")
