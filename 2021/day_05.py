with open("inputs/day_05.txt", "r") as text_file:
    lines = text_file.readlines()
    data = [[tuple(pair.split(",")) for pair in line.strip().split(" -> ")] for line in lines]

for line in data:
    print(line)
