import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        (cost, node, path) = heapq.heappop(queue)

        if node in visited:
            continue
        visited.add(node)

        if node == end:
            return path

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return None

# Example weighted graph
graph = {
    'A': [('B', 2), ('F', 3)],
    'B': [('A', 2), ('C', 4)],
    'C': [('B', 4), ('D', 1)],
    'D': [('C', 1), ('E', 2)],
    'E': [('D', 2), ('J', 8)],
    'F': [('A', 3), ('G', 1)],
    'G': [('F', 1), ('I', 2)],
    'I': [('G', 2), ('J', 1)],
    'J': [('I', 1), ('E', 8)]
}

start_node = 'A'
end_node = 'J'

path = dijkstra(graph, start_node, end_node)

if path:
    print("Path found:", path)
else:
    print("No path found.")
