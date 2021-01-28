# quicksort

# choose a pivot
# move smaller to the left and larger to the right of the pivot
# is it recursive? YES
# time: O(n log n) for avg and best case O(n2) worst case
# space: O(1): in place swaps

def quicksort(nums):

    #base case 
    if len(nums) < 2:
        return nums

    frontier = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[0]: #first num is used as pivot
            frontier += 1
            nums[i], nums[frontier] = nums[frontier], nums[i]

    #move the pivot to its position
    nums[0], nums[frontier] = nums[frontier], nums[0]

    #recursive call on left and right
    left = quicksort(nums[:frontier])
    right = quicksort(nums[frontier+1:])

    #merge everything
    return left + [nums[frontier]] + right


nums1 = [2,5,7,2,7,8,2,8,2,74,14,5,4,3,33,6,8,8]
nums2 = [5,1,8,23,6,8,2,6,1,6,1,89,4]

assert sorted(nums1) == quicksort(nums1)
assert sorted(nums2) == quicksort(nums2)