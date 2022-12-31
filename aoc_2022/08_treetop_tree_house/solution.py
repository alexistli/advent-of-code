"""AoC 8, 2022: Treetop Tree House."""

import math
import pathlib
from typing import Iterable, Iterator

from aoc_2022.utils import get_input, parse_data, parse_ints


Tree = int
Matrix = list[list[int]]


def get_row(i: int, _j: int, data: Matrix) -> list[Tree]:
    return data[i]


def get_column(i: int, j: int, data: Matrix) -> list[Tree]:
    return get_row(j, i, list(zip(*data)))


def check_tree_visibility_from_trees(tree: Tree, trees: Iterable[Tree]) -> bool | None:
    if not trees:
        return True
    if max(trees) < tree:
        return True
    return None


def check_tree_visibility(i: int, j: int, tree: Tree, data: Matrix) -> bool | None:
    row = get_row(i, j, data)
    left, right = row[:j], row[j + 1 :]

    col = get_column(i, j, data)
    upper, lower = col[:i], col[i + 1 :]

    return bool(
        check_tree_visibility_from_trees(tree, left)
        or check_tree_visibility_from_trees(tree, right)
        or check_tree_visibility_from_trees(tree, upper)
        or check_tree_visibility_from_trees(tree, lower)
    )


def part1(data: list[str]) -> int:
    """Solve part 1."""
    parsed_data = [parse_ints(list(row)) for row in data]
    nb_visible_trees = 0
    for i, row in enumerate(parsed_data):
        for j, tree in enumerate(row):
            if check_tree_visibility(i, j, tree, parsed_data):
                nb_visible_trees += 1
    return nb_visible_trees


def get_distance(tree: Tree, trees: Iterable[Tree]) -> int:
    distance = 0
    for t in trees:
        distance += 1
        if t >= tree:
            break
    return distance


def get_scenic_score(i: int, j: int, tree: Tree, data: Matrix) -> int:
    row = get_row(i, j, data)
    left, right = row[:j], row[j + 1 :]

    col = get_column(i, j, data)
    upper, lower = col[:i], col[i + 1 :]

    viewing_distances = (
        [get_distance(tree, reversed(left))]
        + [get_distance(tree, right)]
        + [get_distance(tree, reversed(upper))]
        + [get_distance(tree, lower)]
    )

    return math.prod(viewing_distances)


def part2(data: list[str]) -> int:
    """Solve part 2."""
    parsed_data = [parse_ints(list(row)) for row in data]
    best_scenic_score = 0
    for i, row in enumerate(parsed_data):
        for j, tree in enumerate(row):
            best_scenic_score = max(best_scenic_score, get_scenic_score(i, j, tree, parsed_data))
    return best_scenic_score


def solve(puzzle_input: list[str]) -> Iterator[int]:
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    examples = solve(get_input(pathlib.Path(__file__).parent / "example.txt"))
    print("Examples:\n\t{}".format("\n\t".join(str(solution) for solution in examples)))

    solutions = solve(get_input(pathlib.Path(__file__).parent / "input.txt"))
    print("Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions)))
