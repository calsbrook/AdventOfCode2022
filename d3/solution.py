with open('input.txt') as f:
    lines = f.readlines()

def findValue(letter):
    if letter.islower():
        return (ord(letter) - 96)
    elif letter.isupper():
        return (ord(letter) - 38)

def part1():
    runningTotal = 0
    for line in lines:
        firstHalf = set()
        secondHalf = set()
        for x in range(0, len(line)//2):
            firstHalf.add(line[x])
        for x in range((len(line)//2), len(line)):
            secondHalf.add(line[x])
        for item in firstHalf:
            if item in secondHalf:
                runningTotal += findValue(item)
    print(runningTotal)

def findIntersect(sets):
    workingSet = sets[0].intersection(sets[1])
    finalSet = workingSet.intersection(sets[2])
    return list(finalSet)[0]

def part2():
    runningTotal = 0
    workingLines = []
    for line in lines:
        workingLines.append(set(line.strip()))
        if len(workingLines) == 3:
            result = findIntersect(workingLines)
            runningTotal += findValue(result)
            workingLines = []
    print(runningTotal)

part2()