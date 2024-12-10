file_path = '2024/10/input'

def parseInput(file):
    trailheads = []
    matrix = [list(line) for line in file.read().splitlines()]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '0':
                trailheads.append((i, j))
    return matrix, trailheads

def hasMultiplePaths(matrix, pos, number):
    paths = set()
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    m = len(matrix)
    n = len(matrix[0])
    newPos = [0, 0]
    for dir in directions:
        newPos[0], newPos[1] = pos[0] + dir[0], pos[1] + dir[1]
        if newPos[0] >= m or newPos[0] < 0 or newPos[1] >= n or newPos[1] < 0:
            continue
        if matrix[newPos[0]][newPos[1]] == number:
            paths.add((newPos[0], newPos[1]))
    return paths

def calculateTrailheadScore(matrix, trailhead, index=1):
    sum = set()
    paths = hasMultiplePaths(matrix, trailhead, str(index))
    if index == 9:
        return paths
    else:
        for path in paths:
            for res in calculateTrailheadScore(matrix, path, index + 1):
                sum.add(res)
    return sum

def calculateTrailheadScoreRating(matrix, trailhead, index=1):
    sum = 0
    paths = hasMultiplePaths(matrix, trailhead, str(index))
    if index == 9:
        return len(paths)
    else:
        for path in paths:
            sum += calculateTrailheadScoreRating(matrix, path, index + 1)
    return sum

def part1(matrix, trailheads):
    totalSum = sum(len(calculateTrailheadScore(matrix, trailhead)) for trailhead in trailheads)
    print(f'Part 1: {totalSum}\n', end='')

def part2(matrix, trailheads):
    totalSum = sum(calculateTrailheadScoreRating(matrix, trailhead) for trailhead in trailheads)
    print(f'Part 2: {totalSum}\n', end='')

with open(file_path, 'r') as file:
    matrix, trailheads = parseInput(file)
    part1(matrix, trailheads)
    part2(matrix, trailheads)