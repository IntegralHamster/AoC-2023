import re
with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

elves = {}
robots = []

for line in lines:
    if ":" in line:
        parse = re.split('{', line.replace('}', ''))
        elves[parse[0]] = parse[1].split(',')
    elif '{' in line:
        robots.append(re.findall(r'\b\d+\b', line))

def processing (elves, x, m, a, s):
    current_elf = 'in'
    while True:
        for commands in elves[current_elf]:
            if ":" in commands:
                command, result = commands.split(':')
                if eval(command):
                    if result == 'A':
                        return 1
                    elif result == 'R':
                        return 0
                    else:
                        current_elf = result
                        break
            else:
                if commands == 'A':
                    return 1
                elif commands == 'R':
                    return 0
                else:
                    current_elf = commands

ans1 = 0
for robot in robots:
    ans1 += (int(robot[0]) + int(robot[1]) + int(robot[2]) + int(robot[3])) * processing(elves, int(robot[0]), int(robot[1]), int(robot[2]), int(robot[3]))
print(ans1)

possible_robots_st = [[1, 4000], [1, 4000], [1, 4000], [1, 4000]]

import copy

def processing2_electric_boogaloo (elves, current_elf, possible_robots):
    answer = []
    possible_robots_copy = copy.deepcopy(possible_robots)
    possible_robots_copy2 = copy.deepcopy(possible_robots)
    for commands in elves[current_elf]:
        # print(commands, possible_robots_copy)
        if ":" in commands:
            command, result = commands.split(':')
            command = command.replace('x', '0').replace('m', '1').replace('a', '2').replace('s', '3')
            if '>' in command:
                part, target = command.split('>')
                if possible_robots_copy[int(part)][0] < int(target):
                    if possible_robots_copy[int(part)][1] < int(target):
                        continue
                    else:
                        possible_robots_copy[int(part)][0] = int(target) + 1
                        possible_robots_copy2[int(part)][1] = int(target)
            elif '<' in command:
                part, target = command.split('<')
                if possible_robots_copy[int(part)][1] > int(target):
                    if possible_robots_copy[int(part)][0] > int(target):
                        continue
                    else:
                        possible_robots_copy[int(part)][1] = int(target) - 1
                        possible_robots_copy2[int(part)][0] = int(target)
            if result == 'A':
                answer.append(copy.deepcopy(possible_robots_copy))
            elif result == 'R':
                continue
            else:
                for i in processing2_electric_boogaloo(elves, result, possible_robots_copy):
                    answer.append(i)
            possible_robots_copy = copy.deepcopy((possible_robots_copy2))
        else:
            if commands == 'A':
                answer.append(copy.deepcopy(possible_robots_copy))
            elif commands == 'R':
                continue
            else:
                for i in processing2_electric_boogaloo(elves, commands, possible_robots_copy):
                    answer.append(i)
    return answer

ans2 = 0
for ranges in processing2_electric_boogaloo(elves, 'in', possible_robots_st):
    print(ranges)
    total = 1
    for range in ranges:
        total *= range[1] - range[0] + 1
    ans2 += total
print(ans2)

# 167409079868000 - correct one
# 167125936932000 - current one