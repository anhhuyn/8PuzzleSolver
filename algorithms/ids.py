from constants import initial_state, target_state
from helpers import get_adjacent_states

def iterative_deepening_search():
    def depth_limited_search(state, depth, visited):
        if state == target_state:
            return [state]
        if depth == 0:
            return None
        state_tuple = tuple(tuple(row) for row in state)
        visited.add(state_tuple)
        for neighbor in get_adjacent_states(state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                result = depth_limited_search(neighbor, depth - 1, visited)
                if result:
                    return [state] + result
        return None

    for depth in range(50):
        visited = set()
        result = depth_limited_search(initial_state, depth, visited)
        if result:
            return result
    return None
