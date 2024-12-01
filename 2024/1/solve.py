from collections import defaultdict

file_path = '2024/1/input'

def readLists(file):
    first_list, second_list = [], []
    for line in file:
        data = line.split()
        first_list.append(int(data[0]))
        second_list.append(int(data[1]))
    return first_list, second_list

def part1(first_list, second_list):
    sum =  0
    first_list.sort()
    second_list.sort()
    for index in range(len(first_list)):
        sum += abs(first_list[index] - second_list[index])
    print(f'Part 1: {sum}\n', end='')

def part2(first_list, second_list):
    sum = 0
    numberDict = defaultdict(int)
    for number in second_list:
        numberDict[number] += 1
    for number in first_list:
        sum += number * numberDict.get(number, 0)
    print(f'Part 2: {sum}\n', end='')

with open(file_path, 'r') as file:
    first_list, second_list = readLists(file)
    part1(first_list, second_list)
    part2(first_list, second_list)