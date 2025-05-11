import heapq
from constants import initial_state, target_state
from helpers import get_adjacent_states

def uniform_cost_search():
    pq = [(0, initial_state, [])]
    visited = set()
    while pq:
        cost, state, path = heapq.heappop(pq)
        if state == target_state:
            return path + [state]
        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)
        for neighbor in get_adjacent_states(state):
            heapq.heappush(pq, (cost + 1, neighbor, path + [state]))
    return None
