"""AoC 2, 2022: Rock Paper Scissors."""

from collections import namedtuple
import pathlib
from typing import Iterator

from aoc_2022.helpers import get_input, parse_data


Shape = namedtuple("Shape", "name score")

A = X = Shape("Rock", 1)
B = Y = Shape("Paper", 2)
C = Z = Shape("Scissors", 3)


def get_shape_score_part1(shape: Shape) -> int:
    return shape.score


def get_outcome_score(opponent_shape: Shape, my_shape: Shape) -> int:
    if opponent_shape == my_shape:
        return 3
    elif opponent_shape == A:
        if my_shape == Y:
            return 6
        if my_shape == Z:
            return 0
    elif opponent_shape == B:
        if my_shape == X:
            return 0
        if my_shape == Z:
            return 6
    elif opponent_shape == C:
        if my_shape == X:
            return 6
        if my_shape == Y:
            return 0


def part1(data: list[str]) -> int:
    """Solve part 1."""
    total_score = 0
    for row in data:
        opponent_shape_raw, my_shape_raw = row.split()
        opponent_shape, my_shape = eval(opponent_shape_raw), eval(my_shape_raw)

        shape_score = get_shape_score_part1(my_shape)
        outcome_score = get_outcome_score(opponent_shape, my_shape)
        round_score = shape_score + outcome_score
        total_score += round_score

    return total_score


OUTCOME_MAPPING = {"X": 0, "Y": 3, "Z": 6}


def get_shape_score_part2(opponent_shape: Shape, outcome: str) -> int:
    if outcome == "Z":
        if opponent_shape.score == 1:
            return 2
        if opponent_shape.score == 2:
            return 3
        if opponent_shape.score == 3:
            return 1
    if outcome == "Y":
        return opponent_shape.score
    if outcome == "X":
        if opponent_shape.score == 1:
            return 3
        if opponent_shape.score == 2:
            return 1
        if opponent_shape.score == 3:
            return 2


def part2(data: list[str]) -> int:
    """Solve part 2."""
    total_score = 0
    for row in data:
        opponent_shape_raw, outcome = row.split()
        opponent_shape = eval(opponent_shape_raw)

        shape_score = get_shape_score_part2(opponent_shape, outcome)
        outcome_score = OUTCOME_MAPPING[outcome]
        round_score = shape_score + outcome_score
        total_score += round_score

    return total_score


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
