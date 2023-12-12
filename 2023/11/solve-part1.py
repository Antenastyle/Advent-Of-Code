file_path = '2023/11/input'

def getTotalPathSum(data):
    newData, columns, galaxies, i, totalSum = [], [], [], 0, 0
    for index, line in enumerate(data):
        newData.append(line)
        if checkRowDots(line): 
            newData.insert(index + i, line)
            i += 1
    for index in range(len(newData[0])):
        if checkColumnDots(index, newData): columns.append(index)
    i = 0
    for column in columns: 
        insertColumn(column, newData, i)
        i += 1
    for i, line in enumerate(newData):
        for j, char in enumerate(line):
            if char == '#': galaxies.append([i, j])
    for galaxy in galaxies:
        totalSum += getGalaxySum(galaxy, galaxies)
        galaxies = galaxies[1:]
    return totalSum

def getGalaxySum(g, galaxies):
    sum = 0
    for galaxy in galaxies:
        if g != galaxy: sum += abs(g[0] - galaxy[0]) + abs(g[1] - galaxy[1])
    return sum

def insertColumn(index, data, j):
    for i in range(len(data)):
        data[i] = data[i][:(index + j)] + '.' + data[i][(index + j):]

def checkColumnDots(index, data):
    for i in range(len(data)):
        if data[i][index] != '.': return False
    return True

def checkRowDots(line):
    for char in line:
        if char != '.': return False
    return True

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getTotalPathSum(data))