'''
Myrisa Mitchell
Date: 02/09/22

This program will calculate the BMI of a person. 
BMI = kg/m**2

Step 1: Prompt user to enter weight and height.
Step 1a: Convert weight and height values to floats.
Step 2: Calculate BMI using inputted values.
Step 3: Print out BMI.
'''

#step 1
weight = input("Please enter your weight in lbs: ")
height = input("Please enter your height in inches: ")

#step 1a
weight = float(weight)
height = float(height)

#step2
weight = weight/2.205
height = height/39.37
bmi = weight/height**2

#step3
print("Your BMI with weight",
    weight, "and height", height,
    "is", bmi)
