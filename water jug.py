from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))  # (jug1, jug2, path)

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))

        path = path + [(jug1, jug2)]

        if jug1 == target or jug2 == target:
            print("Path of states by jugs followed is :")
            for state in path:
                print(f"{state[0]} , {state[1]}")
            return

        # All possible operations
        queue.append((jug1_capacity, jug2, path))  # Fill jug1
        queue.append((jug1, jug2_capacity, path))  # Fill jug2
        queue.append((0, jug2, path))              # Empty jug1
        queue.append((jug1, 0, path))              # Empty jug2

        # Pour jug1 -> jug2
        pour = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour, jug2 + pour, path))

        # Pour jug2 -> jug1
        pour = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour, jug2 - pour, path))

# Example: Jug1 = 4L, Jug2 = 3L, Target = 2L
water_jug_bfs(4, 3, 2)

