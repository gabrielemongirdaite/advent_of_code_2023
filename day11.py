import copy
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

    for ind, i in enumerate(rows_to_expand):
        universe.insert(i + ind, '.' * len_row)

    universe_new = copy.deepcopy(universe)
    for ind, i in enumerate(universe):
        strings = []
        for ind2, y in enumerate(columns_to_expand):
            if ind2 == 0:
                strings.append(universe[ind][0:y])
            else:
                strings.append(universe[ind][columns_to_expand[ind2 - 1]: y])

            if y == columns_to_expand[-1]:
                strings.append(universe[ind][y:])
        universe_new[ind] = '.'.join(map(str, strings))
    return universe_new


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


def add_nodes_to_graph(expanded_universe):
    graph = dijkstar.Graph()
    for y, i in enumerate(expanded_universe):
        for x, j in enumerate(i):
            current_point = y * len(expanded_universe) + x
            if path_south(x, y, expanded_universe):
                graph.add_edge(current_point, (y + 1) * len(expanded_universe) + x, 1)
            if path_north(x, y, expanded_universe):
                graph.add_edge(current_point, (y - 1) * len(expanded_universe) + x, 1)
            if path_east(x, y, expanded_universe):
                graph.add_edge(current_point, y * len(expanded_universe) + x + 1, 1)
            if path_west(x, y, expanded_universe):
                graph.add_edge(current_point, y * len(expanded_universe) + x - 1, 1)
    return graph


start_time = time.time()
universe = read_file('input_day11.txt')
new_universe = expand_universe(universe)

graph = add_nodes_to_graph(new_universe)

points = []

for y, i in enumerate(new_universe):
    for x, j in enumerate(i):
        if j == '#':
            points.append(y * len(new_universe) + x)

all_pairs = [(a, b) for idx, a in enumerate(points) for b in points[idx + 1:]]

result = 0
for ind, i in enumerate(all_pairs):
    result += dijkstar.find_path(graph, i[0], i[1])[3]

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

