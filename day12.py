import copy
import time
import itertools
from collections import Counter


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


def arrangements(spring, group):
    if '?' not in spring:
        return 1
    else:
        return count_combinations(spring, group)[0]


def remove_impossible_second_try(possibility, group, spring):
    if possibility[1] == 0 and possibility[2] != group[0:len(possibility[2])]:
        return False
    elif possibility[1] == 1 and possibility[2][-1] > group[0:len(possibility[2])][-1]:
        return False
    elif possibility[0] == len(spring) - 1 and possibility[2] != group:
        return False
    else:
        return True


def update_groups(in_group, current_group):
    current_group_copy = copy.deepcopy(current_group)
    if in_group == 0:
        current_group_copy.append(1)
    else:
        current_group_copy[-1] += 1
    return current_group_copy


def all_possibilities_second_try(spring, group):
    possibilities = []
    if spring[0] == '?':
        possibilities.append([0, 0, [], 1])
        possibilities.append([0, 1, [1], 1])
    else:
        possibilities.append([0, 1 if spring[0] == '#' else 0, [1] if spring[0] == '#' else [], 1])
    for ind, i in enumerate(spring[1:]):
        new_possibilities = []
        for k in possibilities:
            if i == '?':
                new_possibilities.append([ind + 1, 0, k[2], k[3]])
                new_possibilities.append([ind + 1, 1, update_groups(k[1], k[2]), k[3]])
            else:
                new_possibilities.append(
                    [ind + 1, 1 if i == '#' else 0, k[2] if i == '.' else update_groups(k[1], k[2]), k[3]])
        possibilities = new_possibilities
        poss_boolean = []
        for j in possibilities:
            poss_boolean.append(remove_impossible_second_try(j, group, spring))
        possibilities = [x for x, y in zip(possibilities, poss_boolean) if y]
        all_poss = dict(Counter(tuple(((i[0]),) + ((i[1]),) + ((tuple(i[2]),)) for i in possibilities)))
        for j in all_poss:
            r = 0
            for t in possibilities:
                if t[0] == j[0] and t[1] == j[1] and t[2] == list(j[2]):
                    r += t[3]
            all_poss[j] = r

        possibilities = []
        for j in all_poss:
            possibilities.append([j[0], j[1], list(j[2]), all_poss[j]])
    return sum([x[3] for x in possibilities])


springs, groups = read_file('input_day12.txt')

start_time = time.time()
result = 0
for ind, i in enumerate(springs):
    result += arrangements(i, groups[ind])

print(result)

print("--- %s seconds for 1st part (brute force)---" % (time.time() - start_time))


start_time = time.time()

result = 0
for ind, i in enumerate(springs):
    result += all_possibilities_second_try(i, groups[ind])

print(result)
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
new_springs_part2 = []
groups_part2 = []

for ind, i in enumerate(springs):
    new_springs_part2.append(((i + '?') * 5)[:-1])
    groups_part2.append(groups[ind] * 5)

result = 0
for ind, i in enumerate(new_springs_part2):
    r = all_possibilities_second_try(i, groups_part2[ind])
    result += r
print(result)
print("--- %s seconds for 2nd part---" % (time.time() - start_time))