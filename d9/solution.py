with open('input.txt') as f:
    lines = f.readlines()
def check_adjacent(head, tail):
    difference = [abs(head[0]-tail[0]), abs(head[1]-tail[1])]
    if difference[0] > 1:
        return False
    if difference[1] > 1:
        return False
    return True

def part1():
    head = [0,0]
    tail = [0,0]
    tail_visits = [[0,0]]
    for line in lines:
        command = line.strip().split(" ")
        command[1] = int(command[1])
        transform = []
        if command[0] == "U":
            transform = [0, 1]
        elif command[0] == "D":
            transform = [0, -1]
        elif command[0] == "L":
            transform = [-1, 0]
        elif command[0] == "R":
            transform = [1,0]
        else:
            print("OH NO")

        for i in range(0, command[1]):
            previous_pos = head.copy()
            head[0] += transform[0]
            head[1] += transform[1]
            if not check_adjacent(head, tail):
                tail = previous_pos.copy()
                copy_tail = True
                for pos in tail_visits:
                    if pos[0] == tail[0] and pos[1] == tail[1]:
                        copy_tail = False
                if copy_tail:
                    tail_visits.append(tail.copy())
    return len(tail_visits)

def move_parts(leader, follower):
    difference = [abs(leader[0]-follower[0]), abs(leader[1] - follower[1])]
    move = [0,0]
    if difference[0] == 2 and difference[1] == 2:
        if leader[0] > follower[0]:
            move[0] = 1
        else:
            move[0] = -1
        if leader[1] > follower[1]:
            move[1] = 1
        else:
            move[1] = - 1
    elif difference[0] == 2:
        if leader[0] > follower[0]:
            move[0] = 1
        else:
            move[0] = -1
        move[1] = leader[1] - follower[1]
    elif difference[1] == 2:
        if leader[1] > follower[1]:
            move[1] = 1
        else:
            move[1] = - 1
        move[0] = leader[0] - follower[0]
    else:
        move[0] = leader[0] - follower[0]
        move[1] = leader[1] - follower[1]
    return move

def part2():
    rope = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    tail_visits = set()
    tail_visits.add((0,0))
    for line in lines:
        command = line.strip().split(" ")
        command[1] = int(command[1])
        transform = []
        if command[0] == "U":
            transform = [0, 1]
        elif command[0] == "D":
            transform = [0, -1]
        elif command[0] == "L":
            transform = [-1, 0]
        elif command[0] == "R":
            transform = [1,0]
        else:
            print("OH NO")
        for i in range(0, command[1]):
            rope[0][0] += transform[0]
            rope[0][1] += transform[1]
            for j in range(1, len(rope)):
                if not check_adjacent(rope[j-1], rope[j]):
                    movement = move_parts(rope[j-1], rope[j])
                    rope[j][0] += movement[0]
                    rope[j][1] += movement[1]
            tail_visits.add(tuple(rope[9]))
    print(rope)
    print(tail_visits)
    
    return(len(tail_visits))


# print(part1())
print(part2())