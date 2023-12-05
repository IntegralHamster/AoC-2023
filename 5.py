import re

def seed_through_map (seed_num, mapping):
    for remap in mapping:
        if remap[1] <= seed_num <= remap[1] + remap[2] - 1:
            seed_num = remap[0] + seed_num - remap[1]
            break
    return seed_num

def intersecting_lines (line_range, line_segments):
    if len(line_segments) == 0:
        return [line_range]
    else:
        result = []
        segments = sorted(line_segments, key=lambda x: x[0])
        start = line_range[0]
        for segment in segments:
            result.append([start,max(segment[0] - 1,start)])
            start = segment[1] + 1
        for i in result:
            if i[1] == i[0]:
                result.remove(i)
        return result

def seed_through_map2 (seed_range,mapping):
    overlaps_range = []
    overlaps_result = []
    for remap in mapping:
        if seed_range[0] <= remap[1] <= seed_range[1]:
            if remap[1] + remap[2] - 1 <= seed_range[1]:
                overlaps_range.append([remap[1], remap[1] + remap[2] - 1])
                overlaps_result.append([remap[0], remap[0] + remap[2] - 1])
            else:
                overlaps_range.append([remap[1], seed_range[1]])
                overlaps_result.append([remap[0], remap[0] + seed_range[1] - remap[1]])
        elif remap[1] < seed_range[0]:
            if remap[1] + remap[2] - 1 >= seed_range[1]:
                overlaps_range.append([seed_range[0], seed_range[1]])
                overlaps_result.append([remap[0] + seed_range[0] - remap[1] , remap[0] + seed_range[1] - remap[1]])
            elif seed_range[0] <= remap[1] + remap[2] - 1 < seed_range[1]:
                overlaps_range.append([seed_range[0], remap[1] + remap[2] - 1])
                overlaps_result.append([remap[0] + seed_range[0] - remap[1] , remap[0] + remap[2] - 1])
    seeding_result = intersecting_lines(seed_range,overlaps_range)
    for overlap in overlaps_result:
        seeding_result.append(overlap)
    return seeding_result

f = open ('input.txt', 'r')
seeds = []
maps = []
new_map = []
for line in f:
    if line == "<>":
        break
    line = line.strip()
    if line == "":
        True
    elif 'seeds:' in line:
        parse = re.split(': ',line)
        for i in re.split(' ',parse[1]):
            seeds.append(int(i))
    elif 'map' in line:
        if len(new_map) > 0:
            maps.append(new_map)
        new_map = []
    else:
        map_row = []
        for i in re.split(' ',line):
            map_row.append(int(i))
        new_map.append(map_row)
maps.append(new_map)

seeds2 = []
for i in range(len(seeds)):
    if i % 2 == 0:
        seeds2.append([seeds[i],seeds[i]+seeds[i+1] - 1])

for i in range(len(seeds)):
    for map_type in maps:
        seeds[i] = seed_through_map(seeds[i], map_type)

print(min(seeds))

for map_type in maps:
    new_seeds = []
    for cancer in seeds2:
        for k in seed_through_map2(cancer, map_type):
            new_seeds.append(k)
    seeds2 = new_seeds.copy()

seeds2_sort = sorted(seeds2, key=lambda x: x[0])
print(seeds2_sort[0][0])