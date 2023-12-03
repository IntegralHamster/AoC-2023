import re

special_characters = "!@#$%^&*()-+?_=,<>/"

def adjacency_check(array,i,j,length, num_lines):
    check = False
    for num in range(length):
        for dx in range(-1,2):
            for dy in range(-1,2):
                if not (dx == 0 and dy == 0):
                    if -1 < i+dy < num_lines and -1 < j+num+dx < len(array[i]):
                        if array[i+dy][j+num+dx] in special_characters:
                            check = True
                            break
            if check:
                break
        if check:
            break
    return check

def substr_length(array,i,j):
    count = 0
    while True:

        if j+count >= len(array[i]):
            break
        if array[i][j+count] in special_characters or array[i][j+count] == ' ':
            break
        count += 1
    return count

with open('input.txt') as f:
    lines = [line.strip().replace('.',' ') for line in f.readlines()]

inp_len = len(lines)

num_strings = []
gear_positions = []

for i in range(inp_len):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] == '*':
            gear_positions.append([i,j])
        if lines[i][j].isnumeric():
            length = substr_length(lines,i,j)
            flag = adjacency_check(lines,i,j,length,inp_len)
            num_strings.append([i,j,length,flag, int(lines[i][j:j+length])])
            j += length - 1
        j += 1

ans1 = 0
for string in num_strings:
    if string[3]:
        ans1 += string[4]

ans2 = 0
for gear in gear_positions:
    gear_value = 1
    gear_num = 0
    for num in num_strings:
        if (num[0] - 1 <= gear[0] <= num[0] + 1) and (num[1] - 1 <= gear[1] <= num[1] + num[2]):
            gear_value *= num[4]
            gear_num += 1
        if gear_num > 2:
            break
    if gear_num == 2:
        ans2 += gear_value

print(ans1, ans2)
