import copy
import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    coordinates = []
    for i in lines:
        first, second = i.split('~')
        first = [int(k) for k in first.split(',')]
        second = [int(k) for k in second.split(',')]
        coordinates.append([first, second])
    bricks_cubes = []
    for i in coordinates:
        cubes = i
        for ind, k in enumerate(zip(i[0], i[1])):
            if k[0] != k[1]:
                for l in range(k[0] + 1, k[1]):
                    if ind == 0:
                        cubes.append([l, i[0][1], i[0][2]])
                    elif ind == 1:
                        cubes.append([i[0][0], l, i[0][2]])
                    else:
                        cubes.append([i[0][0], i[0][1], l])
        bricks_cubes.append(cubes)
    return bricks_cubes


def find_bricks_at_z(bricks, z):
    bricks_of_interest = []
    for brick_no, i in enumerate(bricks):
        for ind, k in enumerate(zip(*i)):
            if ind == 2:
                brick_z = min(k)
                if brick_z == z:
                    bricks_of_interest.append([brick_no, i])
    return bricks_of_interest


def check_if_occupied(brick_going_down, brick_no, bricks):
    for ind, i in enumerate(bricks):
        for k in brick_going_down:
            if (k in i and brick_no != ind) or k[2] == 0:
                return True
    return False


def check_if_occupied_2(brick_going_down, brick_no, bricks):
    indices = []
    for ind, i in enumerate(bricks):
        for k in brick_going_down:
            if k in i and brick_no != ind and ind not in indices:
                indices.append(ind)
    return indices


def moving_down(initial_bricks, min_z, max_z):
    for i in range(min_z + 1, max_z + 1):
        for k in find_bricks_at_z(initial_bricks, i):
            brick_no = k[0]
            brick_going_down = []
            for l in k[1]:
                brick_going_down.append([l[0], l[1], l[2] - 1])
            while not check_if_occupied(brick_going_down, brick_no, bricks):
                initial_bricks.pop(brick_no)
                initial_bricks.insert(brick_no, brick_going_down)
                brick_going_down_tmp = []
                for l in brick_going_down:
                    brick_going_down_tmp.append([l[0], l[1], l[2] - 1])
                brick_going_down = brick_going_down_tmp
    return initial_bricks


def supporting_bricks(bricks_layout):
    supporting_bricks = {}
    for brick_no, i in enumerate(bricks_layout):
        supporting_bricks[brick_no] = []
        k_tmp = []
        for k in i:
            k_tmp.append([k[0], k[1], k[2] - 1])
        if len(check_if_occupied_2(k_tmp, brick_no, bricks_layout)) > 0:
            supporting_bricks[brick_no].extend(check_if_occupied_2(k_tmp, brick_no, bricks_layout))
    return supporting_bricks


def get_fallen_bricks(crucial_brick, supporting_bricks_layout):
    sup_bricks = {crucial_brick}
    sup_bricks_tmp = {}
    while sup_bricks != sup_bricks_tmp:
        sup_bricks_tmp = copy.deepcopy(sup_bricks)
        for i in supporting_bricks_layout:
            if set(supporting_bricks_layout[i]) - sup_bricks == set() and set(supporting_bricks_layout[i]) != set():
                sup_bricks.add(i)
    return len(sup_bricks) - 1


start_time = time.time()
bricks = read_file('input_day22.txt')
z = []
for i in bricks:
    for k in i:
        z.append(k[2])

min_z = min(z)
max_z = max(z)

new_bricks = moving_down(bricks, min_z, max_z)

sup = supporting_bricks(new_bricks)

crucial_bricks = []
for i in sup:
    if len(sup[i]) == 1 and sup[i] != []:
        crucial_bricks.extend(sup[i])

print('1st part answer: ' + str(len(sup) - len(set(crucial_bricks))))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
impacted_bricks = 0
for i in set(crucial_bricks):
    d = get_fallen_bricks(i, sup)
    impacted_bricks += get_fallen_bricks(i, sup)

print('2nd part answer: ' + str(impacted_bricks))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

