from aoc_2022.helpers import load_day_input
from aoc_2022.day_02.part_1 import A, B, C, get_shape_score


OUTCOM_MAPPING = {"X": 0, "Y": 3, "Z": 6}


def get_shape_score(opponent_shape, outcome):
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


def main():
    data = load_day_input("aoc_2022/day_02/input.txt")

    total_score = 0
    for row in data:
        opponent_shape_raw, outcome = row.split()
        opponent_shape = eval(opponent_shape_raw)

        shape_score = get_shape_score(opponent_shape, outcome)
        outcome_score = OUTCOM_MAPPING[outcome]
        round_score = shape_score + outcome_score
        total_score += round_score

    print(total_score)


if __name__ == "__main__":
    main()
