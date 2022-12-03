def get_calories_by_elf(calories_list):

    elf_calories = []
    for calories in calories_list:
        if calories == "\n":
            yield elf_calories
            elf_calories = []
            continue
        elf_calories += [int(calories)]


def main():
    with open("2022/day_01/input.txt", "r") as f:
        data = [line for line in f.readlines()]

    calories_grouped_by_elf = get_calories_by_elf(data)
    max_elf_colories = max(
        [sum(elf_calories) for elf_calories in calories_grouped_by_elf]
    )
    print(max_elf_colories)


if __name__ == "__main__":
    main()
