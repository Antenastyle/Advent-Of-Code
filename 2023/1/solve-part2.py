file_path = '2023/1/input-part2'

def getCalibrationValue(line):
    line = (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    first_digit = next((int(char) for char in line if char.isdigit()), None)
    last_digit = next((int(char) for char in reversed(line) if char.isdigit()), None)
    return int(str(first_digit) + str(last_digit))

with open(file_path, 'r') as file:
    sum = 0
    for line in file:
        sum += getCalibrationValue(line)
    print(sum, end='')