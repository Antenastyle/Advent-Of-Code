file_path = '2023/6/input'

def getRecordBeaten(data):
    times = data[0].split(':')[1].split()
    records = data[1].split(':')[1].split()
    index, totalSum = 0, 0
    for time in times:
        count = 0
        for i in range(0, int(time) + 1):
            if i * (int(time) - i) > int(records[index]):
                count += 1
        if totalSum == 0: totalSum = count
        else : totalSum *= count
        index += 1
    return totalSum

with open(file_path, 'r') as file:
    data = [line for line in file.read().splitlines() if line]
    print(getRecordBeaten(data))