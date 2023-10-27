from collections import deque

# Define the initial and goal states
initial_state = (3, 3, 1)  # (missionaries on left, cannibals on left, boat position)
goal_state = (0, 0, 0)

# Define the valid state-checking function
def is_valid_state(state):
    missionaries_left, cannibals_left, boat = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    # Check if the number of cannibals doesn't outnumber missionaries on both banks
    if (missionaries_left < cannibals_left and missionaries_left > 0) or \
       (missionaries_right < cannibals_right and missionaries_right > 0):
        return False

    # Check if the number of missionaries and cannibals are within the valid range
    if 0 <= missionaries_left <= 3 and 0 <= cannibals_left <= 3:
        return True

    return False

# Define the function to generate valid next states
def generate_next_states(state):
    next_states = []
    missionaries_left, cannibals_left, boat = state

    # Possible combinations of people to move
    moves = [(1, 0), (0, 1), (2, 0), (0, 2), (1, 1)]

    for move in moves:
        missionaries_delta, cannibals_delta = move

        if boat == 1:
            new_state = (missionaries_left - missionaries_delta, cannibals_left - cannibals_delta, 0)
        else:
            new_state = (missionaries_left + missionaries_delta, cannibals_left + cannibals_delta, 1)

        if is_valid_state(new_state):
            next_states.append(new_state)

    return next_states

# Solve the problem using BFS
def solve_missionaries_and_cannibals(initial_state, goal_state):
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        visited.add(current_state)

        if current_state == goal_state:
            return path

        for next_state in generate_next_states(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Find and print the solution
solution = solve_missionaries_and_cannibals(initial_state, goal_state)

if solution:
    print("Solution found:")
    for i, state in enumerate(solution):
        missionaries_left, cannibals_left, boat = state
        missionaries_right = 3 - missionaries_left
        cannibals_right = 3 - cannibals_left
        print(f"Step {i + 1}: {missionaries_left}M-{cannibals_left}C-{1 if boat == 1 else 0}B -> {missionaries_right}M-{cannibals_right}C-{0 if boat == 1 else 1}B")
else:
    print("No solution found.")
