#part 2
from os.path import dirname, join

def readFile():
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./input.txt")
    return open(file_path, 'r').read().splitlines()


def main(): 
    file = readFile()
    
    for line in file: 
        print(line)

main()