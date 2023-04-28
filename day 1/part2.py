# part 2
from os.path import dirname, join
from array import *

current_dir = dirname(__file__)
file_path = join(current_dir, "./input.txt")
file = open(file_path, 'r').read().splitlines()

myArray = []
finalMax = 0
currentMax = 0

for line in file:
    if (line == '') :
     myArray.append(currentMax)
     currentMax = 0
     continue

    currentMax = currentMax + int(line)

myArray.sort(reverse=True)

print(myArray[0] +  myArray[1] +myArray[2])
