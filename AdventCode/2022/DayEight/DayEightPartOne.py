def check_visible(current_line, current_pos, direction, check_value):
    if int(check_value) > int(data[current_line][current_pos]):
        if current_line == 0 or current_pos == 0 or current_line == (len(data) - 1) or current_pos == (len(data) - 1):
            return True
        if direction == 'L':
            return check_visible(current_line, current_pos - 1, direction, check_value)
        elif direction == 'R':
            return check_visible(current_line, current_pos + 1, direction, check_value)
        elif direction == 'U':
            return check_visible(current_line - 1, current_pos, direction, check_value)
        elif direction == 'D':
            return check_visible(current_line + 1, current_pos, direction, check_value)
    return False

data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

directions = ['L','R','U','D']
num_visible = 0

for line_num, line in enumerate(data):
    for char_num, char in enumerate(line):
        if line_num == 0 or char_num == 0 or line_num == (len(data) - 1) or char_num == (len(data) - 1):
            num_visible += 1
            continue
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
        for dir in process_order:
            if dir == 'L' and check_visible(line_num, char_num - 1, dir, char):
                num_visible += 1
                break
            if dir == 'R' and check_visible(line_num, char_num + 1, dir, char):
                num_visible += 1
                break
            if dir == 'U' and check_visible(line_num - 1, char_num, dir, char):
                num_visible += 1
                break
            if dir == 'D' and check_visible(line_num + 1, char_num, dir, char):
                num_visible += 1
                break

print(num_visible)