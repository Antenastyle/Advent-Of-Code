import re
from itertools import product

file_path = '2023/3/input'

def getGears(data):
    totalSum = 0
    maxY = len(data)

    for y in range(maxY):
        for c in re.finditer(r"\*", data[y]):
            adjacentNumbers = []
            for checkY in [-1, 0, 1]:
                for number in re.finditer(r"\d+", data[y + checkY]):
                    if c.start() in range(number.start() - 1, number.end() + 1):
                        adjacentNumbers.append(int(number.group(0)))
            if len(adjacentNumbers) == 2:
                totalSum += adjacentNumbers[0] * adjacentNumbers[1]
    return totalSum


with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getGears(data))