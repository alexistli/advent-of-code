"""AoC 6, 2022: Tuning Trouble."""

import pathlib
from typing import Iterator

from aoc_2022.utils import get_input, parse_data


def get_marker_position(data: list[str], marker_size: int) -> int:
    """Return the marker's last character position in a data stream.

    Marker is a sequence of `marker_size` characters all different"""
    for i in range(0, len(data) - marker_size):
        potential_marker = data[i : i + marker_size]
        if len(set(potential_marker)) == marker_size:
            return i + marker_size


def part1(data: list[str]) -> int:
    """Solve part 1."""
    marker_size = 4
    return get_marker_position(data[0], marker_size)


def part2(data: list[str]) -> int:
    """Solve part 2."""
    marker_size = 14
    return get_marker_position(data[0], marker_size)


def solve(puzzle_input: list[str]) -> Iterator[int]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    solutions = solve(get_input(pathlib.Path(__file__).parent / "input.txt"))
    print(
        "Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions))
    )
