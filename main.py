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
    ida_star,
    simple_hill_climbing,
    steepest_ascent_hill_climbing,
    stochastic_hill_climbing,
    simulated_annealing,
    beam_search,
    genetic_algorithm,
    uncertain_bfs, 
    search_with_no_observations,
    partially_observable_bfs
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("8-Puzzle Solver")
    font = pygame.font.Font(None, 30)

    # Tạo thư mục frames để lưu ảnh từng bước
    if not os.path.exists("frames"):
        os.makedirs("frames")

    # Danh sách nút: 2 cột
    button_labels = [
        # Cột trái: thuật toán tìm kiếm không có/có thông tin
        [
            ("IDS", iterative_deepening_search),
            ("BFS", breadth_first_search),
            ("DFS", depth_first_search),
            ("Uniform Cost", uniform_cost_search),
            ("Greedy", greedy_search),
            ("A*", a_star),
            ("IDA*", ida_star),
             ("Partially Observable BFS", partially_observable_bfs)
        ],
        # Cột phải: thuật toán tìm kiếm cục bộ
        [
            ("Simple HC", simple_hill_climbing),
            ("Steepest HC", steepest_ascent_hill_climbing),
            ("Stochastic HC", stochastic_hill_climbing),
            ("SA", simulated_annealing),
            ("Beam Search", lambda: beam_search(5)),
            ("GA", genetic_algorithm),
            ("Uncertain BFS", uncertain_bfs),
            ("No Observations", search_with_no_observations)
        ]
    ]

    while True:
        screen.fill(WHITE)

        # Vẽ các nút cho từng cột
        for col_index, col in enumerate(button_labels):
            for row_index, (label, _) in enumerate(col):
                x = 50 + col_index * 260  # mỗi cột cách nhau 260px
                y = 50 + row_index * 60
                pygame.draw.rect(screen, BLACK, (x, y, 200, 50), 2)
                text = font.render(label, True, BLACK)
                screen.blit(text, (x + 20, y + 15))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for col_index, col in enumerate(button_labels):
                    for row_index, (_, algo) in enumerate(col):
                        btn_x = 50 + col_index * 260
                        btn_y = 50 + row_index * 60
                        if btn_x < x < btn_x + 200 and btn_y < y < btn_y + 50:
                            execute_algorithm(screen, algo)

if __name__ == "__main__":
    main()