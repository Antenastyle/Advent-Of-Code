file_path = '2023/2/input'

def isPossibleGame(line):
    max_blue = 0
    max_green = 0
    max_red = 0
    data = line[line.find(':') + 1:].strip().split('; ')
    for block in data:
        blocks = block.split(', ')
        for cubes in blocks:
            digit,word = cubes.split(' ')
            if word == 'blue': max_blue = max(max_blue, int(digit))
            elif word == 'red': max_red = max(max_red, int(digit))
            else: max_green = max(max_green, int(digit))
    return max_blue * max_green * max_red

with open(file_path, 'r') as file:
    sum = 0
    for line in file:
        sum += isPossibleGame(line)
    print(sum)