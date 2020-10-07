from collections import OrderedDict

# LRU Cache using ordered dictionary
class LRU_Cache():

    def __init__(self, capacity=10):
        # Initialize class variables
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        value = self.cache.get(key, -1)
        if value != -1:
            self.cache.move_to_end(key)

        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache.__setitem__(key, value)

        # exceeded capacity, remove oldest
        if len(self.cache) > self.capacity:
            oldest = next(iter(self.cache))
            del self.cache[oldest]


print(" ---- STARTING TEST CASES ------")
#basic test cases
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

assert our_cache.get(1) == 1       # returns 1
assert our_cache.get(2) == 2       # returns 2
assert our_cache.get(9) == -1      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

assert our_cache.get(3) == -1      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# edge cases
# zero size
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
assert our_cache.get(1) == -1

# negative value
our_cache = LRU_Cache(-1)
our_cache.set(1, 1)
assert our_cache.get(1) == -1

# no size provided, will default to 10 as per implementation
our_cache = LRU_Cache()
our_cache.set(1, 1)
assert our_cache.get(1) == 1

#very large cache size
our_cache = LRU_Cache(1000000)

for i in range(1000001):
   our_cache.set(i, i)
assert our_cache.get(5000) == 5000

print(" ---- TEST CASES COMPLETED ------")