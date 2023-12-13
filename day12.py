import time
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    springs = []
    groups = []
    for i in lines:
        springs.append(i.split(' ')[0])
        groups.append([int(x) for x in i.split(' ')[1].split(',')])
    return springs, groups


def current_grouping(spring, sign):
    r = 0
    tmp = [r]
    indices = [-1]
    for ind, i in enumerate(spring):
        if i == sign:
            r += 1
            tmp[-1] = r
            indices[-1] = ind
        else:
            r = 0
            tmp.append(0)
            indices.append(-1)
    return [x for x in tmp if x != 0], [x for x in indices if x != -1]


def count_combinations(spring, group):
    repeat = spring.count('?')
    combo = list(itertools.product(['.', '#'], repeat=repeat))
    r = 0
    possible_springs = []
    for i in combo:
        new_spring = spring
        for j in i:
            new_spring = new_spring.replace('?', j, 1)
        current_setup = current_grouping(new_spring, '#')[0]
        if current_setup == group:
            r += 1
            possible_springs.append(new_spring)
    return r, possible_springs


def replacing_question_marks(possible_combinations):
    new_spring = ''
    for i in list(zip(*possible_combinations)):
        if len(set(i)) == 1:
            new_spring += i[0]
        else:
            new_spring += '?'
    return new_spring


# def possibilities(possible_combinations):
#     poss = []
#     all_indices = []
#     for i in possible_combinations:
#         current_setup, current_indices = current_grouping(i, '#')
#         all_indices.append(current_indices)
#     for i in list(zip(*all_indices)):
#         poss.append(len(set(i)))
#     return poss


def arrangements(spring, group):
    if '?' not in spring:
        return 1
    else:
        return count_combinations(spring, group)[0]


springs, groups = read_file('input_day12.txt')

# start_time = time.time()
# result = 0
# for ind, i in enumerate(springs):
#     result += arrangements(i, groups[ind])
#
# print(result)
#
# print("--- %s seconds for 1st part---" % (time.time() - start_time))

new_springs = []

for ind, i in enumerate(springs):
    new_springs.append(replacing_question_marks(count_combinations(i, groups[ind])[1]))

# ending_in_question = 0
# for ind, i in enumerate(new_springs):
#     print(i, groups[ind])
#     ending_in_question += 1 if i[-1] == '?' else 0

result = 0
for ind, i in enumerate(springs):
    if i[-1] == '#':
        i = new_springs[ind]
    r1 = arrangements(i, groups[ind])
    r2 = arrangements('?' + i, groups[ind])
    r3 = arrangements(i + '?', groups[ind])
    if r1 * r2 ** 4 >= r3 ** 4 * r1:
        result += r1 * r2 ** 4
        #print(r1 * r2 ** 4)
    else:
        result += r3 ** 4 * r1
        #print(r3 ** 4 * r1)

print(result)

# new_springs_part2 = []
# groups_part2 = []
#
# for ind, i in enumerate(new_springs):
#     if '?' in i:
#         new_springs_part2.append(((i + '?') * 5)[:-1])
#         groups_part2.append(groups[ind] * 5)
#     else:
#         new_springs_part2.append(i)
#         groups_part2.append(groups[ind])


# start_time = time.time()
# result = 0
# for ind, i in enumerate(new_springs_part2):
#     print(ind, i)
#     result += arrangements(i, groups_part2[ind])


# print(result)
#
# print("--- %s seconds for 1st part---" % (time.time() - start_time))
