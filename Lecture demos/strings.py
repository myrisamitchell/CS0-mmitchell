# def main():
#     s = "Pirates of the Carribean"
#     # split_string = s.split()
#     for i in range (len(s)):
#         print(s[i])

# main()



def main():
    str_string = "The next Tuesday is tomorrow"
    #prints out whole string
    #To print in reverse: [ : :-1]
    print(str_string[ : :])

    #String conditionals
    #print("Tuesday" in str_string)
    #Checks if the string is in the original string and returns True


main()

import string

def main2():
    str_string = "The next Tuesday is tomorrow"
    lower_string = ""
    for ch in str_string:
        if ch in string.ascii_uppercase:
            ch = ch.lower()
        elif ch in string.whitespace:
            ch = "-"
        lower_string += ch
    print(lower_string)

main2()