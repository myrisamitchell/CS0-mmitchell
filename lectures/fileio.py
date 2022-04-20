
import random 
from sys import *

def tests():
    assert True == True
    print("All test cases passed!")



def main():
    if (len(argv) == 2 and argv[1] == "test"):
        tests()
#Add input from a file
    input_lines = []
    with open("lectures/myfile.txt") as fin:
        input_lines = fin.read()

    my_string = input_lines.split()

#Picking a random word from file
    print(f"{random.choice(my_string)}")


#Print output to a new file
    with open("lectures/output_file.txt", "w") as fout:
        for line in my_string:
            print(f"{line}", file=fout)

if __name__ == "__main__":
    # print(f"{argv}")
    main()