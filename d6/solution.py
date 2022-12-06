with open('input.txt') as f:
    lines = f.readlines()

def part1():
    line = lines[0]
    for i in range(0, len(line)-3):
        setLine = set(line[i:i+4])
        if len(setLine) == 4:
            return i + 4
def part2():
    line = lines[0]
    for i in range(0, len(line)-13):
        setLine = set(line[i:i+14])
        if len(setLine) == 14:
            return i + 14

print(part1())
print(part2())