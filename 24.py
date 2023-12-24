with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

hailstones = []

for line in lines:
    parse = line.split(' @ ')
    coordinates = [int(i.strip()) for i in parse[0].split(',')]
    velocities = [int(i.strip()) for i in parse[1].split(',')]
    hailstones.append([coordinates.copy(), [coordinates[i] + velocities[i] for i in range(len(coordinates))], velocities].copy())

def line_coefficients_2d (x1, x2, y1, y2):
    a = (y2 - y1) / (x2 - x1)
    b = y1 - a*x1
    return (a, b)

def line_coefficients_3d (x1, x2, y1, y2, z1, z2)

for i in range(len(hailstones)):
    hailstones[i].append(line_coefficients_2d(hailstones[i][0][0], hailstones[i][1][0], hailstones[i][0][1], hailstones[i][1][1]))


def intersect_2d (a1, c1, a2, c2):
    b1 = b2 = -1
    det = a1*b2 - b1*a2
    if det == 0:
        return False
    else:
        return ((b1*c2 - b2*c1)/det, (c1*a2 - a1*c2)/det)

boundaries = (200000000000000,400000000000000)
ans = 0
for i in range(len(hailstones) - 1):
    for j in range(i, len(hailstones)):
        intersection = intersect_2d(hailstones[i][3][0], hailstones[i][3][1], hailstones[j][3][0], hailstones[j][3][1])
        if intersection:
            if not (boundaries[0] <= intersection[0] <= boundaries[1]) or not (boundaries[0] <= intersection[1] <= boundaries[1]):
                continue
            t1 = (intersection[0] - hailstones[i][0][0]) / hailstones[i][2][0]
            t2 = (intersection[0] - hailstones[j][0][0]) / hailstones[j][2][0]
            if t1 < 0 or t2 < 0:
                continue
            print(i, j)
            ans += 1

print(ans)

# for part 2 go here, thanks IFT https://i.imgur.com/UAFyfwO.png