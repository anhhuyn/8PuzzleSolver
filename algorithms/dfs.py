from collections import deque
from constants import initial_state, target_state
from helpers import get_adjacent_states

def depth_first_search(depth_limit=15):
    stack = [(initial_state, [], 0)]  # (trạng thái hiện tại, đường đi, độ sâu)
    visited = set()

    while stack:
        state, path, depth = stack.pop()

        if state == target_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if depth_limit is None or depth < depth_limit:
            for neighbor in get_adjacent_states(state):
                neighbor_tuple = tuple(tuple(row) for row in neighbor)
                if neighbor_tuple not in visited:
                    stack.append((neighbor, path + [state], depth + 1))

    return None
