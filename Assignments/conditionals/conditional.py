'''
Name: Myrisa Mitchell
Date: March 20, 2022

This program will compute the sum, product, max, min, and average
of 5 numbers prompted from the user. 

Step 1: Define a function that takes 5 numbers and calculates the sum
Step 2: Define a function that takes 5 numbers and calculates the product
Step 3: Define a function that takes 5 numbers and calculates the average
Step 4: Define a function that takes 5 numbers and finds the maximum 
Step 5: Define a function that takes 5 numbers and finds the minimum
Step 6: Define a main function
Step 6a: Prompt users for 5 numbers
Step 6b: Call all functions and displays results
Step 7: Define a test function that tests each function twice
'''

#Step  1
def sum_numbers(num1, num2, num3, num4, num5):
    add_all_nums = num1 + num2 + num3 + num4 + num5
    print(f"The sum of {num1}, {num2}, {num3}, {num4}, and {num5} is {add_all_nums}.")
    return add_all_nums

#Step 2
def multiply_nums(num1, num2, num3, num4, num5):
    num_product = num1 * num2 * num3 * num4 * num5
    print(f"The product of {num1}, {num2}, {num3}, {num4}, and {num5} is {num_product}.")
    return num_product

#Step 3
def ave_nums(num1, num2, num3, num4, num5):
    ave_nom = num1 + num2 + num3 + num4 + num5
    nums_average = ave_nom / 5
    print(f"The average of {num1}, {num2}, {num3}, {num4}, and {num5} is {nums_average}.")
    return nums_average

#Step 4
def max_nums(num1, num2, num3, num4, num5):
    if (num1 > num2 and num1 > num3 and num1 > num4 and num1 > num5):
        print(f"{num1} is the biggest number you entered.")
    elif (num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5):
        print(f"{num2} is the greatest number you entered.")
    elif (num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5):
        print(f"{num3} is the biggest number you entered.")
    elif (num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5):
        print(f"{num4} is the biggest number you entered.")
    else:
        print(f"{num5} is the biggest number you entered.")

#Step 5
def min_nums(num1, num2, num3, num4, num5):
    if (num1 < num2 and num1 < num3 and num1 < num4 and num1 < num5):
        print(f"{num1} is the smallest number you entered.")
    elif (num2 < num1 and num2 < num3 and num2 < num4 and num2 < num5):
        print(f"{num2} is the smallest number you entered.")
    elif (num3 < num1 and num3 < num2 and num3 < num4 and num3 < num5):
        print(f"{num3} is the smallest number you entered.")
    elif (num4 < num1 and num4 < num2 and num4 < num3 and num4 < num5):
        print(f"{num4} is the smallest number you entered.")
    else:
        print(f"{num5} is the smallest number you entered.")

#Step 6
def main():
    #Step 6a
    num1 = float(input("Please enter a number: "))
    num2 = float(input("Please enter another number: "))
    num3 = float(input("Please enter another number: "))
    num4 = float(input("Please enter another number: "))
    num5 = float(input("Please enter another number: "))

    #Step 6b
    sum_numbers()
    multiply_nums()
    ave_nums()
    max_nums()
    min_nums()

main()