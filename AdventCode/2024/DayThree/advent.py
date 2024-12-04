import re

with open('input.txt') as file_object:
    data = file_object.readlines()

mul_re = re.compile(r"mul\(\d+,\d+\)", re.IGNORECASE)
results = 0

for line in data:
    matches = re.findall(mul_re, line.strip())
    for match in matches:
        l_num , r_num = match.split(",")
        l_num = l_num.replace("mul(", "")
        r_num = r_num.replace(")", "")
        results += int(l_num) * int(r_num)

print(f"TOTAL SUM OF RESULTS: {results}")

results = 0
process = True
mul_do_re = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", re.IGNORECASE)

for line in data:
    matches = re.findall(mul_do_re, line.strip())
    for match in matches:
        if match == 'do()':
            process = True
            continue
        if match == "don't()":
            process = False
            continue
        if process == True:
            l_num , r_num = match.split(",")
            l_num = l_num.replace("mul(", "")
            r_num = r_num.replace(")", "")
            results += int(l_num) * int(r_num)

print(f" TOTAL ENABLED SUM OF RESULTS: {results}")