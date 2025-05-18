import random
from constants import initial_state, target_state
from helpers import get_adjacent_states

def state_to_key(state):
    return tuple(tuple(row) for row in state)

def q_learning(episodes=5000, alpha=0.1, gamma=0.9, epsilon=0.1, max_steps=100):
    q_table = {}
    best_path = None

    for episode in range(episodes):
        state = initial_state
        path = []
        for _ in range(max_steps):
            state_key = state_to_key(state)
            if state_key not in q_table:
                q_table[state_key] = {}

            # Các trạng thái liền kề (hành động có thể thực hiện)
            neighbors = get_adjacent_states(state)

            # Epsilon-greedy chọn hành động
            if random.random() < epsilon:
                next_state = random.choice(neighbors)
            else:
                next_state = max(
                    neighbors,
                    key=lambda s: q_table.get(state_to_key(s), {}).get('value', 0),
                    default=random.choice(neighbors)
                )

            next_key = state_to_key(next_state)
            if next_key not in q_table:
                q_table[next_key] = {}

            # Tính reward
            reward = 100 if next_state == target_state else -1

            # Q-learning update rule
            old_q = q_table[state_key].get('value', 0)
            next_max_q = q_table[next_key].get('value', 0)
            q_table[state_key]['value'] = old_q + alpha * (reward + gamma * next_max_q - old_q)

            path.append(state)
            state = next_state

            if state == target_state:
                best_path = path + [state]
                break

    return best_path
