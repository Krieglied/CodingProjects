### Didn't quite get all the conditioning correct.  The returned number of valid passports is too high


import re

# Process each entry to make sure that the passport has all of the 7 required fields
def processPassport(passport):
	requiredFields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']
	# Both new lines and spaces need to be removed, so re.split is used
	passportEntries = re.split('\n| ', passport)
	print(passportEntries)
	for field in requiredFields:
		if field not in passport:
			return False
	for entry in passportEntries:
		if not entry:
			continue
		value = entry.split(':')[1]
		if ('byr:' in entry) and (int(value) < 1920) and (int(value) > 2002):
			return False
		if ('iyr:' in entry) and (int(value) < 2010) and (int(value) > 2020):
			return False
		if ('eyr:' in entry) and (int(value) < 2020) and (int(value) > 2030):
			return False
		if ('hgt:' in entry):
			if('cm' in entry):
				height = re.split('cm', value)[0]
				if int(height) < 150 and int(height) > 193:
					return False
			if('in' in entry):
				height = re.split('in', value)[0]
				if int(height) < 59 and int(height) > 76:
					return False
		if ('hcl:' in entry) and (not re.match('#\w{6}', value)):
			return False
		if ('ecl:' in entry) and (value not in ['amb','blu','brn','gry','grn','hzl','oth']):
			return False
		if ('pid:' in entry) and (not re.match('\d{9}', value)):
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
