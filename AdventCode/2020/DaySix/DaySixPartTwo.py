# The solution is listed as too low

groups = ''
sum = 0
with open('input6.txt', 'r') as file:
	groups = file.read().split('\n\n')

for group in groups:
    answers = {}
    persons = group.split('\n')
    for person in persons:
        for answer in person:
            if answer not in answers.keys():
                answers[answer] = 1
            else:
                answers[answer] += 1
    for key in answers:
        if (answers[key] == len(persons)):
            sum += 1
print(sum)
