class Monkey(object):
    def __init__(self, items, op, test, true_op, false_op):
        self.items = items
        self.op = op
        self.test = test
        self.true_op = true_op
        self.false_op = false_op
        self.inspections = 0


data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

line_num = 0
monkeys = []

while line_num < len(data):
    line_num += 1
    items = []
    for element in data[line_num].split(' '):
        if ',' in element:
            if element[:-1].isnumeric():
                items.append(int(element[:-1]))
        if element.isnumeric():
            items.append(int(element))
    line_num += 1
    op_line = data[line_num].split(' ')
    op = [data[line_num].split(' ')[6], data[line_num].split(' ')[7]]
    line_num += 1
    test = int(data[line_num].split(' ')[5])
    line_num += 1
    true_op = int(data[line_num].split(' ')[9])
    line_num += 1
    false_op = int(data[line_num].split(' ')[9])
    new_monkey = Monkey(items, op, test, true_op, false_op)
    monkeys.append(new_monkey)
    line_num += 2

index = 0
test_values = []

while index < len(monkeys):
    test_values.append(monkeys[index].test)
    index += 1

lcm = max(test_values)

while True:
    if all(lcm % item == 0 for item in test_values):
        break
    lcm += 1

MAX_ROUNDS = 10000
round = 0

while round < MAX_ROUNDS:
    for monkey in monkeys:
        for item in monkey.items:
            worry_level = item
            monkey.inspections += 1
            if monkey.op[0] == '*':
                if monkey.op[1] == 'old':
                    worry_level *= worry_level
                else:
                    worry_level *= int(monkey.op[1])
            elif monkey.op[0] == '+':
                worry_level += int(monkey.op[1])
            worry_level %= lcm
            if worry_level % monkey.test == 0:
                monkeys[monkey.true_op].items.append(worry_level)
            else:
                monkeys[monkey.false_op].items.append(worry_level)
        monkey.items = []
    round += 1

inspections = []

for monkey in monkeys:
    inspections.append(monkey.inspections)

print(sorted(inspections, reverse=True)[0] * sorted(inspections, reverse=True)[1])