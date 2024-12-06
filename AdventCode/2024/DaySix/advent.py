import sys
sys.setrecursionlimit(7000)

with open('input.txt') as file_object:
    data = file_object.readlines()

directions = "^>v<"
direction = "^"
start = 0

new_data = []
for line in data:
    new_line = list(line.strip())
    new_data.append(new_line)

data = new_data

for lindex in range(len(data)):
    for index in range(len(data[lindex])):
        if data[lindex][index] == "^":
            start = (lindex, index)
            break

def move_guard(pos, direction):
    global data

    if direction == "^":
        if pos[0] - 1 < 0:
            data[pos[0]][pos[1]] = "X"
            return
        if data[pos[0] - 1][pos[1]] in [".", "X"]:
            data[pos[0]][pos[1]] = "X"
            move_guard((pos[0] - 1, pos[1]), direction)
        elif data[pos[0] - 1][pos[1]] == "#":
            direction = ">"
            move_guard((pos[0], pos[1]), direction)
    elif direction == ">":
        if pos[1] + 1 >= len(data[0]):
            data[pos[0]][pos[1]] = "X"
            return
        if data[pos[0]][pos[1] + 1] in [".", "X"]:
            data[pos[0]][pos[1]] = "X"
            move_guard((pos[0], pos[1] + 1), direction)
        elif data[pos[0]][pos[1] + 1] == "#":
            direction = "v"
            move_guard((pos[0], pos[1]), direction)
    elif direction == "v":
        if pos[0] + 1 >= len(data):
            data[pos[0]][pos[1]] = "X"
            return
        if data[pos[0] + 1][pos[1]] in [".", "X"]:
            data[pos[0]][pos[1]] = "X"
            move_guard((pos[0] + 1, pos[1]), direction)
        elif data[pos[0] + 1][pos[1]] == "#":
            direction = "<"
            move_guard((pos[0], pos[1]), direction)
    elif direction == "<":
        if pos[1] - 1 < 0:
            data[pos[0]][pos[1]] = "X"
            return
        if data[pos[0]][pos[1] - 1] in [".", "X"]:
            data[pos[0]][pos[1]] = "X"
            move_guard((pos[0], pos[1] - 1), direction)
        elif data[pos[0]][pos[1] - 1] == "#":
            direction = "^"
            move_guard((pos[0], pos[1]), direction)

total = 0
move_guard(start, data[start[0]][start[1]])

for line in data:
    total += line.count("X")

print(f"TOTAL NUMBER OF MOVES: {total}")