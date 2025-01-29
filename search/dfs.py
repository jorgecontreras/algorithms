# DFS
"""
The DFS algorithm is used to traverse or search tree or graph data structures. 
It starts at the root node and explores as far as possible along each branch before backtracking.
"""

graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for adjacent in graph[node]:
            dfs(visited, graph, adjacent)

# Driver Code 
dfs(visited, graph, 'A')