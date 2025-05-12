import heapq

def astar(start, goal, neighbors_fn, heuristic_fn):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for neighbor in neighbors_fn(current):
            new_cost = cost_so_far[current] + 1  # assuming uniform cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic_fn(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current

    # Reconstruct path
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path, cost_so_far[goal]

# Define a simple graph as an adjacency list
graph = {
    'A': ['B', 'F'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'J'],
    'F': ['A', 'G'],
    'G': ['F', 'I'],


    'I': ['G', 'J'],
    'J': ['E', 'I']
}

# Define neighbors function
def neighbors_fn(node):
    return graph.get(node, [])

# Define heuristic function (straight-line estimated distance to goal)
heuristic_map = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 3,
    'I': 1,
    'J': 0
}

def heuristic_fn(node, goal):
    return heuristic_map.get(node, float('inf'))

# Run A* algorithm
start = 'A'
goal = 'J'
path, cost = astar(start, goal, neighbors_fn, heuristic_fn)

# Output the result
print("Path found:", path)
print("Total cost:", cost)
