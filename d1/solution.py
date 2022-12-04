with open('input.txt') as f:
    lines = f.readlines()
elves = []
runningTotal = 0
for line in lines:
    if len(line) > 1:
        runningTotal += int(line)
    else:
        elves.append(runningTotal)
        runningTotal = 0
elves.append(runningTotal)
print(max(elves))
elves.sort(reverse=True)
print(elves[0]+elves[1]+elves[2])