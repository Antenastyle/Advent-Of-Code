from itertools import product

file_path = '2024/7/input'

def sumOfOperations(operators, lines):
    sum = 0
    for line in lines:
        result = int(line[0])
        operands = line[1].split()
        for comb in product(operators, repeat=len(operands) - 1):
            tempres = int(operands[0])
            operation = ''.join(comb)
            for index in range(len(operands) - 1):
                if operation[index] == '+':
                    tempres += int(operands[index + 1])
                elif operation[index] == '*':
                    tempres *= int(operands[index + 1])
                elif operation[index] == '|':
                    tempres = int(str(tempres) + str(operands[index + 1]))
            if tempres == result:
                sum += result
                break
    return sum

def part1(lines):
    totalSum = sumOfOperations(['+', '*'], lines)
    print(f'Part 1: {totalSum}\n', end='')

def part2(lines):
    totalSum = sumOfOperations(['+', '*', '|'], lines)
    print(f'Part 2: {totalSum}\n', end='')

with open(file_path, 'r') as file:
    lines = [list(line.split(':')) for line in file]
    part1(lines)
    part2(lines)