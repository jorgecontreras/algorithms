def binary_search(target, source, i = 0):
    mid = len(source) // 2

    if target == source[mid]:
        return mid + i
    elif target < source[mid]: # target could be on left side, discard right side
        source = source[:mid]
    else:                      # target could be on right side, discard left side
        source = source[mid:]
        i += mid

    if len(source) <= 1 and source[0] != target:
        return -1

    return binary_search(target, source, i)

source = [1,4,5,7,8,90,92,93,95,97,100,123,145,167]


target = 167
assert binary_search(target, source) == 13

target = 1
assert binary_search(target, source) == 0

target = 1600
assert binary_search(target, source) == -1

target = 7
assert binary_search(target, source) == 3

target = -27
assert binary_search(target, source) == -1




