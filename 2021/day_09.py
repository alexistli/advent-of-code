with open('inputs/day_09.txt', mode='r') as f:
    lines = f.readlines()
    data = [[int(point) for point in list(line.strip())] for line in lines]


# ================ Part 1 ================
low_points = {}
for i, row in enumerate(data):
    for j, point in enumerate(row):
        adjacent_up = data[i - 1][j] if i - 1 >= 0 else float('+inf')
        adjacent_down = data[i + 1][j] if i + 1 <= len(data) - 1 else float('+inf')
        adjacent_left = data[i][j - 1] if j - 1 >= 0 else float('+inf')
        adjacent_right = data[i][j + 1] if j + 1 <= len(data[0]) - 1 else float('+inf')
        if point < min(adjacent_up, adjacent_down, adjacent_left, adjacent_right):
            low_points[(i, j)] = point
total_risk_level = sum(point + 1 for point in low_points.values())
print("Solution for part 1:", total_risk_level)

