import utils


def parse(s: str):
    out = []
    b = False
    i = 0
    for x in s:
        for _ in range(int(x)):
            out.append("." if b else str(i))
        if not b:
            i += 1
        b = not b
    return out


def part1(data):
    free = list(reversed([i for i, x in enumerate(data) if x == "."]))
    busy = [i for i, x in enumerate(data) if x != "."]

    for _ in range(len(free)):
        i = free.pop()
        j = busy.pop()
        if i > j:
            break

        data[i] = data[j]
        data[j] = "."

    return sum(i * int(x) for i, x in enumerate(data) if x != ".")


def get_chunks(data):
    def get_chunk(d, c):
        size = 0
        for x in d:
            if x != c:
                return size
            size += 1
        return size

    free = []
    i = 0
    while i < len(data):
        c = data[i]
        size = get_chunk(data[i:], c)
        free.append((i, c, size))
        i += size
    return free


def part2(data):
    chunks = get_chunks(data)
    free = [c for c in chunks if c[1] == "."]
    files = [c for c in chunks if c[1] != "."]

    for _ in range(len(files)):
        j, _, fsize = files.pop()
        fi = next((i for i, f in enumerate(free) if f[2] >= fsize and f[0] < j), None)
        if fi is not None:
            i, _, asize = free[fi]
            data[i : i + fsize] = data[j : j + fsize]
            data[j : j + fsize] = ["."] * fsize
            free[fi] = (i + fsize, ".", asize - fsize)

    return sum(i * int(x) for i, x in enumerate(data) if x != ".")


data = parse(utils.load_file().strip())
print(part1(data.copy()))
print(part2(data.copy()))
