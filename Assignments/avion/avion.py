'''
Name: Myrisa Mitchell
Date: 04/07/22

This program will look through 5 rows of "blimps" to find CIA blimps that contain 
"FBI" and will output the row number that the CIA blimp

Step 1: Search through each row of blimps in first input
Step 2: If a row contains the string "FBI", print out row number
Step 3: If no rows in the input contain "FBI", print out "He got away!"
Step 4: Create test function with 3 test cases
'''

def tests():
    pass


def search_blimps(blimps):
    cia_blimp = []
    #Step 1
    for i in range(len(blimps)):
        if ("FBI" in blimps[i]):
            cia_blimp.append(i+1)
    #Step 2
    if cia_blimp:
        print(cia_blimp, sep = " ")
    else: 
        #Step 3
        print("HE GOT AWAY!")

def main():
    input_blimp = input("Enter 5 elements of code separated by a space: ")
    blimps = input_blimp.split()
    search_blimps(blimps)

if __name__ == "__main__":
    main()
