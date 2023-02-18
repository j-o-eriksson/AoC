# AoC 2022 day 16
import sys


def _parse(line):
    _, a, _, _, b, _, _, _, _, *cs = line.split()
    return a, (int(b[5:-1]), {c.strip(",") for c in cs})


def hash_valve_pair(a, b):
    return "".join(sorted([a, b]))


def find_shortest_paths(valve, valves):
    visited = {valve}
    distances = {}
    _, neighbors = valves[valve]
    for distance in range(1, 100):
        next_neighbors = []

        for neighbor in neighbors:
            visited.add(neighbor)
            _, n2s = valves[neighbor]
            next_neighbors.extend([nbr for nbr in n2s if nbr not in visited])
            distances[hash_valve_pair(valve, neighbor)] = distance

        neighbors = set(next_neighbors)
        if neighbors == {}:
            break

    return distances


def maximum_flow_naive(node, n, valves, visited):
    if n <= 1:
        return 0

    flow, neighbors = valves[node]
    f1 = max(maximum_flow_naive(nb, n - 1, valves, visited) for nb in neighbors)

    if node in visited:
        return f1

    f2 = flow * (n - 1) + max(
        maximum_flow_naive(nb, n - 2, valves, {*visited, node}) for nb in neighbors
    )

    return max(f1, f2)


def maximum_flow2(valve, n, visited, valves, distances):
    if n <= 1:
        return 0

    next_valves = [(v, f) for v, (f, _) in valves.items() if v not in visited]
    ds = [n - 1 - distances[hash_valve_pair(valve, v)] for v, _ in next_valves]

    flows = [
        f * m + maximum_flow2(v, m, {v, *visited}, valves, distances)
        for (v, f), m in zip(next_valves, ds)
    ]

    return max(flows + [0])


def maximum_flow3(v1, v2, n, visted, valves):
    return 0


valves = dict(_parse(line) for line in open(sys.argv[1]).readlines())
shortest_paths = {
    k: v for valve in valves for k, v in find_shortest_paths(valve, valves).items()
}

visited = {valve for valve, (flow, _) in valves.items() if flow == 0}
print(maximum_flow2("AA", 5, visited, valves, shortest_paths))


# import json
#
# count = 0
# with open("d.json") as f:
#     d = json.load(f)
#     for k, v in d.items():
#         if k not in shortest_paths:
#             break
#         if shortest_paths[k] != v:
#             count += 1
#             print(f"-------\n{k}: {v}, {shortest_paths[k]}")
# print(count / len(shortest_paths))
#
# with open("d.json", "w") as f:
#     json.dump(shortest_paths, f)
