with open('input.txt') as file_object:
    data = file_object.readlines()

pg_order = {}

updates = []

for line in data:
    if "|" in line:
        pg1, pg2 = line.strip().split("|")
        if pg1 in pg_order.keys():
            pg_order[pg1].append(pg2)
        else:
            pg_order[pg1] = [pg2]
        if pg2 not in pg_order.keys():
            pg_order[pg2] = []
    elif line.strip():
        updates.append(line.strip())

correct_updates = []
incorrect_updates = []

for line in updates:
    pgs = line.split(",")
    wrong_order = False
    for index, pg in enumerate(pgs):
        for prev_pg in pgs[:index]:
            if prev_pg in pg_order[pg]:
                wrong_order = True
                incorrect_updates.append(pgs)
                break
        if wrong_order:
            break
    if not wrong_order:
        correct_updates.append(pgs)

total = 0

for group in correct_updates:
    total += int(group[len(group) // 2])

print(f"TOTAL MIDDLE PAGE VALUES: {total}")



def check_update(pgs):
    for index, pg in enumerate(pgs):
        for prev_pg in pgs[:index]:
            if prev_pg in pg_order[pg]:
                return False
    return True

for pgs in incorrect_updates:
    while not check_update(pgs):
        for index, pg in enumerate(pgs):
            for iindex, prev_pg in enumerate(pgs[:index]):
                if prev_pg in pg_order[pg]:
                    pgs.remove(prev_pg)
                    pgs.insert(index, prev_pg)

total = 0

for group in incorrect_updates:
    total += int(group[len(group) // 2])

print(f"SECOND TOTAL MIDDLE PAGE VALUES: {total}")