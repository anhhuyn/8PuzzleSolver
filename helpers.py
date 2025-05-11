# helpers.py
from constants import GRID_SIZE,  target_state
import random

def locate_blank(state):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if state[i][j] == 0:
                return i, j

def get_adjacent_states(state):
    x, y = locate_blank(state)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def calculate_heuristic(state):
    distance = 0
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            value = state[i][j]
            if value != 0:
                target_x = (value - 1) // GRID_SIZE
                target_y = (value - 1) % GRID_SIZE
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

def is_goal(state):
    return state == target_state

def create_random_state():
    """
    Tạo một trạng thái ngẫu nhiên cho bài toán 8-puzzle.
    Trạng thái là một danh sách 3x3 chứa các con số từ 0 đến 8.
    """
    numbers = list(range(9))  # Danh sách các số từ 0 đến 8
    random.shuffle(numbers)  # Xáo trộn danh sách để tạo trạng thái ngẫu nhiên
    return [numbers[i:i+3] for i in range(0, 9, 3)]  # Chuyển thành ma trận 3x3
