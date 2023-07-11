#part 1
from os.path import dirname, join

def readFile():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")
    return open(file_path, 'r').read().splitlines()

def areOverLapping(firstSet, secondSet):
    firstSet_start, firstSet_end = map(int, firstSet.split('-'))
    secondSet_start, secondSet_end = map(int, secondSet.split('-'))

    checkStart =  secondSet_start >= firstSet_start and secondSet_start <= firstSet_end
    checkEnd =  secondSet_end >= firstSet_start and secondSet_end <= firstSet_end
    
    return checkStart or checkEnd

def main(): 
    file = readFile()
    
    totalOverLaps = 0
    for line in file: 
        firstSet, secondSet = line.split(",")

        if areOverLapping(firstSet, secondSet) or areOverLapping(secondSet, firstSet):
            totalOverLaps = totalOverLaps + 1

    return totalOverLaps

print(main())
