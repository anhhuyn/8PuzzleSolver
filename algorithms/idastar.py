from constants import initial_state, target_state
from helpers import get_adjacent_states, calculate_heuristic

def ida_star():
    def dfs(state, g, bound, path):
        f = g + calculate_heuristic(state)
        if f > bound:
            return f, None
        if state == target_state:
            return f, path + [state]
        min_bound = float('inf')
        for neighbor in get_adjacent_states(state):
            result_bound, result_path = dfs(neighbor, g + 1, bound, path + [state])
            if result_path:
                return result_bound, result_path
            min_bound = min(min_bound, result_bound)
        return min_bound, None

    bound = calculate_heuristic(initial_state)
    while True:
        result_bound, result_path = dfs(initial_state, 0, bound, [])
        if result_path:
            return result_path
        bound = result_bound
        if bound == float('inf'):
            return None
