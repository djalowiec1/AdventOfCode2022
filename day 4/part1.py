#part 1
from os.path import dirname, join

def readFile():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")
    return open(file_path, 'r').read().splitlines()

def areContaining(firstSet, secondSet):
    firstSet_start, firstSet_end = map(int, firstSet.split('-'))
    secondSet_start, secondSet_end = map(int, secondSet.split('-'))

    # checking if second set is inside first set 
    return secondSet_start >= firstSet_start and secondSet_end <= firstSet_end

def main(): 
    file = readFile()
    
    totalAssignments = 0
    for line in file: 
        firstSet, secondSet = line.split(",")

        if areContaining(firstSet, secondSet) or areContaining(secondSet, firstSet):
            totalAssignments = totalAssignments + 1

    return totalAssignments

print(main())
