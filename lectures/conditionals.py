'''
Name: Myrisa Mitchell
Date: 2/25/2022
'''

"""def main():
    num = int(input(f"Please enter a whole number: "))
    

    if (num == 0):
        print(f"{num} is zero.")
    elif (num > 0) and (num % 2 == 0):
        print(f"{num} is even.")
        print(f"{num} is positive.")
    elif (num > 0) and (num % 2 ==1):
        print(f"{num} is odd.")
        print(f"{num} is positive.")
    elif (num % 2 == 0):
        print(f"{num} is even.")
        print(f"{num} is negative.")
    else:
        print(f"{num} is odd.")
        print(f"{num} is negative.")

main()"""

"""def main():
    money = int(input(f"How much money do you have in the bank? "))
    ferrari = input(f"Do you have a ferrari [y/yes | n/no]? ")

    if (money >= 1000000 and (ferrari == "y" or ferrari == "yes")):
        print("Congrats! You can retire.")
    else:
        print("Sorry, back to work.")

main()"""

def main():
    num = int(input("Please enter a whole number: "))
    # not inverts the condition/ F -> T & T -> F
    if not (num %2 == 0):
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

main()