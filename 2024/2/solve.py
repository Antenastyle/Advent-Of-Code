file_path = '2024/2/input'

def isLineSafe(line):
    if line != sorted(line) and line != sorted(line, reverse=True):
        return False
    return all(0 < abs(a - b) < 4 for a, b in zip(line, line[1:]))

def part1(lines):
    totalSum = sum(isLineSafe(line) for line in lines)
    print(f'Part 1: {totalSum}\n', end='')

def part2(lines):
    totalSum = sum(isLineSafe(line) or any(isLineSafe(line[:i] + line [i + 1:]) for i in range(len(line))) for line in lines)
    print(f'Part 2: {totalSum}\n', end='')


with open(file_path, 'r') as file:
    lines = [list(map(int, line.split())) for line in file]
    part1(lines)
    part2(lines)