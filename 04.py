import re

from utils import rinput

RE_DIGITS = re.compile(r"(\d+)")
SQ_SIZE = 5


def parse(inp):
    splits = inp.split("\n\n")
    numbers = map(int, splits[0].split(","))
    boards = []
    for br in splits[1:]:
        board = [list(map(int, RE_DIGITS.findall(row))) for row in br.split("\n")]
        boards.append(board)
    board_dcts = []
    for brd in boards:
        dct = {val: (x, y) for y, row in enumerate(brd) for x, val in enumerate(row)}
        board_dcts.append(dct)
    return numbers, boards, board_dcts


def has_won(marks):
    for i in range(SQ_SIZE):
        row = {(x, i) for x in range(SQ_SIZE)}
        col = {(i, y) for y in range(SQ_SIZE)}
        if row <= marks or col <= marks:
            return True
    return False


def sum_of_unmarked(marks, board):
    return sum(
        board[y][x]
        for y in range(SQ_SIZE)
        for x in range(SQ_SIZE)
        if (x, y) not in marks
    )


def solve1(numbers, boards, board_dcts):
    marked = [set() for _ in range(len(board_dcts))]
    for n in numbers:
        for i, dct in enumerate(board_dcts):
            if n in dct:
                marked[i].add(dct[n])
        for marks, board in zip(marked, boards):
            if has_won(marks):
                return n * sum_of_unmarked(marks, board)


def solve2(numbers, boards, board_dcts):
    marked = [set() for _ in range(len(board_dcts))]
    winners = set()
    for n in numbers:
        for i, dct in enumerate(board_dcts):
            if n in dct:
                marked[i].add(dct[n])
        for i, (marks, board) in enumerate(zip(marked, boards)):
            if i not in winners and has_won(marks):
                winners.add(i)
                if len(winners) == len(boards):
                    return n * sum_of_unmarked(marks, board)


print(solve1(*parse(rinput(4))))
print(solve2(*parse(rinput(4))))