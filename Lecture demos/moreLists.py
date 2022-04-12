import copy

def mod_numbers(numbers):    
    for i in range(len(numbers)):
        numbers[i] += 10
    pass
#Copying lists

def main():
    numbers = [42, [123, 456, 789, 321], 27, 32, 15]
    numbers2 = []
    numbers3 = []
    # for i in range(len(numbers)):
    #     numbers2.append(numbers[i])
    # numbers2 = numbers.copy
    #Copying a list within a list
        #Slow way
    '''
    for i in range(len(numbers)):
        if (isinstance(numbers[i], list)):
            tmp_list = []
            for j in range(len(numbers[i])):
                tmp_list.append(numbers[i][j])
            numbers2.append(tmp_list)
        else:
            numbers2.append(numbers[i])
    '''
       
        #Better way 
    numbers2 = copy.deepcopy(numbers)

    print(numbers)
    print(numbers2)


if __name__ == "__main__":
    main()