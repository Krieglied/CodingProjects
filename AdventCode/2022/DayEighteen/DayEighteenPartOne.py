class Cube(object):
    def __init__(self, pos):
        self.pos = pos
        self.neighbors = []


def find_index(cubes, pos):
    for index, cube in enumerate(cubes):
        if cube.pos == pos:
            return index

data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

cubes = []

for index, line in enumerate(data):
    x, y, z = line.split(',')
    new_cube = Cube((int(x),int(y),int(z)))
    if ','.join([str(int(x) + 1), y, z]) in data[:index]:
        current_cube = cubes[find_index(cubes, (int(x) + 1, int(y), int(z)))]
        current_cube.neighbors.append(new_cube)
        new_cube.neighbors.append(current_cube)
    if ','.join([str(int(x) - 1), y, z]) in data[:index]:
        current_cube = cubes[find_index(cubes, (int(x) - 1, int(y), int(z)))]
        current_cube.neighbors.append(new_cube)
        new_cube.neighbors.append(current_cube)
    if ','.join([x, str(int(y) + 1), z]) in data[:index]:
        current_cube = cubes[find_index(cubes, (int(x), int(y) + 1, int(z)))]
        current_cube.neighbors.append(new_cube)
        new_cube.neighbors.append(current_cube)
    if ','.join([x, str(int(y) - 1), z]) in data[:index]:
        current_cube = cubes[find_index(cubes, (int(x), int(y) - 1, int(z)))]
        current_cube.neighbors.append(new_cube)
        new_cube.neighbors.append(current_cube)
    if ','.join([x, y, str(int(z) + 1)]) in data[:index]:
        current_cube = cubes[find_index(cubes, (int(x), int(y), int(z) + 1))]
        current_cube.neighbors.append(new_cube)
        new_cube.neighbors.append(current_cube)
    if ','.join([x, y, str(int(z) - 1)]) in data[:index]:
        current_cube = cubes[find_index(cubes, (int(x), int(y), int(z) - 1))]
        current_cube.neighbors.append(new_cube)
        new_cube.neighbors.append(current_cube)
    cubes.append(new_cube)

surface_area = 0

for cube in cubes:
    surface_area += 6 - len(cube.neighbors)

print(surface_area)