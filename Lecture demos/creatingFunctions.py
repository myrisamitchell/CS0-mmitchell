#To create a function, use colon to signify that following is 
    #part of the function
#List within function must be indented
from audioop import mul


def greeting():
    print("Hello Myrisa")  

print("Outside function")
#Prints out what was defined in function, or Hello Myrisa
greeting()

def f(x):
    print(x**2 - 5)

x=3
f(x)

#Fruitful vs. fruitless

#Fruitless
def calc_values(x):
    print(x**2 // 5)

#Fruitful
def calc_more_values(x):
    answer = x**2 // 5
    return answer 

#Use output from previous function as input for new calculation
x = 5
answer = calc_more_values(x)
print(answer)

answer = calc_more_values(answer)
print(answer)

def prompt_name():
    input_string = input("Please enter your name: ")
    return input_string

def greet(name):
    print("Hello", name)

name = ""
name = prompt_name()
greet(name)

greet(prompt_name())

#Exercise
'''
Myrisa Mitchell
2/18/2022

This program will define a function that takes
two numbers and returns the product of the two numbers

Step 1: Define the function to take two numbers
Step 2: Return product of two number from function
Step 3: Call function with some parameters
Step 4: Print out answer
'''

#Step 1
def multiply_nums(num1, num2):
    #Step 2
    return num1*num2

#Step 3
answer = multiply_nums(42, 5)

#Step 4
print("42 * 5 is equal to", answer)

'''
Global vs. Local variables
Global: Variable that can be called at any time in terminal
Local: Variable assigned to a defined function, cannot be called
    outside of function
'''
#To use a global variable in a function:
def multiply_numbers(num1,num2)
    global multiply_sum
    multiply_sum = num1*num2
    return multiply_sum
'''multiply_sum can be called outside of the function and the
program will recognize it
'''

#Creating a Test Function 
def tests():
    assert multiply_nums(2,3) == 6
    assert multiply_nums(7,8) == 56
    print(f"All test cases passed")

#Main function
def main():
    #To check if inserted function is correct before using it
    tests()
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    answer = multiply_nums(number1,number2)
    print(f"{number1} * {number2} = {answer}")

#Will not do anything until you call it 
main()

'''
Instead of testing every time you change code, use assert
'''
assert 5 == 5
#True
assert 5 == 6 
#False
#Using it with a function
multiply_nums(2,3)
assert multiply_nums(2,3) == 6
#True
assert multiply_nums(2,3) == 7
#False

#Test functions
    #See line 92
