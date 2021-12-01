from utils import iter_file, iter_lines, rinput


def solve1():
    it = iter_file(1)
    prev = int(next(it))
    cnt = 0
    for line in it:
        nxt = int(line)
        if nxt > prev:
            cnt += 1
        prev = nxt
    print(cnt)


def solve2():
    depths = list(map(int, iter_file(1)))
    prev = sum(depths[0:3])
    cnt = 0
    for i in range(1, len(depths)-2):
        nxt = sum(depths[i:i+3])
        if nxt > prev:
            cnt += 1
        prev = nxt
    print(cnt)
        
solve1()
solve2()