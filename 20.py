import copy
import math

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

module_graph = {}
flip_flop = []
for line in lines:
    parse = line.split(' -> ')
    if parse[0] == 'broadcaster':
        modules = []
        for module in parse[1].split(', '):
            modules.append(module)
        module_graph[parse[0]] = ['low', 'B', copy.deepcopy(modules)]
    elif parse[0][0] == '%':
        module_name = parse[0].replace('%', '').strip()
        modules = []
        for module in parse[1].split(', '):
            modules.append(module)
        module_graph[module_name] = ['off', 'F', copy.deepcopy(modules)]
        flip_flop.append(module_name)
    elif parse[0][0] == '&':
        module_name = parse[0].replace('&', '').strip()
        modules = []
        for module in parse[1].split(', '):
            modules.append(module)
        module_graph[module_name] = ['high', 'C', copy.deepcopy(modules), {}]

for key in module_graph.keys():
    for node in module_graph[key][2]:
        if node in module_graph.keys():
            if module_graph[node][1] == 'C':
                module_graph[node][3][key] = 'low'
keys = set(module_graph.keys())
for key in keys:
    for node in module_graph[key][2]:
        if node not in module_graph.keys():
            module_graph[node] = ['low', 'E'] # E for endpoint

def conj_check(module_graph, module_name):
    if 'high' in module_graph[module_name][3].values() and len(set(module_graph[module_name][3].values())) == 1:
        return 'low'
    else:
        return 'high'

def impulse(module_graph, module_from, module_to, value):
    if module_graph[module_to][1] == 'E':
        module_graph[module_to][0] = value
        return
    elif module_graph[module_to][1] == 'F':
        if value == 'high':
            return
        elif module_graph[module_to][0] == 'off':
            module_graph[module_to][0] = 'on'
            value_return = 'high'
        elif module_graph[module_to][0] == 'on':
            module_graph[module_to][0] = 'off'
            value_return = 'low'
    elif module_graph[module_to][1] == 'C':
        module_graph[module_to][3][module_from] = value
        value_return = conj_check(module_graph, module_to)
    return_signal = []
    for destination_module in module_graph[module_to][2]:
        return_signal.append([module_to, destination_module, value_return])
    return return_signal

counts = []
loop = 0
second_loop = {}
get_out = False
while True:
    loop += 1
    low_count = 1
    high_count = 0
    impulse_in = [['broadcaster', i, 'low'] for i in module_graph['broadcaster'][2]]
    while len(impulse_in) > 0:
        impulse_stack = impulse(module_graph, impulse_in[0][0], impulse_in[0][1], impulse_in[0][2])
        if impulse_stack != None:
            for i in impulse_stack:
                impulse_in.append(i)
        if impulse_in[0][2] == 'low':
            low_count += 1
        elif impulse_in[0][2] == 'high':
            high_count += 1
        impulse_in.remove(impulse_in[0])
        for i in module_graph['mg'][3].keys(): # because mg is the only one connected to rx, i'm not coding this for other kinds of connections, use your imagination to change for your solution
            if module_graph['mg'][3][i] == 'high':
                if i not in second_loop.keys():
                    second_loop[i] = loop
                if len(set(second_loop.keys())) == len(set(module_graph['mg'][3].keys())):
                    current_lcm = 1
                    for loop_length in second_loop.values():
                        current_lcm = math.lcm(current_lcm, loop_length)
                    get_out = True
                    break
        if get_out:
            break
    counts.append([low_count, high_count])
    all_off = True
    for fl in flip_flop: # to find the flip flop loop if it is shorter than 1000
        if module_graph[fl][0] == 'on':
            all_off = False
            break
    if all_off or get_out:
        break

low_total = 0
high_total = 0
for i in range(1000):
    low_total += counts[i % len(counts)][0]
    high_total += counts[i % len(counts)][1]
print(low_total*high_total, current_lcm)



