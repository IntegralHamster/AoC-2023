import re

f = open('input.txt', 'r')
inp = []
for line in f:
    if line == '<>':
        break
    inp.append(line.strip())

# part 1

sum = 0
for i in range(len(inp)):
    nums = re.sub(r"\D", "", inp[i])
    sum += 10 * int(nums[0]) + int(nums[-1])
print(sum)

# part 2

cancer_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

cancer_strings = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'zero', 'one', 'two', 'three', 'four', 'five',
                  'six', 'seven', 'eight', 'nine']
sum2 = 0
for i in range(len(inp)):
    left = 999999
    right = -1
    left_digit = -1
    right_digit = - 1
    for cancer in cancer_strings:
        if -1 < inp[i].find(cancer) < left:
            left_digit = cancer_dict[cancer]
            left = inp[i].find(cancer)
        if inp[i].rfind(cancer) > right:
            right_digit = cancer_dict[cancer]
            right = inp[i].rfind(cancer)
    ans = 10*left_digit + right_digit
    sum2 += ans
    print(inp[i], ans)
print(sum2)
