with open("inputs/day_02.txt", "r") as text_file:
    lines = text_file.readlines()
    for line in lines:
        print(line.split())
    data = [(line.split()[0], int(line.split()[1])) for line in lines]


horizontal_pos = 0
depth = 0
for line in data:
    if line[0] == "forward":
        horizontal_pos += line[1]
    elif line[0] == "up":
        depth -= line[1]
    elif line[0] == "down":
        depth += line[1]

print(horizontal_pos, depth, horizontal_pos*depth)


horizontal_pos = 0
depth = 0
aim = 0
for line in data:
    if line[0] == "forward":
        horizontal_pos += line[1]
        depth += aim * line[1]
    elif line[0] == "up":
        aim -= line[1]
    elif line[0] == "down":
        aim += line[1]

print(horizontal_pos, depth, horizontal_pos*depth)
