import time
from functools import cache


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_starting_point(inputs):
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            if inputs[y][x] == 'S':
                return [(x, y)]


def path_south(x, y, inputs):
    if y + 1 < len(inputs) and inputs[y + 1][x] in ['.', 'S']:
        return True
    else:
        return False


def path_north(x, y, inputs):
    if y - 1 >= 0 and inputs[y - 1][x] in ['.', 'S']:
        return True
    else:
        return False


def path_east(x, y, inputs):
    if x + 1 < len(inputs[0]) and inputs[y][x + 1] in ['.', 'S']:
        return True
    else:
        return False


def path_west(x, y, inputs):
    if x - 1 >= 0 and inputs[y][x - 1] in ['.', 'S']:
        return True
    else:
        return False


def remove_duplicates_in_nested_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def find_gardens(starting_points, inputs, current_step):
    gardens = []
    for i in starting_points:
        if path_south(i[0], i[1], inputs):
            gardens.append((i[0], i[1] + 1))
        if path_north(i[0], i[1], inputs):
            gardens.append((i[0], i[1] - 1))
        if path_east(i[0], i[1], inputs):
            gardens.append((i[0] + 1, i[1]))
        if path_west(i[0], i[1], inputs):
            gardens.append((i[0] - 1, i[1]))
    gardens = remove_duplicates_in_nested_list(gardens)
    starting_points = gardens
    current_step += 1
    return find_gardens(starting_points, inputs, current_step) if current_step < 64 else len(gardens)


start_time = time.time()
inputs = read_file('input_day21.txt')
starting_points = find_starting_point(inputs)

print('1st part answer: ' + str(find_gardens(starting_points, inputs, 0)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

