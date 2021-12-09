with open('inputs/day_09.txt', mode='r') as f:
    lines = f.readlines()
    data = [[int(point) for point in list(line.strip())] for line in lines]
    print(data)
