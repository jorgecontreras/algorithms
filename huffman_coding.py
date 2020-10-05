# Huffman Coding

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

#Huffman Class
class Huffman(object):
    def __init__(self):
        pass

    def encode(self, string):
        self._frequency(string)
        self._create_tree()
        huffman_codes = self._huffman_codes(self.nodes[0][0])
        encoded = ""
        for c in string:
            encoded += huffman_codes[c]
        
        return encoded

    def decode(self, string):
        decoded = ""

        #start at root
        node = self.nodes[0][0]
        
        for c in string:
            (l, r) = node.children()
            
            if c == '0':
                node = l
            else:
                node = r

            if type(node) is str:
                decoded += node
                node = self.nodes[0][0]
    
        return decoded


    def _frequency(self, string):
        # Calculate frequency
        freq = {}
        for c in string:
            freq[c] = freq.get(c, 0) + 1

        self.nodes = sorted(freq.items(), key=lambda x: x[1])

    # create the tree
    def _create_tree(self):
        while len(self.nodes) > 1:
            # take the 2 smallest
            (key1, c1) = self.nodes[0]
            (key2, c2) = self.nodes[1]

            # reduce the priority queue
            self.nodes = self.nodes[2:]

            # create a new node, with its 2 children
            node = NodeTree(key1, key2)

            # insert the node back to the priority queue
            self.nodes.append((node, c1 + c2))
            
            #sort the nodes again
            self.nodes = sorted(self.nodes, key=lambda x: x[1])

    # recursively generate the bits
    def _huffman_codes(self, node, bit=''):
        if type(node) is str:
            return {node: bit}
        (l, r) = node.children()
        d = dict()
        d.update(self._huffman_codes(l, bit + '0'))
        d.update(self._huffman_codes(r, bit + '1'))
        
        return d

# tests
encoder = Huffman()
input_string = "AAAAAAABBBCCCCCCCDDEEEEEE"
encoded = encoder.encode(input_string)
assert encoded == "1010101010101000100100111111111111111000000010101010101"

decoded_string = encoder.decode(encoded)
assert decoded_string == "AAAAAAABBBCCCCCCCDDEEEEEE"