with open("inputs/day_07.txt", "r") as text_file:
    line = text_file.readline()
    data = [int(pos) for pos in line.strip().split(",")]

min_pos = min(data)
max_pos = max(data)
fuel_consumptions = [0 for _ in range(min_pos, max_pos + 1)]

for crab in data:
    for i in range(min_pos, max_pos + 1):
        fuel = abs(crab - i)
        fuel_consumptions[i] += fuel

print("Solution for part 1:", min(fuel_consumptions))
