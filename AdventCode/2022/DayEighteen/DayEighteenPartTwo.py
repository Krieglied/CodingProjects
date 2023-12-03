class Cube(object):
    def __init__(self, pos):
        self.pos = pos
        self.type = 'Air'
        self.neighbors = []


def find_index(cubes, pos):
    for index, cube in enumerate(cubes):
        if cube.pos == pos:
            return index

def add_neighbors(index, cubes, cube, pos):
    if index == None:
        new_cube = Cube(pos)
        cube.neighbors.append(new_cube)
        new_cube.neighbors.append(cube)
        cubes.append(new_cube)
    elif find_index(cube.neighbors, pos) == None:
        curr_cube = cubes[index]
        curr_cube.neighbors.append(cube)
        cube.neighbors.append(curr_cube)

def create_neighbors(cubes, cube):
    x, y, z = cube.pos
    add_neighbors(find_index(cubes, (x + 1, y, z)), cubes, cube, (x + 1, y, z))
    add_neighbors(find_index(cubes, (x - 1, y, z)), cubes, cube, (x - 1, y, z))
    add_neighbors(find_index(cubes, (x, y + 1, z)), cubes, cube, (x, y + 1, z))
    add_neighbors(find_index(cubes, (x, y - 1, z)), cubes, cube, (x, y - 1, z))
    add_neighbors(find_index(cubes, (x, y, z + 1)), cubes, cube, (x, y, z + 1))
    add_neighbors(find_index(cubes, (x, y, z - 1)), cubes, cube, (x, y, z - 1))

data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read().splitlines()

cubes = []

for index, line in enumerate(data):
    x, y, z = line.split(',')
    curr_index = find_index(cubes, (int(x), int(y), int(z)))
    if curr_index:
        current_cube = cubes[curr_index]
    else:
        current_cube = Cube((int(x), int(y), int(z)))
        cubes.append(current_cube)
    current_cube.type = 'Lava'
    if len(current_cube.neighbors) < 6:
        create_neighbors(cubes, current_cube)

surface_area = 0
internal_cubes = []

for cube in cubes:
    cube_pos = cube.pos
    if cube.type == 'Lava' and cube not in internal_cubes:
        for neighbor in cube.neighbors:
            if neighbor.type == 'Air':
                x, y, z = None, None, None
                if neighbor.pos[0] > cube.pos[0]:
                    x = 2
                elif neighbor.pos[0] < cube.pos[0]:
                    x = -2
                if neighbor.pos[1] > cube.pos[1]:
                    y = 2
                elif neighbor.pos[1] < cube.pos[1]:
                    y = -2
                if neighbor.pos[2] > cube.pos[2]:
                    z = 2
                elif neighbor.pos[2] < cube.pos[2]:
                    z = -2
                end_cube = False
                for other_cube in cubes:
                    other_pos = other_cube.pos
                    if x and x > 0 and other_cube.pos != cube.pos:
                        if (other_cube.pos[0] + x) > cube.pos[0] and other_cube.pos[1] == cube.pos[1] and other_cube.pos[2] == cube.pos[2]:
                            internal_cubes.append(cube)
                            internal_cubes.append(other_cube)
                            end_cube = True
                            break
                    if x and x < 0 and other_cube.pos != cube.pos:
                        if (other_cube.pos[0] + x) < cube.pos[0] and other_cube.pos[1] == cube.pos[1] and other_cube.pos[2] == cube.pos[2]:
                            internal_cubes.append(cube)
                            internal_cubes.append(other_cube)
                            end_cube = True
                            break
                    if y and y > 0 and other_cube.pos != cube.pos:
                        if (other_cube.pos[1] + y) > cube.pos[1] and other_cube.pos[0] == cube.pos[0] and other_cube.pos[2] == cube.pos[2]:
                            internal_cubes.append(cube)
                            internal_cubes.append(other_cube)
                            end_cube = True
                            break
                    if y and y < 0 and other_cube.pos != cube.pos:
                        if (other_cube.pos[0] + y) < cube.pos[1] and other_cube.pos[0] == cube.pos[0] and other_cube.pos[2] == cube.pos[2]:
                            internal_cubes.append(cube)
                            internal_cubes.append(other_cube)
                            end_cube = True
                            break
                    if z and z > 0 and other_cube.pos != cube.pos:
                        if (other_cube.pos[2] + z) > cube.pos[2] and other_cube.pos[1] == cube.pos[1] and other_cube.pos[0] == cube.pos[0]:
                            internal_cubes.append(cube)
                            internal_cubes.append(other_cube)
                            end_cube = True
                            break
                    if z and z < 0 and other_cube.pos != cube.pos:
                        if (other_cube.pos[2] + x) < cube.pos[2] and other_cube.pos[1] == cube.pos[1] and other_cube.pos[0] == cube.pos[0]:
                            internal_cubes.append(cube)
                            internal_cubes.append(other_cube)
                            end_cube = True
                            break
                if not end_cube:
                    surface_area += 1

print(pockets)
print(surface_area)