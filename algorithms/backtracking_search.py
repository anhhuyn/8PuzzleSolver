# algorithms/backtracking_search.py

from constants import initial_state, target_state
from helpers import get_adjacent_states

def backtracking_search():
    def backtrack(state, path, visited):
        print(f"Visiting state: {state}")  # Debugging line
        if state == target_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            print(f"Already visited: {state}")  # Debugging line
            return None
        visited.add(state_tuple)

        neighbors = get_adjacent_states(state)
        for neighbor in neighbors:
            result = backtrack(neighbor, path + [state], visited)
            if result:
                return result
        return None

    visited = set()
    return backtrack(initial_state, [], visited)
