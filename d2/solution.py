with open('input.txt') as f:
    lines = f.readlines()

values = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "Draw": 3,
    "Win": 6
}

moveSelection = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    },
}
def part1():
    p1Score = 0
    p2Score = 0

    for line in lines:
        p1Move = line[0]
        p2Move = line[2]
        p1Score += values[p1Move]
        p2Score += values[p2Move]
        if p1Move == "A":
            if p2Move == "X":
                p1Score += values["Draw"]
                p2Score += values["Draw"]
            elif p2Move == "Y":
                p2Score += values["Win"]
            elif p2Move == "Z":
                p1Score += values["Win"]
        elif p1Move == "B":
            if p2Move == "Y":
                p1Score += values["Draw"]
                p2Score += values["Draw"]
            elif p2Move == "Z":
                p2Score += values["Win"]
            elif p2Move == "X":
                p1Score += values["Win"]
        elif p1Move == "C":
            if p2Move == "Z":
                p1Score += values["Draw"]
                p2Score += values["Draw"]
            elif p2Move == "X":
                p2Score += values["Win"]
            elif p2Move == "Y":
                p1Score += values["Win"]

    print(p1Score)
    print(p2Score)

def part2():
    p1Score = 0
    p2Score = 0

    for line in lines:
        p1Move = line[0]
        outcome = line[2]

        if outcome == "X":
            p1Score += values["Win"]
        elif outcome == "Y":
            p1Score += values["Draw"]
            p2Score += values["Draw"]
        elif outcome == "Z":
            p2Score += values["Win"]
        
        p1Score += values[p1Move]
        p2Score += values[moveSelection[p1Move][outcome]]
    print(p1Score)
    print(p2Score)

part2()