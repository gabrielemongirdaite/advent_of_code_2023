import time
from operator import itemgetter
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    direction, length, colors = [], [], []
    for i in lines:
        line_tmp = i.split(' ')
        direction.append(line_tmp[0])
        length.append(int(line_tmp[1]))
        colors.append(line_tmp[2])
    return direction, length, colors


def remove_duplicates_in_nested_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def define_perimeter(direction, length):
    coordinates = [(0, 0)]
    for ind, i in enumerate(direction):
        starting_point = coordinates[-1]
        for k in range(1, length[ind] + 1):
            if i == 'U':
                coordinates.append((starting_point[0], starting_point[1] - k))
            elif i == 'D':
                coordinates.append((starting_point[0], starting_point[1] + k))
            elif i == 'L':
                coordinates.append((starting_point[0] - k, starting_point[1]))
            else:
                coordinates.append((starting_point[0] + k, starting_point[1]))
    return coordinates


def find_difference(sequence):
    return [j[0] - i[0] for i, j in zip(sequence[:-1], sequence[1:])]


def check_if_open(group, polygon):
    c = False
    point = Point(group[0][0] + 1, group[0][1])
    if polygon.contains(point):
        c = True
    return c


def count_cubes(coord, polygon):
    coord_by_row = []
    step = 0
    for i in range(min_y, max_y + 1):
        x_tmp = []
        while step < len(coord) and coord[step][1] == i:
            x_tmp.append([coord[step][0], i])
            step += 1
        coord_by_row.append(x_tmp)
    all_groups = []
    for i in coord_by_row:
        groups = []
        diff = find_difference(i)
        group = [i[0]]
        for ind, k in enumerate(diff):
            if k == 1:
                group.append(i[ind + 1])
            else:
                if len(group) == 1:
                    group.append(i[ind + 1])
                    groups.append(group)
                    group = [i[ind + 1]]
                else:
                    groups.append(group)
                    group = [i[ind], i[ind + 1]]
                    groups.append(group)
                    group = [i[ind + 1]]
        if k == 1:
            groups.append(group)
        all_groups.append(groups)
        cubes = 0
    for i in all_groups:
        for ind, k in enumerate(i):
            if check_if_open(k, polygon):
                d = k[-1][0] - k[0][0] - 1
                cubes += d
    return cubes


def convert_hex_to_int(hex):
    return int(hex, 16)


def part2_direction_length(colors):
    dir = []
    length = []
    for i in colors:
        length.append(convert_hex_to_int(i[2:7]))
        dir.append('R' if i[-2] == '0' else 'D' if i[-2] == '1' else 'L' if i[-2] == '2' else 'U')
    return dir, length


start_time = time.time()
direction, length, colors = read_file('input_day18.txt')
coordinates = define_perimeter(direction, length)
old_coordinates = coordinates
polygon = Polygon(old_coordinates)

coordinates = sorted(coordinates, key=itemgetter(1, 0))

min_y = min([i[1] for i in old_coordinates])
max_y = max([i[1] for i in old_coordinates])

cubes = count_cubes(coordinates, polygon)

print('1st part answer: ' + str(cubes + len(coordinates)-1))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


# start_time = time.time()
# direction, length = part2_direction_length(colors)
# coordinates = define_perimeter(direction, length)
# old_coordinates = coordinates
# polygon = Polygon(old_coordinates)
# print('here')
# coordinates = sorted(coordinates, key=itemgetter(1, 0))
#
# min_y = min([i[1] for i in old_coordinates])
# max_y = max([i[1] for i in old_coordinates])
#
# cubes = count_cubes(coordinates, polygon)
# print('2nd part answer: ' + str(cubes + len(coordinates)-1))
# print("--- %s seconds for 2nd part---" % (time.time() - start_time))
