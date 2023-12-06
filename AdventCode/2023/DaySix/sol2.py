import math

with open("input.txt") as file_object:
    data = file_object.readlines()

time = data[0].split(":")[1][:-1].replace(" ", "")
distance = data[1].split(":")[1].replace(" ", "")

ways = 0
for num in range(int(time) // 2 + 1):
    movement = (int(time) - num) * num
    if movement > int(distance):
        ways = math.ceil(((int(time) / 2) - num) * 2) + 1
        break

print(f"The total number of ways to beat the races is {ways}")