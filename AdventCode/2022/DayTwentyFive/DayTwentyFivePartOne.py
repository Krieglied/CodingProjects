data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

sum = 0
max_digit = 1

for line in data:
    digit = 1
    num_sum = 0
    for char in line[::-1]:
        if char.isnumeric():
            num_sum += int(char) * digit
        if char == '=':
            num_sum += -2 * digit
        if char == '-':
            num_sum += -1 * digit
        digit *= 5
    sum += num_sum

print(sum)
#sum = 107 + 2

digit = 1

while digit < sum:
    digit *= 5

max_value = 2 * digit
digit //= 5
output_string = ''

while sum > 0:
    if sum <= 2:
        output_string = str(sum)
        sum = 0
    place_value = sum % digit
    if place_value == 5:
        output_string += '2'
    elif place_value == 4:
        output_string += '1'
    elif place_value == 3:
        output_string += '0'
    elif place_value == 2:
        output_string += '-'
    elif place_value == 1:
        output_string += '='
    sum //= digit
    digit //= 5