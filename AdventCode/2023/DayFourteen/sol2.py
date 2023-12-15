import copy

def move_rock(row_index, col_index, dish_layout, direction):
    # North
    if direction == 0:
        x_direction = col_index 
        y_direction = row_index - 1
        bounds_check = True if y_direction >= 0 else False
    # West
    elif direction == 1:
        x_direction = col_index - 1
        y_direction = row_index
        bounds_check = True if x_direction >= 0 else False
    # South
    elif direction == 2:
        x_direction = col_index
        y_direction = row_index + 1
        bounds_check = True if y_direction < len(dish_layout) - 1 else False
    # East
    elif direction == 3:
        x_direction = col_index + 1
        y_direction = row_index
        bounds_check = True if x_direction < len(dish_layout[0]) - 1 else False
    if dish_layout[y_direction][x_direction] == "." and bounds_check:
        dish_layout[y_direction][x_direction] = "O"
        dish_layout[row_index][col_index] = "."
        move_rock(y_direction, x_direction, dish_layout, direction)

with open("test.txt") as file_object:
    data = file_object.readlines()



for index in range(len(data)):
    data[index] = list(data[index].replace("\n", ""))

og_data = copy.deepcopy(data)

for cycle in range(1000000000):
    if cycle % 1000 == 0:
        print(f"Cycle {cycle}")
    if data == og_data:
        print(cycle)
    for row_index, line in enumerate(data):
        for col_index, char in enumerate(line):
            if char == "O":
                move_rock(row_index, col_index, data, cycle % 4)

total_load = 0

for index, line in enumerate(data[::-1]):
    total_load += (index + 1) * line.count("O")

print(f"Total load is {total_load}")