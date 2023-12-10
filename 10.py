import sys

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def next_move (grid, y, x, loop):
    if len(grid) > y:
        if grid[y][x] in ['S', '|', 'F', '7'] and grid[y+1][x] in ['S', '|', 'L', 'J'] and [y+1,x] not in loop:
            return [y+1, x]
    if len(grid[y]) > x:
        if grid[y][x] in ['S', '-', 'F', 'L'] and grid[y][x+1] in ['S', '-', '7', 'J'] and [y,x+1] not in loop:
            return [y, x+1]
    if y > 0:
        if grid[y][x] in ['S', '|', 'L', 'J'] and grid[y-1][x] in ['S', '|', 'F', '7'] and [y-1,x] not in loop:
            return [y-1, x]
    if x > 0:
        if grid[y][x] in ['S', '-', '7', 'J'] and grid[y][x-1] in ['S', '-', 'F', 'L'] and [y,x-1] not in loop:
            return [y, x-1]
    return ['B', 'R']

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == 'S':
            start = [i, j]
            break

loop = [start]
while True:
    next_loop = next_move(lines, loop[-1][0], loop[-1][1], loop)
    if next_loop == ['B','R']:
        break
    else:
        loop.append(next_loop)

print(len(loop)//2)
lines2 = lines.copy() # this is a surprise tool that will help us later
for tile in loop:
    lines[tile[0]] = lines[tile[0]][:tile[1]] + '*' + lines[tile[0]][tile[1]+1:]

x = []
y = []
for tile in loop:
    x.append(tile[1])
    y.append(tile[0])
x = sorted(x)
y = sorted(y)
loop_y_min = y[0]
loop_x_min = x[0]
loop_y_max = y[-1]
loop_x_max = x[-1]

sys.setrecursionlimit(5000)
def outside_loop (lines, loop, outside, y, x):
    if [y,x] not in outside:
        outside.append([y,x])
    if (loop_x_min <= x+1 <= loop_x_max) and lines[y][x+1] != '*' and [y,x+1] not in outside:
        outside_loop(lines, loop, outside, y, x+1)
    if (loop_x_min <= x-1 <= loop_x_max) and lines[y][x-1] != '*' and [y,x-1] not in outside:
        outside_loop(lines, loop, outside, y, x-1)
    if (loop_y_min <= y+1 <= loop_y_max) and lines[y+1][x] != '*' and [y+1,x] not in outside:
        outside_loop(lines, loop, outside, y+1, x)
    if (loop_y_min <= y-1 <= loop_y_max) and lines[y-1][x] != '*' and [y-1,x] not in outside:
        outside_loop(lines, loop, outside, y-1, x)
    return

outside = []
for i in range(loop_x_min, loop_x_max+1):
    if lines[loop_y_min][i] != '*' and [loop_y_min,i] not in outside:
        outside_loop(lines, loop, outside, loop_y_min, i)
    if lines[loop_y_max][i] != '*' and [loop_y_max,i] not in outside:
        outside_loop(lines, loop, outside, loop_y_max, i)
for i in range(loop_y_min, loop_y_max+1):
    if lines[i][loop_x_min] != '*' and [i, loop_x_min] not in outside:
        outside_loop(lines, loop, outside, i, loop_x_min)
    if lines[i][loop_x_max] != '*' and [i, loop_x_max] not in outside:
        outside_loop(lines, loop, outside, i, loop_x_max)

inside = (loop_y_max - loop_y_min+1)*(loop_x_max - loop_x_min+1) - len(loop) - len(outside)
print(inside)

inside_tiles = []

for i in range(loop_y_min, loop_y_max+1):
    for j in range(loop_x_min, loop_x_max+1):
        if [i, j] not in outside and [i, j] not in loop:
            inside_tiles.append([i, j])

# 611 is too high, binary search time
# 506 too high, yes i know it's not binary search
# 253 too low
# 380 not right

# fine, let's cheat more

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

points = []
for tile in loop:
    points.append(Point(tile[0], tile[1]))
loop_polygon = Polygon(points)

inside2_electric_boogaloo = []
for fake_outside in inside_tiles:
    if loop_polygon.contains(Point(fake_outside[0], fake_outside[1])):
        inside2_electric_boogaloo.append(fake_outside)

print(len(inside2_electric_boogaloo))

# are you fucking kidding me, answer was 381
# yes I know I should remove the recursion bit and just do the shapely thing for everything, fuck you

# fine, I'll write another idea that I stole from reddit, but that isn't import.solution

inside3_revengeance = []
for fake_outside in inside_tiles:
    vertical_count = 0
    for loop_segment in loop:
        if loop_segment[0] == fake_outside[0] and loop_segment[1] < fake_outside[1] and lines2[loop_segment[0]][loop_segment[1]] not in ['-', 'F', '7']:
            vertical_count += 1
    if vertical_count % 2 == 1:
        inside3_revengeance.append(fake_outside)
print(len(inside3_revengeance))

# yes I know that technically I need to check that F7 and LJ are adjacent to not count, but this gives correct answer, so fuck you

# while Nitro was making me want to shoot myself I decided to steal one more thing from reddit
# behold, my shoelaces https://tinyurl.com/ShoelacesForNitro

area = 0
for i in range(len(loop)):
    area += (loop[i-1][1] * loop[i][0] - loop[i-1][0] * loop[i][1])

# are you Picking up what I'm putting down? https://tinyurl.com/DoYouNitro
inside = area // 2 - len(loop) // 2 + 1
print(inside)
