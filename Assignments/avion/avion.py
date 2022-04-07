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
    assert search_blimps(FBI-12, HAND-97, FOURTH3, HAR-35, HIFBI-7) == [1, 5]


def search_blimps(blimps):
    cia_blimp = []
    #Step 1
    for i in range(5):
        if ("FBI" in blimps[i]):
            cia_blimp.append(i+1)
    #Step 2
    if cia_blimp:
        #Source: https://github.com/robertusbagaskara/kattis-solutions/blob/master/source/Avion/avion.py
        for i in range(len(cia_blimp)):
            print('%i ' % cia_blimp[i], end = '')
    else: 
        #Step 3
        print("HE GOT AWAY!")

def main():
    tests()
    blimps = input()
    search_blimps(blimps)

if __name__ == "__main__":
    main()
