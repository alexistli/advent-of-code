"""AoC 11, 2021: Dumbo Octopus."""


from typing import TypeVar
from aoc_2022.helpers import load_day_input

import pathlib

Data = list[list[int]]


def parse_data(puzzle_input: list[str]) -> Data:
    """Parse input."""
    return [[int(o) for o in list(row.strip("\n"))] for row in puzzle_input]


def flash_octopus(data: Data, i: int, j: int) -> int:
    flashes = 1
    data[i][j] = 0
    flashes += increment_neighbor_octopus(data, i, j)
    return flashes


def increment_neighbor_octopus(data: Data, i: int, j: int) -> int:
    flashes = 0
    for current_i, row in enumerate(data[i - 1 : i + 2]):
        for current_j, _octopus in enumerate(row[j - 1 : j + 2]):
            if current_i == 1 and current_j == 1:
                continue
            if data[current_i : current_i + 1][current_j : current_j + 1] == []:
                continue
            if data[current_i][current_j] == 0:
                continue
            data[current_i][current_j] += 1
            if data[current_i][current_j] > 9:
                flashes += flash_octopus(data, current_i, current_j)

    return flashes


def simulate_step(data: Data) -> None:
    for i, row in enumerate(data):
        for j, _octopus in enumerate(row):
            data[i][j] += 1

    flashes = 0
    for i, row in enumerate(data):
        for j, _octopus in enumerate(row):
            if data[i][j] > 9:
                flashes += flash_octopus(data, i, j)

    return flashes


def part1(data: Data):
    """Solve part 1."""
    flashes = 0
    for _ in range(0, 100):
        flashes += simulate_step(data)

    return flashes


def part2(data: Data):
    """Solve part 2."""


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(load_day_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    solutions = solve(load_day_input(pathlib.Path(__file__).parent / "input.txt"))
    print(
        "Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions))
    )
