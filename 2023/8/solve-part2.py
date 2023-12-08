import re

file_path = '2023/8/input'

def getSteps(data):
    instructions = 15000 * data[0]
    desertMap, actualPoints = [], []
    for i in range(1, len(data)):
        new = re.sub("|".join(map(re.escape, ['=', '(', ')', ','])), '', data[i]).split()
        if(new[0][2] == 'A'): actualPoints.append(new[0])
        desertMap.append(new)
    steps = 0
    for instruction in instructions:
        for i, point in enumerate(actualPoints):
            actualPoints[i] = followInstruction(point, instruction, desertMap)
        steps += 1
        if areEndingPoints(actualPoints): break
    return steps

def followInstruction(pos, ins, desertMap):
    index = next(i for i, line in enumerate(desertMap) if line[0] == pos)
    if ins == 'L': return desertMap[index][1]
    else: return desertMap[index][2]

def areEndingPoints(points):
    for point in points:
        if(point[2] != 'Z'): return False
    return True

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getSteps(data))