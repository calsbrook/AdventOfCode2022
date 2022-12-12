with open('input.txt') as f:
    lines = f.readlines()

def get_heightmap():
    heightmap = []
    for line in lines:
        heightmap.append([*line.strip()])
    return heightmap
heightmap = get_heightmap()

def find_start_end():
    start = []
    end = []
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[i])):
            if heightmap[i][j] == "S":
                start = [i, j]
            if heightmap[i][j] == "E":
                end = [i, j]
    return start, end

def is_valid(pos, move):
    if pos[0] != move[0] and pos[1] != move[1]:
        return False
    if abs(pos[0] - move[0]) > 1:
        return False
    if abs(pos[1] - move[1]) > 1:
        return False
    if move[0] < 0 or move[0] > len(heightmap)-1:
        return False
    if move[1] < 0 or move[1] > len(heightmap[0])-1:
        return False
    if heightmap[pos[0]][pos[1]] == "S":
        letter = "`"
    else:
        letter = heightmap[pos[0]][pos[1]]
    if heightmap[move[0]][move[1]] == "E":
        other_letter = "{"
    else:
        other_letter = heightmap[move[0]][move[1]]
    if ord(letter) - ord(other_letter) < -1:
        return False
    return True

def find_moves(pos):
    possible_moves = [
        [pos[0]-1, pos[1]],
        [pos[0]+1, pos[1]],
        [pos[0], pos[1]-1],
        [pos[0], pos[1]+1]
    ]
    moves = []
    for move in possible_moves:
        if is_valid(pos, move):
            moves.append(move)
    return moves

def bfs(start, end):
    queue = [[start]]
    seen = set([tuple(start)])
    while queue:
        path = queue.pop(0)
        pos = path[-1]
        if pos == end:
            return path
        moves = find_moves(pos)
        for move in moves:
            move_tup = tuple(move)
            if move_tup not in seen:
                new_path = path.copy()
                new_path.append(move)
                queue.append(new_path)
                seen.add(move_tup)
def find_all_a():
    locations = []
    for i in range(0, len(heightmap)):
        for j in range(0, len(heightmap[i])):
            if heightmap[i][j] == "a":
                locations.append([i, j])
    return locations

def part1():
    start, end = find_start_end()
    return len(bfs(start, end)) - 1

def part2():
    _, end = find_start_end()
    locations = find_all_a()
    distances = []
    for location in locations:
        path = bfs(location, end)
        if path is not None:
            distances.append(len(path)-1)
    # print(distances)
    return min(distances)

print(part1())
print(part2())
