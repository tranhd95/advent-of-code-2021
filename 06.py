from utils import rinput
from collections import deque

inp = list(map(int, rinput(6).strip().split(",")))


def solve1(lst, days):
    for d in range(days):
        for i, t in enumerate(lst):
            if t == 0:
                lst.append(9)
                lst[i] = 6
            else:
                lst[i] -= 1
    print(len(lst))


def solve_eff(lst, days):
    cnt = [0] * 9
    for t in lst:
        cnt[t] += 1
    q = deque(cnt)
    for _ in range(days):
        q.rotate(-1)
        q[6] += q[8]
    print(sum(q))


solve_eff(inp, 80)
solve_eff(inp, 256)
