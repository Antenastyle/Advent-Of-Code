import re

file_path = '2023/8/input'

def getSteps(data):
    instructions = 75 * data[0]
    desertMap = []
    for i in range(1, len(data)):
        new = re.sub("|".join(map(re.escape, ['=', '(', ')', ','])), '', data[i]).split()
        desertMap.append(new)
    actual = 'AAA'
    steps = 0
    for instruction in instructions:
        actual = followInstruction(actual, instruction, desertMap)
        steps += 1
        if actual == 'ZZZ': break
    return steps

def followInstruction(pos, ins, desertMap):
    index = next(i for i, line in enumerate(desertMap) if line[0] == pos)
    if ins == 'L': return desertMap[index][1]
    else: return desertMap[index][2]


with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getSteps(data))