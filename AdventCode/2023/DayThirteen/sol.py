def test_hor_reflect(pattern:list) -> int:
    if len(pattern) % 2 == 0:
        if pattern[:len(pattern) // 2] == pattern[len(pattern) // 2:][::-1]:
            return (len(pattern) // 2) * 100
        return 0
    else:
        for num in range(2):
            first_half = pattern[num:len(pattern) // 2 + num]
            second_half = pattern[len(pattern) // 2 + num: len(pattern) - (1 - num)]
            if first_half != second_half[::-1]:
                continue
            else:
                return (len(pattern) // 2 + num) * 100
        return 0 

def test_vert_reflect(pattern: list) -> int:
    if len(pattern[0]) % 2 == 0:
        for row in pattern:
            if row[:len(pattern) // 2 + 1] != row[len(pattern) // 2 + 1:][::-1]:
                return 0
        return len(pattern[0]) // 2
    else:
        true_reflect = True
        for num in range(2):
            for row in pattern:
                first_half = row[num:len(row) // 2 + num]
                second_half = row[len(row) // 2 + num: len(row) - (1 - num)]
                if first_half != second_half[::-1]:
                    true_reflect = False
                    break
            if true_reflect:
                return len(row) // 2 + num
            true_reflect = True
        return 0

with open("input.txt") as file_object:
    data = file_object.readlines()

patterns = []
pattern = []

for line in data:
    line = line.replace("\n", "")
    if line == "":
        patterns.append(pattern)
        pattern = []
    else:
        pattern.append(line)

patterns.append(pattern)
pattern = []

pattern_notes = 0

for pattern in patterns:
    pattern_notes += test_vert_reflect(pattern)
    pattern_notes += test_hor_reflect(pattern)

print(f"The number after summarizing notes is {pattern_notes}")