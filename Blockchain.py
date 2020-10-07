import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, data):
        if self.head:
            block = Block(datetime.now(tz=None), data, self.head.hash)
            self.head.next = block
            self.head = block
        else:
            block = Block(datetime.now(tz=None), data, 0)
            self.head = block
            self.tail = block
        self.size += 1

    def get_size(self):
        return self.size
        
    def traverse(self):
        current = self.tail
        while current:
            print("[ hash={} ][ timestamp={} ][ next= {}]".format(current.previous_hash, current.timestamp, current.data))
            current = current.next

# test case 1
print("======================================")
print("    Blockchain - running test cases        ")
print("======================================")
coins = Blockchain()
coins.add("Paid for groceries: $53.40")
coins.add("Bought soda online: $23.99")
coins.add("Received payment: $437.00")
coins.add("Netflix subscription: $8.99")

coins.traverse()

#test case 2 - multiple insertions
wallet = Blockchain()

for i in range(90909):
    wallet.add("Inserted a new block with id: " + str(i))

assert wallet.get_size() == 90909

#test case 3 - empty blockchain
nada = Blockchain()
nada.traverse()

assert nada.get_size() == 0
print("======================================")
print("        tests completed        ")
print("======================================")