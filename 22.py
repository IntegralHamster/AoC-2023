from shapely.geometry import LineString, Point

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

bricks = []

for line in lines:
    parse = line.split('~')
    brick_start = [int(i) for i in parse[0].split(',')]
    brick_end = [int(i) for i in parse[1].split(',')]
    bricks.append([brick_start, brick_end])

bricks = sorted(bricks, key=lambda x: (x[0][2], x[1][2]))
def overlap(brick1, brick2):
    br_l1 = LineString([(brick1[0][0], brick1[0][1]), (brick1[1][0], brick1[1][1])])
    br_l2 = LineString([(brick2[0][0], brick2[0][1]), (brick2[1][0], brick2[1][1])])
    if br_l1.length > 0 and br_l2.length > 0:
        return (br_l1.intersects(br_l2))
    else:
        if int(br_l1.length) == 0:
            br_l1 = Point(brick1[0][0], brick1[0][1])
            end1 = Point(brick2[0][0], brick2[0][1])
            end2 = Point(brick2[1][0], brick2[1][1])
            return br_l2.contains(br_l1) or br_l1 == end1 or br_l1 == end2
        elif int(br_l2.length) == 0:
            br_l2 = Point(brick2[0][0], brick2[0][1])
            end1 = Point(brick1[0][0], brick1[0][1])
            end2 = Point(brick1[1][0], brick1[1][1])
            return br_l1.contains(br_l2) or br_l2 == end1 or br_l2 == end2

brick_overlap = {}
for i in range(len(bricks)):
    overlap_cache = []
    for j in range(0, i+1):
        if i != j:
            if overlap(bricks[i], bricks[j]):
                overlap_cache.append(j)
    if len(overlap_cache) != 0:
        brick_overlap[i] = overlap_cache

for i in range(len(bricks)):
    if bricks[i][0][2] == 1 or bricks[i][1][2] == 1:
        continue
    if i not in brick_overlap.keys():
        while bricks[i][0][2] != 1 and bricks[i][1][2] != 1:
            bricks[i][0][2] -= 1
            bricks[i][1][2] -= 1
        continue
    max_z1 = max([bricks[j][0][2] for j in brick_overlap[i]])
    max_z2 = max([bricks[j][1][2] for j in brick_overlap[i]])
    max_z = max(max_z1, max_z2)
    if (bricks[i][0][2] == max_z + 1) or (bricks[i][1][2] == max_z + 1):
        continue
    while (bricks[i][0][2] != max_z + 1) and (bricks[i][1][2] != max_z + 1):
        bricks[i][0][2] -= 1
        bricks[i][1][2] -= 1

disintegratable = [1 for i in range(len(bricks))]

for i in brick_overlap.keys():
    remove = []
    for j in brick_overlap[i]:
        if max(bricks[j][0][2], bricks[j][1][2]) + 1 != min(bricks[i][0][2], bricks[i][1][2]):
            remove.append(j)
    for j in remove:
        brick_overlap[i].remove(j)

stood_on = set()
for i in brick_overlap.keys():
    if len(brick_overlap[i]) == 1:
        disintegratable[brick_overlap[i][0]] = 0
    for j in brick_overlap[i]:
        stood_on.add(j)

print(sum(disintegratable))

import sys
sys.setrecursionlimit(5000)
def we_faaaaaall(brick_overlap, stood_on, brick_num):
    if brick_num not in stood_on:
        return
    faaaaall = set([brick_num])
    for i in brick_overlap.keys():
        if set(brick_overlap[i]).issubset(faaaaall) and i not in faaaaall:
            faaaaall.add(i)
            new_fall = we_faaaaaall(brick_overlap, stood_on, i)
            if new_fall != None:
                for k in new_fall:
                    faaaaall.add(k)
    return faaaaall

london_bridge_has_fallen_down = 0
for j in stood_on:
    london_bridge_has_fallen_down += len(we_faaaaaall(brick_overlap, stood_on, j)) - 1

print(london_bridge_has_fallen_down)
