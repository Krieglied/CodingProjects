import re, math

with open("input.txt") as file_object:
    data = file_object.readlines()

instructions = data[0].replace("\n", "")
a_nodes = {}
nodes = {}

for index, line in enumerate(data[2:]):
    results = re.split(r"[ =\(,\)\n]+", line)
    if len(results) == 4:
        value, left_name, right_name = results[:-1]
    else:
        value, left_name, right_name = results
    nodes[value] = [value, left_name, right_name]
    if value[2] == "A":
        a_nodes[value] = nodes[value]




a_node_steps = []

for a_node, value in a_nodes.items():
    steps = 0
    instruction_index = 0
    current_node = value
    while current_node[0][2] != "Z":
        if instructions[instruction_index] == 'L':
            next_node = nodes[current_node[1]]
        else:
            next_node = nodes[current_node[2]]
        instruction_index = (instruction_index + 1) % len(instructions)
        current_node = next_node
        steps += 1
    
    a_node_steps.append(steps)

    print(f"The total number of steps for {a_node} is {steps}")

print(f"The least common multiple step is {math.lcm(*a_node_steps)}")