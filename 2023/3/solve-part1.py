import re
from itertools import product

file_path = '2023/3/input'

def isSymbol(characters):
    for char in characters:
        if char not in ".0123456789":
            return True
    return False

def getAdjacentSum(data, number, start, end, lineY):
    totalSum = 0
    maxY = len(data)
    maxX = len(data[0])

    adjacentCoordinates = product(
        range(lineY - 1, lineY + 2),
        range(start - 1, end + 2)
    )

    adjacentCharacters = [
        data[y][x]
        for y, x in adjacentCoordinates
        if 0 <= y < maxY and 0 <= x < maxX
        and (y != lineY or x not in range(start, end + 1))
    ]

    if isSymbol(adjacentCharacters):
        totalSum += int(number)
    return totalSum


with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    sum = 0
    for y, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            sum += getAdjacentSum(data, m.group(0), m.start(), m.end() - 1, y)
    print(sum)