def grow_fish_school(fishes, days):
    while days > 0:
        number_fishlings = 0
        number_fishes_new_cycle = 0
        for fish_age, fish_count in sorted(fishes.items()):
            new_fish_age = fish_age - 1
            if new_fish_age < 0:
                new_fish_age = 6
                number_fishes_new_cycle = fish_count
                number_fishlings = fish_count
                del fishes[fish_age]
                continue
            del fishes[fish_age]
            fishes[new_fish_age] = fish_count
        days -= 1
        if number_fishlings > 0:
            fishes[8] = number_fishlings
        if number_fishes_new_cycle > 0:
            fishes[6] = fishes.get(6, 0) + number_fishes_new_cycle
    return fishes


def map_fishes(fish_list):
    fish_map = {}
    for fish in fish_list:
        fish_map[fish] = fish_map.get(fish, 0) + 1
    return fish_map


with open("inputs/day_06.txt", "r") as text_file:
    line = text_file.readline()
    data = [int(age) for age in line.strip().split(",")]

fishes = map_fishes(data)

fishes_80_days = grow_fish_school(dict(fishes), 80)
nb_fishes = sum(fishes_80_days.values())
print("Solution for part 1:", nb_fishes)

fishes_256_days = grow_fish_school(dict(fishes), 256)
nb_fishes = sum(fishes_256_days.values())
print("Solution for part 2:", nb_fishes)
