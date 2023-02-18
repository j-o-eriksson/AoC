# AoC 2022 day 19
import copy
import math
import sys


ROBOTS = {"ore": 0, "clay": 1, "obsidian": 2, "geode": 3}


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


def can_purchase(price, resources):
    return all(resources[k] >= v for k, v in price.items())


def pay_resources(resources, price):
    return {k: resources[k] - price.get(k, 0) for k in resources}


def should_purchase(purchasable, price_list, resources_old, production):
    resources_new = pay_resources(resources_old, price_list[purchasable])

    d1 = {r: purchase_delay(price_list[r], resources_old, production) for r in ROBOTS}
    d2 = {r: purchase_delay(price_list[r], resources_new, production) for r in ROBOTS}

    prio = ROBOTS[purchasable]
    if any(d2[r] > d1[r] and rprio > prio for r, rprio in ROBOTS.items()):
        return False

    return True


# ore (obsidian) = ore + obsidian * ore_obsidian 


def purchase_delay(price, resources, production):
    if all(resources[k] >= v for k, v in price.items()):
        return 0

    if any(resources[k] < v and production[k] == 0 for k, v in price.items()):
        return 100000

    return max(math.ceil((v - resources[k]) / production[k]) for k, v in price.items())


blueprints = [parse(line) for line in open(sys.argv[1]).readlines()]


production = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
prices = blueprints[0]


N = 24
for i in range(N):
    print(f"== Minute {i + 1} ==")

    # buy if purchase doesn't delay higher-priority purchase
    produced = copy.deepcopy(production)
    purchasables = [r for r in ROBOTS.keys() if can_purchase(prices[r], resources)]
    if purchasables:
        print(f"can purchase {' and '.join(purchasables)}")
        for purchasable in reversed(purchasables):
            if should_purchase(purchasable, prices, resources, production):
                production[purchasable] += 1
                resources = pay_resources(resources, prices[purchasable])
                print(f"purchased {purchasable} robot")
                break

    for k, v in produced.items():
        resources[k] += v
        if v > 0:
            print(f"{v} {k} robots produce {v} {k}; you now have {resources[k]} {k}")
    print()


print(resources)


def next_purchase_naive(t, resources, production, prices):
    if t <= 1:
        return resources["geode"] + production["geode"] * t

    delays = {r: purchase_delay(prices[r], resources, production) for r in ROBOTS}

    oo = []
    for r, d in delays.items():
        if d < 100:
            r2 = copy.deepcopy(resources)
            for resource, prod in production.items():
                r2[resource] += prod * d

            p2 = copy.deepcopy(production)
            p2[r] += 1

            t1 = t - d - 1 if d == 0 else t - d
            oo.append(next_purchase_naive(t1, r2, p2, prices))

    return max(oo)


def _max_naive(t, resources, production, prices):
    s = "geode"
    if t <= 1:
        return resources[s] + production[s] * t

    r_no_purchase = copy.deepcopy(resources)
    p_no_purchase = copy.deepcopy(production)
    for k, v in production.items():
        r_no_purchase[k] += v

    oo = [_max_naive(t - 1, r_no_purchase, p_no_purchase, prices)]

    purchasables = [r for r in ROBOTS.keys() if can_purchase(prices[r], resources)]
    for r in purchasables:
        r2 = pay_resources(resources, prices[r])
        for k, v in production.items():
            r2[k] += v

        p2 = copy.deepcopy(production)
        p2[r] += 1

        oo.append(_max_naive(t - 1, r2, p2, prices))

    return max(oo)
