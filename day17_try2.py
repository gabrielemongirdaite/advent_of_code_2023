from collections import defaultdict
from heapq import *


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))

    q, seen, mins = [(0, f, (), '')], set(), {f: 0}
    while q:
        print(q)
        (cost, v1, path, direction) = heappop(q)
        if (v1, direction) not in seen:
            seen.add((v1, direction))
            print(seen)
            path = (v1, path)
            if v1 == t:
                return cost, path
            for c, v2 in g.get(v1, ()):
                str_tmp = ''.join(
                    [direction, '<' if v1 - v2 == 1 else '>' if v2 - v1 == 1 else 'v' if v1 < v2 else '^'])
                if (v2, str_tmp) in seen:
                    continue
                # if len(str_tmp) < 4:
                #     to_continue = True
                # else:
                #     if str_tmp[len(str_tmp) - 4:] not in ['>>>>', '<<<<', 'vvvv', '^^^^']:
                #         to_continue = True
                #     else:
                #         to_continue = False
                to_continue = True
                if not to_continue:
                    continue
                prev = mins.get(v2, None)
                next = cost + c
                if prev is None or next < prev:
                    mins[v2] = next
                    heappush(q, (next, v2, path, str_tmp))
    return float("inf"), None


def add_nodes_to_graph(inputs):
    graph = []
    for y, i in enumerate(inputs):
        for x, j in enumerate(i):
            current_point = y * len(inputs[0]) + x
            if y + 1 <= len(inputs) - 1:
                graph.append((current_point, (y + 1) * len(inputs[0]) + x, int(inputs[y + 1][x])))
            if y - 1 >= 0:
                graph.append((current_point, (y - 1) * len(inputs[0]) + x, int(inputs[y - 1][x])))
            if x + 1 <= len(inputs[0]) - 1:
                graph.append((current_point, y * len(inputs[0]) + x + 1, int(inputs[y][x + 1])))
            if x - 1 >= 0:
                graph.append((current_point, y * len(inputs[0]) + x - 1, int(inputs[y][x - 1])))
    return graph


inputs = read_file('input_day17.txt')
graph = add_nodes_to_graph(inputs)

print(dijkstra(graph, 0, 4))
