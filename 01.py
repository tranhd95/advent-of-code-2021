from itertools import pairwise
from utils import iter_file


def solve1(lst):
    print(sum(snd > fst for fst, snd in pairwise(lst)))


def solve2(lst):
    sums = [sum(lst[i : i + 3]) for i in range(len(lst) - 2)]
    print(solve1(sums))


inp = list(map(int, iter_file(1)))

solve1(inp)
solve2(inp)