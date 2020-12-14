groups = ''
sum = 0
with open('input6.txt', 'r') as file:
	groups = file.read().split('\n\n')

for group in groups:
    answers = []
    persons = group.split('\n')
    for person in persons:
        for answer in person:
            if answer not in answers:
                answers += answer
    sum += len(answers)
print(sum)
