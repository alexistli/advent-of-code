from aoc_2022.helpers import get_input
from aoc_2022.day_02.part_1 import A, B, C, get_shape_score


def main():
    data = get_input("aoc_2022/day_02/input.txt")

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
