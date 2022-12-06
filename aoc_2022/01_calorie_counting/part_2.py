from aoc_2022.day_01.part_1 import get_calories_by_elf
from aoc_2022.helpers import load_day_input


def main():
    data = load_day_input("aoc_2022/day_01/input.txt")
    calories_grouped_by_elf = get_calories_by_elf(data)
    summed_elf_colories = [
        sum(elf_calories) for elf_calories in calories_grouped_by_elf
    ]
    top_3_elf_calories = sorted(summed_elf_colories, reverse=True)[:3]
    sum_top_3_elf_calories = sum(top_3_elf_calories)
    print(sum_top_3_elf_calories)


if __name__ == "__main__":
    main()
