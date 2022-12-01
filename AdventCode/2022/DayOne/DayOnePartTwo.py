data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

elf_calorie = []
current_calorie = 0

for amount in data:    
    if amount != '\n':
        current_calorie += int(amount)
    else:
        elf_calorie.append(current_calorie)
        current_calorie = 0

print(sum(sorted(elf_calorie, reverse=True)[:3]))