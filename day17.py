import time
import dijkstar
from itertools import product


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def add_nodes_to_graph(inputs, min_steps, max_steps):
    graph = dijkstar.Graph()
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            for direction in ['^', 'v', '>', '<']:
                current_point = str(y * len(inputs[0]) + x) + direction
                if direction in ['^', 'v']:  # possible to go > and <
                    cost = 0
                    for k in range(1, min_steps):
                        if x + k <= len(inputs[0]) - 1:
                            cost += int(inputs[y][x + k])
                    for k in range(min_steps, max_steps + 1):
                        if x + k <= len(inputs[0]) - 1:
                            cost += int(inputs[y][x + k])
                            graph.add_edge(current_point, str(y * len(inputs[0]) + x + k) + '>', cost)
                    cost = 0
                    for k in range(1, min_steps):
                        if x - k >= 0:
                            cost += int(inputs[y][x - k])
                    for k in range(min_steps, max_steps + 1):
                        if x - k >= 0:
                            cost += int(inputs[y][x - k])
                            graph.add_edge(current_point, str(y * len(inputs[0]) + x - k) + '<', cost)
                else:  # possible to go ^ and v
                    cost = 0
                    for k in range(1, min_steps):
                        if y + k <= len(inputs) - 1:
                            cost += int(inputs[y + k][x])
                    for k in range(min_steps, max_steps + 1):
                        if y + k <= len(inputs) - 1:
                            cost += int(inputs[y + k][x])
                            graph.add_edge(current_point, str((y + k) * len(inputs[0]) + x) + 'v', cost)
                    cost = 0
                    for k in range(1, min_steps):
                        if y - k >= 0:
                            cost += int(inputs[y - k][x])
                    for k in range(min_steps, max_steps + 1):
                        if y - k >= 0:
                            cost += int(inputs[y - k][x])
                            graph.add_edge(current_point, str((y - k) * len(inputs[0]) + x) + '^', cost)
    return graph


start_time = time.time()
inputs = read_file('input_day17.txt')
graph = add_nodes_to_graph(inputs, 1, 3)

all_possibilities = []
start_point = ['0']
start_direction = ['^', 'v', '>', '<']
end_point = ['19880']
end_direction = ['^', 'v', '>', '<']

for i in [x + y for x, y in product(start_point, start_direction)]:
    for j in [x + y for x, y in product(end_point, end_direction)]:
        try:
            all_possibilities.append(dijkstar.find_path(graph, i, j)[3])
        except:
            pass

print('1st part answer: ' + str(min(all_possibilities)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
graph = add_nodes_to_graph(inputs, 4, 10)

all_possibilities = []
start_point = ['0']
start_direction = ['^', 'v', '>', '<']
end_point = ['19880']
end_direction = ['^', 'v', '>', '<']

for i in [x + y for x, y in product(start_point, start_direction)]:
    for j in [x + y for x, y in product(end_point, end_direction)]:
        try:
            all_possibilities.append(dijkstar.find_path(graph, i, j)[3])
        except:
            pass

print('2nd part answer: ' + str(min(all_possibilities)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))