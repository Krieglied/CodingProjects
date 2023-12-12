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

inserted = 0

for index, row in enumerate(additional_rows):
    if row == 1:
        data.insert(index + inserted, "." * len(data[0][:-1]) + "\n")
        inserted += 1

inserted = 0

for index, col in enumerate(additional_cols):
    if col == 1:
        for col_index, line in enumerate(data):
            data[col_index] = line[:index + inserted] + "." + line[index + inserted:]
        inserted += 1

distance_sum = 0

for index, gal in enumerate(found_galaxies[:-1]):
    for end_point in range(index + 1, len(found_galaxies)):
        x_distance = abs(gal[1] - found_galaxies[end_point][1])
        y_distance = abs(gal[0] - found_galaxies[end_point][0])
        distance_sum += x_distance + y_distance

print(f"The sum of the lengths is {distance_sum}")