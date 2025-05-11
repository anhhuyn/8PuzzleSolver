# constants.py
WIDTH, HEIGHT = 400, 600
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE
FONT_SIZE = 40

# Colors
WHITE = (240, 240, 240)
BLACK = (0, 0, 0)
LIGHT_GREEN = (144, 238, 144)
RED = (255, 69, 0)

# States
#initial_state = [[2, 6, 5], [0, 8, 7], [4, 3, 1]]
initial_state = [[1, 2, 3], [4, 0, 5], [7, 8, 6]]  # solvable DFS

target_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
