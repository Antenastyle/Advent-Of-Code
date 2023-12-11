file_path = '2023/10/input'

def getFarthestDistance(data):
    steps = 1
    startX, startY = getStartingPoint(data)
    nextX, nextY, lastX, lastY = getNextPoint(data, startX, startY, -1, -1)
    while(nextX != startX or nextY != startY):
        nextX, nextY, lastX, lastY = getNextPoint(data, nextX, nextY, lastX, lastY)
        steps += 1
    return int(steps / 2)

def getStartingPoint(data):
    for i, line in enumerate(data):
        for j, char in enumerate(data[i]):
            if char == 'S': return i, j
    return -1, -1

def getNextPoint(data, x, y, lastX, lastY):
    print(x, y, lastX, lastY)
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
    print(getFarthestDistance(data))