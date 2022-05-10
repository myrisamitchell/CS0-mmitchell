from sys import *

def tests():
    pass

def parse_input(input_lines):
    str_to_int = {}
    int_to_str = {}
    for line in input_lines:
        if (line[0] == "clear"):
            str_to_int.clear()
            int_to_str.clear()
            continue
        split_line = line.split()
        if (split_line[0] == "def"):
            str_to_int[split_line[1]] = int(split_line[2])
            int_to_str[int(split_line[2])] = split_line[1]
        else:
            if (str_to_int.get(split_line[1]) != None):
                total = str_to_int[split_line[1]]
                valid = True
            total = 0
            valid = False
            for i in range(2, len(split_line)-1):
                if (split_line[i] == "+"):
                    if str_to_int.get(split_line[i+1] != None):
                        total += str_to_int[split_line[i+1]]
                    else:
                        valid = False
                elif (split_line[i] == "-"):
                    if str_to_int.get(split_line[i+1] != None):
                        total -= str_to_int[split_line[i+1]]
                    else:
                        valid = False
            for i in range(1, len(split_line)):
                    print(f"{split_line[i]}", end = ' ')
            if (valid):
                if (int_to_str.get(total) != None):
                    print(f"{int_to_str[total]}")
                else:
                    print("unknown")
            else:
                print("unknown")

def main():
    input_lines = []
    line = input()
    while (line != ""):
        input_lines.append(line)
        line = input()
    parse_input(input_lines[:-1])


if __name__ == "__main__":
    if (len(argv) == 2 and argv[1] == "test"):
        tests()
    else:
        main()