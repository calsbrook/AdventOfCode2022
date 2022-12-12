with open('input.txt') as f:
    lines = f.readlines()

def create_commands(input):
    output = []
    for line in input:
        command = line.strip().split(" ")
        if len(command) == 2:
            command[1] = int(command[1])
        output.append(command)
    return output

def part1():
    checked_cycles = [20, 60, 100, 140, 180, 220]
    x_values = []
    cycle = 1
    register = 1
    commands = create_commands(lines)
    for command in commands:
        if cycle in checked_cycles:
            x_values.append(register)
        if command[0] == "addx":
            cycle += 1
            if cycle in checked_cycles:
                x_values.append(register)
            register += command[1]
        cycle += 1
    multiplied_values = []
    for i in range(0, len(x_values)):
        multiplied_values.append(x_values[i] * checked_cycles[i])
    return sum(multiplied_values)

def part2():
    screen = []
    working_line = []
    cycle = 1
    register = 1
    commands = create_commands(lines)
    for command in commands:
        if len(working_line) == 40:
            screen.append(working_line.copy())
            working_line = []
        if command[0] == "addx":
            working_line.append(pixel(register, cycle))
            cycle += 1
            if len(working_line) == 40:
                screen.append(working_line.copy())
                working_line = []
            register += command[1]
        working_line.append(pixel(register, cycle))
        cycle += 1
    screen.append(working_line.copy())
    for line in screen:
        print("".join(line))

def pixel(register, cycle):
    pos = cycle % 40
    if register == pos or register + 1 == pos or register - 1 == pos:
        return "#"
    return "."
# print(part1())
part2()

