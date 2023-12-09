with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

def sequence_difference (sequence):
    difference = []
    for i in range(len(sequence) - 1):
        difference.append(sequence[i+1] - sequence[i])
    return difference

def next_number (sequence):
    sequences = [sequence]
    while len(set(sequences[-1])) > 1:
        sequences.append(sequence_difference((sequences[-1])))
    len_s = len(sequences)
    for i in range(len_s - 1):
        sequences[len_s - i - 2].append(sequences[len_s - i - 2][-1] + sequences[len_s - i - 1][-1])
    return sequences[0][-1]

ans1 = 0
ans2 = 0
for line in lines:
    ans1 += next_number([int(i) for i in line.split()])
    ans2 += next_number(list(reversed([int(i) for i in line.split()])))
print(ans1)
print(ans2)
