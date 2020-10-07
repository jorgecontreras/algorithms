# Problem 6 - Union and Intersection of linked lists

Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

# solution

1. The union is done by simply adding all elements of both lists into a third one. It takes **O(N)** time

2. For the intersection, we traverse the second list once for each element of the first list, adding the matches to a third list. This operation is slower because the list is passed multiple times (n times).
So, interesection would take O(n*k), where n is the size of list 1 and k is the size of list 2.

# space
The algorithm will use an additional set() to temporarily store the elements. This requires linear space **O(N)**