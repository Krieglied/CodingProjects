class Tree(object):
    def __init__(self, name):
        self.name = name
        self.filesize = 0
        self.dirsize = 0
        self.children = []

def value_traverse(node):
    sum = 0
    if node.children:
        for child in node.children:
            sum += value_traverse(child)
    if (node.filesize + node.dirsize) <= 100000:
        print(f'Node {node.name} has {node.filesize} in files and {node.dirsize} in subdirectories.')
        sum += node.filesize + node.dirsize
    return sum


data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

filesize = 0
nodes = []
children = []

for line in data[::-1]:
    line_comps = line.strip().split(' ')
    if line_comps[0].isnumeric():
        filesize += int(line_comps[0])
    elif line_comps[1] == 'cd' and line_comps[2] != '..':
        new_node = Tree(line_comps[2])
        new_node.filesize = filesize
        for child in children:
            new_node.dirsize += child.filesize
            new_node.children.append(child)
            nodes.remove(child)
        nodes.append(new_node)
        filesize = 0
        children = []
    elif line_comps[0] == 'dir':
        for node in nodes:
            if node.name == line_comps[1]:
                children.append(node)
                break

print(value_traverse(nodes[0]))