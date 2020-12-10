# Process each entry to make sure that the passport has all of the 7 required fields
def processPassport(passport):
	requiredFields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
	for field in requiredFields:
		if field not in passport:
			return False
	return True
	
input = ''

with open('input4.txt', 'r') as file:
	input = file.read().split('\n\n')

count = 0
for entry in input:
	if processPassport(entry):
		count = count + 1
print(count)
