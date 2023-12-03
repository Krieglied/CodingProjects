import re

def convert_num_word(input):
    conversions = {"one": "1", "two": "2", "three": "3",
                   "four": "4", "five": "5", "six": "6",
                   "seven": "7", "eight": "8", "nine": "9"}
    return input if input.isnumeric() else conversions[input]

data = []

with open("input.txt") as file_object:
    data = file_object.readlines()

sum = 0
for line in data:
    # Part 1 solution
    # results = re.findall(r'\d', line)
    results = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
    line_digits = convert_num_word(results[0]) + convert_num_word(results[-1])
    sum += int(line_digits)

print(f"The sum is {sum}")