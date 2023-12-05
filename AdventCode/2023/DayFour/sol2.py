import math, re

with open("input.txt") as file_object:
    data = file_object.readlines()

rewards = {}
for num in range(0, len(data)):
    rewards[str(num)] = 1
sum = 0

for count, line in enumerate(data):
    winning_nums, card_nums = line.split("|")
    winning_nums = winning_nums.split(":")[1].split(" ")
    card_nums = card_nums[:-1].split(" ")
    for index in range(card_nums.count("")):
        card_nums.remove("")
    for index in range(winning_nums.count("")):
        winning_nums.remove("")
    matching_nums = 0
    for num in card_nums:
        if num in winning_nums:
            matching_nums += 1

    if matching_nums:
        for num in range(1, matching_nums + 1):
            rewards[str(count + num) ] += rewards[str(count)]

for value in rewards.values():
    sum += int(value)

print(f"The sum is {sum}")