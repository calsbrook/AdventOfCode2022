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
        firstHalf = set(line[:len(line)//2])
        secondHalf = set(line[len(line)//2:])
        intersectingSet = firstHalf.intersection(secondHalf)
        runningTotal += findValue(list(intersectingSet)[0])
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

part1()