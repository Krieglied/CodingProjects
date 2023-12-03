data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

sum = 0
prev_dir = ' '
prev_amount = 0

for line in data:
    direction, amount = line.strip().split(' ')
    if (direction in 'LR' and prev_dir not in 'LR') or (direction in 'UD' and prev_dir not in 'UD'):
        sum += int(amount) - 1
    if (direction in 'LR' and prev_dir in 'UD') or (direction in 'UD' and prev_dir in 'LR'):
        if int(prev_amount) == 1:
            sum -= 1
    prev_dir = direction
    prev_amount = amount

print(sum)