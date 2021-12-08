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

ones = 0
fours = 0
sevens = 0
heights = 0
for line in data:
    for digit in line[1]:
        if len(digit) == 2:
            ones += 1
        elif len(digit) == 4:
            fours += 1
        elif len(digit) == 3:
            sevens += 1
        elif len(digit) == 7:
            heights += 1

occurences = ones + fours + sevens + heights
print("Solution for part 1:", occurences)

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
