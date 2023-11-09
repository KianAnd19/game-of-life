import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
FADE_STEPS = 10
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

grid = np.zeros((ROWS, COLS), dtype=int)
fade_grid = np.zeros((ROWS, COLS), dtype=int)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))


def draw_cells():
    for y, row in enumerate(fade_grid):
        for x, cell in enumerate(row):
            if cell > 0:
                # Invert the color intensity: it should be less intense as the cell's fade value decreases
                color_intensity = int(255 * (1 - (cell / FADE_STEPS)))
                color = (color_intensity, color_intensity, color_intensity)  # RGB color from black to white
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))




def update_cells():
    new_grid = grid.copy()
    new_fade_grid = fade_grid.copy()
    for y in range(ROWS):
        for x in range(COLS):
            alive_neighbors = sum(grid[(y + i) % ROWS][(x + j) % COLS] for i in (-1, 0, 1) for j in (-1, 0, 1) if (i, j) != (0, 0))
            if grid[y][x] and not 2 <= alive_neighbors <= 3:
                new_grid[y][x] = 0
                new_fade_grid[y][x] = FADE_STEPS  # Cell starts fading out
            elif not grid[y][x] and alive_neighbors == 3:
                new_grid[y][x] = 1
                new_fade_grid[y][x] = FADE_STEPS  # Cell is born, starts at full intensity
            # Reduce the fade value by 1, to a minimum of 0, for cells that are not alive
            if new_fade_grid[y][x] > 0 and new_grid[y][x] == 0:
                new_fade_grid[y][x] -= 1
            # Keep alive cells at full intensity
            if new_grid[y][x] == 1:
                new_fade_grid[y][x] = FADE_STEPS
    return new_grid, new_fade_grid




running = True
paused = False
while running:
    screen.fill(WHITE)
    draw_cells()
    draw_grid()
    pygame.display.flip()

    if not paused:
        grid, fade_grid = update_cells()


    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            cell_x, cell_y = x // CELL_SIZE, y // CELL_SIZE
            if grid[cell_y][cell_x] == 0:  # If the cell is dead
                grid[cell_y][cell_x] = 1
                fade_grid[cell_y][cell_x] = FADE_STEPS  # Revive the cell with full intensity
            else:  # If the cell is alive
                grid[cell_y][cell_x] = 0
                fade_grid[cell_y][cell_x] = 0  # Immediately set fade to 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
        

pygame.quit()
