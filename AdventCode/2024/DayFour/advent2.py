with open('input.txt') as file_object:
    data = file_object.readlines() 

xmas = 0 

for lindex, line in enumerate(data[1:-1], start=1):
    for index, char in enumerate(line[1:-2], start=1):
        total = 0 
        if char == "A":
            l_range = [lindex - 1, lindex + 1]
            i_range = [index - 1, index + 1]                

            for yindex in l_range:
                for xindex in i_range:
                    if data[yindex][xindex] == "M":
                        diff_y = lindex - yindex
                        diff_x = index - xindex
                        if data[lindex + diff_y][index + diff_x] == "S":
                            total += 1
            if total == 2:
                xmas += 1

print(f"TOTAL X-MAS APPEARANCE: {xmas}")