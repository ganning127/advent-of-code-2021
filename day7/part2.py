
from __future__ import annotations
from unittest import TestCase, main
from enum import unique, Enum
from os.path import isfile, join, dirname
from math import ceil, floor
from numpy import array, abs, sum, median, mean


@unique
class PART(Enum):
    ONE: str = "one"
    TWO: str = "two"

    def fuel_usage(self, d: array) -> int:
        if self == PART.ONE:
            return d
        elif self == PART.TWO:
            return d*(d+1)/2


class CrabSubmarines(object):
    def __init__(self, crab_starting_positions: array) -> None:
        self.crab_starting_positions: array = crab_starting_positions

    def calculate_minimum_fuel_usage(self, part: PART) -> int:
        if part == PART.ONE:
            return int(sum(abs(self.crab_starting_positions - median(self.crab_starting_positions))))
        elif part == PART.TWO:
            return int(min(sum(PART.TWO.fuel_usage(abs(self.crab_starting_positions - floor(mean(self.crab_starting_positions))))),
                           sum(PART.TWO.fuel_usage(abs(self.crab_starting_positions - ceil(mean(self.crab_starting_positions)))))))

    @staticmethod
    def load(puzzle_input_file_path: str) -> CrabSubmarines:
        assert isfile(
            puzzle_input_file_path), f"File not found: {puzzle_input_file_path}"

        with open(puzzle_input_file_path) as puzzle_input_file:
            crab_starting_positions: array = array(
                [int(puzzle_input) for puzzle_input in puzzle_input_file.read().split(",") if puzzle_input != ""])

        return CrabSubmarines(crab_starting_positions=crab_starting_positions)


class Examples(TestCase):
    def test_part_one_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_one_example}")

        test_puzzle: CrabSubmarines = CrabSubmarines.load(
            puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(
            test_puzzle.calculate_minimum_fuel_usage(part=PART.ONE), 37)

        print(f"Unittest {Examples.test_part_one_example} was successful.")

    def test_part_two_example(self) -> None:
        print(f"\nPerforming unittest: {Examples.test_part_two_example}")

        test_puzzle: CrabSubmarines = CrabSubmarines.load(
            puzzle_input_file_path=join(dirname(__file__), "example.txt"))
        self.assertEqual(
            test_puzzle.calculate_minimum_fuel_usage(part=PART.TWO), 168)

        print(f"Unittest {Examples.test_part_two_example} was successful.")


class Solutions(TestCase):
    def test_part_one(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_one}")

        test_puzzle: CrabSubmarines = CrabSubmarines.load(
            puzzle_input_file_path="input.txt")

        print(
            f"Part one solution calculated to be: {test_puzzle.calculate_minimum_fuel_usage(part=PART.ONE)}.")

    def test_part_two(self) -> None:
        print(f"\nCalculating solution to {Solutions.test_part_two}")

        test_puzzle: CrabSubmarines = CrabSubmarines.load(
            puzzle_input_file_path="input.txt")

        print(
            f"Part two solution calculated to be: {test_puzzle.calculate_minimum_fuel_usage(part=PART.TWO)}.")


if __name__ == "__main__":
    main()
