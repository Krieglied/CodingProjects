import re

with open("test.txt") as file_object:
    data = file_object.readlines()

additional_rows = [1] * len(data)
additional_cols = [1] * len(data[0][:-1])    

found_galaxies = []

for index, line in enumerate(data):
    if "#" in line:
        additional_rows[index] = 0
        galaxies = re.finditer(r"#", line)
        for gal in galaxies:
            additional_cols[gal.start()] = 0
            found_galaxies.append((index, gal.start()))

distance_sum = 0

for index, gal in enumerate(found_galaxies):
    for end_point in range(index + 1, len(found_galaxies)):
        min_y = min(gal[0], found_galaxies[end_point][0])
        max_y = max(gal[0], found_galaxies[end_point][0])
        min_x = min(gal[1], found_galaxies[end_point][1])
        max_x = max(gal[1], found_galaxies[end_point][1])
        x_distance = (max_x + sum(additional_cols[min_x + 1: max_x])) - min_x
        y_distance = (max_y + sum(additional_cols[min_y + 1: max_y])) - min_y
        distance_sum += x_distance + y_distance

print(f"The sum of the lengths is {distance_sum}")