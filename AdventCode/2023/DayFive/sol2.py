def map_value(full_seed_info, map, action, prev):
    for seed_info in full_seed_info:
        prev_value = seed_info[prev]
        mapped = False
        for map_line in map:
            mod_value = int(map_line[0]) - int(map_line[1])
            if int(map_line[1]) <= int(prev_value) < int(map_line[1]) + int(map_line[2]):
                seed_info[action] = int(prev_value) + mod_value
                mapped = True
        if not mapped:
            seed_info[action] = prev_value

    return full_seed_info

with open("input.txt") as file_object:
    data = file_object.readlines()

seed_line = data[0].split(":")[1][:-1].split(" ")
while seed_line.count(""):
    seed_line.remove("")

seed_nums = set()

for index in range(0, len(seed_line), 2):
    seed_nums.update(range(int(seed_line[index]), int(seed_line[index]) + int(seed_line[index + 1])))

full_seed_info = []
map_order = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temp', 'humidity', 'location']
for seed in seed_nums:
    seed_info = {}
    for order in map_order:
        if order == 'seed':
            seed_info[order] = seed
        else:
            seed_info[order] = ''
    full_seed_info.append(seed_info)

soil_map = []
fertilizer_map = []
water_map = []
light_map = []
temp_map = []
humidity_map = []
location_map = []
action = ""


for line in data[2:]:
    if "map" in line:
        action = line.split(" ")[0]
        continue
    if line == "\n":
        continue
    if "seed-to-soil" in action:
        soil_map.append(line.replace("\n", "").split(" "))
    elif "soil-to-fertilizer" in action:
        fertilizer_map.append(line.replace("\n", "").split(" "))
    elif "fertilizer-to-water" in action:
        water_map.append(line.replace("\n", "").split(" "))
    elif "water-to-light" in action:
        light_map.append(line.replace("\n", "").split(" "))
    elif "light-to-temperature" in action:
        temp_map.append(line.replace("\n", "").split(" "))
    elif "temperature-to-humidity" in action:
        humidity_map.append(line.replace("\n", "").split(" "))
    elif "humidity-to-location" in action:
        location_map.append(line.replace("\n", "").split(" "))
    
full_seed_info = map_value(full_seed_info, soil_map, map_order[1], map_order[0])
full_seed_info = map_value(full_seed_info, fertilizer_map, map_order[2], map_order[1])
full_seed_info = map_value(full_seed_info, water_map, map_order[3], map_order[2])
full_seed_info = map_value(full_seed_info, light_map, map_order[4], map_order[3])
full_seed_info = map_value(full_seed_info, temp_map, map_order[5], map_order[4])
full_seed_info = map_value(full_seed_info, humidity_map, map_order[6], map_order[5])
full_seed_info = map_value(full_seed_info, location_map, map_order[7], map_order[6])

print(f"The lowest location number is {min([seed_info['location'] for seed_info in full_seed_info])}")