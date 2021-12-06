# 08:24

from collections import defaultdict, Counter

from utils import iter_file, iter_lines

import pandas as pd


def solve1(inp):
    df = pd.DataFrame(((d for d in number) for number in inp))
    gamma = ""
    for col in df:
        gamma += df[col].value_counts().idxmax()
    epsilon = int("".join("1" if x == "0" else "0" for x in gamma), 2)
    gamma = int(gamma, 2)
    print(gamma * epsilon)


def solve2(inp):
    df = pd.DataFrame(((d for d in number) for number in inp))
    oxy, co2 = set(), set()
    for col in df:
        if not oxy:
            crit = df[col].value_counts().idxmax()
            oxy = set(df[df[col] == crit].index.tolist())
        elif len(oxy) == 1:
            break
        else:
            vc = df[col].loc[oxy].value_counts()
            crit = vc.idxmax()
            if vc.loc["0"] == vc.loc["1"]:
                crit = "1"
            oxy &= set(df[df[col] == crit].index.tolist())
    for col in df:
        if not co2:
            crit = df[col].value_counts().idxmin()
            co2 = set(df[df[col] == crit].index.tolist())
        elif len(co2) == 1:
            break
        else:
            vc = df[col].loc[co2].value_counts()
            crit = vc.idxmin()
            if vc.loc["0"] == vc.loc["1"]:
                crit = "0"
            co2 &= set(df[df[col] == crit].index.tolist())
    oxy = int("".join(df.loc[oxy].values[0]), 2)
    co2 = int("".join(df.loc[co2].values[0]), 2)
    print(oxy * co2)


test = list(iter_lines(test))

solve1(iter_file(3))
solve2(iter_file(3))
