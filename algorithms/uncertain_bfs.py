import random
from collections import deque
from constants import initial_state, target_state
from helpers import get_adjacent_states

def uncertain_bfs(probability=0.8, double_step_chance=0.3):
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

        neighbors = get_adjacent_states(state)
        for neighbor in neighbors:
            if random.random() < probability:
                extended_path = path + [state]

                # Với một xác suất, ta mở rộng luôn bước tiếp theo từ neighbor
                if random.random() < double_step_chance:
                    sub_neighbors = get_adjacent_states(neighbor)
                    for sub_neighbor in sub_neighbors:
                        if random.random() < probability:
                            queue.append((sub_neighbor, extended_path + [neighbor]))
                else:
                    queue.append((neighbor, extended_path))

    return None
