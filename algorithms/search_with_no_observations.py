import random
from collections import deque
from constants import initial_state, target_state
from helpers import get_adjacent_states, create_random_state

def search_with_no_observations(probability=0.8, num_initial_beliefs=5):
    belief = [create_random_state() for _ in range(num_initial_beliefs)]
    queue = deque([(state, []) for state in belief]) 
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == target_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        neighbors = get_adjacent_states(state)
        for neighbor in neighbors:
            if random.random() < probability:
                queue.append((neighbor, path + [state]))

    return None
