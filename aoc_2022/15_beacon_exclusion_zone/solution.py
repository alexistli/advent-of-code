"""AoC 15, 2022: Beacon Exclusion Zone."""


import pathlib
from typing import Iterator


from aoc_2022.helpers import get_input, parse_data


CWD = pathlib.Path(__file__).parent


def part1(data: list[str]) -> int:
    """Solve part 1."""


def part2(data: list[str]) -> int:
    """Solve part 2."""


def solve(puzzle_input: list[str]) -> Iterator[int]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(CWD / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(e) for e in examples)))

    solutions = solve(get_input(CWD / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(s) for s in solutions)))
