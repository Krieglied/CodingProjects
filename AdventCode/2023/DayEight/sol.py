import re

with open("input.txt") as file_object:
    data = file_object.readlines()

instructions = data[0].replace("\n", "")
nodes = {}

for index, line in enumerate(data[2:]):
    results = re.split(r"[ =\(,\)\n]+", line)
    if len(results) == 4:
        value, left_name, right_name = results[:-1]
    else:
        value, left_name, right_name = results
    nodes[value] = [value, left_name, right_name]
    if value == "AAA":
        current_node = nodes[value]

steps = 0
instruction_index = 0

while current_node[0] != "ZZZ":
    if instructions[instruction_index] == 'L':
        next_node = nodes[current_node[1]]
    else:
        next_node = nodes[current_node[2]]
    instruction_index = (instruction_index + 1) % len(instructions)
    current_node = next_node
    steps += 1

print(f"The total number of steps is {steps}")