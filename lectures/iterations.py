'''
Name: Myrisa Mitchell
Date: 03/04/22

This program is to demonstrate loops.
'''

''' 
for i in range(10):
    if (i%2 == 0):
        continue
    print(i)
'''
'''def main():

    for i in range (10):
        if (i%2 == 1):
            continue
        print(i)
    else:
        print("We printed off numbers")

    print("Outside of for loop")

main()'''

def is_prime(number):
    for i in range(2, ((number//2)+1)):
        if (number%i == 0):
            '''print(f"{number} is not prime.")
            print(f"{number} is divisible by {i}.")'''
            return False, i
    else:
        '''print(f"{n} is prime.")'''
        return True, 0

def print_result(prime, number, divisor):
    if not (prime):
        print(f"{number} is not prime.")
        print(f"{number} is divisible by {divisor}.")
    else:
        print(f"{number} is prime.")

def tests():
    assert is_prime(42) == (False, 2)
    assert is_prime(13) == (True, 0)
    assert is_prime(47) == (True, 0)
    print("All test cases passed.")

def main():
    tests()
    n = int(input("Please enter a whole number greater than 2: "))
    prime, divisor = is_prime(n)
    print_result(prime, n, divisor)

main()