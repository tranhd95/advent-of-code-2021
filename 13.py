from utils import iter_lines, rinput


def parse(inp):
    points = set()
    folds = []
    raw_points, raw_folds = inp.split("\n\n")
    for line in iter_lines(raw_points):
        points.add(tuple(map(int, line.split(","))))
    for line in iter_lines(raw_folds):
        axis, val = line.split("=")
        folds.append((axis[-1], int(val)))
    max_x, max_y = max(x for x, _ in points), max(y for _, y in points)
    grid = [[(x, y) in points for x in range(max_x + 1)] for y in range(max_y + 1)]
    return grid, folds


def fold(points, axis, along):
    if axis == "x":
        left = [[x for x in row[:along]] for row in points]
        right = [[x for x in reversed(row[along + 1 :])] for row in points]
        return merge(left, right)
    else:
        top = [row for row in points[:along]]
        bot = [row for row in reversed(points[along + 1 :])]
        return merge(top, bot)


def merge(fst, snd):
    merged = list(fst)
    for y, row in enumerate(fst):
        for x, _ in enumerate(row):
            merged[y][x] = fst[y][x] or snd[y][x]
    return merged


def print_grid(points):
    for row in points:
        for x in row:
            print("#" if x else ".", end="")
        print()


def solve1(inp):
    grid, folds = parse(inp)
    return sum(x for row in fold(grid, *folds[0]) for x in row)


def solve2(inp):
    grid, folds = parse(inp)
    for ins in folds:
        grid = fold(grid, *ins)
    print_grid(grid)


print(solve1(rinput(13)))
solve2(rinput(13))
