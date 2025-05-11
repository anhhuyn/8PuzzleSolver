import heapq
from constants import initial_state, target_state
from helpers import get_adjacent_states, calculate_heuristic

def greedy_search():
    pq = [(calculate_heuristic(initial_state), initial_state, [])]
    visited = set()
    while pq:
        _, state, path = heapq.heappop(pq)
        if state == target_state:
            return path + [state]
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for neighbor in get_adjacent_states(state):
            heapq.heappush(pq, (calculate_heuristic(neighbor), neighbor, path + [state]))
    return None
