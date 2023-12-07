import time
from collections import Counter
from operator import itemgetter


def read_file(file_name, part=1):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    cards = []
    for i in lines:
        c, b = i.split(' ')
        if part == 1:
            c = [
                int(x) if x.isdigit() else 10 if x == 'T' else 11 if x == 'J' else 12 if x == 'Q' else 13 if x == 'K' else 14
                for x in c]
        else:
            c = [
                int(x) if x.isdigit() else 10 if x == 'T' else 1 if x == 'J' else 12 if x == 'Q' else 13 if x == 'K' else 14
                for x in c]
        cards.append([c, int(b)])
    return cards


def count_the_same(card):
    a = dict(Counter(card))
    return a


outcomes = ['five of a kind', 'four of a kind', 'full house', 'three of a kind', 'two pairs', 'one pair', 'high card']


def card_combinations(card):
    same = count_the_same(card[0])
    len_same = len(same)
    max_same = max(same.values())
    if len_same == 1:
        return outcomes[0]
    elif len_same == 2 and max_same == 4:
        return outcomes[1]
    elif len_same == 2:
        return outcomes[2]
    elif len_same == 3 and max_same == 3:
        return outcomes[3]
    elif len_same == 3:
        return outcomes[4]
    elif len_same == 4:
        return outcomes[5]
    else:
        return outcomes[6]


def updated_card_combinations(card):
    outcome = card_combinations(card)
    if 1 not in card[0]:
        return outcome
    else:
        max_1 = count_the_same(card[0])[1]
        if outcome == outcomes[0]:
            return outcomes[0]
        elif outcome == outcomes[1]:
            return outcomes[0]
        elif outcome == outcomes[2]:
            return outcomes[0]
        elif outcome == outcomes[3]:
            return outcomes[1]
        elif outcome == outcomes[4] and max_1 == 1:
            return outcomes[2]
        elif outcome == outcomes[4] and max_1 == 2:
            return outcomes[1]
        elif outcome == outcomes[5]:
            return outcomes[3]
        elif outcome == outcomes[6]:
            return outcomes[5]


def clusters(cards):
    cluster = []
    for i in outcomes:
        tmp = []
        for c in cards:
            if c[-1] == i:
                tmp.append(c)
        cluster.append(tmp)
    return cluster


def order_in_cluster(cluster):
    relevant_lists = []
    for i in cluster:
        relevant_lists.append(i[0])
    new_cluster = sorted(relevant_lists, key=itemgetter(0, 1, 2, 3, 4), reverse=True)
    new_cluster_full = []
    for i in new_cluster:
        for j in cluster:
            if i == j[0]:
                new_cluster_full.append([i, j[1], j[2]])
    return new_cluster_full


def final_order(clusters):
    new_order = []
    for i in clusters:
        if i:
            new_order.extend(order_in_cluster(i))
    result = 0
    for ind, i in enumerate(new_order):
        # print(len(new_order) - ind, i[1], i[0])
        result += (len(new_order) - ind) * i[1]
    return result


start_time = time.time()
cards = read_file('input_day7.txt')
cards_updated = []
for i in cards:
    cards_updated.append([i[0], i[1], card_combinations(i)])
clusters_part_1 = clusters(cards_updated)
print('1st part answer: ' + str(final_order(clusters_part_1)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
cards_part_2 = read_file('input_day7.txt', 2)
cards_updated_part_2 = []
for i in cards_part_2:
    cards_updated_part_2.append([i[0], i[1], updated_card_combinations(i)])
clusters_part_2 = clusters(cards_updated_part_2)
print('2nd part answer: ' + str(final_order(clusters_part_2)))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
