with open('test_input.txt') as file_object:
    data = file_object.readlines()

reports = 0

for line in data:
    line = line.strip().split(" ")
    safe = True
    direction = 0
    for index in range(len(line) - 1):
        if abs(int(line[index]) - int(line[index + 1])) > 3:
            safe = False
            break
        if int(line[index]) - int(line[index + 1]) == 0:
            safe = False
            break
        elif int(line[index]) - int(line[index + 1]) > 0:
            if not direction:
                direction = "dec"
            if direction == "inc":
                safe = False
                break
        elif int(line[index]) - int(line[index + 1]) < 0:
            if not direction:
                direction = "inc"
            if direction == "dec":
                safe = False
                break
    if safe:
        reports += 1

print(f"NUMBER OF SAFE REPORTS: {reports}")

reports = 0

for line in data:
    line = line.strip().split(" ")
    unsafe = 0
    direction = 0
    for index in range(len(line) - 1):
        if abs(int(line[index]) - int(line[index + 1])) > 3:
            unsafe += 1
            if unsafe > 1:
                break
        if int(line[index]) - int(line[index + 1]) == 0:
            unsafe += 1
            if unsafe > 1:
                break
        elif int(line[index]) - int(line[index + 1]) > 0:
            if not direction:
                direction = "dec"
            if direction == "inc":
                unsafe += 1
                if unsafe > 1:
                    break
        elif int(line[index]) - int(line[index + 1]) < 0:
            if not direction:
                direction = "inc"
            if direction == "dec":
                unsafe += 1
                if unsafe > 1:
                    break
    if unsafe < 2:
        reports += 1

print(f"NUMBER OF MOD SAFE REPORTS: {reports}")