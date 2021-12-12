from utils import iter_lines, rinput
from collections import defaultdict


def parse(inp):
    graph = defaultdict(set)
    for line in iter_lines(inp):
        frm, to = line.split("-")
        graph[frm].add(to)
        graph[to].add(frm)
    return graph


def solve1(inp):
    graph = parse(inp)
    return dfs(graph, "start", set(), True)


def dfs(G, v, seen, revisiting):
    if v == "end":
        return 1
    
    paths_cnt = 0

    for w in G[v]:
        if w == "start":
            continue
        elif w not in seen or w.isupper():
            paths_cnt += dfs(G, w, seen | {v}, revisiting)
        elif not revisiting:
            paths_cnt += dfs(G, w, seen | {v}, True)
    return paths_cnt


def solve2(inp):
    return dfs(parse(inp), "start", set(), False)


print(solve1(rinput(12)))
print(solve2(rinput(12)))
