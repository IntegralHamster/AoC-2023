with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

start1 = [0, 0]
start2 = [0, 0]
corners1 = []
corners2 = []
perimeter1 = 0
perimeter2 = 0
for line in lines:
    parse = line.split(' ')
    if parse[0] == 'R':
        start1[0] += int(parse[1])
    elif parse[0] == 'L':
        start1[0] -= int(parse[1])
    elif parse[0] == 'D':
        start1[1] += int(parse[1])
    elif parse[0] == 'U':
        start1[1] -= int(parse[1])
    if parse[2][7] == '0':
        start2[0] += int(parse[2][2:7], base = 16)
    elif parse[2][7] == '2':
        start2[0] -= int(parse[2][2:7], base = 16)
    elif parse[2][7] == '1':
        start2[1] += int(parse[2][2:7], base = 16)
    elif parse[2][7] == '3':
        start2[1] -= int(parse[2][2:7], base = 16)
    corners1.append([start1[0], start1[1]])
    corners2.append([start2[0], start2[1]])
    perimeter1 += int(parse[1])
    perimeter2 += int(int(parse[2][2:7], base = 16))

area1 = 0
area2 = 0
for i in range(len(corners1)):
    area1 += (corners1[i-1][1] * corners1[i][0] - corners1[i-1][0] * corners1[i][1])
    area2 += (corners2[i-1][1] * corners2[i][0] - corners2[i-1][0] * corners2[i][1])

inside1 = abs(area1) // 2 - perimeter1 // 2 + 1
inside2 = abs(area2) // 2 - perimeter2 // 2 + 1
print(inside1 + perimeter1, inside2 + perimeter2)