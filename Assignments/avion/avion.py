'''
Name: Myrisa Mitchell
Date: 04/07/22

Avion Kattis problem
This program will look through 5 rows of "blimps" to find CIA blimps that contain 
"FBI" and will output the row number that the CIA blimp

Step 1: Search through each row of blimps in first input
Step 2: If a row contains the string "FBI", print out row number
Step 3: If no rows in the input contain "FBI", print out "He got away!"
Step 4: Create test function with 3 test cases
'''

def tests():
    blimps1 = ["FBI-12", "HAND-97", "FOURTH3", "HAR35", "HIFBI-7"]
    blimps2 = ["HI-34T", "FNI-J2", "FBI-7", "CRIFBI-3", "HRG43H"]
    blimps3 = ["CRY-Y3", "HE-3HA", "AH75H3", "HE-6HTE", "MARIKA-8"]
    assert search_blimps(blimps1) == [1, 5]
    assert search_blimps(blimps2) == [3, 4]
    assert search_blimps(blimps3) == []  


def search_blimps(blimps):
    cia_blimp = []
    #Step 1
    for i in range(5):
        if ("FBI" in blimps[i]):
            cia_blimp.append(i+1)
    return cia_blimp

def main():
    tests()

    # blimp1 = input()
    # blimp2 = input()
    # blimp3 = input()
    # blimp4 = input()
    # blimp5 = input()
    blimps = [input() for i in range(5)]
    ciaBlimp = search_blimps(blimps)
    if not ciaBlimp:
        print("HE GOT AWAY!")
    else:
        print(*ciaBlimp)

if __name__ == "__main__":
    main()
