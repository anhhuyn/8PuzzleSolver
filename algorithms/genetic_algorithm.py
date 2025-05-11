import random
from helpers import calculate_heuristic, is_goal, target_state

def genetic_algorithm(population_size=100, generations=1000, mutation_rate=0.1):
    def create_random_state():
        numbers = list(range(9))
        random.shuffle(numbers)
        return [numbers[i:i + 3] for i in range(0, 9, 3)]

    def fitness(state):
        return calculate_heuristic(state)

    def crossover(parent1, parent2):
        flat1 = sum(parent1, [])
        flat2 = sum(parent2, [])
        cut = random.randint(1, 7)
        child = flat1[:cut] + [n for n in flat2 if n not in flat1[:cut]]
        return [child[i:i + 3] for i in range(0, 9, 3)]

    def mutate(state):
        flat = sum(state, [])
        if random.random() < mutation_rate:
            i, j = random.sample(range(9), 2)
            flat[i], flat[j] = flat[j], flat[i]
        return [flat[i:i + 3] for i in range(0, 9, 3)]

    population = [create_random_state() for _ in range(population_size)]
    best_path = []
    best_state = population[0]

    for generation in range(generations):
        population.sort(key=fitness)

        best_state = population[0]
        best_path.append(best_state)

        if is_goal(best_state):
            return best_path

        next_population = population[:10]

        while len(next_population) < population_size:
            parent1, parent2 = random.sample(population[:50], 2)
            child = mutate(crossover(parent1, parent2))
            next_population.append(child)

        population = next_population

    return best_path
