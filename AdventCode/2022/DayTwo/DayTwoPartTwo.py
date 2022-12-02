data = []

with open('./data.txt', 'r') as file_object:
    data = file_object.readlines()

score = 0

for line in data:
    # Win
    if 'Z' in line:
        score += 6
    # Tie
    elif 'Y' in line:
        score += 3

    # Opponent Rock
    if 'A' in line and 'Z' in line:
        # Me Paper
        score += 2
    elif 'A' in line and 'Y' in line:
        # Me Rock
        score += 1
    elif 'A' in line and 'X' in line:
        # Me Scissors
        score += 3
    # Opponent Paper
    elif 'B' in line and 'Z' in line:
        # Me Scissors
        score += 3
    elif 'B' in line and 'Y' in line:
        # Me Paper
        score += 2
    elif 'B' in line and 'X' in line:
        # Me Rock
        score += 1
    # Opponent Scissors
    elif 'C' in line and 'Z' in line:
        # Me Rock
        score += 1
    elif 'C' in line and 'Y' in line:
        # Me Scissors
        score += 3
    elif 'C' in line and 'X' in line:
        # Me Paper
        score += 2
    
print(score)
