class Node(object):
    def __init__(self, point, weight, neighbors):
        self.point = point
        self.weight = weight
        self.neighbors = neighbors


def get_neighbors(x, y):

def dijkstra(graph):
    src = graph[0]
    target = graph[len(graph) - 1]
    nodes = []
    sdistance = {}
    previous = {}

    for vertex in graph:
        sdistance[vertex.point] = 99999
        previous[vertex.point] = None
        nodes.append(vertex)

    sdistance[src.point] = 0
    nearest_node = None

    while(len(nodes) > 0):
        short_distance = 99999
        for vertex in nodes:
            if(sdistance[vertex.point] < short_distance):
                short_distance = sdistance[vertex.point]
                nearest_node = vertex
        
        nodes.remove(nearest_node)

        if(nearest_node == target):
            print(f'Shortest distance is {short_distance}')

        for neighbor in nearest_node.neighbors:
            alt = short_distance + neighbor.weight
            if (alt < sdistance[neighbor.point]):
                sdistance[neighbor.point] = alt
                previous[neighbor.point] = nearest_node



data = []

with open('./test.txt', 'r') as file_object:
    data = file_object.read().splitlines()

graph = []

for line_num, line in enumerate(data):
    for char_num, char in enumerate(line):
        neighbors = []
        if line_num > 0:
            
        new_node = Node((), get_neighbors())