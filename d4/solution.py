with open('input.txt') as f:
    lines = f.readlines()

def part1():
    runningTotal = 0
    for line in lines:
        elf1, elf2 = createElves(line)
        if checkContains(elf1, elf2) or checkContains(elf2, elf1):
            runningTotal += 1
    return runningTotal
        
def checkContains(first, second):
    if first["min"] > second["min"]:
        return False
    if first["max"] < second["max"]:
        return False
    return True

def createElves(line):
    elf1String, elf2String = line.split(",")
    elf1MinMax = elf1String.split('-')
    elf2MinMax = elf2String.split('-')
    elf1 = {
        "min": int(elf1MinMax[0]),
        "max": int(elf1MinMax[1])
    }
    elf2 = {
        "min": int(elf2MinMax[0]),
        "max": int(elf2MinMax[1])
    }
    return elf1, elf2

def part2():
    runningTotal = 0
    for line in lines:
        elf1, elf2 = createElves(line)
        if checkOverlaps(elf1, elf2):
            runningTotal += 1
    return runningTotal

def checkOverlaps(first, second):
    if first["min"] > second["max"]:
        return False
    if second["min"] > first["max"]:
        return False
    return True

print(part2())