import time
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    seeds = lines[0]
    maps = []
    map = []
    for i in lines[2:]:
        if i != '':
            map.append(i.split(' '))
        else:
            maps.append(map)
            map = []
    return seeds, maps


def extend_map(seeds, maps):
    all_queues = []
    for i in seeds:
        queue = [int(i)]
        for j in maps:
            r = 0
            for k in j[1:]:
                if queue[-1] in range(int(k[1]), int(k[1]) + int(k[2])) and r == 0:
                    queue.append(int(k[0]) + (queue[-1] - int(k[1])))
                    r += 1
            if r == 0:
                queue.append(queue[-1])
        all_queues.append(queue)
    return all_queues


def seed_pairs(seeds):
    seeds_part_2 = []
    i = 0
    while i < len(seeds):
        seeds_part_2.append(range(int(seeds[i]), int(seeds[i]) + int(seeds[i + 1])))
        i += 2
    return seeds_part_2


def range_intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


# https://stackoverflow.com/questions/6462272/subtract-overlaps-between-two-ranges-without-sets
def range_diff(r1, r2):
    s1, e1 = r1[0], r1[-1] + 1
    s2, e2 = r2[0], r2[-1] + 1
    endpoints = sorted((s1, s2, e1, e2))
    result = []
    if endpoints[0] == s1 and endpoints[1] != s1:
        result.append(range(endpoints[0], endpoints[1]))
    if endpoints[3] == e1 and endpoints[2] != e1:
        result.append(range(endpoints[2], endpoints[3]))
    return result


def multirange_diff(r1_list, r2_list):
    for r2 in r2_list:
        r1_list = list(itertools.chain(*[range_diff(r1, r2) for r1 in r1_list]))
    return r1_list


def ranges(first_set_ranges, second_set_ranges):
    queue = []
    for i in first_set_ranges:
        covered = []
        for j in second_set_ranges:
            for k in j[1:]:
                r_intersect = range_intersect(i, range(int(k[1]), int(k[1]) + int(k[2])))
                if r_intersect is not None:
                    r1 = r_intersect[0] - int(k[1])
                    r2 = r_intersect[-1] - r_intersect[0] + 1
                    r3 = r_intersect[0] - i[0]
                    r4 = i[-1] - r_intersect[-1]
                    queue.append(range(int(k[0]) + r1, int(k[0]) + r1 + r2))
                    if r_intersect[0] == i[0] and r_intersect[-1] == i[-1]:
                        covered.append(i)
                    elif r3 == 0:
                        covered.append(range(i[0], r_intersect[-1] + 1))
                    elif r4 == 0:
                        covered.append(range(r_intersect[0], i[-1] + 1))
                    else:
                        covered.append(r_intersect)
        if not covered:
            queue.append(i)
            covered.append(i)
        if multirange_diff([i], covered):
            queue.extend(multirange_diff([i], covered))
    return queue


start_time = time.time()
seeds, maps = read_file("input_day5.txt")
seeds = list(filter(None, seeds.split(':')[1].split(' ')))
all_paths = extend_map(seeds, maps)
result = []
for i in all_paths:
    result.append(i[-1])
print('1st part answer: ' + str(min(result)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
seed_to_soil = ranges(seed_pairs(seeds), [maps[0]])
soil_to_fertilizer = ranges(seed_to_soil, [maps[1]])
fertilizer_to_water = ranges(soil_to_fertilizer, [maps[2]])
water_to_light = ranges(fertilizer_to_water, [maps[3]])
light_to_temperature = ranges(water_to_light, [maps[4]])
temperature_to_humidity = ranges(light_to_temperature, [maps[5]])
humidity_to_location = ranges(temperature_to_humidity, [maps[6]])

mins = []
for i in humidity_to_location:
    mins.append(i[0])
print('2nd part answer: ' + str(min(mins)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
