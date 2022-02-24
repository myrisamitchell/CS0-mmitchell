'''
Name: Myrisa Mitchell
Date: 2/23/2022

This program will prompt for the three sides of a triangle, 
calculate the area and perimeter, and print out the area and
perimeter. 

Step 1: Prompt for sides of triangle.
Step 2: Calculate area of triangle.
Step 3: Calculate perimeter of triangle. 
Step 4: Display area and perimeter of the triangle.
'''

import math 

#Step 2
def calc_area(side1,side2,side3):
    '''
    This function calculates the area of the triangle.
    '''
    semi_peri = (side1+side2+side3) // 2
    area = math.sqrt(semi_peri*(semi_peri-side1)(semi_peri-side2)(semi_peri-side3))
    return area

#Step 3
def calc_peri(side1,side2,side3):
    '''
    This function calculates the perimeter of the triangle.
    '''
    perimeter = side1+side2+side3
    return perimeter

def main():
    #Step 1
    side1 = int(input("Please enter one side of the triangle in inches: "))
    side2 = int(input("Please enter the second side of the triangle in inches: "))
    side3 = int(input("Please enter the third side of the triangle in inches: "))

main()