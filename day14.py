import time
from operator import itemgetter
import re


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_columns(inputs):
    columns = []
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            if y == 0:
                columns.append(j)
            else:
                columns[x] = columns[x] + j
    return columns


def find_empty_spots_in_every_column(columns, sign):
    empty_spots = []
    for x, i in enumerate(columns):
        for y, j in enumerate(i):
            if j == sign:
                empty_spots.append([x, y])
    return empty_spots


def tilt_north(empty_spots, immovable_rocks, rocks):
    rocks = sorted(rocks, key=itemgetter(1))
    rocks_spots = []
    for i in rocks:
        possible_spots = [k for k in empty_spots if k[0] == i[0] and k[1] < i[1]]
        immovable_rock = [k for k in immovable_rocks if k[0] == i[0] and k[1] < i[1]]
        if not possible_spots:
            rocks_spots.append(i)
        elif not immovable_rock:
            new_spot = min(possible_spots)
            rocks_spots.append(new_spot)
            empty_spots.remove(new_spot)
            empty_spots.append(i)
        else:
            closest_immovable_rock = max(immovable_rock)
            possible_spots = [k for k in possible_spots if k[1] > closest_immovable_rock[1]]
            if not possible_spots:
                rocks_spots.append(i)
            else:
                new_spot = min(possible_spots)
                rocks_spots.append(new_spot)
                empty_spots.remove(new_spot)
                empty_spots.append(i)
    return rocks_spots, empty_spots


def tilt_south(empty_spots, immovable_rocks, rocks):
    rocks = sorted(rocks, key=itemgetter(1), reverse=True)
    rocks_spots = []
    for i in rocks:
        possible_spots = [k for k in empty_spots if k[0] == i[0] and k[1] > i[1]]
        immovable_rock = [k for k in immovable_rocks if k[0] == i[0] and k[1] > i[1]]
        if not possible_spots:
            rocks_spots.append(i)
        elif not immovable_rock:
            new_spot = max(possible_spots)
            rocks_spots.append(new_spot)
            empty_spots.remove(new_spot)
            empty_spots.append(i)
        else:
            closest_immovable_rock = min(immovable_rock)
            possible_spots = [k for k in possible_spots if k[1] < closest_immovable_rock[1]]
            if not possible_spots:
                rocks_spots.append(i)
            else:
                new_spot = max(possible_spots)
                rocks_spots.append(new_spot)
                empty_spots.remove(new_spot)
                empty_spots.append(i)
    return rocks_spots, empty_spots


def tilt_west(empty_spots, immovable_rocks, rocks):
    rocks = sorted(rocks, key=itemgetter(0))
    rocks_spots = []
    for i in rocks:
        possible_spots = [k for k in empty_spots if k[1] == i[1] and k[0] < i[0]]
        immovable_rock = [k for k in immovable_rocks if k[1] == i[1] and k[0] < i[0]]
        if not possible_spots:
            rocks_spots.append(i)
        elif not immovable_rock:
            new_spot = min(possible_spots)
            rocks_spots.append(new_spot)
            empty_spots.remove(new_spot)
            empty_spots.append(i)
        else:
            closest_immovable_rock = max(immovable_rock)
            possible_spots = [k for k in possible_spots if k[0] > closest_immovable_rock[0]]
            if not possible_spots:
                rocks_spots.append(i)
            else:
                new_spot = min(possible_spots)
                rocks_spots.append(new_spot)
                empty_spots.remove(new_spot)
                empty_spots.append(i)
    return rocks_spots, empty_spots


def tilt_east(empty_spots, immovable_rocks, rocks):
    rocks = sorted(rocks, key=itemgetter(0), reverse=True)
    rocks_spots = []
    for i in rocks:
        possible_spots = [k for k in empty_spots if k[1] == i[1] and k[0] > i[0]]
        immovable_rock = [k for k in immovable_rocks if k[1] == i[1] and k[0] > i[0]]
        if not possible_spots:
            rocks_spots.append(i)
        elif not immovable_rock:
            new_spot = max(possible_spots)
            rocks_spots.append(new_spot)
            empty_spots.remove(new_spot)
            empty_spots.append(i)
        else:
            closest_immovable_rock = min(immovable_rock)
            possible_spots = [k for k in possible_spots if k[0] < closest_immovable_rock[0]]
            if not possible_spots:
                rocks_spots.append(i)
            else:
                new_spot = max(possible_spots)
                rocks_spots.append(new_spot)
                empty_spots.remove(new_spot)
                empty_spots.append(i)
    return rocks_spots, empty_spots


start_time = time.time()
all_rows = read_file('input_day14.txt')
all_columns = find_columns(all_rows)
empty_spots = find_empty_spots_in_every_column(all_columns, '.')
immovable_rocks = find_empty_spots_in_every_column(all_columns, '#')
rocks = find_empty_spots_in_every_column(all_columns, 'O')

initial_rocks_mapping = {}
for i in rocks:
    initial_rocks_mapping[(i[0], i[1])] = [i]

rocks_spots = tilt_north(empty_spots, immovable_rocks, rocks)[0]

result = 0
num_rows = len(all_rows)
for i in rocks_spots:
    result += num_rows - i[1]

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
empty_spots = find_empty_spots_in_every_column(all_columns, '.')
immovable_rocks = find_empty_spots_in_every_column(all_columns, '#')
rocks = find_empty_spots_in_every_column(all_columns, 'O')


seen_rocks = [rocks]
for i in range(1000000000):
    print(i)
    rocks, empty_spots = tilt_north(empty_spots, immovable_rocks, rocks)
    rocks, empty_spots = tilt_west(empty_spots, immovable_rocks, rocks)
    rocks, empty_spots = tilt_south(empty_spots, immovable_rocks, rocks)
    rocks, empty_spots = tilt_east(empty_spots, immovable_rocks, rocks)
    rocks.sort()
    if rocks in seen_rocks:
        how_many_to_skip = seen_rocks.index(rocks)
        pattern_length = i + 1 - how_many_to_skip
        break
    seen_rocks.append(rocks)

num_rows = len(all_rows)
result = 0
for i in seen_rocks[how_many_to_skip + (1000000000 - how_many_to_skip) % pattern_length]:
    result += num_rows - i[1]

print('2nd part answer: ' + str(result))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
