data = []

with open('./test', 'r') as file_object:
    data = file_object.read().splitlines()

bottom = "#######"

bottoms = { "1" : [1, "..####."],
            "2" : [3, "...#..."],
            "3" : [3, "....#.."],
            "4" : [4, "..#...."],
            "5" : [2, "..##..."]
}

rock = 1
jet_order = 0
height = 0

while rock <= 2022:
    