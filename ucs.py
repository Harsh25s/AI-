import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, w):
        if u in self.graph:
            self.graph[u].append((v, w))
        else:
            self.graph[u] = [(v, w)]

    def ucs(self, start, goal):
        priority_queue = [(0, start)]  # (cost, node)
        visited = set()
        while priority_queue:
            cost, node = heapq.heappop(priority_queue)

            if node in visited:
                continue

            visited.add(node)

            if node == goal:
                return cost

            if node in self.graph:
                for neighbor, weight in self.graph[node]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (cost + weight, neighbor))

        return float("inf")  # If goal is not reachable

# Example usage
if __name__ == '__main__':
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'D', 3)
    g.add_edge('C', 'E', 8)
    g.add_edge('D', 'E', 7)
    g.add_edge('E', 'D', 9)

    start_node = 'A'
    goal_node = 'E'
    cost = g.ucs(start_node, goal_node)
    
    if cost != float("inf"):
        print(f"Shortest path cost from {start_node} to {goal_node} is {cost}")
    else:
        print(f"There is no path from {start_node} to {goal_node}")
