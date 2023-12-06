import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    t = [int(s) for s in list(filter(None, lines[0].split(':')[1].split(' ')))]
    d = [int(s) for s in list(filter(None, lines[1].split(':')[1].split(' ')))]
    return t, d


def part_1(t, d):
    wins = 1
    for ind, i in enumerate(t):
        win = 0
        for j in range(0, i + 1):
            if (i - j) * j > d[ind]:
                win += 1
        wins *= win
    return wins


start_time = time.time()
t, d = read_file('input_day6.txt')
print('1st part answer: ' + str(part_1(t, d)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(part_1([38947970], [241154910741091])))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
