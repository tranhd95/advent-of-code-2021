from utils import iter_file

DAY = 2

def solve1(inp):
    h, d = 0, 0
    for line in inp:
        cmd, amnt = line.split(" ")
        amnt = int(amnt)
        match cmd:
            case "forward":
                h += amnt
            case "down":
                d += amnt
            case "up":
                d -= amnt
    print(h*d)


def solve2(inp):
    h, d, a = 0, 0, 0
    for line in inp:
        cmd, amnt = line.split(" ")
        amnt = int(amnt)
        match cmd:
            case "forward":
                h += amnt
                d += a * amnt
            case "down":
                a += amnt
            case "up":
                a -= amnt
    print(h*d)

inp = list(iter_file(DAY))

solve1(inp)
solve2(inp)