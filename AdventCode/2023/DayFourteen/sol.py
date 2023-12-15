def move_rock(row_index, col_index, dish_layout):
    if dish_layout[row_index - 1][col_index] == "." and row_index - 1 >= 0:
        dish_layout[row_index - 1][col_index] = "O"
        dish_layout[row_index][col_index] = "."
        move_rock(row_index - 1, col_index, dish_layout)

with open("input.txt") as file_object:
    data = file_object.readlines()

for index in range(len(data)):
    data[index] = list(data[index])

for row_index, line in enumerate(data):
    for col_index, char in enumerate(line):
        if char == "O":
            move_rock(row_index, col_index, data)

total_load = 0

for index, line in enumerate(data[::-1]):
    total_load += (index + 1) * line.count("O")

print(f"Total load is {total_load}")