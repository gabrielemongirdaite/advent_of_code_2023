import time


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    cards = []
    for ind, i in enumerate(lines):
        winning_numbers = [int(s) for s in list(filter(None, i.split(':')[1].split('|')[0].split(' ')))]
        numbers = [int(s) for s in list(filter(None, i.split(':')[1].split('|')[1].split(' ')))]
        cards.append([ind + 1, winning_numbers, numbers])
    return cards


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def points(cards):
    result_part_1 = 0
    part_2 = {}
    for i in cards:
        part_2[i[0]] = 1
    for i in cards:
        result_part_1 += 2 ** (len(intersection(i[1], i[2])) - 1) if intersection(i[1], i[2]) != [] else 0
    return result_part_1


def scratchcards(cards):
    part_2 = {}
    for i in cards:
        part_2[i[0]] = 1
    for i in cards:
        if intersection(i[1], i[2]):
            for j in range(i[0] + 1, i[0] + 1 + len(intersection(i[1], i[2]))):
                part_2[j] += 1 * part_2[i[0]]
    return part_2


start_time = time.time()
cards = read_file("input_day4.txt")
print('1st part answer: ' + str(points(cards)))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
scratch_cards = scratchcards(cards)
result = 0
for i in scratch_cards:
    result += scratch_cards[i]
print('2nd part answer: ' + str(result))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
