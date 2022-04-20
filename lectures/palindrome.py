'''
Determines if an inputted string is a palindrome.
'''

from datetime import MAXYEAR
from pickle import TRUE


def input_name():
    firstname = input("Please enter your first name: ")
    return firstname

def greet_player(first_name):
    print(f"{first_name}, welcome to our program.")
    print(f"This will determine if a string is a palindrome.")

def input_string():
    inputted_string = input("Please enter a string to check if it is a palindrome: ")
    return inputted_string

def is_palindrome(in_string):
    # supercalifragilisticexpialidocious
    # for ch in in_string:
    #     if (ch == in_string[-1]):
    #         print("Still may be a palindrome.")
    in_string = in_string.lower()
    back_string = in_string[::-1]
    if (in_string == back_string):
        return True 
    else:
        return False
    # print(f"in_string = {in_string[::-1]}")
'''
    for ch in range(len(in_string)//2):
        # print(f"in_string[ch] = {in_string[ch]}")
        # print(f"in_string[-ch] = {in_string[-ch-1]}")
        # print(f"ch = {in_string[ch]}")
        if (in_string[ch] != in_string[-ch-1]):
            # print(f"in_string[ch] = {in_string[ch]}")
            # print(f"in_string[-ch] = {in_string[-ch]}")
            print(f"This is not a palindrome.")
            break
    else: 
        print(f"Your string is a palindrome.")
'''
def tests():
    assert is_palindrome("racecar") == True
    assert is_palindrome("superman") == False
    print("All test cases passed!")

def main():
    tests()
    first_name = input_name()
    greet_player(first_name)

    in_string = input_string()
    is_pali = is_palindrome(in_string)
    if (is_pali):
        print(f"Your string '{in_string}' is a palindrome.")
    else:
        print(f"Your string '{in_string}' is not a palindrome. ")


if __name__ == "__main__":
    main()