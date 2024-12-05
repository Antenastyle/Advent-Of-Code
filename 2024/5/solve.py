file_path = '2024/5/input'

def parseInput(file):
    div = False
    rules, updates = [], []
    for line in file.read().splitlines():
        if line == '':
            div = True
            continue
        if not div:
            rules.append(line.split('|'))
        else:
            updates.append(line.split(','))
    return rules, updates

def isUpdateCorrect(update, rules):
    for index in range(len(update)):
        for rule in rules:
            if rule[0] == update[index]:
                if rule[1] in update[:index]:
                    return False
            if rule[1] == update[index]:
                if rule[0] in update[index:]:
                    return False
    return True

def orderUpdate(update, rules):
    new, clone = [], []
    for number in update:
        clone.append(number)

    dependencies = {num: [] for num in clone}
    for rule in rules:
        if rule[0] in clone and rule[1] in clone:
            dependencies[rule[1]].append(rule[0])

    while clone:
        for number in clone:
            if all(dep in new for dep in dependencies[number]):
                new.append(number)
                clone.remove(number)
                break
    return new        

def part1(rules, updates):
    totalSum = 0
    for update in updates:
        if isUpdateCorrect(update, rules):
            totalSum += int(update[len(update) - len(update)//2 - 1])
    print(f'Part 1: {totalSum}\n', end='')

def part2(rules, updates):
    totalSum = 0
    for update in updates:
        if not isUpdateCorrect(update, rules):
            orderedUpdate = orderUpdate(update, rules)
            totalSum += int(orderedUpdate[len(update) - len(update)//2 - 1])
    print(f'Part 2: {totalSum}\n', end='')

with open(file_path, 'r') as file:
    rules, updates = parseInput(file)
    part1(rules, updates)
    part2(rules, updates)