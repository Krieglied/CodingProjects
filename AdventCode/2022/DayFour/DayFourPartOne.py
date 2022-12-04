data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

assignment_pair = 0

for line in data:
    first_assign, second_assign = line.split(',')
    first_assign = first_assign.split('-')
    second_assign = second_assign.strip().split('-')
    if int(first_assign[0]) in range(int(second_assign[0]), int(second_assign[1]) + 1) and int(first_assign[1]) in range(int(second_assign[0]), int(second_assign[1]) + 1):
        assignment_pair += 1
    elif int(second_assign[0]) in range(int(first_assign[0]), int(first_assign[1]) + 1) and int(second_assign[1]) in range(int(first_assign[0]), int(first_assign[1]) + 1):
        assignment_pair += 1
print(assignment_pair)