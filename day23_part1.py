import time
from collections import defaultdict
import sys
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
            # print(len(path)-1)
            results.append(len(path)-1)
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
        if inputs[y][x] == 'v':
            return True
        elif inputs[y][x] in ['^', '>', '<']:
            return False
        elif inputs[y + 1][x] in ['.', 'v', '^', '>', '<']:
            return True
        else:
            return False
    else:
        return False


def path_north(x, y, inputs):
    if y >= 1:
        if inputs[y][x] == '^':
            return True
        elif inputs[y][x] in ['v', '>', '<']:
            return False
        elif inputs[y - 1][x] in ['.', 'v', '^', '>', '<']:
            return True
        else:
            return False
    else:
        return False


def path_east(x, y, inputs):
    if x < len(inputs[0]) - 1:
        if inputs[y][x] == '>':
            return True
        elif inputs[y][x] in ['^', 'v', '<']:
            return False
        elif inputs[y][x + 1] in ['.', 'v', '^', '>', '<']:
            return True
        else:
            return False
    else:
        return False


def path_west(x, y, inputs):
    if x >= 1:
        if inputs[y][x] == '<':
            return True
        elif inputs[y][x] in ['^', 'v', '>']:
            return False
        elif inputs[y][x - 1] in ['.', 'v', '^', '>', '<']:
            return True
        else:
            return False
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


def create_graph(inputs, vertices):
    g = Graph(vertices)
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            if j != '#':
                current_point = y * len(inputs[0]) + x
                if path_south(x, y, inputs):
                    # print('going south:', current_point, (y + 1) * len(inputs[0]) + x)
                    g.addEdge(current_point, (y + 1) * len(inputs[0]) + x)
                if path_north(x, y, inputs):
                    # print('going north:', current_point, (y - 1) * len(inputs[0]) + x)
                    g.addEdge(current_point, (y - 1) * len(inputs[0]) + x)
                if path_east(x, y, inputs):
                    # print('going east:', current_point, y * len(inputs[0]) + x + 1)
                    g.addEdge(current_point, y * len(inputs[0]) + x + 1)
                if path_west(x, y, inputs):
                    # print('going west:', current_point,  y * len(inputs[0]) + x - 1)
                    g.addEdge(current_point, y * len(inputs[0]) + x - 1)
    return g


start_time = time.time()
inputs = read_file('input_day23.txt')
vert, all_vert = count_vertices(inputs)
g = create_graph(inputs, len(inputs)*len(inputs[0]))

s, d = min(all_vert), max(all_vert)
results = []
g.printAllPaths(s, d, results)

print('1st part answer: ' + str(max(results)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))
