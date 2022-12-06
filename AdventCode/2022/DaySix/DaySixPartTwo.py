data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.read()

index = 0

while index < len(data):
    marker = data[index:index + 14]
    if len(marker) == len(set(marker)):
        print(f'Start of packet at index {index + 14}')
        break
    index += 1