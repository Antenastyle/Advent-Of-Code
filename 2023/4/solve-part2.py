file_path = '2023/4/input'

def getWinningValue(data):
    score, totalSum = 0, 0
    cardCount = []
    for i in range(len(data)):
        cardCount.append(1)
    for index, line in enumerate(data):
        winningNumbers = line.split('|')[0].split(':')[1].split()
        myNumbers = line.split('|')[1].split()
        winnersCount = len([number for number in myNumbers if number in winningNumbers])
        score = pow(2, winnersCount - 1)
        for i in range(winnersCount):
            cardCount[index + i + 1] += cardCount[index]
        totalSum += score
        score, winnersCount = 0, 0
    return sum(cardCount)
        

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getWinningValue(data))
