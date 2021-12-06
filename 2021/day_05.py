def cover_point(diagram, x1, y1):
    if diagram[y1][x1] == ".":
        diagram[y1][x1] = 0
    diagram[y1][x1] += 1


def create_diagram(data):
    x_max = 0
    y_max = 0
    for line in data:
        for point in line:
            x_max = max(x_max, point[0])
            y_max = max(y_max, point[1])
    diagram = [["." for _ in range(x_max + 1)] for _ in range(y_max + 1)]

    for line in data_1:
        x1, y1 = int(line[0][0]), int(line[0][1])
        cover_point(diagram, x1, y1)
        x2, y2 = int(line[1][0]), int(line[1][1])
        while x1 != x2 or y1 != y2:
            if x1 != x2:
                x1 += 1 if x1 < x2 else -1
            if y1 != y2:
                y1 += 1 if y1 < y2 else -1
            cover_point(diagram, x1, y1)
    return diagram


with open("inputs/day_05.txt", "r") as text_file:
    lines = text_file.readlines()
    data = []

    for line in lines:
        data_row = []
        for pair in line.strip().split(" -> "):
            x, y = pair.split(",")
            row_pair = (int(x), int(y))
            data_row.append(row_pair)
        data.append(data_row)


data_1 = [line for line in data if line[0][0] == line[1][0] or line[0][1] == line[1][1]]
diagram_1 = create_diagram(data_1)

for line in diagram_1:
    print(''.join(str(point) for point in line))

number_points = sum(sum(1 for point in line if point != "." and point >= 2) for line in diagram_1)
print(number_points)
