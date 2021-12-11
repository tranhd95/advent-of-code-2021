from itertools import product, count
from utils import rinput, iter_lines


def parse(inp):
    return {
        (x, y): int(v)
        for y, line in enumerate(iter_lines(inp))
        for x, v in enumerate(line)
    }


def neighbourhood(coords):
    x, y = coords
    for n in product(range(x - 1, x + 2), range(y - 1, y + 2)):
        if n != coords:
            yield n


def sim_step(grid):
    for coords in grid:
        grid[coords] += 1

    flashes = [coords for coords, energy in grid.items() if energy > 9]
    has_flashed = set(flashes)

    while flashes:
        curr = flashes.pop()
        has_flashed.add(curr)
        for neighbour in neighbourhood(curr):
            if neighbour in grid:
                grid[neighbour] += 1
                if grid[neighbour] > 9 and neighbour not in has_flashed:
                    flashes.append(neighbour)
                    has_flashed.add(neighbour)

    for flashed in has_flashed:
        grid[flashed] = 0

    return len(has_flashed)


def solve1(inp, steps=100):
    grid = parse(inp)
    return sum(sim_step(grid) for _ in range(steps))


def solve2(inp):
    grid = parse(inp)
    for step in count():
        if sim_step(grid) == len(grid.values()):
            return step + 1


print(solve1(rinput(11)))
print(solve2(rinput(11)))
