import copy
import time
import re
import itertools
from functools import reduce


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    workflows = []
    step = 0
    while lines[step] != '':
        workflow_name = lines[step].split('{')[0]
        conditions = []
        for i in lines[step].split('{')[1][:-1].split(','):
            if ':' in i:
                n = int(re.findall(r'\d+', i)[0])
                c = i[0]
                sgn = i[1]
                next_move = i.split(':')[1]
                conditions.append([c, sgn, n, next_move])
            else:
                conditions.append([i])
        workflows.append({workflow_name: conditions})
        step += 1

    parts = []
    for i in lines[step + 1:]:
        parts.append([int(k) for k in re.findall(r'\d+', i)])
    return workflows, parts


def find_workflow(start, workflows):
    for ind, i in enumerate(workflows):
        if list(i.keys())[0] == start:
            break
    return ind


def go_through_condition(part, workflow, start):
    x, m, a, s = part[0], part[1], part[2], part[3]
    for i in workflow[start]:
        if len(i) == 4:
            if i[0] == 'x':
                if i[1] == '<':
                    if x < i[2]:
                        return i[3]
                else:
                    if x > i[2]:
                        return i[3]
            elif i[0] == 'm':
                if i[1] == '<':
                    if m < i[2]:
                        return i[3]
                else:
                    if m > i[2]:
                        return i[3]
            elif i[0] == 'a':
                if i[1] == '<':
                    if a < i[2]:
                        return i[3]
                else:
                    if a > i[2]:
                        return i[3]
            else:
                if i[1] == '<':
                    if s < i[2]:
                        return i[3]
                else:
                    if s > i[2]:
                        return i[3]
        else:
            return i[0]


def assess_part(part, workflows):
    start = 'in'
    start_ind = find_workflow(start, workflows)
    while start not in ['A', 'R']:
        start = go_through_condition(part, workflows[start_ind], start)
        start_ind = find_workflow(start, workflows)
    return start


def remove_duplicates_in_nested_list(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def get_paths_resulting_in_accepted(workflows):
    starting_point = 'in'
    start_ind = find_workflow(starting_point, workflows)
    all_paths = []
    start = [[[starting_point], start_ind]]
    while start:
        updated_start = []
        for ind, i in enumerate(start):
            for k in workflows[i[1]][i[0][-1]]:
                tmp = []
                tmp.extend(i[0])
                tmp.append(k[-1])
                updated_start.append([tmp, find_workflow(tmp[-1], workflows)])
        start_new = []
        for i in updated_start:
            if i[0][-1] in ['A', 'R']:
                all_paths.append(i[0])
            else:
                start_new.append(i)
        start = start_new
    return remove_duplicates_in_nested_list([k for k in all_paths if k[-1] == 'A'])


def get_conditions_for_path(path, workflows):
    conditions = []
    for ind, i in enumerate(path[1:]):
        if i == 'A':
            start_ind = find_workflow(path[ind], workflows)
            A_ind = []
            for idx, k in enumerate(workflows[start_ind][path[ind]]):
                if i == k[-1]:
                    A_ind.append(idx)
            conditions_A = []
            for t in A_ind:
                conditions_tmp = copy.deepcopy(conditions)
                for ind_c, l in enumerate(range(0, t + 1)):
                    if ind_c == t:
                        conditions_tmp.append(workflows[start_ind][path[ind]][ind_c][0:-1])
                    else:
                        c, sgn, n, next_move = workflows[start_ind][path[ind]][ind_c]
                        if sgn == '>':
                            new_sgn = '<'
                            new_n = n + 1
                        else:
                            new_sgn = '>'
                            new_n = n - 1
                        conditions_tmp.append([c, new_sgn, new_n])
                conditions_A.append(conditions_tmp)
            conditions = conditions_A
        else:
            start_ind = find_workflow(path[ind], workflows)
            for idx, k in enumerate(workflows[start_ind][path[ind]]):
                if i == k[-1]:
                    break
            for ind_c, l in enumerate(range(0, idx + 1)):
                if ind_c == idx:
                    conditions.append(workflows[start_ind][path[ind]][ind_c][0:-1])
                else:
                    c, sgn, n, next_move = workflows[start_ind][path[ind]][ind_c]
                    if sgn == '>':
                        new_sgn = '<'
                        new_n = n + 1
                    else:
                        new_sgn = '>'
                        new_n = n - 1
                    conditions.append([c, new_sgn, new_n])

    conditions2 = []
    for k in conditions:
        conditions2.append([l for l in k if l != []])
    conditions_updated = []
    # print(conditions2)
    for t in conditions2:
        conditions_updated_tmp = []
        for k in t:
            c = k[0]
            sgn = k[1]
            n = k[2]
            if sgn == '>':
                new_range = range(n + 1, 4001)
            else:
                new_range = range(1, n)
            conditions_updated_tmp.append([c, new_range])
        conditions_updated.append(conditions_updated_tmp)
    # print(conditions_updated, len(conditions_updated))

    new_conditions = []
    for ind1, t in enumerate(conditions_updated):
        x, m, a, s = range(1, 4001), range(1, 4001), range(1, 4001), range(1, 4001)
        for k in t:
            x2, y2 = k[1][0], k[1][-1] + 1
            if k[0] == 'x':
                x1, y1 = x[0], x[-1] + 1
                x = range(max(x1, x2), min(y1, y2))
            elif k[0] == 'm':
                x1, y1 = m[0], m[-1] + 1
                m = range(max(x1, x2), min(y1, y2))
            elif k[0] == 'a':
                x1, y1 = a[0], a[-1] + 1
                a = range(max(x1, x2), min(y1, y2))
            elif k[0] == 's':
                x1, y1 =s[0], s[-1] + 1
                s = range(max(x1, x2), min(y1, y2))
        new_conditions.append([x, m, a, s])
    return new_conditions


def union_size(all_conditions):
    result = 0
    for k in all_conditions:
        result_tmp = 1
        for l in k:
            result_tmp *= (l[-1] + 1 - l[0])
        result += result_tmp

    return result


start_time = time.time()
workflows, parts = read_file('input_day19.txt')

result = 0
for i in parts:
    o = assess_part(i, workflows)
    if o == 'A':
        result += sum(i)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
paths = get_paths_resulting_in_accepted(workflows)

all_conditions = []
for i in paths:
    all_conditions.extend(get_conditions_for_path(i, workflows))

print('2nd part answer: ' + str(union_size(all_conditions)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))



