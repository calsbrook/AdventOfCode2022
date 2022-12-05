with open('input.txt') as f:
    lines = f.readlines()

stacks = [[],[],[],[],[],[],[],[],[]]

def part1():
    lineCounter = 0
    for line in lines:
        if lineCounter < 8:
            for i in range(0, 9):
                if line[i*4 + 1] is not " ":
                    stacks[i].append(line[i*4+1])
            lineCounter += 1
        elif lineCounter < 10:
            lineCounter += 1
        else:
            instruction = line.strip().split(" ")
            executeMove(int(instruction[1]), int(instruction[3]), int(instruction[5]))
    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)

def executeMove(quantity, moveFrom, moveTo):
    for i in range(0, quantity):
        stacks[moveTo - 1].insert(0, stacks[moveFrom - 1].pop(0))

def executeManyMove(quantity, moveFrom, moveTo):
    tempList = []
    for i in range(0, quantity):
        tempList.append(stacks[moveFrom - 1].pop(0))
    stacks[moveTo - 1] = tempList + stacks[moveTo - 1]

def part2():
    lineCounter = 0
    for line in lines:
        if lineCounter < 8:
            for i in range(0, 9):
                if line[i*4 + 1] is not " ":
                    stacks[i].append(line[i*4+1])
            lineCounter += 1
        elif lineCounter < 10:
            lineCounter += 1
        else:
            instruction = line.strip().split(" ")
            executeManyMove(int(instruction[1]), int(instruction[3]), int(instruction[5]))
    result = ""
    for stack in stacks:
        result += stack[0]
    print(result)
part1()
stacks = [[],[],[],[],[],[],[],[],[]]
part2()