def cover_point(diagram, x1, y1):
    if diagram[y1][x1] == ".":
        diagram[y1][x1] = 0
    diagram[y1][x1] += 1


with open("inputs/day_05.txt", "r") as text_file:
    lines = text_file.readlines()
    data = [[tuple(pair.split(",")) for pair in line.strip().split(" -> ")] for line in lines]

x_max = 0
y_max = 0
data_1 = []
for line in data:
    x_max = max(x_max, int(line[0][0]), int(line[1][0]))
    y_max = max(y_max, int(line[1][0]), int(line[1][1]))
    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        data_1.append(line)


diagram = [["." for _ in range(x_max + 1)] for _ in range(y_max + 1)]

for line in data_1:
    x1, y1 = int(line[0][0]), int(line[0][1])
    cover_point(diagram, x1, y1)
    x2, y2 = int(line[1][0]), int(line[1][1])
    while x1 != x2 or y1 != y2:
        if x1 > x2:
            x1 -= 1
        elif x1 < x2:
            x1 += 1
        elif y1 > y2:
            y1 -= 1
        elif y1 < y2:
            y1 += 1
        cover_point(diagram, x1, y1)

for line in diagram:
    print(''.join(str(point) for point in line))

number_points = sum(sum(1 for point in line if point != "." and point >= 2) for line in diagram)
print(number_points)
