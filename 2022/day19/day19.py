# AoC 2022 day 19
import copy
import math
import sys
from typing import Dict
from dataclasses import dataclass


def parse(s):
    b, cs = s.split(": ")
    _, blueprint_id = b.split()

    costs = {}
    resource_list = []
    for recipe in cs.split(".")[:-1]:
        _, robot_type, _, _, quantity, resource_type, *snd = recipe.split()
        resource_list = {resource_type: int(quantity)}
        if snd:
            resource_list[snd[2]] = int(snd[1])
        costs[robot_type] = resource_list
    return costs


def _pay_resources(resources, price):
    return {k: resources[k] - price.get(k, 0) for k in resources}


def _purchase_delay(price, resources, production):
    if all(resources[k] >= v for k, v in price.items()):
        return 0

    if any(resources[k] < v and production[k] == 0 for k, v in price.items()):
        return math.inf

    return max(math.ceil((v - resources[k]) / production[k]) for k, v in price.items())


@dataclass
class State:
    t: int
    production: Dict[str, int]
    resources: Dict[str, int]


def advance_state(state, purchase, dt, blueprint):
    next_state = copy.deepcopy(state)

    # step
    next_state.t -= dt

    # produce
    for r, p in next_state.production.items():
        next_state.resources[r] += p * dt

    # purchase
    next_state.resources = _pay_resources(next_state.resources, blueprint[purchase])
    next_state.production[purchase] += 1

    return next_state


def upper_bound(state, query):
    return (
        sum(state.t - i for i in range(1, state.t))
        + state.resources[query]
        + state.production[query] * state.t
    )


class DepthFirst:
    def __init__(self, query, blueprint):
        self.best = 0
        self.query = query
        self.blueprint = blueprint
        self.maxes = {
            r: max([v.get(r, 0) for v in blueprint.values()]) for r in blueprint
        }
        self.maxes[query] = math.inf

    def branch_and_bound(self, state):
        if state.t <= 0:
            correction = state.t * state.production[self.query]
            self.best = max(self.best, state.resources[self.query] + correction)
            return

        next_purchases = [
            (r, _purchase_delay(p, state.resources, state.production) + 1)
            for r, p in self.blueprint.items()
        ]
        branches = filter(
            lambda p: p[1] != math.inf and state.production[p[0]] < self.maxes[p[0]],
            next_purchases,
        )

        for robot, delay in branches:
            branch = advance_state(state, robot, delay, self.blueprint)

            if upper_bound(branch, self.query) > self.best:
                self.branch_and_bound(branch)


if __name__ == "__main__":
    blueprints = [parse(line) for line in open(sys.argv[1]).readlines()]

    production = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}

    # part 1
    q1 = 0
    start1 = State(24, production, resources)
    for i, blueprint in enumerate(blueprints):
        explorer = DepthFirst("geode", blueprint)
        explorer.branch_and_bound(start1)
        q1 += (i + 1) * explorer.best
    print(f"part 1: {q1}")

    # part 2
    q2 = 1
    start1 = State(32, production, resources)
    for blueprint in blueprints[:3]:
        explorer = DepthFirst("geode", blueprint)
        explorer.branch_and_bound(start1)
        q2 *= explorer.best
    print(f"part 2: {q2}")
