import re

with open("input.txt") as file_object:
    data = file_object.readlines()

parts = []
symbols = []

for index, line, in enumerate(data):
    line_parts = re.finditer(r"\d+", line)
    line_symbols = re.finditer(r"[^\.\d\n]", line)
    parts_line = []
    symbol_line = []
    
    for symbol in line_symbols:
        symbols.append((index, symbol.start()))

    for part in line_parts:
        parts_line.append((part.span(), part.group(0)))    
    parts.append(parts_line)

valid_part_nums = []

for symbol in symbols:
    adjacent_parts = []
    if symbol[0] != 0:
        top_line = parts[symbol[0] - 1]
    current_line = parts[symbol[0]]
    if symbol[0] != len(data) - 1:
        bottom_line = parts[symbol[0] + 1]

    for iindex, part in enumerate(top_line):
        if (part[0][0] - 1) <= symbol[1] <= (part[0][1]):
            adjacent_parts.append(part)

    for iindex, part in enumerate(current_line):
        if symbol[1] == (part[0][0] - 1) or symbol[1] == (part[0][1]):
            adjacent_parts.append(part)

    for iindex, part in enumerate(bottom_line):
        if (part[0][0] - 1) <= symbol[1] <= (part[0][1]):
            adjacent_parts.append(part)
    
    if len(adjacent_parts) == 2:
        valid_part_nums.append(int(adjacent_parts[0][1]) * int(adjacent_parts[1][1]))

print(f"The sum of part numbers is {sum(valid_part_nums)}")