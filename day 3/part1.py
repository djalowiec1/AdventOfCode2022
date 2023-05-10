#part 1
from os.path import dirname, join
from string import ascii_letters

def readFile():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")
    return open(file_path, 'r').read().splitlines()

def score(input):
    score = 1
    for letter in ascii_letters:
        if letter == input:
            return score 
        score = score + 1

def commonItem(line):
    firstHalf = line[:len(line)//2]
    secondHalf = line[len(line)//2:]

    for match in firstHalf:
        if match in secondHalf:
            return match

def main(): 
    file = readFile()
    finalScore = 0
    
    for line in file:    
        item = commonItem(line)
        finalScore = finalScore + score(item)

    print(finalScore)


main()