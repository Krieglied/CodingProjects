import math, re

with open("input.txt") as file_object:
    data = file_object.readlines()

sum = 0

for line in data:
    winning_nums, card_nums = line.split("|")
    game_title, winning_nums = winning_nums.split(":")
    winning_nums = winning_nums.split(" ")
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
        print(f"{game_title} had {matching_nums} matches")
        sum += math.pow(2, matching_nums - 1)

print(f"The sum is {int(sum)}")