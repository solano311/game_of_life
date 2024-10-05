from random import choice

from grid import Grid


def random_equal_chance(grid: Grid) -> None:
    for x, y, _ in grid:
        grid.set_cell(x, y, choice((True, False)))


def glider(grid: Grid, x: int, y: int) -> None:
    grid.birth_cell(x + 1, y)
    grid.birth_cell(x + 2, y + 1)
    grid.birth_cell(x, y + 2)
    grid.birth_cell(x + 1, y + 2)
    grid.birth_cell(x + 2, y + 2)


def blinker(grid: Grid, x: int, y: int) -> None:
    grid.birth_cell(x, y)
    grid.birth_cell(x + 1, y)
    grid.birth_cell(x + 2, y)


def toad(grid: Grid, x: int, y: int) -> None:
    grid.birth_cell(x + 1, y)
    grid.birth_cell(x + 2, y)
    grid.birth_cell(x + 3, y)
    grid.birth_cell(x, y + 1)
    grid.birth_cell(x + 1, y + 1)
    grid.birth_cell(x + 2, y + 1)
