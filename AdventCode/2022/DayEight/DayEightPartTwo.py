def check_visible(current_line, current_pos, direction, check_value):
    if int(check_value) > int(data[current_line][current_pos]):
        if current_line == 0 or current_pos == 0 or current_line == (len(data) - 1) or current_pos == (len(data) - 1):
            return 1
        if direction == 'L':
            return 1 + check_visible(current_line, current_pos - 1, direction, check_value)
        elif direction == 'R':
            return 1 + check_visible(current_line, current_pos + 1, direction, check_value)
        elif direction == 'U':
            return 1 + check_visible(current_line - 1, current_pos, direction, check_value)
        elif direction == 'D':
            return 1 + check_visible(current_line + 1, current_pos, direction, check_value)
    return 1

data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

directions = ['L','R','U','D']
best_scenic_score = 0

for line_num, line in enumerate(data):
    for char_num, char in enumerate(line):
        process_order = []
        if line_num < (len(data) // 2):
            process_order.append('U')
            directions.remove('U')
        else:
            process_order.append('D')
            directions.remove('D')
        if char_num < (len(line) // 2):
            process_order.append('L')
            directions.remove('L')
        else:
            process_order.append('R')
            directions.remove('R')
        process_order.extend(directions)
        directions = ['L','R','U','D']
        scores = [0, 0, 0, 0]
        for dir in process_order:
            if dir == 'L':
                if char_num == 0:
                    scores[0] = 0
                else:
                    scores[0] = check_visible(line_num, char_num - 1, dir, char)
            if dir == 'R':
                if char_num == (len(line) - 1):
                    scores[1] = 0
                else:
                    scores[1] = check_visible(line_num, char_num + 1, dir, char)
            if dir == 'U':
                if line_num == 0:
                    scores[2] = 0
                else:
                    scores[2] = check_visible(line_num - 1, char_num, dir, char)
            if dir == 'D':
                if line_num == (len(data) - 1):
                    scores[3] = 0
                else:
                    scores[3] = check_visible(line_num + 1, char_num, dir, char)
        if (scores[0] * scores[1] * scores[2] * scores[3]) > best_scenic_score:
            best_scenic_score = scores[0] * scores[1] * scores[2] * scores[3]

print(best_scenic_score)