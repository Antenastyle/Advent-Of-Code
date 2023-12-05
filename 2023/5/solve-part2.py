file_path = '2023/5/input'

def getLowestLocation(data):
    initial_seeds = data[0].split(':')[1].split()
    lowest = 5678493126517895346891234
    for i in range(0, len(initial_seeds), 2):
        for seed in range(int(initial_seeds[i]), int(initial_seeds[i]) + int(initial_seeds[i + 1])):
            for index in range(1, 8):
                seed = getSourceToDestination(seed, data, index)
            if seed < lowest: lowest = seed
    return lowest

def getSourceToDestination(source, data, index):
    map = data[index].split('\n')
    map.pop(0)
    for line in map:
        destStart, sourceStart, i = line.split()
        if int(sourceStart) <= source <= (int(sourceStart) + (int(i) - 1)):
            dest = int(destStart) + (source - int(sourceStart))
            return dest
    return int(source)

with open(file_path, 'r') as file:
    data = [line for line in file.read().split('\n\n') if line]
    print(getLowestLocation(data))