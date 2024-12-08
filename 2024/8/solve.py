import itertools

file_path = '2024/8/input'

def parseInput(file):
    dict = {}
    matrix = [list(line) for line in file.read().splitlines()]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != '.':
                if matrix[i][j] in dict:
                    dict[matrix[i][j]].append((i, j))
                else:
                    dict[matrix[i][j]] = [(i, j)]
    return matrix, dict

def getAntinodes(matrix, keys):
    m = len(matrix)
    n = len(matrix[0])
    antinodes = set()
    for key in keys:
        combs = list(itertools.combinations(dict.get(key), 2))
        for comb in combs:
            pos1, pos2 = comb[0], comb[1]
            distX = abs(pos1[0] - pos2[0])
            distY = abs(pos1[1] - pos2[1])
            if pos2[1] < pos1[1]:
                a1 = (pos1[0] - distX, pos1[1] + distY)
            else:
                a1 = (pos1[0] - distX, pos1[1] - distY)
            if pos2[1] < pos1[1]:
                a2 = (pos2[0] + distX, pos2[1] - distY)
            else:
                a2 = (pos2[0] + distX, pos2[1] + distY)
            if (a1[0] < m and a1[0] >= 0) and (a1[1] < n and a1[1] >= 0):
                antinodes.add(a1)
            if (a2[0] < m and a2[0] >= 0) and (a2[1] < n and a2[1] >= 0):
                antinodes.add(a2)
    return len(antinodes)

def getResonantAntinodes(matrix, keys):
    sum = 0
    m = len(matrix)
    n = len(matrix[0])
    antinodes = set()
    for key in keys:
        for node in dict.get(key):
            antinodes.add(node)
        combs = list(itertools.combinations(dict.get(key), 2))
        for comb in combs:
            pos1, pos2 = comb[0], comb[1]
            distX = abs(pos1[0] - pos2[0])
            distY = abs(pos1[1] - pos2[1])
            a1, a2 = (pos1[0], pos1[1]), (pos2[0], pos2[1])
            while (a1[0] < m and a1[0] >= 0) and (a1[1] < n and a1[1] >= 0):
                if a2[1] < a1[1]:
                    a1 = (a1[0] - distX, a1[1] + distY)
                else:
                    a1 = (a1[0] - distX, a1[1] - distY)
                if (a1[0] < m and a1[0] >= 0) and (a1[1] < n and a1[1] >= 0):
                    antinodes.add(a1)
            while (a2[0] < m and a2[0] >= 0) and (a2[1] < n and a2[1] >= 0):
                if a2[1] < a1[1]:
                    a2 = (a2[0] + distX, a2[1] - distY)
                else:
                    a2 = (a2[0] + distX, a2[1] + distY)
                if (a2[0] < m and a2[0] >= 0) and (a2[1] < n and a2[1] >= 0):
                    antinodes.add(a2)
    return len(antinodes)

def part1(matrix, dict):
    totalSum = getAntinodes(matrix, dict.keys())
    print(f'Part 1: {totalSum}\n', end='')

def part2(matrix, dict):
    totalSum = getResonantAntinodes(matrix, dict.keys())
    print(f'Part 2: {totalSum}\n', end='')

with open(file_path, 'r') as file:
    matrix, dict = parseInput(file)
    part1(matrix, dict)
    part2(matrix, dict)