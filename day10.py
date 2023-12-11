import time
import dijkstar


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


# south, north, east, west
moves_dict = {}
moves_dict['|'] = [['L', 'J', '|'], ['7', 'F', '|'], [], []]
moves_dict['-'] = [[], [], ['7', 'J', '-'], ['L', 'F', '-']]
moves_dict['L'] = [[], ['7', 'F', '|'], ['J', '7', '-'], []]
moves_dict['J'] = [[], ['7', 'F', '|'], [], ['L', 'F', '-']]
moves_dict['7'] = [['L', 'J', '|'], [], [], ['L', 'F', '-']]
moves_dict['F'] = [['L', 'J', '|'], [], ['7', 'J', '-'], []]
moves_dict['.'] = [[], [], [], []]
starting_pipe = '7'  # 'F'  # '7'

vertical_left = ['|', 'J', '7']
vertical_right = ['|', 'L', 'F']
horizontal_above = ['-', 'J', 'L']
horizontal_below = ['-', '7', 'F']


def path_south(x, y, pipes):
    current_pipe = pipes[y][x]
    if current_pipe == 'S':
        current_pipe = starting_pipe
    if y < len(pipes) - 1:
        pipe = pipes[y + 1][x]
        if pipe == 'S':
            pipe = starting_pipe
        return pipe in moves_dict[current_pipe][0]
    else:
        return False


def path_north(x, y, pipes):
    current_pipe = pipes[y][x]
    if current_pipe == 'S':
        current_pipe = starting_pipe
    if y >= 1:
        pipe = pipes[y - 1][x]
        if pipe == 'S':
            pipe = starting_pipe
        return pipe in moves_dict[current_pipe][1]
    else:
        return False


def path_east(x, y, pipes):
    current_pipe = pipes[y][x]
    if current_pipe == 'S':
        current_pipe = starting_pipe
    if x < len(pipes[0]) - 1:
        pipe = pipes[y][x + 1]
        if pipe == 'S':
            pipe = starting_pipe
        return pipe in moves_dict[current_pipe][2]
    else:
        return False


def path_west(x, y, pipes):
    current_pipe = pipes[y][x]
    if current_pipe == 'S':
        current_pipe = starting_pipe
    if x >= 1:
        pipe = pipes[y][x - 1]
        if pipe == 'S':
            pipe = starting_pipe
        return pipe in moves_dict[current_pipe][3]
    else:
        return False


def add_nodes_to_graph(pipes):
    graph = dijkstar.Graph()
    for y, i in enumerate(pipes):
        for x, j in enumerate(i):
            current_point = y * len(pipes) + x
            if path_south(x, y, pipes):
                graph.add_edge(current_point, (y + 1) * len(pipes) + x, 1)
            if path_north(x, y, pipes):
                graph.add_edge(current_point, (y - 1) * len(pipes) + x, 1)
            if path_east(x, y, pipes):
                graph.add_edge(current_point, y * len(pipes) + x + 1, 1)
            if path_west(x, y, pipes):
                graph.add_edge(current_point, y * len(pipes) + x - 1, 1)
    return graph


def add_nodes_to_graph_part_2(full_path, pipes):
    graph = dijkstar.Graph()
    for y in range(0, len(pipes) + 1):
        for x in range(0, len(pipes[0]) + 1):
            current_point = y * len(pipes) + x
            if current_point not in full_path:
                # print('point', y, x)
                above_point = (y - 1) * len(pipes) + x
                below_point = (y + 1) * len(pipes) + x
                right_point = y * len(pipes) + x + 1
                left_point = y * len(pipes) + x - 1
                above_right_point = (y - 1) * len(pipes) + x + 1
                above_left_point = (y - 1) * len(pipes) + x - 1
                below_right_point = (y + 1) * len(pipes) + x + 1
                below_left_point = (y + 1) * len(pipes) + x - 1
                if above_point not in full_path:
                    graph.add_edge(current_point, above_point, 1)
                    # print('added', (y - 1), x)
                else:
                    current_point1 = current_point
                    above_point1 = above_point
                    above_right_point1 = above_right_point
                    while above_point1 in full_path and above_right_point1 in full_path:
                        y1 = above_point1 // len(pipes)
                        x1 = above_point1 % len(pipes)
                        y2 = above_right_point1 // len(pipes)
                        x2 = above_right_point1 % len(pipes)
                        added = 0
                        if pipes[y1][x1] in vertical_left and pipes[y2][x2] in vertical_right:
                            graph.add_edge(current_point1, above_point1, 1)
                            # print('added (extended)', above_point1 // len(pipes), x)
                            added = 1
                        current_point1 = above_point1
                        y1 = current_point1 // len(pipes)
                        x1 = current_point1 % len(pipes)
                        above_point1 = (y1 - 1) * len(pipes) + x1
                        above_right_point1 = (y1 - 1) * len(pipes) + x1 + 1
                    if above_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, above_point1, 1)
                        # print('added (extended)', above_point1 // len(pipes), x)
                    if above_right_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, above_right_point1, 1)
                        # print('added (extended)', above_right_point1 // len(pipes), x + 1)
                if below_point not in full_path:
                    graph.add_edge(current_point, below_point, 1)
                    # print('added', (y + 1), x)
                else:
                    current_point1 = current_point
                    below_point1 = below_point
                    below_right_point1 = below_right_point
                    while below_point1 in full_path and below_right_point1 in full_path:
                        # print('+')
                        y1 = below_point1 // len(pipes)
                        x1 = below_point1 % len(pipes)
                        y2 = below_right_point1 // len(pipes)
                        x2 = below_right_point1 % len(pipes)
                        added = 0
                        if pipes[y1][x1] in vertical_left and pipes[y2][x2] in vertical_right:
                            graph.add_edge(current_point1, below_point1, 1)
                            # print('added (extended)', below_point1 // len(pipes), x)
                            added = 1
                        current_point1 = below_point1
                        y1 = current_point1 // len(pipes)
                        x1 = current_point1 % len(pipes)
                        below_point1 = (y1 + 1) * len(pipes) + x1
                        below_right_point1 = (y1 + 1) * len(pipes) + x1 + 1
                    if below_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, below_point1, 1)
                    if below_right_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, below_right_point1, 1)
                if right_point not in full_path:
                    graph.add_edge(current_point, right_point, 1)
                    # print('added', y, x + 1)
                else:
                    current_point1 = current_point
                    right_point1 = right_point
                    below_right_point1 = below_right_point
                    while right_point1 in full_path and below_right_point1 in full_path:
                        y1 = right_point1 // len(pipes)
                        x1 = right_point1 % len(pipes)
                        y2 = below_right_point1 // len(pipes)
                        x2 = below_right_point1 % len(pipes)
                        added = 0
                        if pipes[y1][x1] in horizontal_above and pipes[y2][x2] in horizontal_below:
                            graph.add_edge(current_point1, right_point1, 1)
                            # print('added (extended)', y, right_point1 % len(pipes[0]))
                            added = 1
                        current_point1 = right_point1
                        y1 = current_point1 // len(pipes)
                        x1 = current_point1 % len(pipes)
                        right_point1 = y1 * len(pipes) + x1 + 1
                        below_right_point1 = (y1 + 1) * len(pipes) + x1 + 1
                    if right_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, right_point1, 1)
                    if below_right_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, below_right_point1, 1)

                if left_point not in full_path:
                    graph.add_edge(current_point, left_point, 1)
                    # print('added', y, x - 1)
                else:
                    current_point1 = current_point
                    left_point1 = left_point
                    below_left_point1 = below_left_point
                    while left_point1 in full_path and below_left_point1 in full_path:
                        y1 = left_point1 // len(pipes)
                        x1 = left_point1 % len(pipes)
                        y2 = below_left_point1 // len(pipes)
                        x2 = below_left_point1 % len(pipes)
                        added = 0
                        if pipes[y1][x1] in horizontal_above and pipes[y2][x2] in horizontal_below:
                            graph.add_edge(current_point1, left_point1, 1)
                            # print('added (extended)', y, left_point1 % len(pipes[0]))
                            added = 1
                        current_point1 = left_point1
                        y1 = current_point1 // len(pipes)
                        x1 = current_point1 % len(pipes)
                        left_point1 = y1 * len(pipes) + x1 - 1
                        below_left_point1 = (y1 + 1) * len(pipes) + x1 - 1
                    if left_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, left_point1, 1)
                    if below_left_point1 not in full_path and added == 1:
                        graph.add_edge(current_point1, below_left_point1, 1)
                if above_right_point not in full_path:
                    graph.add_edge(current_point, above_right_point, 1)
                    # print('added', y - 1, x + 1)
                if above_left_point not in full_path:
                    graph.add_edge(current_point, above_left_point, 1)
                    # print('added', y - 1, x - 1)
                if below_right_point not in full_path:
                    graph.add_edge(current_point, below_right_point, 1)
                    # print('added', y + 1, x + 1)
                if below_left_point not in full_path:
                    graph.add_edge(current_point, below_left_point, 1)
                    # print('added', y + 1, x - 1)
    return graph


# start_time = time.time()
pipes = read_file('input_day10.txt')
for y, pipe in enumerate(pipes):
    for x, p in enumerate(pipe):
        if p == 'S':
            start_x, start_y = x, y

graph_part1 = add_nodes_to_graph(pipes)

starting_point = start_y * len(pipes) + start_x
# in_path = 0
# paths = []
#
# for y, i in enumerate(pipes):
#     for x, j in enumerate(i):
#         ending_point = y * len(pipes) + x
#         try:
#             paths.append(dijkstar.find_path(graph_part1, starting_point, ending_point))
#             in_path += 1
#         except:
#             pass
# print('1st part answer: ' + str(in_path / 2))
# print("--- %s seconds for 1st part---" % (time.time() - start_time))

# taken from paths, where third value equals to in_path/2 or in_path/2-1
furthest_point = 7521
before_1 = 7520
before_2 = 7661


full_path = dijkstar.find_path(graph_part1, starting_point, furthest_point)[0]
full_path_part2 = dijkstar.find_path(graph_part1, before_2, starting_point)[0]
full_path.extend(full_path_part2)

points = []
for i in full_path:
    y = i // len(pipes)
    x = i % len(pipes)
    points.append([x, y])

min_x = min(points, key=lambda z: z[0])[0]
max_x = max(points, key=lambda z: z[0])[0]
min_y = min(points, key=lambda z: z[1])[1]
max_y = max(points, key=lambda z: z[1])[1]

graph_part2 = add_nodes_to_graph_part_2(full_path, pipes)
# print(graph_part2)

end_point_2 = 0
r = 0
holes = []
for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
        start_point = y * len(pipes) + x
        if start_point not in full_path:
            try:
                dijkstar.find_path(graph_part2, start_point, end_point_2)
            except:
                r += 1
                holes.append([x, y])
print(r)

# import matplotlib.pyplot as plt
#
# xs, ys = zip(*points)  # create lists of x and y values
#
# plt.figure()
# plt.plot(xs, ys)
# plt.show()


import matplotlib as mlib
import matplotlib.pyplot as plt
import numpy as np


def plot_colored_grid(data, colors=['white', 'green'], bounds=[0, 0.5, 1], grid=False, labels=False, frame=True):
    """Plot 2d matrix with grid with well-defined colors for specific boundary values.

    :param data: 2d matrix
    :param colors: colors
    :param bounds: bounds between which the respective color will be plotted
    :param grid: whether grid should be plotted
    :param labels: whether labels should be plotted
    :param frame: whether frame should be plotted
    """

    # create discrete colormap
    cmap = mlib.colors.ListedColormap(colors)
    norm = mlib.colors.BoundaryNorm(bounds, cmap.N)

    # enable or disable frame
    plt.figure(frameon=frame)

    # show grid
    if grid:
        plt.grid(axis='both', color='k', linewidth=1)
        plt.xticks(np.arange(0.5, data.shape[1], 1))  # correct grid sizes
        plt.yticks(np.arange(0.5, data.shape[0], 1))

    # disable labels
    if not labels:
        plt.tick_params(bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)
    # plot data matrix
    plt.imshow(data, cmap=cmap, norm=norm)

    xs, ys = zip(*points)  # create lists of x and y values
    plt.plot(xs, ys)
    # display main axis
    plt.show()


points_boolean = []

for y, i in enumerate(pipes):
    tmp = []
    for x, j in enumerate(i):
        if [x, y] in holes:
            tmp.append(True)
        else:
            tmp.append(False)
    points_boolean.append(tmp)

plot_colored_grid(np.array(points_boolean))