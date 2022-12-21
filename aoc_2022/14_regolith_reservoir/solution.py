"""AoC 14, 2022: Regolith Reservoir."""


from aoc_2022.helpers import get_input

import pathlib

CWD = pathlib.Path(__file__).parent

SAND_ORIGIN = (500, 0)
X_MAX = 800
Y_MAX = 180


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [row.strip("\n") for row in puzzle_input]


def generate_path_between_two_points(start: tuple[int, int], end: tuple[int, int]):
    x_start = int(start.split(",")[0])
    x_end = int(end.split(",")[0])

    y_start = int(start.split(",")[1])
    y_end = int(end.split(",")[1])

    if x_start != x_end:
        missing_points = {(i, y_end) for i in range(*sorted((x_start, x_end)))}
    else:
        missing_points = {(x_end, j) for j in range(*sorted((y_start, y_end)))}
    return missing_points | {
        (x_start, y_start),
        (x_end, y_end),
    }


def generate_path_coordinates(points: list[str]):
    paths = []
    for index, coordinates in enumerate(points[:-1]):
        path = generate_path_between_two_points(coordinates, points[index + 1])
        paths.append(path)

    return paths


def create_drawing_from_scan(data: list[str]):
    drawing = [["."] * X_MAX for _ in range(Y_MAX)]

    paths = [
        generate_path_coordinates(path_points.split(" -> ")) for path_points in data
    ]

    lowest_path_point = SAND_ORIGIN[1]

    for path in paths:
        for path_line in path:
            for path_point in path_line:
                x, y = path_point
                drawing[y][x] = "#"
                if y > lowest_path_point:
                    lowest_path_point = y

    return drawing, lowest_path_point


def insert_grain(drawing, max_depth):
    grain = SAND_ORIGIN
    is_bottom = False
    while not is_bottom:
        x, y = grain
        if y + 1 == max_depth:
            drawing[y][x] = "o"
            is_bottom = True
            return x, y + 1
        elif drawing[y + 1][x] == ".":
            grain = x, y + 1
        elif drawing[y + 1][x - 1] == ".":
            grain = x - 1, y + 1
        elif drawing[y + 1][x + 1] == ".":
            grain = x + 1, y + 1
        else:
            drawing[y][x] = "o"
            is_bottom = True
    return x, y


def simulate_falling_sand(
    drawing: list[list[str]], lowest_path_point, max_depth, stop_func
):
    steps = 0
    is_finished = False
    while not is_finished:
        final_grain_pos = insert_grain(drawing, max_depth)
        if stop_func(final_grain_pos):
            is_finished = True
        else:
            steps += 1

    return steps


def part1(data: list[str]):
    """Solve part 1."""
    drawing, lowest_path_point = create_drawing_from_scan(data)
    steps = simulate_falling_sand(
        drawing,
        lowest_path_point,
        max_depth=Y_MAX,
        stop_func=lambda x: x[1] > lowest_path_point,
    )
    return steps


def part2(data: list[str]):
    """Solve part 2."""
    drawing, lowest_path_point = create_drawing_from_scan(data)
    steps = simulate_falling_sand(
        drawing,
        lowest_path_point,
        max_depth=lowest_path_point + 2,
        stop_func=lambda x: x[1] == 0,
    )
    return steps + 1


def solve(puzzle_input: list[str]):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(CWD / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(e) for e in examples)))

    solutions = solve(get_input(CWD / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(s) for s in solutions)))
