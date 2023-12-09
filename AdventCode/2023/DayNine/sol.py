import re

with open("input.txt") as file_object:
    data = file_object.readlines()

sum = 0

for line in data:
    nums = re.split(r"[ \n]", line)
    while "" in nums:
        nums.remove("")
    difference_lists = []
    found_zeros = False
    current_line = nums
    difference_lists.append(current_line)
    while not found_zeros:
        difference_line = []
        for index, element in enumerate(current_line[:-1]):
            difference_line.append(int(current_line[index + 1]) - int(element))
        if all(item == 0 for item in difference_line):
            found_zeros = True
        else:
            difference_lists.append(difference_line)
            current_line = difference_line
    end_index = len(difference_lists) - 1
    for index in range(end_index, 0, -1):
        difference_lists[index - 1].append(int(difference_lists[index - 1][-1]) + difference_lists[index][-1])
    sum += difference_lists[0][-1]

print(f"The sum is {sum}")