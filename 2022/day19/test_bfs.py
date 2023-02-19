from day19 import DepthFirst, State


def test_dfs():
    blueprint = {
        "ore": {"ore": 4},
        "clay": {"ore": 2},
        "obsidian": {"ore": 3, "clay": 14},
        "geode": {"ore": 2, "obsidian": 7},
    }
    production = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
    resources = {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}
    start = State(16, production, resources)

    dfs = DepthFirst("obsidian", blueprint)
    dfs.branch_and_bound(start)

    assert dfs.best == 6
