data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

sum_priorites = 0

for index in range(0, len(data), 3):
    for item in data[index]:
        if item in data[index + 1] and item in data[index + 2]:
            if ord(item) > 96:
                sum_priorites += ord(item) - 96
            else:
                sum_priorites += ord(item) - 38
            break

print(sum_priorites)