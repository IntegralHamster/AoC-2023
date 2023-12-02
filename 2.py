import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

ans1 = 0
ans2 = 0
red_limit = 12
green_limit = 13
blue_limit = 14

for i in range(len(lines)):
    parse1 = re.split(r"[:;]", lines[i])
    add_flag = True
    red_cubes = -1
    green_cubes = -1
    blue_cubes = -1
    for j in range(len(parse1)-1):
        parse2 = re.split(r",",parse1[j+1])
        for cubes in parse2:
            parse3 = re.split(r"\s", cubes.strip())
            if (int(parse3[0]) > red_cubes and parse3[1] == 'red'):
                red_cubes = int(parse3[0])
            if (int(parse3[0]) > green_cubes and parse3[1] == 'green'):
                green_cubes = int(parse3[0])
            if (int(parse3[0]) > blue_cubes and parse3[1] == 'blue'):
                blue_cubes = int(parse3[0])
            if (red_cubes > red_limit or green_cubes > green_limit or blue_cubes > blue_limit) and add_flag == True:
                add_flag = False
    if add_flag == True:
        ans1 += i+1
    ans2 += red_cubes*green_cubes*blue_cubes

print(ans1, ans2)
