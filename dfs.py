# Define the graph as an adjacency list 
graph = { 
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F'], 
    'D': [], 
    'E': ['F'], 
    'F': [] 
}

# Define the DFS function 
def dfs(graph, start, visited=None): 
    if visited is None: 
        visited = set() 
    visited.add(start)  # mark the node as visited 
    for neighbor in graph[start]: 
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # recursively visit unvisited neighbors 
    return visited 

# Call the DFS function with starting node 'A' 
print(dfs(graph, 'A'))
