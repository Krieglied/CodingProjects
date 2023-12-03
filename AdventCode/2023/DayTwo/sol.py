import re

def valid_game(items: list) -> bool:
    balls = {
        "red" : 12,
        "green" : 13,
        "blue": 14
    }
    for index, item in enumerate(items):
        if not item.isnumeric():
            if int(items[index - 1]) > balls[item.replace(";", "").replace("\n", "")]:
                return False
        else:
            continue
    return True


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
    if valid_game(items):
        sum += id

print(f"The sum is {sum}")