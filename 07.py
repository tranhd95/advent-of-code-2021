from utils import rinput


def solve(inp):
    inp = sorted(inp)
    min_, max_ = min(inp), max(inp)
    costs = []
    for i in range(min_, max_ + 1):
        costs.append(sum(abs(n - i) for n in inp))
    print(min(costs))


def solve2(inp):
    inp = sorted(inp)
    min_, max_ = min(inp), max(inp)
    costs = []
    for i in range(min_, max_ + 1):
        costs.append(sum(sn(abs(n - i), 1, abs(n - i)) for n in inp))
    print(min(costs))


def sn(n, a1, an):
    return n * (a1 + an) / 2


t = list(map(int, test.split(",")))
inp = list(map(int, rinput(7).split(",")))

solve1(inp)
solve2(inp)
