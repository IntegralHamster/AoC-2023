import sys
import time
start_time = time.time()

sys.setrecursionlimit(5000)

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

mirrors = {}
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] != '.':
            mirrors[tuple([x, y])] = lines[y][x]
def beam(x, y, dir_x, dir_y, recursion_history):
    beam_history = []
    while 0 <= x < len(lines[0]) and 0 <= y < len(lines):
        beam_history.append([x,y, dir_x, dir_y])
        if (x,y) not in mirrors.keys():
            x += dir_x
            y += dir_y
        elif mirrors[(x,y)] == '\\':
            dir_x, dir_y = dir_y, dir_x
            x += dir_x
            y += dir_y
        elif mirrors[(x,y)] == '/':
            dir_x, dir_y = -dir_y, -dir_x
            x += dir_x
            y += dir_y
        elif mirrors[(x,y)] == '|':
            if dir_x == 0:
                x += dir_x
                y += dir_y
            else:
                if y - 1 >= 0:
                    if [x, y-1, 0, -1] not in recursion_history:
                        recursion_history.append([x, y-1, 0, -1])
                        for place in beam(x, y-1, 0, -1, recursion_history):
                            beam_history.append(place)
                    else:
                        break
                if y+1 < len(lines):
                    if [x, y+1, 0, 1] not in recursion_history:
                        recursion_history.append([x, y+1, 0, 1])
                        for place in beam(x, y+1, 0, 1, recursion_history):
                            beam_history.append(place)
                    else:
                        break
        elif mirrors[(x,y)] == '-':
            if dir_y == 0:
                x += dir_x
                y += dir_y
            else:
                if x - 1 >= 0:
                    if [x-1, y, -1, 0] not in recursion_history:
                        recursion_history.append([x-1, y, -1, 0])
                        for place in beam(x-1, y, -1, 0, recursion_history):
                            beam_history.append(place)
                    else:
                        break
                if x+1 < len(lines[0]):
                    if [x+1, y, 1, 0] not in recursion_history:
                        recursion_history.append([x+1, y, 1, 0])
                        for place in beam(x+1, y, 1, 0, recursion_history):
                            beam_history.append(place)
                    else:
                        break
    return beam_history

energized = []
for i in range(len(lines)):
    places_visited = []
    history = beam(0,i, 1, 0, [])
    for place in history:
        places_visited.append((place[0], place[1]))
    energized.append(len(set(places_visited)))

    places_visited = []
    history = beam(len(lines[0]) - 1,i, -1, 0, [])
    for place in history:
        places_visited.append((place[0], place[1]))
    energized.append(len(set(places_visited)))

for i in range(len(lines[0])):
    places_visited = []
    history = beam(i,0, 0, 1, [])
    for place in history:
        places_visited.append((place[0], place[1]))
    energized.append(len(set(places_visited)))

    places_visited = []
    history = beam(i,len(lines) - 1, 0, -1, [])
    for place in history:
        places_visited.append((place[0], place[1]))
    energized.append(len(set(places_visited)))

print(energized[0], max(energized))
print(time.time() - start_time)
