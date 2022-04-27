#Count and print letter frequency in a given word

from sys import *

def tests():
    assert parseword("mississippi") == {"m": 1, "i": 4, "s": 4, "p": 2}
    print(f"Tests passed.")

def printletters(letters):
    for k, v in letters.items():
        print(f"{k}: {v}")

def parseword(inputword):
    letters = {}
    for ch in inputword:
        if ch == " ":
            continue
        elif letters.get(ch) != None:
            letters[ch] += 1
        else:
            letters[ch] = 1
    return letters


def main():
    my_word = input("Please enter a word: ")
    my_word = my_word.lower()
    my_word = list(my_word)
    my_word.sort()
    wordparse = parseword(my_word)
    printletters(wordparse)

if __name__ == "__main__":
    if (len(argv) == 2 and argv[1] == "test"):
        tests()
    else:
        main()
