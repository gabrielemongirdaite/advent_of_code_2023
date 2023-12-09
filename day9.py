import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    tmp = []
    for i in lines:
        tmp.append([int(x) for x in i.split(' ')])
    return tmp


def find_difference(sequence):
    return [j - i for i, j in zip(sequence[:-1], sequence[1:])]


def all_zeros(sequence):
    len_seq = len(sequence)
    r = 0
    for i in sequence:
        if i == 0:
            r += 1
    return r == len_seq


def predictions(sequence):
    last_elements = [sequence[-1]]
    first_elements = [sequence[0]]
    diff = find_difference(sequence)
    while not all_zeros(diff):
        last_elements.append(diff[-1])
        first_elements.append(diff[0])
        diff = find_difference(diff)
    d = first_elements[-1]
    first_elements.reverse()
    for i in first_elements[1:]:
        d = i - d
    return sum(last_elements), d


start_time = time.time()
sequences = read_file('input_day9.txt')
r1 = 0
r2 = 0
for i in sequences:
    r1 += predictions(i)[0]
    r2 += predictions(i)[1]
print('1st part answer: ' + str(r1))
print('2nd part answer: ' + str(r2))
print("--- %s seconds for both parts---" % (time.time() - start_time))


