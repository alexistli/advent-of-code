with open("inputs/day_06.txt", "r") as text_file:
    line = text_file.readline()
    data = [int(age) for age in line.strip().split(",")]


fishes = list(data)
counter = 80
while counter > 0:
    fishlings = []
    for fish_idx, fish_age in enumerate(fishes):
        fish_age -= 1
        if fish_age < 0:
            fish_age = 6
            fishlings.append(8)
        fishes[fish_idx] = fish_age
    counter -= 1
    fishes.extend(fishlings)

print("Solution for part 1:", len(fishes))
