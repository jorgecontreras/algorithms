# merge sort

#
# MergeSort is a divide and conquer algorithm that divides a list into equal halves 
# until it has two single elements and then merges the sub-lists until the entire 
# list has been reassembled in order.
#

def merge_sort(elements):

    # Base case, a list of 0 or 1 items is already sorted
    if len(elements) <= 1:
        return elements

    # otherwise, find the midpoint and split the list
    mid_point = len(elements) // 2
    
    # left
    left = elements[:mid_point]
    
    # right
    right = elements[mid_point:]
    
    # call merge_sort recursively with the left and right half
    left = merge_sort(left)
    right = merge_sort(right)

    # merge our two halves an return
    return merge(left, right)

def merge(left, right):
    # given two ordered lists, merge them together in order
    # returning the merged list
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) or right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
            if left_index == len(left):
                # done with left, just copy all the remaining from the right
                merged += right[right_index:]
                break
        else:
            merged.append(right[right_index])
            right_index += 1
            if right_index == len(right):
                # done with right, just copy all the remaining elements from left
                merged += left[left_index:]  
                break

    return merged

# tests

elements = [45,23,1,98,451,3,55,23,71,421,56,16,16,24]

merge_sorted = merge_sort(elements)
sorted_elements = sorted(elements)

print('running tests')
assert merge_sorted == sorted_elements
print('all tests completed')