import pygame
import numpy as np

# Initialize pygame
pygame.init()



# Constants
WIDTH, HEIGHT = 800, 800
CELL_SIZE = 20
FADE_STEPS = 20  # Number of steps it takes for a cell to fade out
ROWS, COLS = HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE

# Adjust the HEIGHT to include space for the title
TITLE_HEIGHT = 60  # Height for the title space
HEIGHT = 800 + TITLE_HEIGHT
ROWS = (HEIGHT - TITLE_HEIGHT) // CELL_SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constants for the Title
title_font = pygame.font.SysFont("Arial", 48)
title_surface = title_font.render("Game of Life", True, BLACK)
title_rect = title_surface.get_rect(center=(WIDTH // 2, title_font.get_height() // 2))



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

grid = np.zeros((ROWS, COLS), dtype=int)
fade_grid = np.zeros((ROWS, COLS), dtype=int)

#Draws the gird
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, TITLE_HEIGHT), (x, HEIGHT))
    for y in range(TITLE_HEIGHT, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WIDTH, y))

# Colours the cells
def draw_cells():
    for y, row in enumerate(fade_grid):
        for x, cell in enumerate(row):
            if cell > 0:
                color_intensity = int(255 * (1 - (cell / FADE_STEPS)))
                color = (color_intensity, color_intensity, color_intensity)
                pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE + TITLE_HEIGHT, CELL_SIZE, CELL_SIZE))


#Checks if condotions hold for all the cells
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



# This is the main game loop
running = True
paused = False
while running:
    screen.fill(WHITE)
    draw_cells()
    draw_grid()

    screen.blit(title_surface, title_rect)

    pygame.display.flip()

    if not paused:
        grid, fade_grid = update_cells()


    pygame.time.wait(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            # Check if the click is below the title area
            if y >= TITLE_HEIGHT:
                # Adjust cell_y to account for the title area
                cell_x, cell_y = x // CELL_SIZE, (y - TITLE_HEIGHT) // CELL_SIZE
                # Ensure the click is within the grid bounds
                if 0 <= cell_x < COLS and 0 <= cell_y < ROWS:
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
