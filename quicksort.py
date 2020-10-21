# Quicksort

def quicksort(items, start, end):
    left_index = start
    pivot_index = end
    pivot_value = items[pivot_index]

    while left_index != pivot_index:
        item = items[left_index]
        
        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index



quicksort(items, 0, len(items) - 1)




unordered = [43,2,9,13,3,40,55,10,4,7,3,9,2,5,88,34,15,67]
ordered = quicksort(unordered)