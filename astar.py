import heapq

def astar(graph, start, goal):
    open_list = []  # Priority queue for nodes to be evaluated
    heapq.heappush(open_list, (0, start))  # Start node with cost 0
    came_from = {}  # Keep track of the path

    g_score = {node: float('inf') for node in graph}  # Cost from start along the best known path
    g_score[start] = 0  # Cost from start to start is 0

    f_score = {node: float('inf') for node in graph}  # Estimated total cost from start to goal
    f_score[start] = heuristic(start, goal)

    while open_list:
        current_f, current_node = heapq.heappop(open_list)

        if current_node == goal:
            return reconstruct_path(came_from, current_node)

        for neighbor in graph[current_node]:
            tentative_g_score = g_score[current_node] + graph[current_node][neighbor]

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if neighbor not in [node for _, node in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current_node):
    path = [current_node]
    while current_node in came_from:
        current_node = came_from[current_node]
        path.insert(0, current_node)
    return path

def heuristic(node, goal):
    # You should define your heuristic function here (e.g., Euclidean distance)
    # For a grid, Manhattan distance is often used.
    x1, y1 = node
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)

# Example usage:
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
}

start_node = (0, 0)
goal_node = (1, 1)

path = astar(graph, start_node, goal_node)
if path:
    print("A* Path:", path)
else:
    print("No path found.")
