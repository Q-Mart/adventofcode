import utils
from collections import namedtuple

data = utils.get_day(2021, 4)

MARKER = 'X'
BingoSubsystem = namedtuple(
    'BingoSubsystem',
    ['numbers',
     'last_called',
     'last_winning_product',
     'boards']
)

def parse(data):
    numbers = data[0].split(',')
    boards = []

    # Start from first board
    i = 2
    while i<len(data):
        new_board = []
        for j in range(5):
            new_board.append(data[i+j].split())

        boards.append(new_board)
        i += 6

    return BingoSubsystem(numbers, None, None, boards)

def _calc_result(index, subsystem):
    winning_board = subsystem.boards[index]

    sum_unmarked = 0
    for row in winning_board:
        for elem in row:
            if elem != MARKER:
                sum_unmarked += int(elem)

    return sum_unmarked * subsystem.last_called

def run_bingo(subsystem, f_when_winner_found):
    # Base cases
    # If we are out of numbers, no winner
    if subsystem.numbers == [] or subsystem.boards == []:
        return subsystem.last_winning_product

    # Check for a winner
    for i, board in enumerate(subsystem.boards):

        row_found = False
        for row in board:
            if row == [MARKER, MARKER, MARKER, MARKER, MARKER]:
                row_found = True

        col_found = False
        for j in range(len(board)):
            col_found = True
            for row in board:
                if row[j] != MARKER:
                    col_found = False
                    continue

            if col_found == True:
                break

        last_winning_product = None
        if row_found or col_found:
            result = _calc_result(i, subsystem)

            should_return, last_winning_product = f_when_winner_found(i, result, subsystem)
            if should_return:
                return last_winning_product

    # Pop the next number and mark the boards
    number = subsystem.numbers[0]

    for board in subsystem.boards:
        for row in board:
            for i in range(len(row)):
                if row[i] == number:
                    row[i] = MARKER

    new_subsystem = BingoSubsystem(
        subsystem.numbers[1:],
        int(number),
        subsystem.last_winning_product,
        subsystem.boards
    )
    return run_bingo(new_subsystem, f_when_winner_found)



test_data = [
    "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
    "",
    "22 13 17 11  0",
    " 8  2 23  4 24",
    "21  9 14 16  7",
    " 6 10  3 18  5",
    " 1 12 20 15 19",
    "",
    " 3 15  0  2 22",
    " 9 18 13 17  5",
    "19  8  7 25 23",
    "20 11 10 24  4",
    "14 21 16 12  6",
    "",
    "14 21 17 24  4",
    "10 16 15  9 19",
    "18  8 23 26 20",
    "22 11 13  6  5",
    " 2  0 12  3  7"
]

part_1_f = lambda i, r, s: (True, r)

def part_2_f(i, result, subsystem):
    should_return = False

    subsystem.boards.pop(i)
    if subsystem.boards == []:
        should_return = True

    return should_return, result

subsystem = parse(test_data)
assert(run_bingo(subsystem, part_1_f) == 4512)

subsystem = parse(test_data)
assert(run_bingo(subsystem, part_2_f) == 1924)

subsystem = parse(data)
utils.print_part_1(run_bingo(subsystem, part_1_f))

subsystem = parse(data)
utils.print_part_2(run_bingo(subsystem, part_2_f))

