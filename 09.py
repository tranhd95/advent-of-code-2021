from collections import defaultdict
from math import prod

from utils import iter_lines, rinput


def parse(inp):
    dct = defaultdict(lambda: 10)
    for y, row in enumerate(iter_lines(inp)):
        for x, val in enumerate(row):
            dct[(x, y)] = int(val)
    return dct


def neighbourhood(hmap, coords):
    x, y = coords
    yield (x, y - 1), hmap[(x, y - 1)]
    yield (x, y + 1), hmap[(x, y + 1)]
    yield (x - 1, y), hmap[(x - 1, y)]
    yield (x + 1, y), hmap[(x + 1, y)]


def get_low_points(hmap):
    for coords, cell_height in hmap.copy().items():
        if all(cell_height < neighbour for _, neighbour in neighbourhood(hmap, coords)):
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
        for ncoords, nval in neighbourhood(hmap, (x, y)):
            if nval < 9 and ncoords not in basin:
                q.append(ncoords)
                basin.add(ncoords)
    return len(basin)


solve1(rinput(9))
solve2(rinput(9))
