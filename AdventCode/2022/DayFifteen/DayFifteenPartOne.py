data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

not_pos = []
not_line = 2000001

for line in data:
    split_line = line.strip().split(' ')
    sensor = [int(split_line[2][2:-1]), int(split_line[3][2:-1])]
    beacon = [int(split_line[8][2:-1]), int(split_line[9][2:])]
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    if not_line in range(sensor[1] - distance, sensor[1] + distance + 1):
        range_value = 0
        if not_line > sensor[1]:
            range_value = sensor[1] + distance - not_line
        elif not_line < sensor[1]:
            range_value = abs(sensor[1] - distance - not_line)
        for x in range(sensor[0] - range_value, sensor[0] + range_value + 1):
            not_pos.append(x)
    if beacon[1] == not_line:
        not_pos.remove(beacon[0])

print(len(set(not_pos)))