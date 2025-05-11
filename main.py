# main.py
import pygame
import os
from constants import WIDTH, HEIGHT, WHITE, BLACK
from game import execute_algorithm
from algorithms import (
    breadth_first_search,
    depth_first_search,
    uniform_cost_search,
    greedy_search,
    a_star,
    iterative_deepening_search,
    ida_star
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("8-Puzzle Solver")
    font = pygame.font.Font(None, 30)

    # Tạo thư mục frames để lưu ảnh từng bước
    if not os.path.exists("frames"):
        os.makedirs("frames")

    button_labels = [
        ("IDS", iterative_deepening_search),
        ("Greedy", greedy_search),
        ("Uniform Cost", uniform_cost_search),
        ("BFS", breadth_first_search),
        ("DFS", depth_first_search),
        ("A*", a_star),
        ("IDA*", ida_star),
    ]

    while True:
        screen.fill(WHITE)

        # Vẽ nút thuật toán
        for idx, (label, _) in enumerate(button_labels):
            pygame.draw.rect(screen, BLACK, (50, 50 + idx * 60, 200, 50), 2)
            text = font.render(label, True, BLACK)
            screen.blit(text, (80, 65 + idx * 60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for idx, (_, algo) in enumerate(button_labels):
                    if 50 < x < 250 and 50 + idx * 60 < y < 100 + idx * 60:
                        # Gọi thực thi thuật toán
                        execute_algorithm(screen, algo)

if __name__ == "__main__":
    result = depth_first_search()
    if result:
        print("Solution found with", len(result)-1, "moves:")
        for step in result:
            for row in step:
                print(row)
            print("-----")
    else:
        print("No solution found.")
    main()
