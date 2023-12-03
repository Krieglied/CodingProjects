og_data = []

with open('./test.txt', 'r') as file_object:
    og_data = file_object.read().splitlines()

mod_data = list(range(len(og_data)))

og_data = [int(x) for x in og_data]

for index, line in enumerate(og_data):
    new_index = line
    item = mod_data.pop(index)
    counter = 0
    while new_index > len(mod_data):
        new_index -= len(mod_data)
        counter += 1
    while new_index < 0:
        new_index = len(mod_data) + new_index
        counter -= 1
    new_index += counter
    if new_index == 0:
        new_index = len(mod_data)
    mod_data.insert(new_index, item)


start_index = og_data.index(0)
start_index = mod_data.index(start_index)
grove_coord = [start_index + 1000, start_index + 2000, start_index + 3000]

while grove_coord[0] > len(og_data) or grove_coord[1] > len(og_data) or grove_coord[2] > len(og_data):
    if grove_coord[0] > len(og_data):
        grove_coord[0] -= len(og_data)
    if grove_coord[1] > len(og_data):
        grove_coord[1] -= len(og_data)
    if grove_coord[2] > len(og_data):
        grove_coord[2] -= len(og_data)

print(int(mod_data[grove_coord[0]]) + int(mod_data[grove_coord[1]]) + int(mod_data[grove_coord[2]]))
