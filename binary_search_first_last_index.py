
# Given a sorted array that may have duplicate values, 
# use binary search to find the first and last indexes of a given value.
# For example, if you have the array [0, 1, 2, 2, 3, 3, 3, 4, 5, 6] 
# and the given value is 3, the answer will be [4, 6] 
# (because the value 3 occurs first at index 4 and last at index 6 in the array).
# 
# The expected complexity of the problem is  𝑂(𝑙𝑜𝑔(𝑛)) .


def binary_search(target, source, i=0):
    mid = len(source) // 2
    
    if target == source[mid]:
        return mid + i
    elif target < source[mid]:
        source = source[:mid]
    else:
        i += mid
        source = source[mid:]
        
    if len(source) == 1 and source[0] != target:
        return -1
    
    return binary_search(target, source, i)
    
        
def first_and_last_index(arr, number):
    """
    Given a sorted array that may have duplicate values, use binary 
    search to find the first and last indexes of a given value.

    Args:
        arr(list): Sorted array (or Python list) that may have duplicate values
        number(int): Value to search for in the array
    Returns:
        a list containing the first and last indexes of the given value
    """
    
    # find occurence of element in any position, return -1 if not found
    start_index = binary_search(number, arr)
    if start_index < 0:
        return [-1, -1]

    # with the element found, keep looking in adjacent indexes both sides
    index = start_index
    
    #find first ocurrence (go to left one by one)
    while arr[index] == number:
        if index == 0:
            left = 0
            break
        elif arr[index-1] == number:
            index -= 1
        else:
            left = index
            break
    
    #find last ocurrence (go to right one by one)
    index = start_index
    while arr[index] == number:
        if index == len(arr) - 1:
            right = index
            break
        elif arr[index + 1] == number:
            index += 1
        else:
            right = index
            break
            
    return [left, right]

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

# test case 1
input_list = [1]
number = 1
solution = [0, 0]
test_case_1 = [input_list, number, solution]
test_function(test_case_1)

# test case 2
input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)

# test case 3
input_list = [0, 1, 2, 3, 4, 5]
number = 5
solution = [5, 5]
test_case_3 = [input_list, number, solution]
test_function(test_case_3)

# test case 4
input_list = [0, 1, 2, 3, 4, 5]
number = 6
solution = [-1, -1]
test_case_4 = [input_list, number, solution]
test_function(test_case_4)
