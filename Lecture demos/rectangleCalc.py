'''
Name: Myrisa Mitchell
Date: 2/21/2022

This program will ask for two sides of a rectangle and 
calculate the area and perimeter

Step 1: Prompt for two sides
Step 2: Calculate area
Step 3: Calculate perimeter
Step 4: Print out area and perimeter
'''

#Step 2
def calc_area(side1,side2):
    '''
    This function takes in two sides of a rectangle
    and returns the area.
    '''
    area = side1 * side2 
    return area

#Step 3
def calc_peri(side1,side2):
    '''
    This function takes in two sides of a rectangle
    and returns the perimeter.
    '''
    perimeter = (2 * side1) + (2 * side2)
    return perimeter

def main():
    #Step 1
    side1 = float(input("Please enter side 1: "))
    side2 = float(input("Please input side 2: "))

    #Step 2
    rect_area = calc_area(side1,side2)

    #Step 3
    rect_peri = calc_peri(side1,side2)

    print(f"The area of a rectangle with sides {side1} and {side2} is {rect_area}.")
    print(f"The perimeter of a rectangle with sides {side1} and {side2} is {rect_peri}.")

    pass

main()

'''
You can store multiple variables within one fuction. 
def calc_rectangle(side1,side2):
    #This function takes in two sides of a rectangle and
    calculates the area and perimeter and returns a tuple(area, perimeter).
    area = side1 * side2
    perimeter = (2 * side1) + (2 * side2)
    return area, perimeter

rect_values = calc_rectangle(side1,side)
print(f"The area of this rectangle is {rect_values[0]}.")
print(f"The perimeter of this rectnagle is {rect_values[1]}.")
'''