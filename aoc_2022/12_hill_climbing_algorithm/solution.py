"""AoC 12, 2022: Hill Climbing Algorithm."""


from aoc_2022.helpers import load_day_input

import pathlib

CWD = pathlib.Path(__file__).parent


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def part1(data: list[str]):
    """Solve part 1."""


def part2(data: list[str]):
    """Solve part 2."""


def solve(puzzle_input: list[str]):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(load_day_input(CWD / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(e) for e in examples)))

    # examples_2 = solve(load_day_input(CWD / "example2.txt"))
    # print("Examples 2:\n\t{}".format("\n\t".join(str(e) for e in examples_2)))

    solutions = solve(load_day_input(CWD / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(s) for s in solutions)))
