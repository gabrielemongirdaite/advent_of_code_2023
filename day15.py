import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines[0].split(',')


def part1(input):
    current_value = 0
    for i in input:
        current_value += ord(i)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def perform_hashmap(input, boxes):
    label = input.split('=')[0] if '=' in input else input[:-1]
    focal_length = int(input.split('=')[1]) if '=' in input else 0
    box_no = part1(label)
    if focal_length > 0:
        r = 0
        for ind, i in enumerate(boxes[box_no]):
            if i[0] == label:
                boxes[box_no][ind] = [label, focal_length]
                r += 1
                break
        if r == 0:
            boxes[box_no].append([label, focal_length])
    else:
        for ind, i in enumerate(boxes[box_no]):
            if i[0] == label:
                boxes[box_no].pop(ind)
                break
    return boxes


start_time = time.time()
inputs = read_file('input_day15.txt')

result = 0
for k in inputs:
    result += part1(k)

print('1st part answer: ' + str(result))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
boxes = [[] for _ in range(256)]

for i in inputs:
    boxes = perform_hashmap(i, boxes)

result = 0
for box_no, i in enumerate(boxes):
    for slot, j in enumerate(i):
        result += (box_no + 1) * (slot + 1) * j[1]

print('2nd part answer: ' + str(result))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))