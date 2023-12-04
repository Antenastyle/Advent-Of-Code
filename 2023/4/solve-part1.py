file_path = '2023/4/input'

def getWinningValue(line):
    winnersCount = 0
    winningNumbers = line.split('|')[0].split(':')[1].split()
    myNumbers = line.split('|')[1].split()
    winnersCount = len([number for number in myNumbers if number in winningNumbers])
    if winnersCount > 0:
        return pow(2, (winnersCount - 1))
    else: 
        return 0

with open(file_path, 'r') as file:
    sum = 0
    for line in file:
        sum += getWinningValue(line)
    print(sum)