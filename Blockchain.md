# Problem 5 - Blockchain

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

# solution 

This is a singly linked list. Using a head and a tail for faster insertions **O(1)**

_Note_: If I had used only head, I would need to traverse the whole linked list for every insertion, taking **O(N)** in that case.

# space

The algorithm to add a block takes constant space. **O(1)**