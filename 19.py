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
    possible_robots_copy = copy.deepcopy(possible_robots) # I don't trust copying lists
    possible_robots_copy2 = copy.deepcopy(possible_robots) # and this one we will need to preserve range change
    for commands in elves[current_elf]:
        if ":" in commands:
            command, result = commands.split(':')
            command = command.replace('x', '0').replace('m', '1').replace('a', '2').replace('s', '3')
            if '>' in command:
                part, target = command.split('>')
                if possible_robots_copy[int(part)][0] < int(target): # it only affects ranges if the target is within ranges, if it is below lowest range then it's always true
                    if possible_robots_copy[int(part)][1] < int(target): # target outside of range, so condition would never be true
                        continue
                    else:
                        possible_robots_copy[int(part)][0] = int(target) + 1 # target within range
                        possible_robots_copy2[int(part)][1] = int(target) # this is the range for when condition isn't true
            elif '<' in command:
                part, target = command.split('<')
                if possible_robots_copy[int(part)][1] > int(target): # same thing but in reverse
                    if possible_robots_copy[int(part)][0] > int(target):
                        continue
                    else:
                        possible_robots_copy[int(part)][1] = int(target) - 1
                        possible_robots_copy2[int(part)][0] = int(target)

            if result == 'A':
                answer.append(copy.deepcopy(possible_robots_copy)) # result is A, all current ranges are possible
            elif result == 'R':
                possible_robots_copy = copy.deepcopy((possible_robots_copy2)) # result is R, so all current ranges are impossible, take all others from copy and continue to next instruction
                continue
            else:
                for i in processing2_electric_boogaloo(elves, result, possible_robots_copy):
                    answer.append(i) # result is another elf, get results from him
            possible_robots_copy = copy.deepcopy((possible_robots_copy2)) # to continue we must take the range that wasn't fitting current condition
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
    total = 1
    for range in ranges:
        total *= range[1] - range[0] + 1
    ans2 += total
print(ans2)
