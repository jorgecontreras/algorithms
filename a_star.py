
        
# calculate straight distance between a and b
def get_distance(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    
    d = (dx**2 + dy**2)**(1/2)
    return d
    
# A Node is an intersection in the map.
class Node:
    def __init__(self, name):
        self.name = name
    
# Frontier is a dictionary of nodes that can be expanded. example:
# self.nodes 
# 
#  {
#      '5': Node,
#      '33' : Node,
#      '27' : Node
#  }
#
class Frontier:
    
    def __init__(self, M, goal):
        self.nodes = {}
        self.arrived = False
        self.M = M
        self.goal = goal
        self.best_path = None
    
        # Path dictionary
        #
        # Here we will keep track of the paths explored.
        # The key is the edge of a given path
        # The value is a list of all the nodes visited 
        # in that path, and its route cost.
        #
        # example:
        #
        # {
        #     5: {'cost': 135, 'visited': [8, 33, 2, 17, 6]},
        #     14 : {'cost': 240, 'visited': [8, 33, 2, 15, 23]},
        #     7 : {cost: 90, 'visited': [8, 33, 6, 12]}
        # }
        # 
        self.paths = {}
    
    # add a new node to the frontier
    def add(self, node: Node):
        self.nodes[node.name] = node
    
    # remove a node from the frontier
    def remove(self, node: Node):
        if node.name in self.nodes:
            self.nodes.pop(node.name)
        
        # the goal test is made here,
        # right after removing a node
        if self.goal in self.nodes:
            self.arrived = True
            self.best_path = self.paths[self.goal]
        
    # get the size of the frontier
    def size(self):
        return len(self.nodes)
    
    # for debugging and inspection
    def __str__(self):
        data = "\n Paths explored:"
        
        for p, path in self.paths.items():
            data += "\n | Path edge:" + str(p)
            data += " | cost: " + str(path['cost'])
            data += " | nodes in path: " + str(path['visited'])
        
        data += "\n\n Nodes in the frontier: "
        for name, node in self.nodes.items():
            data += "\n ------ "
            data += "\n name: " + str(name)
            data += "\n ------ "
        
        return data
    
    # from the frontier get the smallest path
    def poll(self):
        smallest_cost = None
        for front in self.nodes:
            if smallest_cost is None or self.paths[front]['cost'] < smallest_cost:
                smallest_path = self.paths[front]
                closest_node = front
                smallest_cost = self.paths[front]['cost']
        return closest_node, smallest_path
    
    # find adjacent nodes that are not in the list of visited nodes*
    # * in some cases we DO want to explore a path that was already in the dictionary
    # who knows, maybe this new path is cheaper?
    def adjacent(self, node: Node):
        adjacent = []
        for i in self.M.roads[node.name]:
            if i not in self.paths:
                adjacent.append(i)
            if i in self.paths and i in self.nodes:
                adjacent.append(i)
        return adjacent
    
        #return [i for i in self.M.roads[node.name] if i not in self.nodes and i not in self.paths]
    
    # calculate the cost of a segment (distance between two nodes)
    def segment_cost(self, n1: Node, n2: Node):
        return get_distance(self.M.intersections[n1.name], self.M.intersections[n2.name])
    
    # calculate the estimated straight line distance between a node and the goal
    def estimated_cost(self, node):
        return get_distance(self.M.intersections[node], self.M.intersections[self.goal])
        
    
    # EXPAND
    # expanding involves the following steps:
    #
    # [1] Take a node as an input and find all adjacent intersections that have not been explored yet.
    # [2] Create a new Node() for each intersection.
    # [3] Calculate the new cost of each path and store it in the paths dictionary.
    # [4] Add the new paths to the path dictionary.
    # [5] Add the new nodes to the frontier.
    # [6] From the frontier, remove the expanded node (input). It's no longer frontier, it becomes visited.
    #
    # *** Both the cost and the paths will use the input node as a starting point. ***
    def expand(self, node, path):
        adjacent = self.adjacent(node) # [1]
        for a in adjacent:
            n = Node(a) # [2]
            self.update_path(node, n) # [3][4]
            #self.add(n) # [5]
        self.remove(node) # [6]
        
        #self.paths.pop(node.name) # [7]
            
    def update_path(self, n1: Node, n2: Node):
        cost = self.segment_cost(n1, n2)
        new_cost = self.paths[n1.name]['cost'] - self.estimated_cost(n1.name) + self.estimated_cost(n2.name) + cost
        # the path we are trying to add was already visited
        if n2.name in self.paths:
            if new_cost < self.paths[n2.name]['cost']:
                self.paths[n2.name] = {'cost': new_cost, 'visited': self.paths[n1.name]['visited'] + [n2.name] }
                self.add(n2)
                
        else:
            self.paths[n2.name] = {'cost': new_cost, 'visited': self.paths[n1.name]['visited'] + [n2.name] }
            self.add(n2)  
            
def shortest_path(M,start,goal):
    print("shortest path called")
    
    # Initialize our frontier, with the Map and destination (goal)
    frontier = Frontier(M, goal)
    
    # Here we create our first Node to be explored, which is the "start"
    node = Node(start)
    
    # Now we add our only node to the Frontier and to the list of paths
    frontier.add(node)
    frontier.paths[start] = {'cost': 0, 'visited': [start]} 
    
    # The process is launched here by checking the size of the frontier
    # we'll start expanding from the only node 'start'
    node, path = frontier.poll()
    
    frontier.expand(Node(node), path)
    x = 30
    
    while frontier.size() > 0 and x > 0:
        x -= 1
        node, path = frontier.poll()
        
        if frontier.best_path is not None and path['cost'] > frontier.best_path['cost']:
            break
            
        frontier.expand(Node(node), path)
    
    best_path = None
    if frontier.best_path is not None:
        best_path = frontier.best_path['visited']
    return best_path
    
    
