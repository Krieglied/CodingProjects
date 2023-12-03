from sympy import symbols, solve

class Monkey(object):
    def __init__(self, name):
        self.name = name
        self.value = 0
        self.op = None
        self.children = []

def traverse_monkeys(monkey, branch=None):
    if monkey.name == 'humn':
        print('x', end='')
        return 1
    if monkey.op == None:
        if branch == 'branch 1':
            print(f'{monkey.value} ', end='')
        return monkey.value
    sum = 0
    if branch == 'branch 1':
        print(' ( ', end='')
    if branch == None:
        branch = 'branch 1'
        value1 = traverse_monkeys(monkey.children[0], branch)
        branch = None
    else:
        value1 = traverse_monkeys(monkey.children[0], branch)
    if branch == 'branch 1':
        print(f" {monkey.op} ", end='')
    if branch == None:
        branch = 'branch 2'
        value2 = traverse_monkeys(monkey.children[1], branch)
        branch = None
    else:
        value2 = traverse_monkeys(monkey.children[1], branch)
    if branch == 'branch 1':
        print(' ) ', end='')
    if monkey.op == '+':
        sum = value1 + value2
    elif monkey.op == '-':
        sum = value1 - value2
    elif monkey.op == '*':
        sum = value1 * value2
    elif monkey.op == '/':
        sum = value1 // value2
    elif monkey.op == "=":
        print(f'Value 1 is {value1}, Value 2 is {value2}')
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
        if line_comps[0][:-1] == 'root':
            new_monkey.op = '='
        else:
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

#x = symbols('x')
#expr = " (  (  ( 2  *  (  (  101381294475907  )  -  (  (  (  (  ( 2  *  (  (  (  (  (  (  781  )  +  (  (  (  (  ( 18  )  *  (  (  (  (  (  (  222  )  +  (  (  (  (  ( 2  *  (  (  (  ( 4  *  (  ( 453  )  +  (  (  (  (  ( 3  *  (  (  (  (  (  ( 2  *  (  ( 8  )  +  (  (  (  (  (  (  (  114  )  +  (  (  (  (  ( 2  *  (  ( 3  *  (  (  (  (  (  (  536  )  +  (  ( x -  (  375  )  )  *  (  29  )  )  )  / 2  )  +  (  670  )  )  / 3  )  -  (  304  )  )  )  +  ( 52  )  )  )  -  (  480  )  )  / 5  )  -  (  978  )  )  * 3  )  )  /  ( 9  )  )  -  ( 78  )  )  / 3  )  +  ( 291  )  )  * 16  )  )  )  -  (  30  )  )  / 2  )  -  (  181  )  )  / 4  )  +  (  567  )  )  )  -  ( 965  )  )  * 2  )  +  (  830  )  )  / 2  )  )  )  -  (  227  )  )  / 3  )  +  (  628  )  )  )  -  (  993  )  )  / 3  )  -  (  825  )  )  * 2  )  )  / 2  )  -  (  244  )  )  / 5  )  +  ( 204  )  )  )  -  (  155  )  )  +  (  74  )  )  / 3  )  )  * 2  )  +  (  187  )  )  / 3  )  -  (  136  )  )  )  +  (  553  )  )  / 3  )  -  483  )  * 4  )  )  )  +  (  358  )  )  / 4  )"
#sol = solve(expr)

#print(sol[0])
print(2976808259026882988 - 480)