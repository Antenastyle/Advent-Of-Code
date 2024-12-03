import re

file_path = '2024/3/input'

def part1(input):
    totalSum = sum([int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', input)])
    print(f'Part 1: {totalSum}\n', end='')

def part2(input):
    totalSum = 0
    segments = re.split(r"(do\(\)|don't\(\))", input)
    action = "do"
    for segment in segments:
        if segment == "do()":
            action = "do"
        elif segment == "don't()":
            action = "don't"
        elif action == "do":
            totalSum += sum([int(a) * int(b) for a, b in re.findall(r'mul\((\d+),(\d+)\)', segment)])
    print(f'Part 2: {totalSum}\n', end='')


with open(file_path, 'r') as file:
    input = "".join(file.readlines())
    part1(input)
    part2(input)