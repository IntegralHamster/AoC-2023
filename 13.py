with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

tests = []
test = []
for line in lines:
    if line == '':
        tests.append(test)
        test = []
    else:
        test.append(line)
tests.append(test)

def symmetry_search(lines, factor, old_symmetry):
    for i in range(len(lines) - 1):
        if lines[i] == lines[i+1] and i != old_symmetry:
            count = 0
            flag = 1
            while i + 1 + count < len(lines) and i - count >= 0:
                if lines[i - count] != lines[i + count + 1]:
                    flag = 0
                    break
                else:
                    count += 1
            if flag == 1:
                return (i+1)*factor
    return 0

ans1 = 0
symmetry_memory = []
for test in tests:
    horizontal_lines = [list(line) for line in test]
    vertical_lines = [[] for i in range(len(horizontal_lines[0]))]

    for j in range(len(horizontal_lines)):
        for i in range(len(horizontal_lines[j])):
            vertical_lines[i].append(horizontal_lines[j][i])

    ver_ans = (symmetry_search(vertical_lines,1, -1))
    hor_ans = (symmetry_search(horizontal_lines, 100, -1))
    if hor_ans != 0:
        ans1 += hor_ans
        symmetry_memory.append([-1, hor_ans // 100 - 1])
    elif ver_ans != 0:
        symmetry_memory.append([ver_ans - 1, -1])
        ans1 += ver_ans

print(ans1)

ans2 = 0
for num in range(len(tests)):
    horizontal_lines = [list(line) for line in tests[num]]
    flag = 0
    for i in range(len(horizontal_lines)):
        for j in range(len(horizontal_lines[i])):
            if horizontal_lines[i][j] == '#':
                horizontal_lines[i][j] = '.'
            else:
                horizontal_lines[i][j] = '#'
            vertical_lines = [[] for i in range(len(horizontal_lines[0]))]

            for k in range(len(horizontal_lines)):
                for l in range(len(horizontal_lines[k])):
                    vertical_lines[l].append(horizontal_lines[k][l])
            ver_ans = 0
            hor_ans = 0
            ver_ans = (symmetry_search(vertical_lines,1, symmetry_memory[num][0]))
            hor_ans = (symmetry_search(horizontal_lines, 100, symmetry_memory[num][1]))
            if ver_ans != 0 or hor_ans != 0:
                ans2 += ver_ans + hor_ans
                flag = 1
                break
            if horizontal_lines[i][j] == '#':
                horizontal_lines[i][j] = '.'
            else:
                horizontal_lines[i][j] = '#'
        if flag == 1:
            break
print(ans2)
