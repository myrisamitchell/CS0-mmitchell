from sys import *

def tests():
    pass 

def main():
    my_dictionary = {}

    my_dictionary["apple"] = 42
    my_dictionary[0] = "apple"
    my_dictionary["red"] = [42, 24, 15, 5, "rain"]
    my_dictionary["second"] = {1: "apple", "computer": "mouse", "green": [42, 24, 15]}

    # print(my_dictionary)

    if my_dictionary.get("apple") != None:
        my_dictionary["apple"] = "Pear"

    # print(my_dictionary.get("apple"))

    my_dictionary["red"].append(42)

# Print values without keys in list form
    print(f"{my_dictionary.items()}")
    for k in my_dictionary.keys():
        print(f"{my_dictionary[k]}")
    # Print keys and values
    for k, v in my_dictionary.items():
        print(f"{my_dictionary[k]}")
        print(f"{k}: {v}")
    #Print values without keys in dictionary form
    print(f"{my_dictionary.values()}")





    # print(f'The value in the dictionary key apple is: {my_dictionary["apple"]}')

if __name__ == "__main__":
    if (len(argv)) == 2 and argv[1] == "test":
        tests()
    else:
        main()