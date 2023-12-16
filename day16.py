import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def beam_direction(x, y, max_x, max_y, current_direction, inputs):
    new_triplet = []
    energized_tiles = []
    if x == -1 or y == -1 or x == max_x + 1 or y == max_y + 1:
        c = True
    elif inputs[y][x] == '.':
        c = True
    else:
        c = False
    if c:
        # print('test ', inputs[y][x], y, x, current_direction)
        if current_direction == '>':
            if x + 1 <= max_x:
                new_x = x + 1
                if inputs[y][x + 1] == '.' or inputs[y][x + 1] == '-':
                    new_y = y
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y][x + 1] == '\\':
                    energized_tiles.append([new_x, y])
                    if y + 1 <= max_y:
                        new_y = y + 1
                        new_direction = 'v'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y][x + 1] == '/':
                    energized_tiles.append([new_x, y])
                    if y - 1 >= 0:
                        new_y = y - 1
                        new_direction = '^'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y][x + 1] == '|':
                    energized_tiles.append([new_x, y])
                    if y - 1 >= 0:
                        new_y = y - 1
                        new_direction = '^'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                    if y + 1 <= max_y:
                        new_y = y + 1
                        new_direction = 'v'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
        elif current_direction == '<':
            if x - 1 >= 0:
                new_x = x - 1
                if inputs[y][x - 1] == '.' or inputs[y][x - 1] == '-':
                    new_y = y
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y][x - 1] == '\\':
                    energized_tiles.append([new_x, y])
                    if y - 1 >= 0:
                        new_y = y - 1
                        new_direction = '^'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y][x - 1] == '/':
                    energized_tiles.append([new_x, y])
                    if y + 1 <= max_y:
                        new_y = y + 1
                        new_direction = 'v'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y][x - 1] == '|':
                    energized_tiles.append([new_x, y])
                    if y - 1 >= 0:
                        new_y = y - 1
                        new_direction = '^'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                    if y + 1 <= max_y:
                        new_y = y + 1
                        new_direction = 'v'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
        elif current_direction == '^':
            if y - 1 >= 0:
                new_y = y - 1
                if inputs[y - 1][x] == '.' or inputs[y - 1][x] == '|':
                    new_x = x
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y - 1][x] == '\\':
                    energized_tiles.append([x, new_y])
                    if x - 1 >= 0:
                        new_x = x - 1
                        new_direction = '<'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y - 1][x] == '/':
                    energized_tiles.append([x, new_y])
                    if x + 1 <= max_x:
                        new_x = x + 1
                        new_direction = '>'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y - 1][x] == '-':
                    energized_tiles.append([x, new_y])
                    if x - 1 >= 0:
                        new_x = x - 1
                        new_direction = '<'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                    if x + 1 <= max_x:
                        new_x = x + 1
                        new_direction = '>'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
        else:
            if y + 1 <= max_y:
                new_y = y + 1
                # print('test 2:', inputs[y + 1][x])
                if inputs[y + 1][x] == '.' or inputs[y + 1][x] == '|':
                    new_x = x
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y + 1][x] == '\\':
                    energized_tiles.append([x, new_y])
                    if x + 1 <= max_x:
                        new_x = x + 1
                        new_direction = '>'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y + 1][x] == '/':
                    energized_tiles.append([x, new_y])
                    if x - 1 >= 0:
                        new_x = x - 1
                        new_direction = '<'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                elif inputs[y + 1][x] == '-':
                    energized_tiles.append([x, new_y])
                    if x - 1 >= 0:
                        new_x = x - 1
                        new_direction = '<'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
                    if x + 1 <= max_x:
                        new_x = x + 1
                        new_direction = '>'
                        energized_tiles.append([new_x, new_y])
                        new_triplet.append([new_x, new_y, new_direction])
    else:
        energized_tiles.append([x, y])
        if current_direction == '>':
            if inputs[y][x] == '-':
                if x + 1 <= max_x:
                    new_x = x + 1
                    new_y = y
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '\\':
                new_x = x
                # energized_tiles.append([new_x, y])
                if y + 1 <= max_y:
                    new_y = y + 1
                    new_direction = 'v'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '/':
                new_x = x
                # energized_tiles.append([new_x, y])
                if y - 1 >= 0:
                    new_y = y - 1
                    new_direction = '^'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '|':
                new_x = x
                # energized_tiles.append([new_x, y])
                if y - 1 >= 0:
                    new_y = y - 1
                    new_direction = '^'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                if y + 1 <= max_y:
                    new_y = y + 1
                    new_direction = 'v'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
        elif current_direction == '<':
            if inputs[y][x] == '-':
                if x - 1 >= 0:
                    new_x = x - 1
                    new_y = y
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '\\':
                new_x = x
                # energized_tiles.append([new_x, y])
                if y - 1 >= 0:
                    new_y = y - 1
                    new_direction = '^'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '/':
                new_x = x
                # energized_tiles.append([new_x, y])
                if y + 1 <= max_y:
                    new_y = y + 1
                    new_direction = 'v'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '|':
                new_x = x
                # energized_tiles.append([new_x, y])
                if y - 1 >= 0:
                    new_y = y - 1
                    new_direction = '^'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                if y + 1 <= max_y:
                    new_y = y + 1
                    new_direction = 'v'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
        elif current_direction == '^':
            if inputs[y][x] == '|':
                if y - 1 >= 0:
                    new_y = y - 1
                    new_x = x
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '\\':
                new_y = y
                # energized_tiles.append([x, new_y])
                if x - 1 >= 0:
                    new_x = x - 1
                    new_direction = '<'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '/':
                new_y = y
                # energized_tiles.append([x, new_y])
                if x + 1 <= max_x:
                    new_x = x + 1
                    new_direction = '>'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '-':
                new_y = y
                # energized_tiles.append([x, new_y])
                if x - 1 >= 0:
                    new_x = x - 1
                    new_direction = '<'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                if x + 1 <= max_x:
                    new_x = x + 1
                    new_direction = '>'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
        else:
            if inputs[y][x] == '|':
                if y + 1 <= max_y:
                    new_y = y + 1
                    new_x = x
                    new_direction = current_direction
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '\\':
                new_y = y
                # energized_tiles.append([x, new_y])
                if x + 1 <= max_x:
                    new_x = x + 1
                    new_direction = '>'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '/':
                new_y = y
                # energized_tiles.append([x, new_y])
                if x - 1 >= 0:
                    new_x = x - 1
                    new_direction = '<'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
            elif inputs[y][x] == '-':
                new_y = y
                # energized_tiles.append([x, new_y])
                if x - 1 >= 0:
                    new_x = x - 1
                    new_direction = '<'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
                if x + 1 <= max_x:
                    new_x = x + 1
                    new_direction = '>'
                    energized_tiles.append([new_x, new_y])
                    new_triplet.append([new_x, new_y, new_direction])
    return new_triplet, energized_tiles


def remove_duplicates_in_nested_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def going_through_contraption(current_state, inputs):
    last_state = current_state
    visited_tiles = []
    energized_tiles = []
    while last_state:
        current_state_tmp = []
        for i in last_state:
            # print('last state:', last_state)
            new_beam_direction, energized_tiles_tmp = beam_direction(i[0], i[1], max_x, max_y, i[2], inputs)
            if new_beam_direction not in visited_tiles:
                visited_tiles.append(new_beam_direction)
                current_state_tmp.extend(new_beam_direction)
                # print('beam direction:', new_beam_direction)
                # print('current_state:', current_state_tmp)
            energized_tiles.extend(energized_tiles_tmp)
            # print('energised states: ', len(remove_duplicates_in_nested_list(energized_tiles)))
            # print('-------------')
        last_state = current_state_tmp
    # for i in sorted(remove_duplicates_in_nested_list(energized_tiles)):
    #     print(i)
    return len(remove_duplicates_in_nested_list(energized_tiles))


inputs = read_file(('input_day16.txt'))
max_x = len(inputs[0]) - 1
max_y = len(inputs) - 1

start_time = time.time()
print(going_through_contraption([[-1, 0, '>']], inputs))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
possible_number_of_energized_tiles = []
for x, i in enumerate(inputs[0]):
    possible_number_of_energized_tiles.append(going_through_contraption([[x, -1, 'v']], inputs))
    possible_number_of_energized_tiles.append(going_through_contraption([[x, max_y + 1, '^']], inputs))

for y, i in enumerate(inputs):
    possible_number_of_energized_tiles.append(going_through_contraption([[-1, y, '>']], inputs))
    possible_number_of_energized_tiles.append(going_through_contraption([[max_x + 1, y, '<']], inputs))

print(max(possible_number_of_energized_tiles))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
