class Tree(object):
    def __init__(self, name):
        self.name = name
        self.filesize = 0
        self.dirsize = 0
        self.children = []

def value_traverse(node, min_size):
    mins = []
    if node.children:
        for child in node.children:
            if (child.filesize + child.dirsize > min_size):
                mins.append(child.filesize + child.dirsize)
                mins.extend(value_traverse(child, min_size))
    return mins


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
            new_node.dirsize += child.filesize + child.dirsize
            new_node.children.append(child)
            nodes.remove(child)
        nodes.append(new_node)
        filesize = 0
        children = []
    elif line_comps[0] == 'dir':
        for node in nodes[::-1]:
            if node.name == line_comps[1]:
                children.append(node)
                break

taken_space = 70000000 - nodes[0].dirsize - nodes[0].filesize
minimum_size = 30000000 - taken_space
values = value_traverse(nodes[0], minimum_size)
print(min(values))