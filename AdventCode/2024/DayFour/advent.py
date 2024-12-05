with open('input.txt') as file_object:
    data = file_object.readlines() 

search_string = "XMAS"

total = 0 

for lindex, line in enumerate(data):
    for index, char in enumerate(line):
        if char == "X":
            search_char = search_string[search_string.find(char) + 1] 
            if lindex == 0:
                l_range = [0, 1]
            elif lindex == len(data) - 1:
                l_range = [len(data) - 2, len(data) - 1]
            else:
                l_range = [lindex - 1, lindex, lindex + 1]

            if index == 0:
                i_range = [0, 1]
            elif index == len(data[0]) - 2:
                i_range = [len(data[0]) - 3, len(data[0]) - 2]
            else:
                i_range = [index - 1, index, index + 1]
            
            for yindex in l_range:
                for xindex in i_range:
                    if data[yindex][xindex] == "M":
                        # NW
                        if yindex < lindex and xindex < index:
                            if lindex  - 3 >= 0 and index - 3 >= 0:
                                if data[yindex - 1][xindex - 1] == "A" and data[yindex - 2][xindex - 2] == "S":
                                    total += 1
                        # NE
                        elif yindex < lindex and xindex > index:
                            if lindex - 3 >= 0 and index + 3 <= len(data[0]) - 1:
                                if data[yindex - 1][xindex + 1] == "A" and data[yindex - 2][xindex + 2] == "S":
                                    total += 1
                        # SE
                        elif yindex > lindex and xindex > index:
                            if lindex + 3 <= len(data) - 1 and index + 3 <= len(data[0]) - 1:
                                if data[yindex + 1][xindex + 1] == "A" and data[yindex + 2][xindex + 2] == "S":
                                    total += 1
                        # SW
                        elif yindex > lindex and xindex < index:
                            if lindex + 3 <= len(data) - 1 and index - 3 >= 0:
                                if data[yindex + 1][xindex - 1] == "A" and data[yindex + 2][xindex - 2] == "S":
                                    total += 1
                        # S
                        elif yindex > lindex:
                            if lindex + 3 <= len(data) - 1:
                                if data[yindex + 1][xindex] == "A" and data[yindex + 2][xindex] == "S":
                                    total += 1
                        # N
                        elif yindex < lindex:
                            if lindex - 3 >= 0:
                                if data[yindex - 1][xindex] == "A" and data[yindex - 2][xindex] == "S":
                                    total += 1
                        # E
                        elif xindex > index:
                            if index + 3 <= len(data[0]) - 1:
                                if data[yindex][xindex + 1] == "A" and data[yindex][xindex + 2] == "S":
                                    total += 1
                        # W
                        elif xindex < index:
                            if index - 3 >= 0:
                                if data[yindex][xindex - 1] == "A" and data[yindex][xindex - 2] == "S":
                                    total += 1
                        

print(f"TOTAL XMAS APPEARANCE: {total}")