import time
import re
import copy


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    return lines


def find_numbers(line):
    first = int(re.findall(r"\d", line)[0])
    first_ind = line.find(str(first))
    last = int(re.findall(r"\d", line)[-1])
    last_int = line.rfind(str(last))
    return (first * 10 + last, (first_ind, last_int))


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def find_first_last(str_search, number):
    return (
        str_search.find(number) if str_search.find(number) != -1 else 10000,
        str_search.rfind(number) if str_search.find(number) != -1 else -10000)


def replace_spelled_numbers(lines):
    new_lines = copy.deepcopy(lines)
    for ind, i in enumerate(new_lines):
        one_first, one_last = find_first_last(i, "one")
        two_first, two_last = find_first_last(i, "two")
        three_first, three_last = find_first_last(i, "three")
        four_first, four_last = find_first_last(i, "four")
        five_first, five_last = find_first_last(i, "five")
        six_first, six_last = find_first_last(i, "six")
        seven_first, seven_last = find_first_last(i, "seven")
        eight_first, eight_last = find_first_last(i, "eight")
        nine_first, nine_last = find_first_last(i, "nine")

        numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        numbers_int = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        first = [one_first, two_first, three_first, four_first, five_first, six_first, seven_first, eight_first,
                 nine_first]
        last = [one_last, two_last, three_last, four_last, five_last, six_last, seven_last, eight_last, nine_last]
        minimum = min(first)
        maximum = max(last)

        first_last_number = find_numbers(i)[1]

        if first_last_number[0] > minimum:
            new_lines[ind] = i.replace(numbers[first.index(min(first))], numbers_int[first.index(min(first))], 1)

        if minimum + len(numbers[first.index(min(first))]) <= maximum or first_last_number[1] < maximum:
            new_lines[ind] = rreplace(new_lines[ind], numbers[last.index(max(last))],
                                      numbers_int[last.index(max(last))], 1)

    return new_lines


start_time = time.time()
lines = read_file('input_day1.txt')
r = 0
for i in lines:
    r += find_numbers(i)[0]
print('1st part answer: '+ str(r))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
updated_data = replace_spelled_numbers(lines)
r = 0
for i in updated_data:
    #print(find_numbers(i)[0])
    r += find_numbers(i)[0]
print('2nd part answer: '+ str(r))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))

