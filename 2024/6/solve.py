file_path = '2024/6/input'

def parseInput(file):
    start = []
    matrix = [list(line) for line in file.read().splitlines()]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '^':
                start.append(i)
                start.append(j)
                matrix[i][j] = '.'
    return matrix, start

def calculatePositions(matrix, start):
    directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    pos = [0, 0]
    pos[0], pos[1] = start[0], start[1]
    positions = set()
    positions.add((pos[0], pos[1]))
    dir, rep = 0, 0
    end, next = False, False
    while not end:
        pos[0] += directions[dir][0]
        pos[1] += directions[dir][1]
        if rep >= len(matrix):
            return -1
        if pos[0] >= len(matrix) or pos[0] < 0 or pos[1] >= len(matrix[0]) or pos[1] < 0:
            end = True
            break
        if matrix[pos[0]][pos[1]] != '.':
            pos[0] -= directions[dir][0]
            pos[1] -= directions[dir][1]
            dir =  dir + 1 if dir < 3 else 0
        else:
            if (pos[0], pos[1]) in positions:
                if next:
                    rep += 1
                else:
                    rep = 1
                    next = True
            else: 
                next = False
                rep = 0
            positions.add((pos[0], pos[1]))
    return positions

def calculateRoute(matrix, start):
    pos = [0, 0]
    sum = 0
    for position in calculatePositions(matrix, start):
        pos[0], pos[1] = start[0], start[1]
        matrix[position[0]][position[1]] = 'O'
        if calculatePositions(matrix, pos) == -1:
            sum += 1
        matrix[position[0]][position[1]] = '.'
    return sum

def part1(matrix, start):
    totalSum = len(calculatePositions(matrix, start))
    print(f'Part 1: {totalSum}\n', end='')

def part2(matrix, start):
    totalSum = calculateRoute(matrix, start)
    print(f'Part 2: {totalSum}\n', end='')

with open(file_path, 'r') as file:
    matrix, start = parseInput(file)
    part1(matrix, start)
    part2(matrix, start)