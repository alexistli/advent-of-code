"""AoC 15, 2022: Beacon Exclusion Zone."""


import pathlib
import re
from typing import Iterator


from aoc_2022.helpers import get_input, parse_data


CWD = pathlib.Path(__file__).parent

POSITIONS_PATTERN = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)

Coords = tuple[int, int]
Column = list[str]


def compute_manhattan_distance(x1, y1, x2, y2) -> int:
    """Compute Manhattan distance between two points."""
    return abs(x2 - x1) + abs(y2 - y1)


def parse_positions(data: list[str]):
    sensors, beacons = set(), set()
    for row in data:
        match = POSITIONS_PATTERN.match(row)
        sx, sy = int(match.group(1)), int(match.group(2))
        bx, by = int(match.group(3)), int(match.group(4))
        d = compute_manhattan_distance(sx, sy, bx, by)
        sensors.add((sx, sy, d))
        beacons.add((bx, by))
    return sensors, beacons


def check_possible_location(sensors, beacons, x, y):
    for sx, sy, d in sensors:
        if compute_manhattan_distance(x, y, sx, sy) <= d and (x, y) not in beacons:
            return False
    return True


def part1(data):
    sensors, beacons = parse_positions(data)
    count = 0
    column_to_check = 2_000_000
    for x in range(
        min(x - d for x, _, d in sensors), max(x + d for x, _, d in sensors)
    ):
        if (
            not check_possible_location(sensors, beacons, x, column_to_check)
            and (x, column_to_check) not in beacons
        ):
            count += 1
    return count


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
