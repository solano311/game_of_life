import pygame

from grid import Grid
from init_states import blinker, glider, random_equal_chance, toad
from rules import FULL_RULES

COLOR_BG = (10, 10, 10)
COLOR_GRID = (50, 50, 50)
COLOR_ALIVE = (200, 200, 200)
WINDOW = (1500, 800)
CELL_SIZE = 10
FPS = 60


def main() -> None:
    grid = Grid(WINDOW[0] // CELL_SIZE, WINDOW[1] // CELL_SIZE)
    # glider(grid, 2, 2)
    # random_equal_chance(grid)
    # toad(grid, 40, 40)
    pygame.init()
    clock = pygame.time.Clock()
    scr = pygame.display.set_mode(WINDOW)
    running = True
    paused = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = not running
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

        if pygame.mouse.get_pressed(num_buttons=3)[0]:
            # left mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid.birth_cell(mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)

        if pygame.mouse.get_pressed(num_buttons=3)[2]:
            # right mouse button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid.kill_cell(mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)

        # Draw screen
        scr.fill(COLOR_GRID)
        for x, y, alive in grid:
            color = COLOR_ALIVE if alive else COLOR_BG
            rect = pygame.Rect(
                x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE - 1, CELL_SIZE - 1
            )
            pygame.draw.rect(scr, color, rect)

        # Evolve
        if not paused:
            grid.next_gen(FULL_RULES)

        pygame.display.update()
        clock.tick(FPS)

    print(f"Última geração: {grid.generation}")
    pygame.quit()


if __name__ == "__main__":
    main()
