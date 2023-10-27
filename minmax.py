import random

# Create a random graph as an adjacency matrix (representing costs between nodes)
def create_random_graph(num_nodes):
    graph = [[random.randint(1, 10) for _ in range(num_nodes)] for _ in range(num_nodes)]
    return graph

# Minimax algorithm to find the optimal path
def minimax(graph, start, depth, maximizing_player):
    if depth == 0:
        return graph[start][start]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(len(graph[start])):
            if i != start:
                eval = minimax(graph, i, depth - 1, False)
                max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(len(graph[start])):
            if i != start:
                eval = minimax(graph, i, depth - 1, True)
                min_eval = min(min_eval, eval)
        return min_eval

# Find the best path using the Minimax algorithm
def find_best_path(graph):
    best_path = []
    for i in range(len(graph)):
        path_score = minimax(graph, i, 2, False)
        best_path.append((i, path_score))
    
    best_path.sort(key=lambda x: x[1], reverse=True)
    return best_path[0]

# Example usage:
random.seed(1)  # Set a seed for reproducibility
num_nodes = 5
random_graph = create_random_graph(num_nodes)

print("Random Graph:")
for row in random_graph:
    print(row)

best_start_node, best_score = find_best_path(random_graph)
print("\nBest Starting Node:", best_start_node)
print("Best Score (Minimax Value):", best_score)
