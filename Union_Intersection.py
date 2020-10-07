# Union and Intersection of Two Linked Lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # keep original head to restore at the end
    llist_1_start = llist_1.head
    llist_2_start = llist_2.head

    # create a temporary set
    temporary_set = set()

    # add all elements of list 1
    while llist_1.head:
        item = llist_1.head.value
        temporary_set.add(item)
        llist_1.head = llist_1.head.next

    # add all elements of list 2
    while llist_2.head:
        item = llist_2.head.value
        temporary_set.add(item)
        llist_2.head = llist_2.head.next

    #create new resulting list
    llist_3 = LinkedList()
    for item in temporary_set:
        llist_3.append(item)

    # return list to start
    llist_1.head = llist_1_start
    llist_2.head = llist_2_start
    
    return llist_3


def intersection(llist_1, llist_2):
    # keep original head to restore at the end
    llist_1_start = llist_1.head
    llist_2_start = llist_2.head
    
    #create a temporary set
    temporary_set = set()

    while llist_1.head:
        item = llist_1.head.value
        while llist_2.head:
            # if element is found in both lists, add it to the set
            if item == llist_2.head.value:
                temporary_set.add(item)
            llist_2.head = llist_2.head.next
        llist_1.head = llist_1.head.next
        llist_2.head = llist_2_start

    # create intersected list
    llist_3 = LinkedList()
    for item in temporary_set:
        llist_3.append(item)

    # return list to start
    llist_1.head = llist_1_start
    llist_2.head = llist_2_start
    return llist_3 


print("======================================")
print("    Union and Intersection - tests        ")
print("======================================")

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print("union:")
print (union(linked_list_1,linked_list_2))

print("intersection:")
print (intersection(linked_list_1,linked_list_2))

print("--------------------")

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)



print("union:")
print (union(linked_list_3,linked_list_4))
print("intersection:")
print (intersection(linked_list_3,linked_list_4))

# Test case 3 - empty lists

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print("union:")
print (union(linked_list_5,linked_list_6))
print("intersection:")
print (intersection(linked_list_5,linked_list_6))


print("======================================")
print("    test cases completed        ")
print("======================================")