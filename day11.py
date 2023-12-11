import time
import dijkstar


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def expand_universe(universe):
    len_row = len(universe[0])
    len_column = len(universe)
    rows_to_expand = []
    columns_to_expand = []
    columns = []
    for y, i in enumerate(universe):
        if i == '.' * len_row:
            rows_to_expand.append(y)
    for y, i in enumerate(universe):
        for x, j in enumerate(i):
            if y == 0:
                columns.append(j)
            else:
                columns[x] = columns[x] + j
    for x, i in enumerate(columns):
        if i == '.' * len_column:
            columns_to_expand.append(x)
    return rows_to_expand, columns_to_expand


def path_south(x, y, expanded_universe):
    if y < len(expanded_universe) - 1:
        return True
    else:
        return False


def path_north(x, y, expanded_universe):
    if y >= 1:
        return True
    else:
        return False


def path_east(x, y, expanded_universe):
    if x < len(expanded_universe[0]) - 1:
        return True
    else:
        return False


def path_west(x, y, expanded_universe):
    if x >= 1:
        return True
    else:
        return False


def add_nodes_to_graph(expanded_universe, rows_expand, columns_expand, expansion):
    graph = dijkstar.Graph()
    for y, i in enumerate(expanded_universe):
        for x, j in enumerate(i):
            current_point = y * len(expanded_universe) + x
            if path_south(x, y, expanded_universe):
                if y in rows_expand:
                    graph.add_edge(current_point, (y + 1) * len(expanded_universe) + x, 1 + expansion)
                else:
                    graph.add_edge(current_point, (y + 1) * len(expanded_universe) + x, 1)
            if path_north(x, y, expanded_universe):
                if y - 1 in rows_expand:
                    graph.add_edge(current_point, (y - 1) * len(expanded_universe) + x, 1 + expansion)
                else:
                    graph.add_edge(current_point, (y - 1) * len(expanded_universe) + x, 1)
            if path_east(x, y, expanded_universe):
                if x in columns_expand:
                    graph.add_edge(current_point, y * len(expanded_universe) + x + 1, 1 + expansion)
                else:
                    graph.add_edge(current_point, y * len(expanded_universe) + x + 1, 1)
            if path_west(x, y, expanded_universe):
                if x-1 in columns_expand:
                    graph.add_edge(current_point, y * len(expanded_universe) + x - 1, 1 + expansion)
                else:
                    graph.add_edge(current_point, y * len(expanded_universe) + x - 1, 1)
    return graph


start_time = time.time()
universe = read_file('input_day11.txt')

rows_expand, columns_expand = expand_universe(universe)

graph = add_nodes_to_graph(universe, rows_expand, columns_expand, 1)

points = []

for y, i in enumerate(universe):
    for x, j in enumerate(i):
        if j == '#':
            points.append(y * len(universe) + x)

all_pairs = [(a, b) for idx, a in enumerate(points) for b in points[idx + 1:]]

result = 0
for ind, i in enumerate(all_pairs):
    result += dijkstar.find_path(graph, i[0], i[1])[3]

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()

graph_part2 = add_nodes_to_graph(universe, rows_expand, columns_expand, 999999)

result = 0
for ind, i in enumerate(all_pairs):
    result += dijkstar.find_path(graph_part2, i[0], i[1])[3]

print('2nd part answer: ' + str(result))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))