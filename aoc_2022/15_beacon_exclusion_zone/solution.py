"""AoC 15, 2022: Beacon Exclusion Zone."""


import pathlib
import re
from typing import Iterator


from aoc_2022.helpers import get_input, parse_data


CWD = pathlib.Path(__file__).parent

POSITIONS_PETTERN = re.compile(
    r"Sensor at x=(?P<sensor_x>-?\d+), y=(?P<sensor_y>-?\d+): closest beacon is at x=(?P<beacon_x>-?\d+), y=(?P<beacon_y>-?\d+)"
)


Coords = tuple[int, int]
Map = list[list[str]]


def parse_positions_pattern(data: list[str]) -> Iterator[tuple[Coords, Coords]]:
    for row in data:
        match = POSITIONS_PETTERN.match(row)
        sensor_coords = int(match.group("sensor_x")), int(match.group("sensor_y"))
        beacon_coords = int(match.group("beacon_x")), int(match.group("beacon_y"))
        yield sensor_coords, beacon_coords


def init_map(parsed_positions: list[tuple[Coords]]) -> tuple[Map, tuple[int, int]]:
    min_x = min_y = max_x = max_y = 0
    for sensor_coords, beacon_coords in parsed_positions:
        min_x = min(min_x, sensor_coords[0], beacon_coords[0])
        min_y = min(min_y, sensor_coords[1], beacon_coords[1])
        max_x = max(max_x, sensor_coords[0], beacon_coords[0])
        max_y = max(max_y, sensor_coords[1], beacon_coords[1])
    empty_map = [["."] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]
    return empty_map, (min_x, min_y)


def compute_manhattan_distance(point_a: Coords, point_b: Coords) -> int:
    """Compute Manhattan distance between two points."""
    return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])


def fill_covered_area(map: Map, sensor_index_0: Coords, beacon_index_0: Coords) -> None:
    sensor_beacon_distance = compute_manhattan_distance(sensor_index_0, beacon_index_0)
    for i, row in enumerate(map):
        for j, point in enumerate(row):
            if (
                compute_manhattan_distance(sensor_index_0, (i, j))
                <= sensor_beacon_distance
            ):
                if point == ".":
                    map[i][j] = "#"


def fill_map(parsed_positions: list[tuple[Coords, Coords]]) -> Map:
    map, (min_x, min_y) = init_map(parsed_positions)
    for sensor_coords, beacon_coords in parsed_positions:
        sensor_index_0 = (sensor_coords[0] - min_x, sensor_coords[1] - min_y)
        map[sensor_index_0[0]][sensor_index_0[1]] = "S"
        beacon_index_0 = (beacon_coords[0] - min_x, beacon_coords[1] - min_y)
        map[beacon_index_0[0]][beacon_index_0[1]] = "B"
        fill_covered_area(map, sensor_index_0, beacon_index_0)

    return map


def part1(data: list[str]) -> int:
    """Solve part 1."""
    ROW_TO_CHECK = 10
    parsed_positions = [(s, b) for s, b in parse_positions_pattern(data)]
    filled_map = fill_map(parsed_positions)
    empty_positions_on_line_to_check = len(
        [p for row in filled_map if (p := row[ROW_TO_CHECK]) == "#"]
    )
    return empty_positions_on_line_to_check


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

    # solutions = solve(get_input(CWD / "input.txt"))
    # print("Solutions:\n\t{}".format("\n\t".join(str(s) for s in solutions)))
