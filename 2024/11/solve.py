import functools

file_path = '2024/11/input'

@functools.cache
def blink(stone, actual, iterations):
    if actual == iterations:
        return 1
    if stone == 0:
        return blink(1, actual + 1, iterations)
    stoneValue = str(stone)
    size = len(stoneValue)
    if size % 2 == 0:
        return (blink(int(stoneValue[:size // 2]), actual + 1, iterations) + blink(int(stoneValue[size // 2:]), actual + 1, iterations))
    return blink(stone * 2024, actual + 1, iterations)

def part1(stones):
    totalSum = sum(blink(int(stone), 0, 25) for stone in stones)
    print(f'Part 1: {totalSum}\n', end='')

def part2(stones):
    totalSum = sum(blink(int(stone), 0, 75) for stone in stones)
    print(f'Part 2: {totalSum}\n', end='')

with open(file_path, 'r') as file:
    stones = file.read().split()
    part1(stones)
    part2(stones)