# part 1
from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./input.txt")
file = open(file_path, 'r').read().splitlines()

finalMax = 0
currentMax = 0

for line in file:
    if (line == '') :
     currentMax = 0
     continue

    currentMax = currentMax + int(line)

    if (currentMax > finalMax ):
        finalMax = currentMax

print(finalMax)
