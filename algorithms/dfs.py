from constants import initial_state, target_state
from helpers import get_adjacent_states

def depth_first_search():
    stack = [(initial_state, [])]
    visited = set()
    while stack:
        state, path = stack.pop()
        if state == target_state:
            return path + [state]
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for neighbor in get_adjacent_states(state):
            stack.append((neighbor, path + [state]))
    return None
