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
        newLines[i - 1].append((newLines[i - 1][len(newLines[i - 1]) - 1]) + newLines[i][len(newLines[i]) - 1])
        i -= 1
    sum = line[len(line) - 1] + newLines[0][len(newLines[0]) - 1]
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