data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

stack_line = 0
stacks = 0
list_stacks = []
actions_line = 0

while True:
    if data[stack_line].strip()[0].isnumeric():
        num_stacks = data[stack_line].strip().split(' ')
        stacks = int(num_stacks[-1])
        actions_line = stack_line + 2
        stack_line -= 1
        break
    stack_line += 1

for x in range(stacks):
    list_stacks.append(list())

while stack_line > -1:
    start_data = 1
    for x in range(stacks):
        if data[stack_line][start_data].isalpha():
            list_stacks[x].append(data[stack_line][start_data])
        start_data += 4
    stack_line -= 1

for line in data[actions_line:]:
    actions = line.strip().split(' ')
    amount = int(actions[1])
    src = int(actions[3]) - 1
    dst = int(actions[5]) - 1
    for x in range(amount):
        list_stacks[dst].append(list_stacks[src].pop())

for x in list_stacks:
    print(x[-1], end='')