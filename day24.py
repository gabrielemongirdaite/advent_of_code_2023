import time
import itertools


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    all_points = []
    for i in lines:
        points = []
        tmp = i.split(' @ ')
        points.append([int(k) for k in tmp[0].split(', ')])
        points.append([int(k) + int(l) for k, l in zip(tmp[0].split(', '), tmp[1].split(', '))])
        all_points.append(points)
    return all_points


def find_intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    try:
        px = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
        py = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / (
                (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4))
    except:
        px = float('inf')
        py = float('inf')
    return [px, py]


def check_if_intersection_within_range(start, end, intersection, points1, points2):
    if intersection == [float('inf'), float('inf')]:
        return False
    elif start <= intersection[0] <= end and start <= intersection[1] <= end:
        if intersection[0] > points1[0][0] > points1[1][0] or \
                intersection[1] > points1[0][1] > points1[1][1] or \
                intersection[0] > points2[0][0] > points2[1][0] or \
                intersection[1] > points2[0][1] > points2[1][1] or \
                intersection[0] < points1[0][0] < points1[1][0] or \
                intersection[1] < points1[0][1] < points1[1][1] or \
                intersection[0] < points2[0][0] < points2[1][0] or \
                intersection[1] < points2[0][1] < points2[1][1]:
            return False
        else:
            return True
    else:
        return False


all_points = read_file('input_day24.txt')
result = 0
for i in list(itertools.combinations(all_points, 2)):
    intersection = find_intersection(i[0][0][0], i[0][0][1], i[0][1][0], i[0][1][1], i[1][0][0], i[1][0][1], i[1][1][0],
                                     i[1][1][1])
    result += check_if_intersection_within_range(200000000000000, 400000000000000, intersection, i[0], i[1])

print(result)
