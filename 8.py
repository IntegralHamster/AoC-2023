import re
import math

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

maps = {}
for line in lines:
    if line != '':
        if '=' not in line:
            steps = (line.replace('R', '1')).replace('L', '0')
        else:
            parse = list(filter(lambda a: a != '', re.split(r"[=(), ]", line)))
            maps.update({parse[0]: [parse[1],parse[2]]})

current_position = 'AAA'
step = 0
while True:
    if current_position == 'ZZZ':
        break
    else:
        current_position = maps[current_position][int(steps[step % len(steps)])]
        step += 1
print(step)

def find_loop(steps, maps, position):
    step = 0
    position_log = [[position, step]]
    z_log = []
    while True:
        position = maps[position][int(steps[step % len(steps)])]
        step += 1
        if position[2] == 'Z':
            z_log.append(step)
        if [position, step % len(steps)] not in position_log:
            position_log.append([position, step % len(steps)])
        else:
            return z_log

current_position2 = [i for i in maps.keys() if i[2] == 'A']
loops_and_zeds = []
for pos in current_position2:
    loops_and_zeds.append(find_loop(steps, maps, pos))
    print(pos)
lcm = 1
for i in range(len(loops_and_zeds)):
    lcm = lcm * loops_and_zeds[i][-1] // math.gcd(lcm,loops_and_zeds[i][-1])
print(lcm)