"""AoC 1, 2022: Calorie Counting."""


import pathlib
from typing import Iterator

from aoc_2022.utils import get_input, parse_data


def get_calories_by_elf(calories_list: list[str]) -> Iterator[list[int]]:
    elf_calories = []
    for calories in calories_list:
        if calories == "":
            yield elf_calories
            elf_calories = []
            continue
        elf_calories += [int(calories)]


def part1(data: list[str]) -> int:
    """Solve part 1."""
    calories_grouped_by_elf = get_calories_by_elf(data)
    max_elf_colories = max(
        [sum(elf_calories) for elf_calories in calories_grouped_by_elf]
    )
    return max_elf_colories


def part2(data: list[str]) -> int:
    """Solve part 2."""
    calories_grouped_by_elf = get_calories_by_elf(data)
    summed_elf_colories = [
        sum(elf_calories) for elf_calories in calories_grouped_by_elf
    ]
    top_3_elf_calories = sorted(summed_elf_colories, reverse=True)[:3]
    sum_top_3_elf_calories = sum(top_3_elf_calories)
    return sum_top_3_elf_calories


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
