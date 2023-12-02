import time
import re


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    dct = {}
    for i in lines:
        red = []
        blue = []
        green = []
        for j in i.split(':')[1].split(';'):
            for k in j.split(','):
                if "red" in k:
                    red.append(int(re.findall(r"\d+", k)[0]))
                elif "blue" in k:
                    blue.append(int(re.findall(r"\d+", k)[0]))
                else:
                    green.append(int(re.findall(r"\d+", k)[0]))
        dct[int(re.findall(r"\d+", i.split(':')[0])[0])] = [red, green, blue]
    return dct


def game_possible(games):
    result = 0
    result_part2 = 0
    for i in games:
        r = max(games[i][0])
        g = max(games[i][1])
        b = max(games[i][2])
        if r <= 12 and g <= 13 and b <= 14:
            result += i
        result_part2 += r * g * b
    return result, result_part2


start_time = time.time()
games = read_file("input_day2.txt")
print('1st part answer: ' + str(game_possible(games)[0]))
print("--- %s seconds for 1st part---" % (time.time() - start_time))

start_time = time.time()
print('2nd part answer: ' + str(game_possible(games)[1]))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))
