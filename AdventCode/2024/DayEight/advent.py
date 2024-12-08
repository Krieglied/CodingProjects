import itertools

with open('input.txt') as file_object:
    data = file_object.readlines()

antennas = {}
found_points = set()

for lindex, line in enumerate(data):
    for index, char in enumerate(line.strip()):
        if char != ".":
            if char not in antennas.keys():
                antennas[char] = []
            antennas[char].append((lindex, index))

for key, value in antennas.items():
    permutations = list(itertools.permutations(value, 2))

    for item in permutations:
        if (item[1], item[0]) in permutations:
            permutations.remove((item[1], item[0]))

    for pos1, pos2 in permutations:
        y_diff = abs(pos1[0] - pos2[0])
        x_diff = abs(pos1[1] - pos2[1])
        if (pos1[0] < pos2[0] and pos1[1] < pos2[1]) or (pos2[0] < pos1[0] and pos2[1] < pos1[1]):
            far_point1 = (min(pos1[0], pos2[0]) - y_diff, min(pos1[1], pos2[1]) - x_diff)
            far_point2 = (max(pos1[0], pos2[0]) + y_diff, max(pos1[1], pos2[1]) + x_diff)
        elif (pos1[0] > pos2[0] and pos1[1] < pos2[1]) or (pos1[0] < pos2[0] and pos1[1] > pos2[1]):
            far_point1 = (max(pos1[0], pos2[0]) + y_diff, min(pos1[1], pos2[1]) - x_diff)
            far_point2 = (min(pos1[0], pos2[0]) - y_diff, max(pos1[1], pos2[1]) + x_diff)
        # Same Horizontal
        elif pos1[0] == pos2[0]:
            far_point1 = (pos1[0], min(pos1[1], pos2[1]) - x_diff)
            far_point2 = (pos1[0], max(pos1[1], pos2[1]) + x_diff)
        # Same Vertical
        elif pos1[1] == pos2[1]:
            far_point1 = (min(pos1[0], pos2[0]) - y_diff, pos1[1])
            far_point2 = (max(pos1[0], pos2[0]) + y_diff, pos1[1])

        if 0 <= far_point1[0] < len(data) and 0 <= far_point1[1] < len(data[0]) - 1:
            found_points.add(far_point1)
        if 0 <= far_point2[0] < len(data) and 0 <= far_point2[1] < len(data[0]) - 1:
            found_points.add(far_point2)

print(f"NUMBER OF FOUND POINTS: {len(found_points)}")

expanded_found_points = set()

for key, value in antennas.items():
    permutations = list(itertools.permutations(value, 2))

    for item in permutations:
        if (item[1], item[0]) in permutations:
            permutations.remove((item[1], item[0]))

    for pos1, pos2 in permutations:
        y_diff = abs(pos1[0] - pos2[0])
        x_diff = abs(pos1[1] - pos2[1])
        far_point1 = (0, 0)
        far_point2 = (0, 0)
        # B
        #  \
        #   A
        if (pos1[0] < pos2[0] and pos1[1] < pos2[1]) or (pos2[0] < pos1[0] and pos2[1] < pos1[1]):
            far_point = (min(pos1[0], pos2[0]), min(pos1[1], pos2[1]))
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0] - y_diff, far_point[1] - x_diff)
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
            far_point = (max(pos1[0], pos2[0]), max(pos1[1], pos2[1]))
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0] + y_diff, far_point[1] + x_diff)
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
        #   B
        #  /
        # A
        elif (pos1[0] > pos2[0] and pos1[1] < pos2[1]) or (pos1[0] < pos2[0] and pos1[1] > pos2[1]):
            far_point = (max(pos1[0], pos2[0]), min(pos1[1], pos2[1]))
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0] + y_diff, far_point[1] - x_diff)
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
            far_point = (max(pos1[0], pos2[0]), min(pos1[1], pos2[1]))
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0] - y_diff, far_point[1] + x_diff)
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
        # A - B
        elif pos1[0] == pos2[0]:
            far_point = (pos1[0], min(pos1[1], pos2[1]))
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0], far_point[1] - x_diff)
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
            far_point = (pos1[0], max(pos1[1], pos2[1]))
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0], far_point[1] + x_diff)
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
        # A
        # |
        # B
        elif pos1[1] == pos2[1]:
            far_point = (min(pos1[0], pos2[0]), pos1[1])
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0] - y_diff, far_point[1])
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)
            far_point = (max(pos1[0], pos2[0]) + y_diff, pos1[1])
            while 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                far_point = (far_point[0] + y_diff, far_point[1])
                if 0 <= far_point[0] < len(data) and 0 <= far_point[1] < len(data[0]):
                    expanded_found_points.add(far_point)

print(f"NUMBER OF FOUND POINTS: {len(expanded_found_points)}")