from collections import namedtuple
from aoc_2022.helpers import get_input

Shape = namedtuple("Shape", "name score")

A = X = Shape("Rock", 1)
B = Y = Shape("Paper", 2)
C = Z = Shape("Scissors", 3)


def get_shape_score(shape: Shape) -> int:
    return shape.score


def get_outcome_score(opponent_shape: Shape, my_shape: Shape):
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


def main():
    data = get_input("aoc_2022/day_02/input.txt")

    total_score = 0
    for row in data:
        opponent_shape_raw, my_shape_raw = row.split()
        opponent_shape, my_shape = eval(opponent_shape_raw), eval(my_shape_raw)

        shape_score = get_shape_score(my_shape)
        outcome_score = get_outcome_score(opponent_shape, my_shape)
        round_score = shape_score + outcome_score
        total_score += round_score

    print(total_score)


if __name__ == "__main__":
    main()
