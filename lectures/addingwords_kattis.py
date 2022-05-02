from sys import *

def tests():
    pass

def parse_input(input_lines):
    for line in input_lines:
        split_line = line.split()
        

def main():
    input_lines = []
    line = input()
    while (line != "clear"):
        input_lines.append(line)
        line = input()
    parse_input(input_lines)


if __name__ == "__main__":
    if (len(argv) == 2 and argv[1] == "test"):
        tests()
    else:
        main()