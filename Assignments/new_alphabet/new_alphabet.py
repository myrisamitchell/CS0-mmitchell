'''
Name: Myrisa Mitchell
Date: April 25, 2022

This program will convert letters of the alphabet to a "New alphabet".

Step 1: Create dictionary of new alphabet
Step 2: Take input of string and convert to new alphabet
Step 3: Print out string with new alphabet
Step 4: Create test function with 3 test cases
'''

from sys import *

#Step 4
def tests():
    assert convert_string("Nice to meet you!") == "[]\[]|(3 ']['0 []\/[]33'][' `/0|_|!"
    assert convert_string("This is fun.") == "']['[-]|$ |$ #|_|[]\[]."
    assert convert_string("Good job team!") == "600|) _|08 ']['3@[]\/[]!"

#Step 1
def create_dict():
    new_alphabet = {}
    new_alphabet["a"] = "@"
    new_alphabet["b"] = "8"
    new_alphabet["c"] = "("
    new_alphabet["d"] = "|)"
    new_alphabet["e"] = "3"
    new_alphabet["f"] = "#"
    new_alphabet["g"] = "6"
    new_alphabet["h"] = "[-]"
    new_alphabet["i"] = "|"
    new_alphabet["j"] = "_|"
    new_alphabet["k"] = "|<"
    new_alphabet["l"] = "1"
    new_alphabet["m"] = "[]\/[]"
    new_alphabet["n"] = "[]\[]"
    new_alphabet["o"] = "0"
    new_alphabet["p"] = "|D"
    new_alphabet["q"] = "(,)"
    new_alphabet["r"] = "|Z"
    new_alphabet["s"] = "$"
    new_alphabet["t"] = "']['"
    new_alphabet["u"] = "|_|"
    new_alphabet["v"] = "\/"
    new_alphabet["w"] = "\/\/"
    new_alphabet["x"] = "}{"
    new_alphabet["y"] = "`/"
    new_alphabet["z"] = 2
    return new_alphabet

#Step 2
def convert_string(old_alphabet):
    old_alphabet = old_alphabet.lower()
    new_string = ''
    new_alphabet = create_dict()
    for i in old_alphabet:
        if i not in (new_alphabet.keys()):
            new_string += i 
        else: 
            new_string += (new_alphabet.get(i))
    return new_string


def main():
    
    if (len(argv)) == 2 and argv[1] == "test":
        tests()

    old_alphabet = input()
    new_string = convert_string(old_alphabet)
    
    #Step 3
    print(new_string)

if __name__ == "__main__":
    main()