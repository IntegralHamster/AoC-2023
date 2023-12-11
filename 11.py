with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

horizontal_empty = [i for i in range(len(lines[0]))]
vertical_empty = [i for i in range(len(lines))]
galaxies = []

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '#':
            galaxies.append([i,j])
            if i in vertical_empty:
                vertical_empty.remove(i)
            if j in horizontal_empty:
                horizontal_empty.remove(j)

def distance (gal1, gal2, expansion_factor):
    base_distance = abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])
    for expand in horizontal_empty:
        if gal1[1] < expand < gal2[1] or gal2[1] < expand < gal1[1]:
            base_distance += expansion_factor - 1
    for expand in vertical_empty:
        if gal1[0] < expand < gal2[0] or gal2[0] < expand < gal1[0]:
            base_distance += expansion_factor - 1
    return base_distance

total_distance1 = total_distance2 = 0
for i in range(len(galaxies) - 1):
    for j in range(i+1, len(galaxies)):
        total_distance1 += distance(galaxies[i], galaxies[j], 2)
        total_distance2 += distance(galaxies[i], galaxies[j], 1000000)

print(total_distance1, total_distance2)