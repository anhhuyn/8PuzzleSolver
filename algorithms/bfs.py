from collections import deque
from constants import initial_state, target_state
from helpers import get_adjacent_states

def breadth_first_search():
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == target_state:
            return path + [state]
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for neighbor in get_adjacent_states(state):
            queue.append((neighbor, path + [state]))
    return None
