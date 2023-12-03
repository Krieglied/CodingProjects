def process_line(line_num):
    not_pos = []
    for line in data:
        split_line = line.strip().split(' ')
        sensor = [int(split_line[2][2:-1]), int(split_line[3][2:-1])]
        beacon = [int(split_line[8][2:-1]), int(split_line[9][2:])]
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        if line_num in range(sensor[1] - distance, sensor[1] + distance + 1):
            range_value = 0
            if line_num > sensor[1]:
                range_value = sensor[1] + distance - line_num
            elif line_num < sensor[1]:
                range_value = abs(sensor[1] - distance - line_num)
            for x in range(sensor[0] - range_value, sensor[0] + range_value + 1):
                not_pos.append(x)
    not_pos.sort()
    min_index, max_index = 0, 0
    for index, item in enumerate(not_pos):
        if item >= 0:
            min_index = index
            break
    for index, item in enumerate(not_pos[::-1]):
        if item <= 20:
            max_index = index + 1
            break
    return set(not_pos[min_index:-max_index])
    

data = []
lines = {}

with open('./test.txt', 'r') as file_object:
    data = file_object.read().splitlines()


for y in range(21):
    curr_line = list(process_line(y))
    print(len(curr_line))
    if len(curr_line) == 19:
        lines[y] = curr_line
