file_path = '2023/6/input'

def getRecordBeaten(data):
    time = int(data[0].split(':')[1].replace(' ', ''))
    record = int(data[1].split(':')[1].replace(' ', ''))
    count = 0
    for i in range(0, time + 1):
            if i * (time - i) > record:
                count += 1
    return count

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getRecordBeaten(data))