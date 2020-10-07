# Huffman Coding
import sys

# NodeTree Class
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    #def __str__(self):
    #    return '%s_%s' % (self.left, self.right)

def create_tree(nodes):
    while len(nodes) > 1:
        # take the 2 smallest
        (key1, c1) = nodes[0]
        (key2, c2) = nodes[1]

        # reduce the priority queue
        nodes = nodes[2:]

        # create a new node, with its 2 children
        node = NodeTree(key1, key2)

        # insert the node back to the priority queue
        nodes.append((node, c1 + c2))
            
        #sort the nodes again
        nodes = sorted(nodes, key=lambda x: x[1])

    return nodes

def frequency(data):
    # Calculate frequency
    freq = {}
    for c in data:
        freq[c] = freq.get(c, 0) + 1

    return sorted(freq.items(), key=lambda x: x[1])

# recursively generate the bits
def huffman_codes(node, bit=''):
    if type(node) is str:
        return {node: bit}
    (l, r) = node.children()
    d = dict()
    d.update(huffman_codes(l, bit + '0'))
    d.update(huffman_codes(r, bit + '1'))
        
    return d

def huffman_encoding(data):
    if data == "":
        return None, ""

    freq = frequency(data)
    nodes = create_tree(freq)
    
    if len(freq) == 1:
        huffman_table = {data[0]: '1'} #handle case where there is one single character (on its own or repeated)
    else:
        huffman_table = huffman_codes(nodes[0][0])

    encoded = ""
    for c in data:
        encoded += huffman_table[c]
        
    return encoded, nodes[0][0]

def huffman_decoding(data,tree):
    decoded = ""
    # handle single character
    if type(tree) is str:
        for c in data:
            decoded += tree
        return decoded

    # for all other cases, traverse tree starting at root
    node = tree
        
    for c in data:
        (l, r) = node.children()
            
        if c == '0':
            node = l
        else:
            node = r

        if type(node) is str:
            decoded += node
            node = tree
    
    return decoded



# test case 1
input_string = "AAAAAAABBBCCCCCCCDDEEEEEE"
encoded, tree = huffman_encoding(input_string)
assert encoded == "1010101010101000100100111111111111111000000010101010101"

decoded_string = huffman_decoding(encoded, tree)
assert decoded_string == "AAAAAAABBBCCCCCCCDDEEEEEE"

# test case 2 
a_great_sentence = "The bird is the word"

print("------------------------- EXAMPLE 1 -------------------------")
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# test case 3 - longer string
print("------------------------- EXAMPLE 2 -------------------------")
a_great_sentence = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like)"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


# test case 4 - empty strings
input_string = ""
encoded, tree = huffman_encoding(input_string)

# test case 5 - single character
input_string = "j"
encoded, tree = huffman_encoding(input_string)
print(encoded)
decoded_data = huffman_decoding(encoded, tree)
print(decoded_data)

# test case 6 - same character repeated
input_string = "cccccccccccccccc"
encoded, tree = huffman_encoding(input_string)
print(encoded)
decoded_data = huffman_decoding(encoded, tree)
print(decoded_data)



