with open("input.txt") as file_object:
    data = file_object.readlines()

grid = []

for line in data:
    grid_line = ["."] * len(line)
    grid.append(grid_line)

start_pos = []

for index, line in enumerate(data):
    x_pos = line.find("S")
    if x_pos != -1:
        start_pos = [x_pos, index]
        grid[index][x_pos] = "#"
        break

new_pos = [0, 0]
next_action = ""

for tile in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
    if start_pos[0] + tile[0] < 0 or start_pos[0] + tile[0] > len(data[0]) or start_pos[1] + tile[1] < 0 or start_pos[1] + tile[1] > len(data):
        continue
    elif tile == (0, -1) and data[start_pos[1] + tile[1]][start_pos[0] + tile[0]] in "F|7":
        next_action = data[start_pos[1] + tile[1]][start_pos[0] + tile[0]]
        new_pos = [start_pos[0] + tile[0], start_pos[1] + tile[1]]
        direction = "N"
        break
    elif tile == (1, 0) and data[start_pos[1] + tile[1]][start_pos[0] + tile[0]] in "-7J":
        next_action = data[start_pos[1] + tile[1]][start_pos[0] + tile[0]]
        new_pos = [start_pos[0] + tile[0], start_pos[1] + tile[1]]
        direction = "E"
        break
    elif tile == (0, 1) and data[start_pos[1] + tile[1]][start_pos[0] + tile[0]] in "L|J":
        next_action = data[start_pos[1] + tile[1]][start_pos[0] + tile[0]]
        new_pos = [start_pos[0] + tile[0], start_pos[1] + tile[1]]
        direction = "S"
        break
    elif tile == (-1, 0) and data[start_pos[1] + tile[1]][start_pos[0] + tile[0]] in "-FL":
        next_action = data[start_pos[1] + tile[1]][start_pos[0] + tile[0]]
        new_pos = [start_pos[0] + tile[0], start_pos[1] + tile[1]]
        direction = "W"
        break

actions = [next_action]
prev_action = "S"
grid[new_pos[1]][new_pos[0]] = "#"

while tuple(new_pos) != tuple(start_pos):
    if next_action == "|":
        if direction == "N":
            new_pos[1] -= 1
        elif direction == "S":
            new_pos[1] += 1
    elif next_action == "-":
        if direction == "W":
            new_pos[0] -= 1
        elif direction == "E":
            new_pos[0] += 1
    elif next_action == "F":
        if direction == "N":
            new_pos[0] += 1
            direction = "E"
        elif direction == "W":
            new_pos[1] += 1
            direction = "S"
    elif next_action == "7":
        if direction == "E":
            new_pos[1] += 1
            direction = "S"
        elif direction == "N":
            new_pos[0] -= 1
            direction = "W"
    elif next_action == "L":
        if direction == "S":
            new_pos[0] += 1
            direction = "E"
        elif direction == "W":
            new_pos[1] -= 1
            direction = "N"
    elif next_action == "J":
        if direction == "E":
            new_pos[1] -= 1
            direction = "N"
        elif direction == "S":
            new_pos[0] -= 1
            direction = "W"
    grid[new_pos[1]][new_pos[0]] = "#"
    next_action = data[new_pos[1]][new_pos[0]]
    actions.append(next_action)

with open("grids.txt", "w") as file_object:
    for grid_line in grid:
        line = "".join(grid_line) + "\n"
        file_object.write(line)

print(f"The max distance is {len(actions) // 2}")