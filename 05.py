from collections import defaultdict
import re
from utils import iter_file

RE_DIGIT = re.compile(r"\d+")


def parse(inp):
    return (map(int, RE_DIGIT.findall(ln)) for ln in inp)


def solve1(inp):
    parsed = parse(inp)
    diagram = defaultdict(int)
    for (x1, y1, x2, y2) in parsed:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                diagram[(x1, y)] += 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                diagram[(x, y1)] += 1
    print(sum(val > 1 for val in diagram.values()))


def solve2(inp):
    parsed = parse(inp)
    diagram = defaultdict(int)
    for (x1, y1, x2, y2) in parsed:
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                diagram[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                diagram[(x, y1)] += 1
        else:
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            for i, y in enumerate(range(y1, y2 + dy, dy)):
                diagram[(x1 + dx * i, y)] += 1
    print(sum(val > 1 for val in diagram.values()))


solve1(iter_file(5))
solve2(iter_file(5))
