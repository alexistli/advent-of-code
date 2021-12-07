with open("inputs/day_07.txt", "r") as text_file:
    line = text_file.readline()
    data = [int(pos) for pos in line.strip().split(",")]

min_pos = min(data)
max_pos = max(data)


# ================ Part 1 ================
fuel_consumptions = [0 for _ in range(min_pos, max_pos + 1)]

for crab in data:
    for i in range(min_pos, max_pos + 1):
        fuel = abs(crab - i)
        fuel_consumptions[i] += fuel

print("Solution for part 1:", min(fuel_consumptions))

# ================ Part 2 ================
# step 0: 0 + 0 = 0
# step 1: 0 + 1 = 1
# step 2: 1 + 2 = 3
# step 3: 3 + 3 = 6
# step 4: 6 + 4 = 10
# step 5: 10 + 5 = 15

# cost = previous + step
# cost(n) = cost(n - 1) + n
#         = cost(n - 2) + (n - 1) + n
#         = cost(n - 3) + (n - 2) + (n - 1) + n

# Hypothesis:
# cost(n) = n * (n + 1) / 2

# Verification:
# cost(0) = 0 * (0 + 1) / 2 = 6
# cost(1) = 1 * (1 + 1) / 2 = 1
# cost(4) = 4 * (4 + 1) / 2 = 4 * 5 / 2 = 10
# cost(5) = 5 * (5 + 1) / 2 = 5 * 6 / 2 = 15

fuel_consumptions = [0 for _ in range(min_pos, max_pos + 1)]

for crab in data:
    for i in range(min_pos, max_pos + 1):
        n = abs(crab - i)
        fuel = n * (n + 1) // 2
        fuel_consumptions[i] += fuel

print("Solution for part 2:", min(fuel_consumptions))
