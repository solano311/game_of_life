from typing import Callable, Generator


class Grid:
    def __init__(self, cols: int, rows: int) -> None:
        self.cols = cols
        self.rows = rows
        self._grid = [[False for _ in range(cols)] for _ in range(rows)]
        self.generation = 0

    def __iter__(self) -> Generator[tuple[int, int, bool], None, None]:
        for y in range(self.rows):
            for x in range(self.cols):
                yield x, y, self._grid[y][x]

    def __str__(self) -> str:
        text = ""
        prev_y = -1
        for x, y, alive in self:
            cell = "X" if alive else "O"
            if y != prev_y:  # new line
                text += f"\n ({y}): {cell} "
            else:
                text += f"{cell} "
            prev_y = y
        return text.rstrip()

    def kill_cell(self, x: int, y: int) -> None:
        self._grid[y][x] = False

    def birth_cell(self, x: int, y: int) -> None:
        self._grid[y][x] = True

    def set_cell(self, x: int, y: int, state: bool) -> None:
        self._grid[y][x] = state

    def flip_cell(self, x: int, y: int) -> None:
        self._grid[y][x] = not self._grid[y][x]

    def is_alive(self, x: int, y: int) -> bool:
        return self._grid[y][x]

    def count_living_dead(self) -> tuple[int, int]:
        count = 0
        for _, _, alive in self:
            count += 1 if alive else 0
        return count, self.rows * self.cols - count

    def count_living_neighbours(self, x: int, y: int) -> int:
        c = 0
        for xx in range(x - 1, x + 2):
            for yy in range(y - 1, y + 2):
                if (xx, yy) != (x, y):  # do not count itself
                    c += 1 if self._grid[yy % self.rows][xx % self.cols] else 0
        return c

    def next_gen(self, rules: list[Callable]):
        self.generation += 1
        changes: list[tuple[int, int]] = []
        for x, y, cell in self:
            n = self.count_living_neighbours(x, y)
            for r in rules:
                if cell != r(cell, n):  # cell has changed state
                    changes.append((x, y))
        for x, y in changes:
            self.flip_cell(x, y)
