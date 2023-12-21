import time
from math import lcm


def read_file(file_name):
    text_file = open(file_name, "r")
    lines = text_file.read().split('\n')
    inputs = []
    conjunction_modules = []
    for i in lines:
        tmp = i.split(' -> ')
        module_name = tmp[0] if tmp[0][0] not in ['%', '&'] else tmp[0][1:]
        module_type = '' if tmp[0][0] not in ['%', '&'] else tmp[0][0]
        destination_modules = tmp[1].split(', ')
        inputs.append([module_name, module_type, destination_modules])
        if module_type == '&':
            conjunction_modules.append(module_name)
    conjunction_modules_inputs = {}
    for i in conjunction_modules:
        tmp = []
        for j in inputs:
            if i in j[2]:
                tmp.append([j[0], 'low'])
        conjunction_modules_inputs[i] = tmp
    inputs_new = []
    for i in inputs:
        if i[1] == '&':
            tmp = conjunction_modules_inputs[i[0]]
            inputs_new.append(i + [tmp])
        elif i[1] == '%':
            inputs_new.append(i + ['off'])
        else:
            inputs_new.append(i)
    return inputs_new


def find_module(module, setup):
    for ind, i in enumerate(setup):
        if i[0] == module:
            break
    return ind


def pushing_button(current_setup, placeholder=0):
    destination_modules = ['broadcaster']
    low_signal = 1
    high_signal = 0
    current_signal = ['low']
    input_module = ['button']
    while destination_modules:
        destination_modules_tmp = []
        input_module_tmp = []
        current_signal_tmp = []
        for ind, module in enumerate(destination_modules):
            module_ind = find_module(module, current_setup)
            if module in ['output', 'rx']:
                continue
            if current_setup[module_ind][1] == '':
                destination_modules_tmp.extend(current_setup[module_ind][2])
                input_module_tmp.extend([module] * len(current_setup[module_ind][2]))
                current_signal_tmp.extend([current_signal[ind]] * len(current_setup[module_ind][2]))
            elif current_setup[module_ind][1] == '%':
                if current_signal[ind] == 'low':
                    if current_setup[module_ind][3] == 'off':
                        current_signal_tmp.extend(['high'] * len(current_setup[module_ind][2]))
                        destination_modules_tmp.extend(current_setup[module_ind][2])
                        input_module_tmp.extend([module] * len(current_setup[module_ind][2]))
                        new_module_setup = [current_setup[module_ind][0], current_setup[module_ind][1],
                                            current_setup[module_ind][2], 'on']
                        current_setup.pop(module_ind)
                        current_setup.insert(module_ind, new_module_setup)
                    else:
                        current_signal_tmp.extend(['low'] * len(current_setup[module_ind][2]))
                        destination_modules_tmp.extend(current_setup[module_ind][2])
                        input_module_tmp.extend([module] * len(current_setup[module_ind][2]))
                        new_module_setup = [current_setup[module_ind][0], current_setup[module_ind][1],
                                            current_setup[module_ind][2], 'off']
                        current_setup.pop(module_ind)
                        current_setup.insert(module_ind, new_module_setup)
            else:
                memory = current_setup[module_ind][3]
                current_input_module = input_module[ind]
                new_memory = []
                for k in memory:
                    if k[0] == current_input_module:
                        new_memory.append([k[0], current_signal[ind]])
                    else:
                        new_memory.append(k)
                new_module_setup = [current_setup[module_ind][0], current_setup[module_ind][1],
                                    current_setup[module_ind][2], new_memory]
                current_setup.pop(module_ind)
                current_setup.insert(module_ind, new_module_setup)
                cnt_high_signal = 0
                for i in new_memory:
                    if i[1] == 'high':
                        cnt_high_signal += 1
                if cnt_high_signal == len(new_memory):
                    current_signal_tmp.extend(['low'] * len(current_setup[module_ind][2]))
                else:
                    current_signal_tmp.extend(['high'] * len(current_setup[module_ind][2]))
                destination_modules_tmp.extend(current_setup[module_ind][2])
                input_module_tmp.extend([module] * len(current_setup[module_ind][2]))
                for i in current_setup[find_module('kl', current_setup)][3]:
                    if i[1] == 'high':
                        print(placeholder, current_setup[36][3])
        destination_modules = destination_modules_tmp
        input_module = input_module_tmp
        current_signal = current_signal_tmp
        for i in current_signal:
            if i == 'low':
                low_signal += 1
            elif i == 'high':
                high_signal += 1
    return low_signal, high_signal, current_setup


start_time = time.time()
current_setup = read_file('input_day20.txt')

low_signal = 0
high_signal = 0
for i in range(0, 1000):
    l, h, current_setup = pushing_button(current_setup)
    low_signal += l
    high_signal += h
print('1st part answer: ' + str(low_signal * high_signal))
print("--- %s seconds for 1st part---" % (time.time() - start_time))


start_time = time.time()
current_setup = read_file('input_day20.txt')

for i in range(0, 5000):
    l, h, current_setup = pushing_button(current_setup, i + 1)

print(lcm(3767, 3923, 3931, 4007))
print("--- %s seconds for 2nd part---" % (time.time() - start_time))