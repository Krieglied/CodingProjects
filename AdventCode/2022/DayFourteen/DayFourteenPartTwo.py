def insert_line(x_range, y_range, cave):
    if int(x_range[0]) == int(x_range[1]):
        min_value = min([int(y_range[0]), int(y_range[1])])
        max_value = max([int(y_range[0]), int(y_range[1])]) + 1
        for pos in range(min_value, max_value):
            cave[pos][int(x_range[0])] = '#'
    if int(y_range[0]) == int(y_range[1]):
        min_value = min([int(x_range[0]), int(x_range[1])])
        max_value = max([int(x_range[0]), int(x_range[1])]) + 1
        for pos in range(min_value, max_value):
            cave[int(y_range[0])][pos] = '#'

def drop_sand(x, y, cave):
    if y == (len(cave) - 1) and cave[y][x] == '.':
        return 'ABYSS'
    if cave[y][x] == '.':
        if cave[y + 1][x] == '#' or cave[y + 1][x] == 'o':
            if cave[y + 1][x - 1] == '.':
                return drop_sand(x - 1, y + 1, cave)
            elif cave[y + 1][x + 1] == '.':
                return drop_sand(x + 1, y + 1, cave)
            else:
                cave[y][x] = 'o'
                return 'NO MORE DOWN'
        return drop_sand(x, y + 1, cave)

data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

cave = []
x_range = [999999, -1]
y_range = [999999, -1]

for x in range(1000):
    cave_line = []
    for y in range(1000):
        cave_line.append('.')
    cave.append(cave_line)

for line in data:
    points = line.split('->')
    index = 0
    while index < (len(points) - 1):
        coords1 = points[index].strip().split(',')
        coords2 = points[index + 1].strip().split(',')
        insert_line([coords1[0], coords2[0]], [coords1[1], coords2[1]], cave)
        index += 1
        x_range[0] = min([x_range[0], int(coords1[0]), int(coords2[0])])
        x_range[1] = max([x_range[1], int(coords1[0]), int(coords2[0])])
        y_range[0] = min([y_range[0], int(coords1[1]), int(coords2[1])])
        y_range[1] = max([y_range[1], int(coords1[1]), int(coords2[1])])

del cave[y_range[1] + 3:]

for line in cave:
    del line[701:]
    del line[:301]

cave[len(cave) - 1].clear()

for length in range(len(cave[0])):
    cave[len(cave) - 1].append('#')

starting_x = 200

units_sand = 0

while True:
    if drop_sand(starting_x, 0, cave) == 'NO MORE DOWN':
        units_sand += 1
    if cave[0][starting_x] == 'o':
        break

print(units_sand)