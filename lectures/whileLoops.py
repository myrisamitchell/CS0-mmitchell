'''def main():
    n = int(input("Please enter a number: "))
    while (n < -7 or n > 7):
        if (n < -7 or n > 7):
            print(f"You entered {n} and that is not between -7 and 7. Try again. ")
            n = int(input("Please enter another number: "))
    else:
        print(f"You entered {n} which is between 2 and 7!")    

main()'''

#Determine 5's in a number
'''def main():
    n = 8745655058735
    orig_n = n
    num_digits = 0

    five_counter = 0
    for i in n:
        if i == 5:
            five_counter += 1
    else:
        print(f"There are {five_counter} fives in {n}.")'''

    #Determine numbers in integer
'''    for i in n:
        print(f"i: {i}")'''
    #Determine number of digits in string
'''    while (n > 0):
        n = n // 10
        num_digits += 1
    else:
        print(f"The number of digits in {orig_n} is {num_digits}.")'''

#Count number of digits in integer
def main():
    n = 4555485
    orig_n = n
    five_counter = 0 
    while (n > 0):
        #n_mod = n % 10
        n, n_mod = divmod(n, 10)
        if (n_mod == 5):
            five_counter += 1

        #n = n // 10
    else:
        print(f"There are {five_counter} fives in {orig_n}.")
    
main()