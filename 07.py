from utils import rinput


def solve1(inp):
    inp = sorted(inp)
    min_, max_ = min(inp), max(inp)
    costs = []
    # for i in range(min_, max_ + 1):
    # costs.append()
    # print(min(costs))
    res = min(sum(abs(n - i) for n in inp) for i in range(min_, max_ + 1))
    print(res)


def solve2(inp):
    inp = sorted(inp)
    min_, max_ = min(inp), max(inp)
    costs = []
    for i in range(min_, max_ + 1):
        costs.append(sum(sn(abs(n - i), 1, abs(n - i)) for n in inp))
    print(min(costs))


def sn(n, a1, an):
    return n * (a1 + an) / 2


inp = list(map(int, rinput(7).split(",")))

solve1(inp)
solve2(inp)
