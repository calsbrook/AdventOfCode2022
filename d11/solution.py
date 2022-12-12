with open('input.txt') as f:
    lines = f.read().split("\n\n")

class Monkey:
    def __init__(self, name, starting_items, operation, test ):
        self.name = name
        self.items = []
        for item in starting_items:
            self.items.append(int(item.strip(",")))
        self.operation = self.construct_operation(operation)
        self.test = self.construct_test(test)
        self.inspections = 0
    
    def inspect(self):
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item = item // 3
            self.give_item(item, all_monkeys[self.test(item)])

    def inspect_2(self):
        while self.items:
            self.inspections += 1
            item = self.items.pop(0)
            item = self.operation(item)
            self.give_item(item % monkey_product, all_monkeys[self.test(item)])

    def construct_operation(self, operation):
        if operation[4] == "old":
            return lambda x : x * x
        if operation[3] == "*":
            return lambda x : x * int(operation[4])
        if operation[3] == "+":
            return lambda x : x + int(operation[4])
        if operation[3] == "-":
            return lambda x : x - int(operation[4])
        if operation[3] == "/":
            return lambda x : x / int(operation[4])

    def construct_test(self, test):
        return lambda x : test[1] if (x % int(test[0]) == 0) else test[2]
    
    def get_item(self, item):
        self.items.append(item)
    
    def give_item(self, item, monkey):
        monkey.get_item(item)

def create_commands(subject):
    commands = subject.split("\n")
    for i in range(0,len(commands)):
        commands[i] = commands[i].split(" ")
    return commands

def create_monkeys():
    for subject in lines:
        commands = create_commands(subject)
        name = commands[0][1].strip(":")
        starting_items = commands[1][4:]
        operation = commands[2][3:]
        test = [int(commands[3][5]), int(commands[4][-1]), int(commands[5][-1])]
        all_monkeys.append(Monkey(name, starting_items, operation, test))
    

all_monkeys = []
def part1():
    create_monkeys()
    for _ in range(0,20):
        for monkey in all_monkeys:
            monkey.inspect()
    inspections = list(map(lambda monkey: monkey.inspections, all_monkeys))
    inspections.sort(reverse=True)
    print(inspections)
    return inspections[0] * inspections[1]
all_monkeys = []
monkey_product = 1
for subject in lines:
    commands = create_commands(subject)
    monkey_product *= int(commands[3][5])
def part2():
    create_monkeys()

    for _ in range(0, 10000):
        if _ % 1000 == 0:
            print(100*(_/10000))
        for monkey in all_monkeys:
            monkey.inspect_2()
    # for monkey in all_monkeys:
    #     print(monkey.items)
    inspections = list(map(lambda monkey: monkey.inspections, all_monkeys))
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

print(part2())