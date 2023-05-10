#part 2
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

def commonItem(line1, line2, line3):
    for match in line1:
        if match in line2 and match in line3:
            return match

def main(): 
    file = readFile()
    finalScore = 0

    counter = 0
    for line in file:
        counter = counter + 1

        if counter == 1:
            line1 = line
        if counter == 2:
            line2 = line
        if counter == 3:
            line3 = line
            item = commonItem(line1, line2, line3)
            finalScore = finalScore + score(item)
            counter = 0

    print(finalScore)


main()