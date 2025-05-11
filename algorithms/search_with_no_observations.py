import random
from collections import deque
from constants import initial_state, target_state
from helpers import get_adjacent_states, create_random_state

def search_with_no_observations(probability=0.8, num_initial_beliefs=5):
    # Khởi tạo belief với num_initial_beliefs trạng thái ngẫu nhiên
    belief = [create_random_state() for _ in range(num_initial_beliefs)]
    queue = deque([(state, []) for state in belief])  # Khởi tạo BFS từ các trạng thái belief
    visited = set()

    while queue:
        state, path = queue.popleft()

        # Nếu trạng thái này đã đạt đến trạng thái mục tiêu, trả về đường đi
        if state == target_state:
            return path + [state]

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        # Duyệt qua các trạng thái kế tiếp
        neighbors = get_adjacent_states(state)
        for neighbor in neighbors:
            # Cập nhật belief với xác suất cho các trạng thái kế tiếp
            if random.random() < probability:
                queue.append((neighbor, path + [state]))

    return None
