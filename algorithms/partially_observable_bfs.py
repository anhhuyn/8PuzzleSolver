import random
from collections import deque
from constants import initial_state, target_state, GRID_SIZE
from helpers import get_adjacent_states, create_random_state

def partially_observable_bfs(max_steps=10000, num_initial_beliefs=50):
    def get_partial_observation(state):
        obs = [[-1] * GRID_SIZE for _ in range(GRID_SIZE)]
        for i in range(2):
            for j in range(2):
                obs[i][j] = state[i][j]
        return tuple(tuple(row) for row in obs)

    # Đảm bảo initial_state nằm trong belief
    belief = [initial_state] + [create_random_state() for _ in range(num_initial_beliefs - 1)]
    queue = deque([(state, []) for state in belief])
    visited = set()
    steps = 0

    while queue and steps < max_steps:
        state, path = queue.popleft()

        if state == target_state:
            return path + [state]

        obs = get_partial_observation(state)
        # Gộp quan sát + trạng thái cuối path để tránh bỏ sót đường đi hợp lệ
        visit_key = (obs, tuple(tuple(row) for row in state))
        if visit_key in visited:
            continue
        visited.add(visit_key)

        for neighbor in get_adjacent_states(state):
            queue.append((neighbor, path + [state]))

        steps += 1

    return None
