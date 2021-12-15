import sys
from collections import defaultdict
from heapq import *
from itertools import product

from utils import iter_lines, rinput


def parse(inp):
    graph = defaultdict(lambda: sys.maxsize)
    for y, line in enumerate(iter_lines(inp)):
        for x, price in enumerate(line):
            graph[(x, y)] = int(price)
    return graph, (x, y)


def neighbourhood(x, y):
    yield from ((x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y))


def cheapest_path(graph, start, end):
    dist = {start: 0}
    parent = {start: None}
    pq = [(0, start)]
    seen = set()
    while pq:
        du, u = heappop(pq)
        if u in seen:
            continue
        if u == end:
            break
        seen.add(u)
        for v in neighbourhood(*u):
            if v not in graph:
                continue
            risk_level = graph[v]
            if v not in dist or dist[v] > du + risk_level:
                dist[v] = du + risk_level
                parent[v] = u
                heappush(pq, (dist[v], v))
    return dist[end]


def extend_graph(graph, size, n_tiles):
    return {
        (x + tile_y * size, y + tile_x * size): wrap(cell + tile_y + tile_x)
        for tile_y, tile_x in product(range(n_tiles), range(n_tiles))
        for (x, y), cell in graph.items()
    }


def wrap(n):
    return n - 9 if n > 9 else n


def solve1(inp):
    graph, right_bottom = parse(inp)
    return cheapest_path(graph, (0, 0), right_bottom)


def solve2(inp):
    graph, _ = parse(inp)
    size = len(list(iter_lines(inp)))
    n_tiles = 5
    extended = extend_graph(graph, size, n_tiles)
    return cheapest_path(extended, (0, 0), (size * n_tiles - 1, size * n_tiles - 1))


print(solve1(rinput(15)))
print(solve2(rinput(15)))
