import re
from pathlib import Path
import numpy
from more_itertools import locate


def load_data(file: Path):
    data = file.read_text().splitlines()
    numbers = list(map(int, data.pop(0).split(',')))
    indices_of_empty_lines = list(locate(data, lambda a: a == ''))
    rows_strings = [data[i+1:i + 6] for i in indices_of_empty_lines]
    rows = [list(map(int, re.split(r'\D+', line.strip()))) for row in rows_strings for line in row]
    boards = [rows[i:i+5] for i in range(0, len(rows), 5)]
    return numbers, boards


def is_row_filled(drawn_numbers, boards) -> int:
    return [index for index, board in enumerate(boards) for row in board if set(row).issubset(set(drawn_numbers))]


def is_column_filled(drawn_numbers, boards):
    return is_row_filled(drawn_numbers, map(numpy.transpose, boards))


def calculate_score(numbers, boards, choose_win=True):
    drawn_numbers = []
    boards_that_won = []
    for number in numbers:
        drawn_numbers.append(number)
        winning_boards = list(set(is_row_filled(drawn_numbers, boards) + is_column_filled(drawn_numbers, boards)))
        if len(winning_boards) > 0 and choose_win:
            unmarked = filter(lambda x: x not in drawn_numbers, [n for row in boards[winning_boards[0]] for n in row])
            return sum(unmarked) * number
        if not choose_win and len(winning_boards) == len(boards):
                last_won = next(filter(lambda x: x not in boards_that_won, winning_boards))
                unmarked = filter(lambda x: x not in drawn_numbers, [n for row in boards[last_won] for n in row])
                return sum(unmarked) * number
        boards_that_won = winning_boards

if __name__ == '__main__':
    numbers, boards = load_data(Path('input.txt'))
    print(calculate_score(numbers, boards, choose_win=True))
    print(calculate_score(numbers, boards, choose_win=False))