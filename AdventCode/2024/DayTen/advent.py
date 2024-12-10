with open('input.txt') as file_object:
    data = file_object.readlines()

new_data = []
for line in data:
    new_data.append(line.strip())

data = new_data

def find_max_height(pos, value):
    
    total = []
    if value == 9:
        return [pos]
    # N
    if pos[0] > 0:
        if int(data[pos[0] - 1][pos[1]]) == value + 1:
            total.extend(find_max_height((pos[0] - 1, pos[1]), value + 1))
    # S
    if pos[0] < len(data) - 1:
        if int(data[pos[0] + 1][pos[1]]) == value + 1:
            total.extend(find_max_height((pos[0] + 1, pos[1]), value + 1))
    # W
    if pos[1] > 0:
        if int(data[pos[0]][pos[1] - 1]) == value + 1:
            total.extend(find_max_height((pos[0], pos[1] - 1), value + 1))
    # E
    if pos[1] < len(data[0]) - 1:
        if int(data[pos[0]][pos[1] + 1]) == value + 1:
            total.extend(find_max_height((pos[0], pos[1] + 1), value + 1))
    return total

total = 0 

for lindex, line in enumerate(data):
    for index, char in enumerate(line):
        if char == "0":
            total += len(set(find_max_height((lindex, index), 0) ))

print(f"TOTAL SUM OF TRAILHEADS: {total}")

trailheads = []

def find_unique_max_height(pos, value, trail):
    global trailheads

    total = []
    if value == 9:
        trail.append(pos)
        trailheads.append(trail)
        return trail
    # N
    if pos[0] > 0:
        if int(data[pos[0] - 1][pos[1]]) == value + 1:
            new_trail1 = trail + [pos]
            total.append(find_unique_max_height((pos[0] - 1, pos[1]), value + 1, new_trail1))
    # S
    if pos[0] < len(data) - 1:
        if int(data[pos[0] + 1][pos[1]]) == value + 1:
            new_trail2 = trail + [pos]
            total.append(find_unique_max_height((pos[0] + 1, pos[1]), value + 1, new_trail2))
    # W
    if pos[1] > 0:
        if int(data[pos[0]][pos[1] - 1]) == value + 1:
            new_trail3 = trail + [pos]
            total.append(find_unique_max_height((pos[0], pos[1] - 1), value + 1, new_trail3))
    # E
    if pos[1] < len(data[0]) - 1:
        if int(data[pos[0]][pos[1] + 1]) == value + 1:
            new_trail4 = trail + [pos]
            total.append(find_unique_max_height((pos[0], pos[1] + 1), value + 1, new_trail4))

for lindex, line in enumerate(data):
    for index, char in enumerate(line):
        if char == "0":
            find_unique_max_height((lindex, index), 0, [])

print(f"TOTAL SUM OF UNIQUE TRAILHEAD PATH: {len(trailheads)}")