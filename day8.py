import time
from math import lcm


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    instruction = [x for x in lines[0]]
    network = []
    for i in lines[2:]:
        tmp = i.split(' = ')
        network.append([tmp[0], tmp[1][1:-1].split(', ')])
    return instruction, network


def find_correct_node(start_point, network):
    return [i for i, el in enumerate(network) if start_point in el][0]


def find_starting_nodes(network):
    return [el[0] for i, el in enumerate(network) if el[0][-1] == 'A']


def navigate_network(instruction, network):
    start_point = 'AAA'
    ind = 0
    while start_point != 'ZZZ':
        node = network[find_correct_node(start_point, network)]
        single_instruction = instruction[ind % len(instruction)]
        if single_instruction == 'L':
            start_point = node[1][0]
        else:
            start_point = node[1][1]
        ind += 1
    return ind


def navigate_network_part2(instruction, network):
    start_points = find_starting_nodes(network)
    result = []
    for i in start_points:
        start_point = i
        ind = 0
        while start_point[-1] != 'Z':
            node = network[find_correct_node(start_point, network)]
            single_instruction = instruction[ind % len(instruction)]
            if single_instruction == 'L':
                start_point = node[1][0]
            else:
                start_point = node[1][1]
            ind += 1
        result.append(ind)
    return lcm(*result)


start_time = time.time()
instruction, network = read_file('input_day8.txt')
print('1st part answer: ' + str(navigate_network(instruction, network)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
print('2nd part answer: ' + str(navigate_network_part2(instruction, network)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
