from constants import initial_state, target_state
from helpers import get_adjacent_states, calculate_heuristic

def steepest_ascent_hill_climbing():
    current_state = initial_state  # Lấy `initial_state` từ constants
    path = [current_state]
    while True:
        neighbors = get_adjacent_states(current_state)
        next_state = min(neighbors, key=lambda state: calculate_heuristic(state))
        if calculate_heuristic(next_state) >= calculate_heuristic(current_state):
            break
        current_state = next_state
        path.append(current_state)
        if current_state == target_state:
            return path
    return None
