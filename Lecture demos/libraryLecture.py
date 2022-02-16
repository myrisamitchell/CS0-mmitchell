import math

# To view math library, in terminal, call help(math)

# To use a function, put math. in front of the function. 
math.ceil(5.2)
print(math.ceil(5.2))

math.exp(5)
print(math.exp(5))

import random

#Generates sudo-random numbers (repeatable)
    #Will give a random value between 0-1
random.random()
print(random.random())

#Generates a number between a and b, including a and b
random.randint(1, 20)
print(random.randit(1,20))

#To import a function so you don't have to type it everytime
from random import randint
#or
import random as rd


import os

#Deals with files and operating system

import time
time.localtime()
time.asctime()
    #Prints out time as a string

import string
string.ascii_letters()
    #Prints out a string of all asci letters
string.printable()
    #Prints out all printable letters
