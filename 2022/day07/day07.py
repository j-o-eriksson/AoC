# AoC 2022 day 7
from collections import defaultdict
from pathlib import Path

with open("input.txt") as f:
    lines = f.read().splitlines()


def _change_directory(old_path, new_path):
    if new_path == "/":
        return Path("/")
    elif new_path == "..":
        return old_path.parent
    else:
        return old_path / new_path


class Filesystem:
    def __init__(self, lines):
        self.curr_path = Path("/")
        self.directories = defaultdict(list)
        self.lines = lines
        self.line_idx = 0

    def _apply_command(self, tokens):
        if tokens[1] == "cd":
            self.curr_path = _change_directory(self.curr_path, tokens[2])
            return self.line_idx + 1
        elif tokens[1] == "ls":
            tail = self.lines[self.line_idx + 1 :]
            for i, line in enumerate(tail):
                if line[0] == "$":
                    break
                self.directories[str(self.curr_path)].append(line.split())
            return self.line_idx + i + 1
        else:
            print(f"error: {tokens}")
            return self.line_idx + 1

    def run(self):
        while self.line_idx < len(self.lines):
            tokens = self.lines[self.line_idx].split()
            self.line_idx = self._apply_command(tokens)

        sizes = [self._compute_size(p) for p in self.directories.keys()]

        # part 1
        print(sum(s for s in sizes if s <= 100000))

        # part 2
        delta = self._compute_size("/") - 40000000
        print(min(s for s in sizes if s >= delta))

    def _compute_size(self, path):
        s1 = sum(int(sz) for sz, _ in self.directories[path] if sz.isnumeric())
        s2 = sum(
            self._compute_size(str(Path(path) / p))
            for a, p in self.directories[path]
            if a == "dir"
        )
        return s1 + s2


filesystem = Filesystem(lines)
filesystem.run()
