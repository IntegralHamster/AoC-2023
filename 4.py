import re

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

ans1 = 0
num = 0
win_array = []
for line in lines:
    num += 1
    card = re.split(r"[:|]", line)
    card_win = re.split(r" ", card[1].strip())
    card_num = re.split(r" ", card[2].strip())
    while ("" in card_win):
        card_win.remove("")
    while ("" in card_num):
        card_num.remove("")
    overlap = [number for number in card_num if number in card_win]
    if len(overlap) > 0:
        ans1 += 2**(len(overlap)-1)
    win_array.append([num, len(overlap)])

print(win_array)
copies = [1 for i in range(len(lines))]
for i in range(len(lines)):
    if win_array[i][1] > 0:
        for j in range(win_array[i][1]):
            if i + j + 1 < len(copies):
                copies[i+j+1] += copies[i]

print(copies)
print(ans1, sum(copies))
