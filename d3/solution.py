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
                if item.islower():
                    runningTotal += (ord(item) - 96)
                elif item.isupper():
                    runningTotal += (ord(item) - 38)
                else:
                    print("HELP")
    print(runningTotal)

def findIntersect(set1, set2, set3):
    workingSet = set1.intersection(set2)
    # print(workingSet)
    finalSet = workingSet.intersection(set3)
    # print(finalSet)
    return list(finalSet)[0]

def part2():
    runningTotal = 0
    workingLines = []
    for line in lines:
        if len(workingLines) < 3:
            workingLines.append(line)
        else:
            lineSet1 = set()
            lineSet2 = set()
            lineSet3 = set()
            lineSets = [lineSet1, lineSet2, lineSet3]
            for x in range(0, 3):
                for letter in workingLines[x]:
                    if letter != '\n':
                        lineSets[x].add(letter)
            result = findIntersect(lineSet1, lineSet2, lineSet3)
            runningTotal += findValue(result)
            workingLines = []
    print(runningTotal)

part2()