import re

def valid_game(items: list) -> bool:
    min_balls = {
        "red" : 0,
        "green" : 0,
        "blue": 0
    }
    for index, item in enumerate(items):
        if not item.isnumeric():
            if int(items[index - 1]) > min_balls[item.replace(";", "").replace("\n", "")]:
                min_balls[item.replace(";", "").replace("\n", "")] = int(items[index - 1])
        else:
            continue
    return min_balls

with open('input.txt') as file_object:
    data = file_object.readlines()

sum = 0

for line in data:
    items = re.split(r' |,|:', line)
    while '' in items:
        items.remove('')
    id = int(items[1])
    items.pop(0)
    items.pop(0)
    min_balls = valid_game(items)
    if 999999 not in min_balls.values():
        sum += min_balls["red"] * min_balls["blue"] * min_balls["green"]

print(f"The sum is {sum}")