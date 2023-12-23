import time
from collections import defaultdict
import sys
import dijkstar
import itertools
sys.setrecursionlimit(10000)


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


# https://www.geeksforgeeks.org/find-paths-given-source-destination/
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def printAllPathsUtil(self, u, d, visited, path, results):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            results.append(path_costs(path, costs))
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if not visited[i]:
                    self.printAllPathsUtil(i, d, visited, path, results)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def printAllPaths(self, s, d, results):

        # Mark all the vertices as not visited
        visited = [False] * (self.V)

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.printAllPathsUtil(s, d, visited, path, results)


def path_south(x, y, inputs):
    if y < len(inputs) - 1:
        if inputs[y + 1][x] == '#':
            return False
        else:
            return True
    else:
        return False


def path_north(x, y, inputs):
    if y >= 1:
        if inputs[y - 1][x] == '#':
            return False
        else:
            return True
    else:
        return False


def path_east(x, y, inputs):
    if x < len(inputs[0]) - 1:
        if inputs[y][x + 1] == '#':
            return False
        else:
            return True
    else:
        return False


def path_west(x, y, inputs):
    if x >= 1:
        if inputs[y][x - 1] == '#':
            return False
        else:
            return True
    else:
        return False


def count_vertices(inputs):
    vert = 0
    all_vertices = []
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            if j != '#':
                vert += 1
                all_vertices.append(y * len(inputs[0]) + x)
    return vert, all_vertices


def find_intersections(inputs):
    intersections = []
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            if j != '#':
                inter = path_south(x, y, inputs) + path_north(x, y, inputs) + path_east(x, y, inputs) \
                        + path_west(x, y, inputs)
                if inter > 2:
                    intersections.append(y * len(inputs[0]) + x)
    return intersections


def add_nodes_to_graph_dijkstar(inputs, intersections, start, end):
    graph = dijkstar.Graph()
    intersections_function = set(intersections)
    intersections_function.remove(start)
    intersections_function.remove(end)
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            current_point = y * len(inputs[0]) + x
            if current_point not in intersections_function:
                if path_south(x, y, inputs):
                    # print('going south:', current_point, (y + 1) * len(inputs[0]) + x)
                    graph.add_edge(current_point, (y + 1) * len(inputs[0]) + x, 1)
                if path_north(x, y, inputs):
                    # print('going north:', current_point, (y - 1) * len(inputs[0]) + x)
                    graph.add_edge(current_point, (y - 1) * len(inputs[0]) + x, 1)
                if path_east(x, y, inputs):
                    # print('going east:', current_point, y * len(inputs[0]) + x + 1)
                    graph.add_edge(current_point, y * len(inputs[0]) + x + 1, 1)
                if path_west(x, y, inputs):
                    # print('going west:', current_point,  y * len(inputs[0]) + x - 1)
                    graph.add_edge(current_point, y * len(inputs[0]) + x - 1, 1)
    return graph


def path_costs(path, costs):
    total_costs = 0
    for ind, i in enumerate(path):
        if ind < len(path) - 1:
            total_costs += costs[(i, path[ind +1])]
    return total_costs


start_time = time.time()
inputs = read_file('input_day23.txt')
vert, all_vert = count_vertices(inputs)
s, d = min(all_vert), max(all_vert)
intersections = find_intersections(inputs)
intersections.insert(0, s)
intersections.append(d)

g = Graph(len(inputs) * len(inputs[0]))

costs = {}

for i in list(itertools.combinations(intersections, 2)):
    graph_dijkstar = add_nodes_to_graph_dijkstar(inputs, intersections, i[0], i[1])
    try:
        shortest_path = dijkstar.find_path(graph_dijkstar, i[0], i[1])
        g.addEdge(i[0], i[1])
        costs[(i[0], i[1])] = shortest_path[3]
    except:
        pass
    graph_dijkstar = add_nodes_to_graph_dijkstar(inputs, intersections, i[1], i[0])
    try:
        shortest_path = dijkstar.find_path(graph_dijkstar, i[1], i[0])
        g.addEdge(i[1], i[0])
        costs[(i[1], i[0])] = shortest_path[3]
    except:
        pass

results = []
g.printAllPaths(s, d, results)

print('2nd part answer: ' + str(max(results)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
