with open('input.txt') as file_object:
    data = file_object.readlines()

left_values = []
right_values = []

for line in data:
    l, r = line.split()
    left_values.append(l)
    right_values.append(r)

dist = 0

for item in zip(sorted(left_values), sorted(right_values)):
    dist += abs(int(item[1]) - int(item[0]))

print(f"TOTAL DISTANCE: {dist}")

score = 0

for item in sorted(left_values):
    score += int(item) * right_values.count(item)

print(f"SIMILARITY SCORE: {score}")