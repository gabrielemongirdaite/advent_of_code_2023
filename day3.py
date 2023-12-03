import time
import re


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_symbols(lines):
    coordinates = []
    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            if not j.isdigit() and j != '.':
                coordinates.append([x, y])
    return coordinates


def adjacent_coordinates_for_number(x, y, number):
    len_number = len(str(number))
    coord = []
    for i in range(-1, len_number + 1):
        coord.append([x + i, y - 1])
        coord.append([x + i, y + 1])
    coord.append([x - 1, y])
    coord.append([x + len_number, y])
    return coord


def coordinates_for_number(x, y, number):
    len_number = len(str(number))
    coord = []
    for i in range(0, len_number):
        coord.append([x + i, y])
    return coord


def find_numbers(lines):
    number_coord_part1 = []
    number_coord_part2 = []
    for y, i in enumerate(lines):
        d = {m.start(0): int(m.group(0)) for m in re.finditer("\d+", i)}
        for x in d:
            number_coord_part1.append([d[x], adjacent_coordinates_for_number(x, y, d[x])])
            number_coord_part2.append([d[x], coordinates_for_number(x, y, d[x])])
    return number_coord_part1, number_coord_part2


def adjacent_to_symbol(numbers, symbols):
    result = 0
    for i in numbers:
        for j in i[1]:
            if j in symbols:
                result += int(i[0])
    return result


def find_stars_adjacent(lines):
    coordinates = []
    star = 0
    for y, i in enumerate(lines):
        for x, j in enumerate(i):
            if j == '*':
                coordinates.append([star, adjacent_coordinates_for_number(x, y, '*')])
                star += 1
    return coordinates


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def adjacent_to_stars(numbers, stars):
    result = 0
    for i in stars:
        r = 0
        num = []
        for k in numbers:
            if intersection(i[1], k[1]) != []:
                r += 1
                num.append(k[0])
        if r == 2:
            result += num[0] * num[1]
    return result


start_time = time.time()
lines = read_file("input_day3.txt")
numbers = find_numbers(lines)[0]
symbols = find_symbols(lines)
print('1st part answer: ' + str(adjacent_to_symbol(numbers, symbols)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
stars = find_stars_adjacent(lines)
numbers_part2 = find_numbers(lines)[1]
print('2nd part answer: ' + str(adjacent_to_stars(numbers_part2, stars)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
