# AoC 2022 day 12
import sys


class Climber:
    def __init__(self, lines):
        self.neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.grid = {
            (r, c): (h, 1000) for r, row in enumerate(lines) for c, h in enumerate(row)
        }

        start = next(k for k, (h, _) in self.grid.items() if h == "S")
        self.end = next(k for k, (h, _) in self.grid.items() if h == "E")

        self.grid[start] = ("a", 10000)
        self.grid[self.end] = ("z", 10000)

        self.unvisited = {}
        self.starting_positions = [k for k, (h, _) in self.grid.items() if h == "a"]

    def can_step(self, curr_pos, next_pos):
        if next_pos in self.visited or next_pos not in self.grid:
            return False

        curr_height, _ = self.grid[curr_pos]
        next_height, _ = self.grid[next_pos]
        return ord(next_height) <= ord(curr_height) + 1

    def _probe_neighborhood(self, loc):
        r, c = loc
        steps = [(r + dr, c + dc) for dr, dc in self.neighbors]
        new_locs = [
            (step, self.grid[step]) for step in steps if self.can_step(loc, step)
        ]

        _, count = self.grid[loc]
        for new_loc, (height, new_count) in new_locs:
            c = min(count + 1, new_count) if new_loc in self.unvisited else count + 1
            self.unvisited[new_loc] = (height, c)

    def run(self, start):
        self.grid[start] = ("a", 0)
        self.visited = {start}
        self._probe_neighborhood(start)

        while True:
            new_loc, (h, step_count) = min(
                self.unvisited.items(), key=lambda x: x[1][1]
            )
            del self.unvisited[new_loc]
            self.grid[new_loc] = (h, step_count)

            self.visited.add(new_loc)
            self._probe_neighborhood(new_loc)

            if new_loc == self.end:
                return step_count


lines = open(sys.argv[1]).read().strip().split("\n")
climber = Climber(lines)
print(min(climber.run(start) for start in climber.starting_positions))
