with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def line_check(line, springs):
    pos = 0
    pos_spr = 0
    while pos < len(line):
        if line[pos] == '.':
            pos += 1
        elif line[pos] == '#':
            if pos_spr >= len(springs):
                return 0
            elif len(set(line[pos:pos+springs[pos_spr]])) == 1 and len(line[pos:pos+springs[pos_spr]]) == springs[pos_spr]:
                if pos+springs[pos_spr] < len(line):
                    if line[pos+springs[pos_spr]] == '#':
                        return 0
                pos += springs[pos_spr] + 1
                pos_spr += 1
            else:
                return 0
    if pos_spr >= len(springs):
        return 1
    else:
        return 0

def line_possibilities(line):
    options = []
    if '?' not in line:
        options.append(line)
    else:
        question = line.find('?')
        line1 = line[:question] + '#' + line[question + 1:]
        line2 = line[:question] + '.' + line[question + 1:]
        for option in line_possibilities(line1):
            options.append(option)
        for option in line_possibilities(line2):
            options.append(option)
    return options

ans = 0
for inp in lines:
    tot = 0
    parse = inp.split()
    pattern = [int(i) for i in parse[1].split(',')]
    line0 = parse[0]
    str_option = line_possibilities(line0)
    check_str = []
    for line in str_option:
        if line_check(line, pattern):
            tot += 1
            check_str.append(line)
    ans += tot
    print(pattern, tot)
print(ans)

# well at least i got part 1 on my own
