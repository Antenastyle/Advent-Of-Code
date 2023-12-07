from collections import Counter

file_path = '2023/7/input'

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
handsValue = {
    (5,): 7,
    (1,4): 6,
    (2,3): 5,
    (1,1,3): 4,
    (1,2,2): 3,
    (1,1,1,2): 2,
    (1,1,1,1,1): 1
}

def getTotalWinnings(data):
    hands, bids = [], []
    for i in range(len(data)):
        hands.append(data[i].split()[0])
        bids.append(int(data[i].split()[1]))
    handTypes = []
    for hand in hands:
        count = Counter(hand)
        if len(count) == 1 and 'J' in count:
            handTypes.append((7, hand))
            continue

        biggestCard = sorted(count, key=count.get)[-1]
        if biggestCard == 'J': biggestCard = sorted(count, key=count.get)[-2]

        count[biggestCard] += count.get('J', 0)
        count.pop('J', None)

        handTypes.append((handsValue[tuple(sorted(count.values()))], hand))
    handTypes.sort()
    groupedHands = groupHands(handTypes)
    ranks = rankHands(groupedHands, cards, data, hands)

    totalWinnings = 0
    for i in range(len(hands)):
        totalWinnings += bids[i] * ranks[i]
    return totalWinnings

def groupHands(handTypes):
    groupedType = {}
    for handType in handTypes:
        if handType[0] in groupedType:
            groupedType[handType[0]].append(handType[1])
        else:
            groupedType[handType[0]] = [handType[1]]
    return groupedType.values()

def rankHands(groupedHands, cards, data, hands):
    ranks = [0 for i in range(len(data))]
    rank = 1
    for group in groupedHands:
        group = sorted(group, key=lambda s: tuple(cards.index(c) for c in s))
        for hand in group:
            ranks[hands.index(hand)] = rank
            rank += 1
    return ranks

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getTotalWinnings(data))