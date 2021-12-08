from itertools import permutations

from utils import iter_lines, rinput

unique = {2: 1, 4: 4, 3: 7, 7: 8}

digit_segments = [
    "abcefg",
    "cf",
    "acdeg",
    "acdfg",
    "bcdf",
    "abdfg",
    "abdefg",
    "acf",
    "abcdefg",
    "abcdfg",
]
digit_segments = {k: str(i) for i, k in enumerate(digit_segments)}


def solve(inp):
    entries = parse(inp)
    cnt = 0
    for patterns, digits in entries:
        for digit in digits:
            val = unique.get(len(digit), None)
            if val is not None:
                cnt += 1
    print(cnt)


def parse(inp):
    parsed = []
    for line in iter_lines(inp):
        patterns, digits = line.split(" | ")
        parsed.append((patterns.split(" "), digits.split(" ")))
    return parsed


def solve2(entries):
    sum_ = 0
    for patterns, digits in entries:
        patterns = [sorted(pattern) for pattern in patterns]
        for mapping in permutations(base):
            new2base = {new: ch for new, ch in zip(mapping, base)}
            four = ""
            for pattern in patterns:
                transformed = "".join(sorted(new2base[ch] for ch in pattern))
                if transformed not in digit_segments:
                    break
            else:
                for digit in digits:
                    four += digit_segments[
                        "".join(sorted(new2base[ch] for ch in digit))
                    ]
                sum_ += int(four)
                break
    print(sum_)


solve(rinput(8))
solve2(parse(rinput(8)))
