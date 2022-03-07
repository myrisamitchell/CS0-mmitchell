def main():
    n = 0
    while (n < 10):
        n = int(input("Please enter a number between 2 and 7: "))
        if (n < 2 or n > 7):
            print(f"You entered {n} and that is not between 2 and 7. Try again. ")
        

main()