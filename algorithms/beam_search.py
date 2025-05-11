from helpers import get_adjacent_states, calculate_heuristic
from collections import deque
from constants import target_state, initial_state

def beam_search(beam_width=5):
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        states = [queue.popleft() for _ in range(min(len(queue), beam_width))]
        next_states = []
        for state, path in states:
            if state == target_state:
                return path + [state]
            state_tuple = tuple(tuple(row) for row in state)
            if state_tuple in visited:
                continue
            visited.add(state_tuple)
            neighbors = get_adjacent_states(state)
            for neighbor in neighbors:
                next_states.append((neighbor, path + [state]))
        next_states.sort(key=lambda x: calculate_heuristic(x[0]))
        queue.extend(next_states[:beam_width])
    return None
