"""AoC 8, 2022: Treetop Tree House."""


from aoc_2022.helpers import load_day_input

import pathlib


def parse_data(puzzle_input: list[str]) -> list[str]:
    """Parse input."""
    return [[int(tree) for tree in list(row.strip("\n"))] for row in puzzle_input]


def get_row(i, _j, data):
    row = data[i]
    return row


def get_column(i, j, data):
    col = get_row(j, i, list(zip(*data)))
    return col


def check_tree_visibility(i: int, j: int, tree: int, data: list[str]):
    row = get_row(i, j, data)
    leftmost = row[:j]
    rightmost = row[j + 1 :]
    if not (leftmost and rightmost):
        return True
    if max(leftmost) < tree or max(rightmost) < tree:
        return True

    col = get_column(i, j, data)
    upper = col[:i]
    lower = col[i + 1 :]
    if not (upper and lower):
        return True
    if max(upper) < tree or max(lower) < tree:
        return True

    return False


def part1(data):
    """Solve part 1."""
    nb_visible_trees = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            if check_tree_visibility(i, j, tree, data):
                nb_visible_trees += 1
    return nb_visible_trees


def part2(data):
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
