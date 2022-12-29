"""AoC 8, 2022: Treetop Tree House."""


from typing import Iterator
from aoc_2022.helpers import get_input, parse_data

import pathlib
import math


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


def get_scenic_score(i: int, j: int, tree: int, data: list[str]):
    viewing_distances = []

    row = get_row(i, j, data)
    leftmost = row[:j]
    rightmost = row[j + 1 :]
    distance = 0
    for l in reversed(leftmost):
        distance += 1
        if l >= tree:
            break
    if distance == 0:
        return 0
    viewing_distances.append(distance)

    distance = 0
    for l in rightmost:
        distance += 1
        if l >= tree:
            break
    if distance == 0:
        return 0
    viewing_distances.append(distance)

    col = get_column(i, j, data)
    upper = col[:i]
    lower = col[i + 1 :]

    distance = 0
    for l in reversed(upper):
        distance += 1
        if l >= tree:
            break
    if distance == 0:
        return 0
    viewing_distances.append(distance)

    distance = 0
    for l in lower:
        distance += 1
        if l >= tree:
            break
    if distance == 0:
        return 0
    viewing_distances.append(distance)

    return math.prod(viewing_distances)


def part1(data: list[str]) -> int:
    """Solve part 1."""
    nb_visible_trees = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            if check_tree_visibility(i, j, tree, data):
                nb_visible_trees += 1
    return nb_visible_trees


def part2(data: list[str]) -> int:
    """Solve part 2."""
    best_scenic_score = 0
    for i, row in enumerate(data):
        for j, tree in enumerate(row):
            best_scenic_score = max(
                best_scenic_score, get_scenic_score(i, j, tree, data)
            )
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
    print(
        "Solutions:\n\t{}".format("\n\t".join(str(solution) for solution in solutions))
    )
