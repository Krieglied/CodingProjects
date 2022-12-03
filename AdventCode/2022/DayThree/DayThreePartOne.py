data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

sum_priorites = 0

for line in data:
    for item in line[:len(line) // 2]:
        if item in line[len(line) // 2:]:
            if ord(item) > 96:
                sum_priorites += ord(item) - 96
            else:
                sum_priorites += ord(item) - 38
            break
print(sum_priorites)