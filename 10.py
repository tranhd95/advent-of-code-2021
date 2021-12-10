from collections import Counter
from functools import reduce
from statistics import median

from utils import iter_file, iter_lines, rinput

left, right = "([{<", ")]}>"
pairs = dict(zip(left, right))


def solve1(lines):
    s = []
    table = dict(zip(right, (3, 57, 1197, 25137)))
    error_score = 0
    for line in lines:
        for ch in line:
            if ch in left:
                s.append(ch)
            else:
                curr = s.pop()
                if pairs[curr] != ch:
                    error_score += table[ch]
    return error_score


def solve2(lines):
    scores = []
    table = dict(zip(left, range(1, 5)))
    for i, line in enumerate(lines):
        s = []
        for ch in line:
            if ch in left:
                s.append(ch)
            elif pairs[s.pop()] != ch:
                break
        else:
            scores.append(
                reduce(lambda score, val: score * 5 + table[val], reversed(s), 0)
            )
    return median(scores)


print(solve1(iter_file(10)))
print(solve2(iter_file(10)))
