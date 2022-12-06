"""AoC 6, 2022: Tuning Trouble."""


from aoc_2022.helpers import load_day_input

import pathlib


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input[0]


def get_marker_position(data, marker_size):
    """Return the marker's last character position in a data stream.

    Marker is a sequence of `marker_size` characters all different"""
    for i in range(0, len(data) - marker_size):
        potential_marker = data[i : i + marker_size]
        if len(set(potential_marker)) == marker_size:
            return i + marker_size


def part1(data):
    """Solve part 1."""
    marker_size = 4
    return get_marker_position(data, marker_size)


def part2(data):
    """Solve part 2."""
    marker_size = 14
    return get_marker_position(data, marker_size)


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
