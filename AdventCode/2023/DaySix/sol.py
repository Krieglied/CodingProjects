import math

with open("input.txt") as file_object:
    data = file_object.readlines()

times = data[0].split(":")[1][:-1].split(" ")
distances = data[1].split(":")[1].split(" ")
while times.count(""):
    times.remove("")
while distances.count(""):
    distances.remove("")

victory_ways = 1

for time, distance in zip(times, distances):
    ways = 0
    for num in range(int(time) // 2 + 1):
        movement = (int(time) - num) * num
        if movement > int(distance):
            ways += 1 if (int(time) - num) == num else 2
    victory_ways *= ways

print(f"The total number of ways to beat the races is {victory_ways}")