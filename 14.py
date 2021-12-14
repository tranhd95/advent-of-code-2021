from collections import Counter
from itertools import pairwise

from utils import iter_lines, rinput


def parse(inp):
    template, rules_raw = inp.split("\n\n")
    rules = {}
    for rule in iter_lines(rules_raw):
        frm, to = rule.split(" -> ")
        rules[tuple(frm)] = to
    return template, rules


def solve(inp, steps):
    template, rules = parse(inp)
    letters_cnt = Counter(template)
    pairs_cnt = Counter(pairwise(template))
    for _ in range(steps):
        polymerization = Counter()
        for (left, right), to in rules:
            num_pairs = pairs_cnt[(left, right)]
            polymerization[(left, to)] += num_pairs
            polymerization[(to, right)] += num_pairs
            letters_cnt[to] += num_pairs
        pairs_cnt = polymerization
    most_common = letters_cnt.most_common()
    return most_common[0][1] - most_common[-1][1]


print(solve(rinput(14), 10))
print(solve(rinput(14), 40))
