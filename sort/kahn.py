# Kahn's algogithm for topological sorting
"""
The overall time complexity of the current implementation of Kahn's algorithm 
for topological sorting is O(V + E), where V is the number of vertices (nodes) 
and E is the number of edges in the graph.
"""
from collections import defaultdict, deque


def topological_sort(graph):
    # Count the in-degree of each node
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # Initialize the queue with nodes that have no in-degree
    queue = deque([u for u in graph if in_degree[u] == 0])

    # Initialize the result
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)

        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Check if there is a cycle
    if len(result) != len(graph):
        return None

    return result


# Add tests
graph = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D"],
    "D": []
}

assert topological_sort(graph) == ["A", "B", "C", "D"]
