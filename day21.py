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
                return {(x, y)}


def path_south(x, y, inputs):
    if inputs[(y + 1) % (len(inputs))][x % (len(inputs[0]))] in ['.', 'S']:
        return True
    else:
        return False


def path_north(x, y, inputs):
    if inputs[(y - 1) % (len(inputs))][x % (len(inputs[0]))] in ['.', 'S']:
        return True
    else:
        return False


def path_east(x, y, inputs):
    if inputs[y % (len(inputs))][(x + 1) % (len(inputs[0]))] in ['.', 'S']:
        return True
    else:
        return False


def path_west(x, y, inputs):
    if inputs[y % (len(inputs))][(x - 1) % (len(inputs[0]))] in ['.', 'S']:
        return True
    else:
        return False


def remove_duplicates_in_nested_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def find_gardens(starting_points, inputs, current_step, stop):
    gardens = set()
    for i in starting_points:
        if path_south(i[0], i[1], inputs):
            gardens.add((i[0], i[1] + 1))
        if path_north(i[0], i[1], inputs):
            gardens.add((i[0], i[1] - 1))
        # print(i[0], i[1])
        if path_east(i[0], i[1], inputs):
            gardens.add((i[0] + 1, i[1]))
        if path_west(i[0], i[1], inputs):
            gardens.add((i[0] - 1, i[1]))
    # gardens = remove_duplicates_in_nested_list(gardens)
    starting_points = gardens
    current_step += 1
    if current_step % 131 == 65:
        print(len(gardens))
    return find_gardens(starting_points, inputs, current_step, stop) if current_step < stop else len(gardens)


start_time = time.time()
inputs = read_file('input_day21.txt')
starting_points = find_starting_point(inputs)

print('1st part answer: ' + str(find_gardens(starting_points, inputs, 0, 64)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
find_gardens(starting_points, inputs, 0, 65 + 131 * 2 + 1)
x_input = (26501365 - 65)/131
# https://www.wolframalpha.com/input?i=fit+polynomial&assumption=%7B%22F%22%2C+%22InterpolatingPolynomialCalculator%22%2C+%22data2%22%7D+-%3E%22%7B%7B0%2C3755%7D%2C%7B1%2C33494%7D%2C%7B2%2C92811%7D%7D%22
print('2nd part answer: ' + str(3755 + 14950*x_input + 14789*x_input**2))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
