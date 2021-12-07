import sys
from utils import rinput

def solve1(inp):
    min_, max_ = min(inp), max(inp)
    min_cost = sys.maxsize
    for i in range(min_, max_+1):
        min_cost = min(sum(abs(n - i) for n in inp), min_cost)
    print(min_cost)

def solve2(inp):
    min_, max_ = min(inp), max(inp)
    min_cost = sys.maxsize
    for i in range(min_, max_+1):
        min_cost = min(sum(sn(abs(n - i), 1, abs(n - i)) for n in inp), min_cost)
    print(min_cost)

def sn(n, a1, an):
    return n*(a1 + an)//2

inp = list(map(int, rinput(7).split(",")))

solve1(inp)
solve2(inp)