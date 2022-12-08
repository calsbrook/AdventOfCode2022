import inspect
with open('input.txt') as f:
    lines = f.readlines()

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contains = []
        self.size = 0
    
    def update_size(self):
        runningSize = 0
        if len(self.contains) > 0:
            for file in self.contains:
                if isinstance(file, Directory):
                    file.update_size()
                runningSize += file.size
        self.size = runningSize
    
    def add_parent(self, parent):
        self.parent = parent

    def add_file(self, file):
        self.contains.append(file)
        self.update_size()
    
    def get_size(self):
        self.update_size()
        return self.size

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

def find_dir(name, filesystem):
    for file in filesystem:
        if file.name == name:
            return file
    return None

def construct_filesystem():
    filesystem = []
    root = Directory("/", None)
    filesystem.append(root)
    current_dir = root
    ls_command = False
    for line in lines:
        command = line.strip().split(" ")
        if ls_command and line[0] != "$":
            if command[0] == "dir":
                newguy = Directory(command[1], current_dir)
                filesystem.append(newguy)
                current_dir.add_file(newguy)
            else:
                current_dir.add_file(File(command[1], int(command[0])))
            pass
        if command[0] == "$":
            ls_command = False
            if command[1] == "cd":
                if command[2] == "..":
                    current_dir = current_dir.parent
                elif command[2] == "/":
                    pass
                else:
                    current_dir = find_dir(command[2], current_dir.contains)
            elif command[1] == "ls":
                ls_command = True
    root.update_size()
    return filesystem
def part1():
    filesystem = construct_filesystem()
    runningTotal = 0
    for file in filesystem:
        if file.size <= 100000:
            runningTotal += file.size
    return runningTotal

def part2():
    filesystem = construct_filesystem()
    freeSpace = 70000000 - filesystem[0].size
    sizes = []
    for file in filesystem:
        sizes.append(file.size)
    sizes.sort()
    needed_space = 30000000 - freeSpace
    for size in sizes:
        if size >= needed_space:
            return size

print(part1())
print(part2())