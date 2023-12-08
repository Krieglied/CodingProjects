from functools import cmp_to_key

strengths = {
    "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8,
    "9" : 9, "T" : 10, "J" : 11, "Q" : 12, "K" : 13, "A" : 14, "J": 1
}

def compare_hand(item1, item2):
    for index, char in enumerate(item1[0]):
        if strengths[char] > strengths[item2[0][index]]:
            return 1
        elif strengths[char] < strengths[item2[0][index]]:
            return -1
    return 0

with open("input.txt") as file_object:
    data = file_object.readlines()

card_results = [[], [], [], [], [], [], []]

for line in data:
    cards, bid = line.replace("\n", "").split(" ")
    card_counts = {}
    for item in cards:
        if item == "J":
            continue
        card_counts[item] = cards.count(item)
    joker_count = cards.count("J")
    if joker_count == 5:
        card_counts["J"] = 5
    else:
        card_counts[max(card_counts, key=card_counts.get)] += cards.count("J")
    if len(card_counts) == 1:
        card_results[0].append((cards, int(bid)))
    elif 4 in card_counts.values():
        card_results[1].append((cards, int(bid)))
    elif len(card_counts) == 2:
        card_results[2].append((cards, int(bid)))
    elif len(card_counts) == 3:
        if 3 in card_counts.values():
            card_results[3].append((cards, int(bid)))
        else:
            card_results[4].append((cards, int(bid)))
    elif len(card_counts) == 4:
        card_results[5].append((cards, int(bid)))
    elif len(card_counts) == 5:
        card_results[6].append((cards, int(bid)))

rank = range(len(data), 0, -1)
rank_iter = iter(rank)

sum = 0

for category in card_results:
    category.sort(key=cmp_to_key(compare_hand))
    if len(category) == 0:
        continue
    for card in category[::-1]:
        sum += next(rank_iter) * card[1]

print(f"The total sum is {sum}")