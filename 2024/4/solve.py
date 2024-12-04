file_path = '2024/4/input'

def searchWord(matrix, i, j, word):
    m = len(matrix)
    n = len(matrix[0])
    total = 0

    if matrix[i][j] != word[0]:
        return total
    
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    for dir in range(8):
        currX, currY = i + x[dir], j + y[dir]
        k = 1
        while k < len(word):
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break
            if matrix[currX][currY] != word[k]:
                break
            currX += x[dir]
            currY += y[dir]
            k += 1
        if k == len(word):
            total += 1
    return total

def searchMASPattern(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])

    if matrix[i][j] != 'A':
        return False

    currX, currY, scurrX, scurrY = i - 1, j - 1, i - 1, j + 1
    revX, revY, srevX, srevY = i + 1, j + 1, i + 1, j - 1
    if currX >= m or currX < 0 or revX >= m or revX < 0 or scurrX >= m or scurrX < 0 or srevX >= m or srevX < 0 or currY >= n or currY < 0 or revY >= n or revY < 0 or scurrY >= n or scurrY < 0 or srevY >= n or srevY < 0:
        return False
    if ((matrix[currX][currY] == 'M' and matrix[revX][revY] == 'S') or (matrix[currX][currY] == 'S' and matrix[revX][revY] == 'M')) and ((matrix[scurrX][scurrY] == 'M' and matrix[srevX][srevY] == 'S') or (matrix[scurrX][scurrY] == 'S' and matrix[srevX][srevY] == 'M')):
        return True
    return False

def part1(matrix):
    totalSum = 0
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            result = searchWord(matrix, i, j, 'XMAS')
            if result > 0:
                totalSum += result
    print(f'Part 1: {totalSum}\n', end='')


def part2(matrix):
    totalSum = 0
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            if searchMASPattern(matrix, i, j):
                totalSum += 1
    print(f'Part 2: {totalSum}\n', end='')


with open(file_path, 'r') as file:
    matrix = [list(line) for line in file.read().splitlines() if line]
    part1(matrix)
    part2(matrix)