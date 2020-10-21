# Heap

# A heap can be represented as an array
# Insert happens always at next leaf, keeping a complete binary tree
# Remove happens always at root, adjusting values to keep complete binary tree and heap rules (values)

class Heap():
    def __init__(self):
        self.items = []

    def insert(self, v):
        #first insert at next leaf
        self.items.append(v)
        
        #adjust to keep heap rules
        n = len(self.items)
        p = (n // 2)
        while p > 0:
            if self.items[n - 1] > self.items[p - 1]:
                swap = self.items[n - 1]
                self.items[n - 1] = self.items[p - 1]
                self.items[p - 1] = swap
            n = p
            p = p // 2
            
    def delete(self):
        v = self.items[0]
        if len(self.items) == 1:
            return self.items.pop()
   
        self.items[0] = self.items.pop()
        i = 1
        while i*2 - 1 < len(self.items):
            big = self.items[i*2 - 1]
            
            swap = False
            if i*2 < len(self.items):
                sibling = self.items[i*2]
                if sibling > big:
                    big = sibling
                    swap = True
            
            if big > self.items[i - 1]: 
                if swap:
                    self.items[i*2] = self.items[i - 1] 
                else:
                    self.items[i*2 - 1] = self.items[i - 1]
                self.items[i - 1] = big
            i = i*2
            if swap:
                i += 1
        
        return v

    def findkthlargest(self, k):
        while k > 0:
            v = self.delete()
            k -= 1
        return v


    def sort(self):
        pass

heap = Heap()
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(1)
heap.insert(2)
heap.insert(12)
heap.insert(33)
heap.insert(7)

print(heap.items)

print(heap.findkthlargest(7))