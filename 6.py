import re
import math

def interval_find(a, b):
    # imagine not knowing how parabolas work
    lower_boundary = 0.5*(a - math.sqrt(a**2 - 4*b))
    upper_boundary = 0.5*(a + math.sqrt(a**2 - 4*b))
    return 1 - math.ceil(lower_boundary) + math.floor(upper_boundary) - lower_boundary.is_integer() - upper_boundary.is_integer()

with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

time = []
time2 = ''
for i in re.split(" ",re.split(":",lines[0])[1].strip()):
    if i != '':
        time.append(int(i))
        time2 += i
distance = []
distance2 = ''
for i in re.split(" ",re.split(":",lines[1])[1].strip()):
    if i != '':
        distance.append(int(i))
        distance2 += i

ans1 = 1
for i in range(len(distance)):
    ans1 *= interval_find(time[i], distance[i])
print(ans1) #part 1 answer
print(interval_find(int(time2), int(distance2))) #part 2 answer