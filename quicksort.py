# Quicksort

def quickSort(a, l, r):

    if l >= r:
        return a

    x = a[l]
    i = l
    j = r

    while i <= j:
        while a[i] < x:
            i += 1
        while a[j] > x:
            j -= 1
        if i <= j:
            t = a[i]
            a[i] = a[j]
            a[j] = t
            i += 1
            j -= 1

    quickSort(a, l, j)
    quickSort(a, i, r) 
    
    return a


unordered = [43,2,9,13,3,40,55,10,4,7,3,9,2,5,88,34,15,67]
ordered = quicksort(unordered)
