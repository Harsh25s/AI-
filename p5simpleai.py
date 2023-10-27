# 1. **Uninformed Search (Breadth-First Search):**
#  Problem: Find the shortest path from the start node to the goal node on a grid.

   
   from simpleai.search import breadth_first
   
   # Define the problem
   start = (0, 0)
   goal = (3, 3)
   
   def actions(state):
       x, y = state
       possible_actions = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
       return [(x, y) for (x, y) in possible_actions if 0 <= x < 4 and 0 <= y < 4]
   
   def is_goal(state):
       return state == goal
   
   def cost(state1, action, state2):
       return 1
   
   problem = simpleai.search.SearchProblem(start, is_goal, actions, cost)
   
   # Solve using Breadth-First Search
   result = simpleai.search.breadth_first(problem)
   print("Path:", result.path())
   

# 2. **Informed Search (A* Search):**

#   Problem: Find the shortest path from the start node to the goal node on a weighted grid using A* search.


   from simpleai.search import astar, SearchProblem
   
   # Define the problem
   start = (0, 0)
   goal = (3, 3)
   grid = [
       [1, 2, 1, 3],
       [2, 4, 2, 3],
       [1, 1, 2, 3],
       [1, 2, 2, 3]
   ]
   
   def heuristic(state):
       x, y = state
       return abs(x - goal[0]) + abs(y - goal[1])
   
   def is_goal(state):
       return state == goal
   
   def cost(state1, action, state2):
       return grid[state2[0]][state2[1]]
   
   def actions(state):
       x, y = state
       possible_actions = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
       return [(x, y) for (x, y) in possible_actions if 0 <= x < 4 and 0 <= y < 4]
   
   problem = SearchProblem(start, is_goal, actions, cost)
   
   # Solve using A* Search
   result = astar(problem, graph_search=True, heuristic=heuristic)
   print("Path:", result.path())
   

# 3. **Constraint Satisfaction Problem (CSP):**

#   Problem: Solve a CSP where variables need to be assigned values from a domain while satisfying certain constraints.

   
   from simpleai.search import CspProblem, backtrack
   
   # Define the CSP
   variables = ('A', 'B', 'C')
   domains = {
       'A': [1, 2, 3],
       'B': [1, 2, 3],
       'C': [1, 2, 3]
   }
   
   def constraints(A, a, B, b):
       return a != b
   
   csp = CspProblem(variables, domains, constraints)
   
   # Solve using Backtracking
   result = backtrack(csp)
   print("Solution:", result)
   

# Make sure to check the latest documentation for `simpleai` as the library 
