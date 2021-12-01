with open("inputs/day_01.txt", "r") as text_file:
    data = [int(line) for line in text_file.readlines()]

result = sum(1 for i in range(1, len(data)) if data[i] > data[i - 1])
print(result)

