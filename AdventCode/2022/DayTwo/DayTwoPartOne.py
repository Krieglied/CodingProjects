data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

score = 0

for line in data:
    if 'A' in line:
        score += 3
        # Rock Ties Rock: 1 + 3
        if 'X' in line:
            score += 1
        # Rock Beaten by Paper: 2 + 6
        elif 'Y' in line:
            score += 5
        # Rock Beats Scissors: 3 + 0
            
    elif 'B' in line:
        score += 1
        # Paper Ties Paper: 2 + 3
        if 'Y' in line:
            score += 4
        # Paper Beaten by Scissors: 3 + 6
        elif 'Z' in line:
            score += 8
    elif 'C' in line:
        score += 2
        # Scissors Beaten by Rock: 1 + 6
        if 'X' in line:
            score += 5
        # Scissors Beats Paper: 2 + 0
        # Scissors Ties Scissors: 3 + 3
        elif 'Z' in line:
            score += 4

print(score)