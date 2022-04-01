'''
b = 'this is a string'
a = []
[] indicates a list 
To insert numbers into a list:
a = [2,42,7,83]
To print off element in a list:
a[0]
    Will return: 2
a[1]
    Will return: 42
a[-1]
    Will return last element: 83
a[-2]
    Will return second to last element

Lists inside of lists:
a = [2,42,[84,123],56]
To print off element from list inside of list
a[2][0]
    Will return: 84
    "Go to index 2 and retrieve element 0"

a = [2,42,[84,['apple','broccoli']123],56]
a[2][1][0]
    Will return 'apple'
a[2][1][0][0]
    Will return: 'a'

range(10)
    range(0,10)
a = list(range10)
a = [0,1,2,3,4,5,6,7,8,9]

a = list('apple)
a = ['a','p','p','l','e']

a = list(range(0, 20, 2))
    Will return all even numbers, 20 exclusive.
a = list(range(1, 20, 2))
    Will return all odd numbers, 20 exclusive.
'''

def explode_list(list_element):
    for i in list_element:
        if isinstance(i, list):
            explode_list(i)
        else:
            if isinstance(i, str):
                for j in i:
                    print(j)
            else:
                print(i)
    

def main():
    some_nums = [42, 15, [843, ["purple", [82.4, 152.241]], 123], 231, 5]
    # len_list = len(some_nums[2])
    # print(len_list)
    explode_list(some_nums)
# To print off every element
#   for i in some_nums:
#       if isinstance(i, list) or isinstance(i, str):
#           for j in i:
#               print(j)
#       else:
#           print(i)

if __name__ == "__main__":
    main()