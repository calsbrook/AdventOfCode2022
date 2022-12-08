with open('input.txt') as f:
    lines = f.readlines()

def make_array():
    trees = []
    for line in lines:
        line = [*line.strip()]
        res = [eval(i) for i in line]
        trees.append(res)
    return trees

def check_direction(i, j, trees, direction):
    current_tree = trees[i][j]
    if direction == "left":
        for x in range(0, j):
            if trees[i][x] >= current_tree:
                return False
        return True
    elif direction == "right":
        for x in range(j+1, len(trees[i])):
            if trees[i][x] >= current_tree:
                return False
        return True
    elif direction == "up":
        for x in range(0, i):
            if trees[x][j] >= current_tree:
                return False
        return True
    elif direction == "down":
        for x in range(i+1, len(trees)):
            if trees[x][j] >= current_tree:
                return False
        return True

def check_visible(i, j, trees):
    global border_trees
    global interior_trees
    if i == 0 or j == 0 or i == len(trees)-1 or j == len(trees[i]) -1:
        return 1
    if check_direction(i, j, trees, "right") or check_direction(i, j, trees, "left") or check_direction(i,j,trees, "down") or check_direction(i, j, trees, "up"):
        return 1
    return 0

def calculate_scenic(i, j, trees):
    current_height = trees[i][j]
    left = right = up = down = 0
    leftCheck = rightCheck = upCheck = downCheck = True
    # left
    if i > 0:
        for x in range(1, i+1):
            if trees[i-x][j] < current_height and leftCheck:
                left += 1
            else:
                if leftCheck: left += 1
                leftCheck = False
    else:
        return 0
    # right
    if i < len(trees)-1:
        for x in range(1, len(trees) - i):
            if trees[i+x][j] < current_height and rightCheck:
                right += 1
            else:
                if rightCheck: right += 1
                rightCheck = False
    else:
        return 0
    # up
    if j > 0:
        for x in range(1,j+1):
            if trees[i][j-x] < current_height and upCheck:
                up += 1
            else:
                if upCheck: up += 1
                upCheck = False
    else:
        return 0
    # down
    if j < len(trees[i])-1:
        for x in range(1, len(trees[i])-j):
            if trees[i][j+x] < current_height and downCheck:
                down += 1
            else:
                if downCheck: down += 1
                downCheck = False
    else:
        return 0
    
    if right == 0:
        right = 1
    if left == 0:
        left = 1
    if up == 0:
        up = 1
    if down == 0:
        down = 1
    return left * right * up * down

def part1():
    trees = make_array()
    visible_trees = 0
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            visible_trees += check_visible(i, j, trees)
    return visible_trees

def part2():
    trees = make_array()
    best_scenic = 0
    for i in range(0, len(trees)):
        for j in range(0, len(trees[i])):
            scenic_score = calculate_scenic(i, j, trees)
            if best_scenic < scenic_score:
                best_scenic = scenic_score
    return best_scenic


print(part2())