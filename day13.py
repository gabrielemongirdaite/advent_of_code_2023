import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    tmp = []
    inputs = []
    for i in lines:
        if i == '':
            inputs.append(tmp)
            tmp = []
        else:
            tmp.append(i)
    return inputs


def find_columns(inputs):
    all_columns = []
    for i in inputs:
        columns = []
        for y, t in enumerate(i):
            for x, u in enumerate(t):
                if y == 0:
                    columns.append(u)
                else:
                    columns[x] = columns[x] + u
        all_columns.append(columns)
    return all_columns


def check_if_other_matches(input, ind):
    len_input = len(input)
    min_to_check = min(ind, len_input - (ind + 1) - 1)
    to_left = [x for x in input[ind - min_to_check:ind]]
    to_left.reverse()
    to_right = [x for x in input[ind + 2: ind + 2 + min_to_check]]
    return to_left == to_right


def check_if_other_matches_part2(input, ind):
    len_input = len(input)
    min_to_check = min(ind, len_input - (ind + 1) - 1)
    to_left = [x for x in input[ind - min_to_check:ind]]
    to_left.reverse()
    to_right = [x for x in input[ind + 2: ind + 2 + min_to_check]]
    differences = 0
    for ind, i in enumerate(to_left):
        # print(i, to_right[ind], find_diff_between_strings(i, to_right[ind]))
        differences += len(find_diff_between_strings(i, to_right[ind]))
    # print(differences)
    return True if differences == 1 else False


def find_reflection_points(input):
    r = 0
    for ind, i in enumerate(input):
        if ind + 1 < len(input):
            if i == input[ind + 1] and check_if_other_matches(input, ind):
                r = ind + 1
    return r


def find_diff_between_strings(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]


def find_smudges(input):
    r = 0
    for ind, i in enumerate(input):
        if ind + 1 < len(input):
            # print(ind, i, i == input[ind + 1], check_if_other_matches_part2(input, ind))
            if len(find_diff_between_strings(i, input[ind + 1])) == 1 and check_if_other_matches(input, ind):
                r = ind + 1
            elif i == input[ind + 1] and check_if_other_matches_part2(input, ind):
                r = ind + 1
    return r


start_time = time.time()
all_rows = read_file('input_day13.txt')
all_columns = find_columns(all_rows)

result = 0
for i in all_rows:
    result += find_reflection_points(i) * 100

for i in all_columns:
    result += find_reflection_points(i)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
result = 0
for ind, i in enumerate(all_rows):
    result += find_smudges(i) * 100
    result += find_smudges(all_columns[ind])

print('2nd part answer: ' + str(result))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
