data = []

with open('./test.txt', 'r') as file_object:
    data = file_object.read().splitlines()

geodes_per_bp = {}

for line in data:
    print(line)
    line_comps = line.split(' ')
    bp = int(line_comps[1][:-1])
    ore = int(line_comps[6])
    clay = int(line_comps[12])
    obsidian = [int(line_comps[18]), int(line_comps[21])]
    geode = [int(line_comps[27]), int(line_comps[30])]
    minutes = 1
    # ore, clay, obsidian, geode
    collected_materials = [0, 0, 0, 0]
    # ore, clay, obsidian, geode
    robots = [1, 0, 0, 0]
    while minutes <= 24:
        new_robots = [0, 0, 0, 0]
        # geode robot check first, ore/obsidian
        if collected_materials[0] >= geode[0] and collected_materials[2] >= geode[1]:
            collected_materials[0] -= geode[0]
            collected_materials[2] -= geode[1]
            new_robots[3] += 1
        # obsidian robot check next, ore/clay
        if collected_materials[0] >= obsidian[0] and collected_materials[1] >= obsidian[1]:
            collected_materials[0] -= obsidian[0]
            collected_materials[1] -= obsidian[1]
            new_robots[2] += 1
        # clay robot check next, ore
        if collected_materials[0] >= clay:
            collected_materials[0] -= clay
            new_robots[1] += 1
        # ore robot check last, ore
        if collected_materials[0] >= ore:
            collected_materials[0] -= ore
            new_robots[0] += 1
        collected_materials[0] += robots[0]
        collected_materials[1] += robots[1]
        collected_materials[2] += robots[2]
        collected_materials[3] += robots[3]
        if any(new_robots):
            for index, robot in enumerate(new_robots):
                robots[index] += robot
        minutes += 1