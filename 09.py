from collections import defaultdict
from math import prod

from utils import iter_lines, rinput


def parse(inp):
    dct = defaultdict(lambda: 10)
    for y, row in enumerate(iter_lines(inp)):
        for x, val in enumerate(row):
            dct[(x, y)] = int(val)
    return dct


def neighbourhood(x, y):
    yield from ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))


def get_low_points(hmap):
    for coords, cell_height in hmap.copy().items():
        if all(cell_height < hmap[adj] for adj in neighbourhood(*coords)):
            yield coords, cell_height


def solve1(inp):
    print(sum(h + 1 for _, h in get_low_points(parse(inp))))


def solve2(inp):
    hmap = parse(inp)
    basins = sorted(flood(hmap, coords) for coords, _ in get_low_points(hmap))
    print(prod(basins[-3:]))


def flood(hmap, base):
    q = [base]
    basin = {base}
    while q:
        x, y = q.pop(0)
        for adj in neighbourhood(x, y):
            if hmap[adj] < 9 and adj not in basin:
                q.append(adj)
                basin.add(adj)
    return len(basin)


solve1(rinput(9))
solve2(rinput(9))
