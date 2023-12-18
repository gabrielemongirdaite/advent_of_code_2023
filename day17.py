import time
import dijkstar
import inspect


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def add_nodes_to_graph(inputs):
    graph = dijkstar.Graph()
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            current_point = y * len(inputs[0]) + x
            if y + 1 <= len(inputs) - 1:
                graph.add_edge(current_point, (y + 1) * len(inputs[0]) + x, int(inputs[y + 1][x]))
            if y - 1 >= 0:
                graph.add_edge(current_point, (y - 1) * len(inputs[0]) + x, int(inputs[y - 1][x]))
            if x + 1 <= len(inputs[0]) - 1:
                graph.add_edge(current_point, y * len(inputs[0]) + x + 1, int(inputs[y][x + 1]))
            if x - 1 >= 0:
                graph.add_edge(current_point, y * len(inputs[0]) + x - 1, int(inputs[y][x - 1]))
    return graph


def find_shortest_paths(graph, all_nodes, starting_point):
    visited_nodes = []
    unvisited_nodes = all_nodes
    dct_paths = {}
    for i in unvisited_nodes:
        dct_paths[i] = [float('inf'), '']
    start_node = starting_point
    dct_paths[start_node] = [0, '']
    while unvisited_nodes:
        distance = float('inf')
        for i in unvisited_nodes:
            if dct_paths[i][0] < distance:
                distance = dct_paths[i][0]
                start_node = i
        for i in graph[start_node]:
            if dct_paths[i][0] > dct_paths[start_node][0] + graph[start_node][i]:
                dct_paths[i][0] = dct_paths[start_node][0] + graph[start_node][i]
                dct_paths[i][1] = start_node
        visited_nodes.append(start_node)
        unvisited_nodes.remove(start_node)
    return dct_paths


# def find_shortest_paths(graph, all_nodes, starting_point):
#     visited_nodes = []
#     unvisited_nodes = all_nodes
#     dct_paths = {}
#     for i in unvisited_nodes:
#         dct_paths[i] = [float('inf'), '', '']
#     start_node = starting_point
#     dct_paths[start_node] = [0, '', '']
#     while unvisited_nodes:
#         distance = float('inf')
#         for i in unvisited_nodes:
#             if dct_paths[i][0] < distance:
#                 distance = dct_paths[i][0]
#                 start_node = i
#         print('start node:', start_node, dct_paths[start_node])
#         for i in graph[start_node]:
#             if dct_paths[i][0] > dct_paths[start_node][0] + graph[start_node][i]:
#                 if len(dct_paths[start_node][2]) < 3:
#                     c = True
#                 else:
#                     str_tmp = ''.join([dct_paths[start_node][2], '<' if start_node - i == 1 else '>' if i - start_node == 1 else 'v' if start_node < i else '^'])
#                     if str_tmp[len(str_tmp)-4:] not in ['>>>>', '<<<<', 'vvvv', '^^^^']:
#                         c = True
#                     else:
#                         c = False
#             else:
#                 c = False
#             print('node of interest:', i, c)
#             if c:
#                 dct_paths[i][0] = dct_paths[start_node][0] + graph[start_node][i]
#                 dct_paths[i][1] = start_node
#                 dct_paths[i][2] += ''.join([dct_paths[start_node][2],
#                                             '<' if start_node - i == 1 else '>' if i - start_node == 1 else 'v' if start_node < i else '^'])
#                 print('updated paths:', dct_paths)
#
#         visited_nodes.append(start_node)
#         unvisited_nodes.remove(start_node)
#         print('visited: ', visited_nodes)
#         print('unvisited: ', unvisited_nodes)
#         print(dct_paths)
#         print('-----')
#     return dct_paths


# graph = dijkstar.Graph()
# graph.add_edge('A', 'B', 2)
# graph.add_edge('B', 'A', 2)
# graph.add_edge('A', 'D', 8)
# graph.add_edge('D', 'A', 8)
# graph.add_edge('B', 'D', 5)
# graph.add_edge('D', 'B', 5)
# graph.add_edge('B', 'E', 6)
# graph.add_edge('E', 'B', 6)
# graph.add_edge('D', 'E', 3)
# graph.add_edge('E', 'D', 3)
# graph.add_edge('D', 'F', 2)
# graph.add_edge('F', 'D', 2)
# graph.add_edge('F', 'E', 1)
# graph.add_edge('E', 'F', 1)
# graph.add_edge('F', 'C', 3)
# graph.add_edge('C', 'F', 3)
# graph.add_edge('C', 'E', 9)
# graph.add_edge('E', 'C', 9)
#
# print(graph)
#
# all_nodes = ['A', 'B', 'C', 'D', 'E', 'F']
#
# print(find_shortest_paths(graph, all_nodes, 'A'))


inputs = read_file('input_day17.txt')
graph = add_nodes_to_graph(inputs)

# print(graph)

all_nodes = []
for i in graph:
    all_nodes.append(i)


print(find_shortest_paths(graph, all_nodes, 0))
print(dijkstar.find_path(graph, 0, 9))
