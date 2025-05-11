import heapq
from constants import initial_state, target_state
from helpers import get_adjacent_states, calculate_heuristic

def a_star():
    pq = [(calculate_heuristic(initial_state), 0, initial_state, [])]
    visited = set()
    while pq:
        est_total, cost, state, path = heapq.heappop(pq)
        if state == target_state:
            return path + [state]
        key = tuple(tuple(row) for row in state)
        if key in visited:
            continue
        visited.add(key)
        for neighbor in get_adjacent_states(state):
            new_cost = cost + 1
            est_total = new_cost + calculate_heuristic(neighbor)
            heapq.heappush(pq, (est_total, new_cost, neighbor, path + [state]))
    return None
