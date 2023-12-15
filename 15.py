from collections import OrderedDict

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

strings = lines[0].split(',')

def hash (inp_str):
    hashsum = 0
    for char in inp_str:
        hashsum += ord(char)
        hashsum *= 17
        hashsum %= 256
    return hashsum

hashes = []
ans = 0
for string in strings:
    hsum = hash(string)
    hashes.append([string, hsum])
    ans += hsum
print(ans)

boxes = [OrderedDict() for i in range(256)]

for string in strings:
    if '-' in string:
        lens_name = string.split('-')[0]
        boxnum = hash(lens_name)
        if lens_name in boxes[boxnum].keys():
            boxes[boxnum].pop(lens_name)
    elif '=' in string:
        lens_name, lens_power = string.split('=')
        boxnum = hash(lens_name)
        boxes[boxnum][lens_name] = int(lens_power)

ans2 = []
for i in range(256):
    count = 1
    for key in list(boxes[i].keys()):
        ans2.append(count * (i+1) * boxes[i][key])
        boxes[i].pop(key)
        count += 1

print(sum(ans2))

