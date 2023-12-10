file_path = '2023/9/input'

def getValuesSum(data):
    totalSum = 0
    for line in data:
        line = [int(number) for number in line.split()]
        newLines, index = [], 0
        newLines.append(processLine(line))
        while not checkZeroes(newLines, index):
            newLines.append(processLine(newLines[index]))
            index += 1
        totalSum += getSum(newLines, line)
    return totalSum

def getSum(newLines, line):
    i = len(newLines) - 1
    sum = 0
    while i >= 1:
        newLines[i - 1].insert(0, (newLines[i - 1][0] - newLines[i][0]))
        i -= 1
    sum = line[0] - newLines[0][0]
    return sum

def processLine(line):
    newLine = []
    for i, x in enumerate(line):
        if i == 0: continue
        else: newLine.append(x - line[i - 1])
    return newLine

def checkZeroes(line, index):
    for number in line[index]:
        if number != 0: return False
    line[index].append(0)
    return True

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getValuesSum(data))