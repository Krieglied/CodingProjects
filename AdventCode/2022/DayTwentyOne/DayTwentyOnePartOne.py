class Monkey(object):
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.op = None
        self.children = []

def traverse_monkeys(monkey):
    if monkey.op == None:
        return monkey.value
    sum = 0
    value1 = traverse_monkeys(monkey.children[0])
    value2 = traverse_monkeys(monkey.children[1])
    if monkey.op == '+':
        sum = value1 + value2
    elif monkey.op == '-':
        sum = value1 - value2
    elif monkey.op == '*':
        sum = value1 * value2
    elif monkey.op == '/':
        sum = value1 // value2    
    return sum


data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

monkeys = []
root_index = -1

for index, line in enumerate(data):
    line_comps = line.split(' ')
    new_monkey = Monkey(line_comps[0][:-1])
    if line_comps[0][:-1] == 'root':
        root_index = index
    if line_comps[1].isnumeric():
        new_monkey.value = int(line_comps[1])
    else:
        new_monkey.children.append(line_comps[1])
        new_monkey.op = line_comps[2]
        new_monkey.children.append(line_comps[3])
    monkeys.append(new_monkey)

for monkey in monkeys:
    if monkey.children:
        for x in range(len(monkey.children)):
            name = monkey.children.pop(0)
            for other_monkey in monkeys:
                if other_monkey.name == name:
                    monkey.children.append(other_monkey)
                    break

print(traverse_monkeys(monkeys[root_index]))