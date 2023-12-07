with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

card_sub = {
    '2': "B",
    '3': "C",
    '4': "D",
    '5': "E",
    '6': "F",
    '7': "G",
    '8': "H",
    '9': "I",
    'T': "L",
    'J': "M",
    'Q': "N",
    'K': "O",
    'A': "P"
}
card_sub2 = {
    'J': "B",
    '2': "C",
    '3': "D",
    '4': "E",
    '5': "F",
    '6': "G",
    '7': "H",
    '8': "I",
    '9': "L",
    'T': "M",
    'Q': "N",
    'K': "O",
    'A': "P"
}
hands = []
for line in lines:
    hands.append(line.split())

def ordering1(hand_s):
    for hand in hand_s:
        hand_l = list(hand[0])
        for i in range(len(hand_l)):
            hand_l[i] = card_sub[hand_l[i]]
        hand_count = []
        for i in set(sorted(hand_l)):
            hand_count.append(str(hand_l.count(i)))
        hand_count = sorted(hand_count, reverse=True)
        hand[0] = "".join(hand_l)
        hand.append("".join(hand_count))
    return hand_s

def ordering2(hands):
    for hand in hands:
        hand_l = list(hand[0])
        for i in range(len(hand_l)):
            hand_l[i] = card_sub2[hand_l[i]]
        hand_count = []
        for i in set(sorted(hand_l)):
            hand_count.append([i, hand_l.count(i)])
        hand_count = sorted(hand_count, key=lambda x: x[1], reverse=True)
        for card in hand_count:
            if card[0] != 'B':
                card[1] += hand_l.count('B')
                break
        hand_count = sorted(hand_count, key=lambda x: x[1], reverse=True)
        for card in hand_count:
            if card[0] == 'B' and card[1] != 5:
                hand_count.remove([card[0],card[1]])
        hand[0] = "".join(hand_l)
        hand_power = ""
        for card in hand_count:
            hand_power += str(card[1])
        hand.append(hand_power)
    return hands

#I'm too lazy to code second output, just change ordering1 to ordering2 if you want second part

hands1 = sorted(ordering1(hands), key=lambda x: (x[2], x[0]), reverse = True)
ans = 0
for i in range(len(hands1)):
    ans += (len(hands1) - i) * int(hands1[i][1])
print(ans)

