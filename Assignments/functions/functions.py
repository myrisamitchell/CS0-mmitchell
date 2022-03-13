'''
Name: Myrisa Mitchell
Date: 03/05/22

This program will perform arithmetic operations on two given
numbers prompted from the user.

Step 1: Define a function that sums the two numbers.
Step 1a: Print sum. 
Step 2: Define a function that multiplies two numbers.
Step 2a: Print product.
Step 3: Define a function that divides two numbers.
Step 3a: Print quotient.
Step 4: Define a function that finds the difference of the two numbers.
Step 4a: Print the difference.
Step 5: Define a function that finds the remainder of the first number divided by the second.
Step 5a: Print the remainder
Step 6: Define a function that finds the first number raised to the second number.
Step 6a: Print the value.
Step 7: Define a function that finds the sqrt of both numbers.
Step 7a: Print the sqrt.
Step 8: Promp the user for two numbers.
Step 9: Create test function that tests all functions.
Step 10: Call test function and main function.
'''

from math import sqrt


#Step 1
def find_sum(num1, num2):
    sum_answer = num1 + num2
    #Step 1a
    print(f"{num1} + {num2} = {sum_answer}.")
    return sum_answer

#Step 2
def find_product(num1, num2):
    prod_answer = num1 * num2
    #Step 2a
    print(f"{num1} * {num2} = {prod_answer}.")
    return prod_answer

#Step 3
def find_quotient(num1, num2):
    quot_answer = num1 / num2
    #Step 3a
    print(f"{num1} / {num2} = {quot_answer}.")
    return quot_answer

#Step 4
def find_difference(num1, num2):
    diff_answer = num1 - num2
    #Step 4a
    print(f"{num1} - {num2} = {diff_answer}.")
    return diff_answer
    
#Step 5
def find_remain(num1, num2):
    quot, remain = divmod(num1, num2)
    #Step 5a
    print(f"{num1} / {num2} = {quot} with a remainder of {remain}.")
    return quot, remain

#Step 6
def find_exp(num1, num2):
    exp_answer = num1**num2
    #Step 6a
    print(f"{num1} raised to the power of {num2} is {exp_answer}.")
    return exp_answer

#Step 7
def find_sqrt(num1, num2):
    if (num1 > 0 and num2 > 0):
        sqrt_num1 = sqrt(num1)
        sqrt_num2 = sqrt(num2)
        #Step 7a
        print(f"The square root of {num1} is {sqrt_num1}.")
        print(f"The square root of {num2} is {sqrt_num2}.")
        return sqrt_num1, sqrt_num2
    else:
        print(f"Cannot find the square root of a negative number.")

#Step 9
def tests():
    assert find_sum(12,5) == 17
    assert find_sum(3,9) == 12
    assert find_product(2,6) == 12
    assert find_product(3,12) == 36
    assert find_quotient(45,15) == 3
    assert find_quotient(90,9) == 10
    assert find_difference(42,10) == 32
    assert find_difference(36,14) == 22
    assert find_remain(42,5) == 8, 2
    assert find_remain(94,13) == 7, 3
    assert find_exp(2,3) == 8
    assert find_exp(12,4) == 20736
    assert find_sqrt(81,36) == 9, 6
    assert find_sqrt(16,25) == 4, 5
    print(f"All test cases passed.")


def main():
    #Step 10
    tests()
    #Step 8
    num1 = input("Please enter a number: ")
    num2 = input("Please enter another number: ")
    #Step 10
    find_sum(num1, num2)
    find_product(num1, num2)
    find_quotient(num1, num2)
    find_difference(num1, num2)
    find_remain(num1, num2)
    find_exp(num1, num2)
    find_sqrt(num1, num2)

main()