#part 1
from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./input.txt")
file = open(file_path, 'r').read().splitlines()

finalScore = 0

for line in file:
    if len(line) < 3:
        continue
    
    enemy = line[0]
    outCome = line[2]

    #they drew ROCK
    if enemy == 'A':
        #LOSE
        if outCome == 'X':
            score = 3 + 0
        #DRAW
        if outCome == 'Y':
            score = 1 + 3
        #WIN
        if outCome == 'Z':
            score = 2 + 6
    #paper
    elif enemy == 'B':
        #LOSE
        if outCome == 'X':
            score = 1 + 0
        #DRAW
        if outCome == 'Y':
            score = 2 + 3
        #WIN
        if outCome == 'Z':
            score = 3 + 6
    #scissors
    elif enemy == 'C':
        #LOSE
        if outCome == 'X':
            score = 2 + 0
        #DRAW
        if outCome == 'Y':
            score = 3 + 3
        #WIN
        if outCome == 'Z':
            score = 1 + 6
    else:
        score = 0

    finalScore = finalScore + score

print(finalScore)

