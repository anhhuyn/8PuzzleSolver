# game.py
import pygame
import time
import os
from PIL import Image

from constants import CELL_SIZE, WIDTH, HEIGHT, WHITE, BLACK, LIGHT_GREEN
from helpers import locate_blank


frame_count = 0
frames = []

def save_frame(screen):
    global frame_count, frames
    if not os.path.exists("frames"):
        os.makedirs("frames")
    filename = f"frames/frame_{frame_count:04d}.png"
    pygame.image.save(screen, filename)
    frames.append(filename)
    frame_count += 1

def make_gif():
    if frames:
        images = [Image.open(f) for f in frames]
        images[0].save("solution.gif", save_all=True, append_images=images[1:], duration=500, loop=0)


def render_grid(screen, state):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 40)
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if value != 0:
                pygame.draw.rect(screen, LIGHT_GREEN, rect)
                text = font.render(str(value), True, BLACK)
                screen.blit(text, (j * CELL_SIZE + CELL_SIZE // 3, i * CELL_SIZE + CELL_SIZE // 4))
            pygame.draw.rect(screen, BLACK, rect, 2)
    pygame.display.flip()

def execute_algorithm(_, algo):  # bỏ screen từ menu
    # Tạo cửa sổ game với kích thước chuẩn
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    start_time = time.time()
    solution = algo()
    end_time = time.time()

    execution_time = end_time - start_time

    if solution:
        for state in solution:
            render_grid(screen, state)
            save_frame(screen)
            time.sleep(0.5)

        blank_x, blank_y = locate_blank(solution[-1])
        menu_rect = pygame.Rect(blank_y * CELL_SIZE, blank_x * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (255, 0, 0), menu_rect)

        font = pygame.font.Font(None, 30)
        text = font.render("Menu", True, (255, 255, 255))
        screen.blit(text, (blank_y * CELL_SIZE + 10, blank_x * CELL_SIZE + 10))

        pygame.draw.rect(screen, (255, 255, 255), (0, HEIGHT - 50, WIDTH, 50))
        time_text = font.render(f"Time: {execution_time:.4f} sec", True, (0, 0, 0))
        step_text = font.render(f"Steps: {len(solution) - 1}", True, (0, 0, 0))  # trừ 1 vì trạng thái ban đầu không tính là bước di chuyển
        screen.blit(time_text, (10, HEIGHT - 40))
        screen.blit(step_text, (200, HEIGHT - 40))


        pygame.display.flip()

        make_gif()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu_rect.collidepoint(event.pos):
                        waiting = False

