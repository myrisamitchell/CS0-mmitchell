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
Step 5: Determine if triangle can be formed. 
Step 6: Display consensus on if triangle can be formed. 
'''

from math import sqrt

#Step 2
def calc_area(side1,side2,side3):
    '''
    This function calculates the area of the triangle.
    '''
    semi_peri = (side1+side2+side3) / 2
    area = sqrt(semi_peri*(semi_peri-side1)*(semi_peri-side2)*(semi_peri-side3))
    return area

#Step 3
def calc_peri(side1,side2,side3):
    '''
    This function calculates the perimeter of the triangle.
    '''
    perimeter = side1+side2+side3
    return perimeter

#Step 5
#Source: https://www.codesansar.com/python-programming-examples/check-validity-triangle-given-sides.htm
def if_triangle(side1,side2,side3):
    if (side1+side2>side3 and side1+side3>side2 and side2+side3>side1):
        return True
    else:
        return False

def main():
    #Step 1
    side1 = int(input("Please enter one side of the triangle in inches: "))
    side2 = int(input("Please enter the second side of the triangle in inches: "))
    side3 = int(input("Please enter the third side of the triangle in inches: "))

    #Step 2
    tri_area = int(calc_area(side1,side2,side3))

    #Step 3
    tri_peri = int(calc_peri(side1,side2,side3))

    #Step 4 and 6
    #Source: https://www.codesansar.com/python-programming-examples/check-validity-triangle-given-sides.htm#:~:text=%23%20Validity%20of%20Triangle%20given%20sides,%3D%20float(input('Enter
    if if_triangle(side1,side2,side3):
        #Step 4
        print(f"The area of a triangle with sides of {side1} inches, {side2} inches, and {side3} inches is {tri_area} square inches.")
        print(f"The perimeter of a triangle with sides of {side1} inches, {side2} inches, and {side3} inches is {tri_peri} inches.")
    else:
        print("These sides don't form a triangle. Try again.")

main()