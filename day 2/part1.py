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
    me = line[2]

    if me == 'X':
        score = 1
        if enemy == 'A':
            score = score + 3
        if enemy == 'B':
            score = score + 0
        if enemy == 'C':
            score = score + 6
    #paper
    elif me == 'Y':
        score = 2
        if enemy == 'A':
            score = score + 6
        if enemy == 'B':
            score = score + 3
        if enemy == 'C':
            score = score + 0
    #scissors
    elif me == 'Z':
        score = 3
        if enemy == 'A':
            score = score + 0
        if enemy == 'B':
            score = score + 6
        if enemy == 'C':
            score = score + 3
    else:
        score = 0

    finalScore = finalScore + score

print(finalScore)

