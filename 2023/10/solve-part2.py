file_path = '2023/10/input'

def getEnclosedTiles(data):
    loopTiles, totalTiles = [], 0
    startX, startY = getStartingPoint(data)
    loopTiles.append([startX, startY])
    nextX, nextY, lastX, lastY = getNextPoint(data, startX, startY, -1, -1)
    while(nextX != startX or nextY != startY):
        loopTiles.append([nextX, nextY])
        nextX, nextY, lastX, lastY = getNextPoint(data, nextX, nextY, lastX, lastY)
    print(loopTiles)
    inLoop = False
    for i in range(0, len(data)):
        for j in range(0, len(data[0])):
            if [i, j] in loopTiles:
                if data[i][j] == '|': inLoop = changeLoop(inLoop)
                elif data[i][j] == 'S' and data[i][j + 1] not in ['J', '7'] and not inLoop: inLoop = changeLoop(inLoop)
                if j + 1 < len(data[0]):
                    if data[i][j] == 'F' and data[i][j + 1] not in ['J', '7'] and not inLoop: inLoop = changeLoop(inLoop)
                    elif data[i][j] == 'L' and data[i][j + 1] not in ['J', '7'] and not inLoop: inLoop = changeLoop(inLoop)
                    elif data[i][j] == 'J' and data[i][j + 1] not in ['L', 'F']and not inLoop: inLoop = changeLoop(inLoop)
                    elif data[i][j] in ['7', 'J'] and data[i][j + 1] != '|' and inLoop: inLoop = False
                else: inLoop = False
            else:
                if inLoop:
                    print(data[i][j], i, j)
                    totalTiles += 1
    return totalTiles

def changeLoop(loop):
    if loop: return False
    else: return True

def getStartingPoint(data):
    for i, line in enumerate(data):
        for j, char in enumerate(data[i]):
            if char == 'S': return i, j
    return -1, -1

def getNextPoint(data, x, y, lastX, lastY):
    auxX, auxY = 0, 0
    if data[x][y] == '-':
        auxX = x
        if (y + 1) == lastY: auxY = y - 1
        else: auxY = y + 1
    elif data[x][y] == 'S':
        auxX = x + 1
        auxY = y
    elif data[x][y] == '|':
        auxY = y
        if (x + 1) == lastX: auxX = x - 1
        else: auxX = x + 1
    elif data[x][y] == 'L':
        if (y + 1) == lastY:
            auxX = x - 1
            auxY = y
        else:
            auxX = x
            auxY = y + 1
    elif data[x][y] == 'J':
        if (y - 1) == lastY:
            auxX = x - 1
            auxY = y
        else:
            auxX = x
            auxY = y - 1
    elif data[x][y] == 'F':
        if (y + 1) == lastY:
            auxX = x + 1
            auxY = y
        else:
            auxX = x
            auxY = y + 1
    else:
        if (y - 1) == lastY:
            auxX = x + 1
            auxY = y
        else:
            auxX = x
            auxY = y - 1
    lastX, lastY = x, y
    return auxX, auxY, lastX, lastY


with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getEnclosedTiles(data))