with open("inputs/day_08.txt", "r") as text_file:
    lines = text_file.readlines()
    data = []
    for line in lines:
        patterns, output = line.strip().split("|")
        patterns = patterns.split()
        output = output.split()
        data.append([patterns, output])

    for line in data:
        print(line)

# 0:
# 1:
# 2:
# 3:
# 4:
# 5:
# 6:
# 7:
# 8:
# 9:
