# DFS

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