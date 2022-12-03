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


# ================ Part 2 ================


def unseen_neighbours(i, j, grid, seen):
    neighbours = {}
    up = (i - 1, j)
    down = (i + 1, j)
    left = (i, j - 1)
    right = (i, j + 1)

    x, y = up
    if x >= 0 and up not in seen:
        neighbours.update({up: grid[x][y]})
        seen.add(up)

    x, y = down
    if x <= len(grid) - 1 and down not in seen:
        neighbours.update({down: grid[x][y]})
        seen.add(down)

    x, y = left
    if y >= 0 and left not in seen:
        neighbours.update({left: grid[x][y]})
        seen.add(left)

    x, y = right
    if y <= len(grid[0]) - 1 and right not in seen:
        neighbours.update({right: grid[x][y]})
        seen.add(right)
    return neighbours


basins = []
for coord, point in low_points.items():
    current_basin = []
    points_to_visit = {coord: point}
    seen_points = {coord}

    # Visit the smallest point
    while points_to_visit:
        smallest_coords = min(points_to_visit, key=lambda x: x[1])
        smallest_value = points_to_visit.pop(smallest_coords)

        if smallest_value == 9:
            continue

        current_basin.append(smallest_value)

        # Identify current unseen neighbours and add to list
        i, j = smallest_coords
        neighbours = unseen_neighbours(i, j, data, seen_points)
        points_to_visit.update(neighbours)

    basins.append(current_basin)

three_largest = []
for basin in basins:
    if len(three_largest) < 3:
        three_largest.append(len(basin))
        continue

    three_largest.sort()
    if len(basin) > three_largest[0]:
        three_largest[0] = len(basin)

product_three_largest = three_largest[0] * three_largest[1] * three_largest[2]
print("Solution for part 2:", product_three_largest)

