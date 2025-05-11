import random
import math
from constants import initial_state, target_state
from helpers import get_adjacent_states, calculate_heuristic

def simulated_annealing():
    current_state = initial_state  
    current_temp = 1000
    cooling_rate = 0.003
    path = [current_state]

    while current_temp > 1:
        neighbors = get_adjacent_states(current_state)
        next_state = random.choice(neighbors)
        delta_e = calculate_heuristic(next_state) - calculate_heuristic(current_state)
        
        if delta_e < 0 or random.random() < math.exp(-delta_e / current_temp):
            current_state = next_state
            path.append(current_state)
            if current_state == target_state:
                return path
        
        current_temp *= 1 - cooling_rate
    return None
