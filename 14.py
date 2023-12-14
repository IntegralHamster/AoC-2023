import copy

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

round_rocks = []
square_rocks = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'O':
            round_rocks.append([j, i])
        elif lines[i][j] == '#':
            square_rocks.append([j, i])

def move_north(square_rocks, round_rocks, num):
    while True:
        if [round_rocks[num][0], round_rocks[num][1] - 1] not in (square_rocks + round_rocks) and round_rocks[num][1] - 1 >= 0:
            round_rocks[num][1] -= 1
        else:
            break
    return

def move_west(square_rocks, round_rocks, num):
    while True:
        if [round_rocks[num][0] - 1, round_rocks[num][1]] not in (square_rocks + round_rocks) and round_rocks[num][0] - 1 >= 0:
            round_rocks[num][0] -= 1
        else:
            break
    return

def move_south(square_rocks, round_rocks, num):
    while True:
        if [round_rocks[num][0], round_rocks[num][1] + 1] not in (square_rocks + round_rocks) and round_rocks[num][1] + 1 < len(lines):
            round_rocks[num][1] += 1
        else:
            break
    return

def move_east(square_rocks, round_rocks, num):
    while True:
        if [round_rocks[num][0] + 1, round_rocks[num][1]] not in (square_rocks + round_rocks) and round_rocks[num][0] + 1 < len(lines):
            round_rocks[num][0] += 1
        else:
            break
    return

# Except runtime of about a minute or two or three, but first thing printed is part 1 answer

pattern = [copy.deepcopy(round_rocks)]
cycle = 0
while cycle < 1000000:
    round_rocks = sorted(round_rocks, key=lambda x: (x[1], x[0]))
    if cycle == 0:
        ans1 = 0
    for num in range(len(round_rocks)):
        move_north(square_rocks, round_rocks, num)
        if cycle == 0:
            ans1 += len(lines) - round_rocks[num][1]
    if cycle == 0:
        print(ans1)
    round_rocks = sorted(round_rocks, key=lambda x: (x[0], x[1]))
    for num in range(len(round_rocks)):
        move_west(square_rocks, round_rocks, num)
    round_rocks = sorted(round_rocks, key=lambda x: (x[1], x[0]), reverse=True)
    for num in range(len(round_rocks)):
        move_south(square_rocks, round_rocks, num)
    round_rocks = sorted(round_rocks, key=lambda x: (x[0], x[1]), reverse=True)
    for num in range(len(round_rocks)):
        move_east(square_rocks, round_rocks, num)
    cycle += 1
    if round_rocks not in pattern:
        pattern.append(copy.deepcopy(round_rocks))
    else:
        print(cycle)
        break
    print(cycle)

loop = pattern.index(round_rocks)
end_position = (1000000000 - loop) % (cycle - loop) + loop
print(end_position)

ans2 = 0
for num in range(len(round_rocks)):
    ans2 += len(lines) - pattern[end_position][num][1]
print(ans2)