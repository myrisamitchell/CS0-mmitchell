'''
Name: Myrisa Mitchell
Date: April 15, 2022

This program will search through a list and add pieces alternatively to Alice and Bob's sums.

Step 1: Take input of list of broken integer
Step 2: Add piece to Alice's sum
Step 3: Add piece to Bob's sum
Step 4: Print out both sums
Step 5: Define test function with three test cases
'''

#Step 5
def tests():
    list1 = [4, 2, 3, 1] 
    assert sort_sums(list1) == (7, 3)
    list2 = [8, 3, 2, 9, 1]
    assert sort_sums(list2) == (11, 12)
    list3 = [4, 5, 2]
    assert sort_sums(list3) == (6, 5)


#Step 1
def broken_integer():
    pieces = []
    num_pieces = int(input())
    piece_list = input()
    piece_list = piece_list.split()
    piece_list = [int(i) for i in piece_list]
    for i in piece_list:
        pieces.append(i)    
    return pieces

def sort_sums(integer_list):
    alice_turn = True
    alice_sum = 0
    bob_sum = 0
    for i in integer_list:
        #Step 2
        if alice_turn:
            alice_sum += i
            alice_turn = False
        #Step 3
        else:
            bob_sum += i
            alice_turn = True
    return alice_sum, bob_sum

def main():
    tests()
    integer_list = broken_integer()
    sums = sort_sums(integer_list)

    #Step 4
    print(sums[0], sums[1])

if __name__ == "__main__":
    main()