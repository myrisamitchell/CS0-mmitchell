#To create a function, use colon to signify that following is 
    #part of the function
#List within function must be indented
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


