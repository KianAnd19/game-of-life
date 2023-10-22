import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

grid = np.zeros((ROWS, COLS), dtype=int)


def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


def draw_cells():
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def update_cells():
    new_grid = grid.copy()
    for y in range(ROWS):
        for x in range(COLS):
            alive_neighbors = sum(grid[(y + i) % ROWS][(x + j) % COLS] for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))
            if grid[y][x] and not 2 <= alive_neighbors <= 3:
                new_grid[y][x] = 0
            elif not grid[y][x] and alive_neighbors == 3:
                new_grid[y][x] = 1
    return new_grid


running = True
paused = False
while running:
    screen.fill(WHITE)
    draw_cells()
    draw_grid()
    pygame.display.flip()

    if not paused:
        grid = update_cells()

    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            grid[y // CELL_SIZE][x // CELL_SIZE] = 1 - grid[y // CELL_SIZE][x // CELL_SIZE]
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
        

pygame.quit()
