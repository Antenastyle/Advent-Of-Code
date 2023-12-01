file_path = '2023/1/input-part1'

def getCalibrationValue(line):
    first_digit = next((int(char) for char in line if char.isdigit()), None)
    last_digit = next((int(char) for char in reversed(line) if char.isdigit()), None)
    return int(str(first_digit) + str(last_digit))

with open(file_path, 'r') as file:
    sum = 0
    for line in file:
        sum += getCalibrationValue(line)
    print(sum, end='')