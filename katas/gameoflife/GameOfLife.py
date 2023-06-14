from dataclasses import dataclass
from typing import Tuple


class Grid():

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = [0 for x in range(width * height)]

    def get(self, x: int, y: int) -> int:
        return self._get(x, y)

    def lives(self, x: int, y: int) -> None:
        address = self._address(x, y)
        if address != -1:
            self.grid[address] = 1

    def dies(self, x, y):
        self.grid[self._address(x, y)] = 0

    def count_neighbours(self, x: int, y: int) -> int:
        nw = self._get(x + 1, y - 1)
        n = self._get(x, y - 1)
        ne = self._get(x - 1, y - 1)

        sw = self._get(x + 1, y + 1)
        s = self._get(x, y + 1)
        se = self._get(x - 1, y + 1)

        w = self._get(x + 1, y)
        e = self._get(x - 1, y)

        return (nw + n + ne + w + e + sw + se + s)

    def _address(self, x: int, y: int) -> int:
        result = x + y * self.width
        if result < 0 or result >= len(self.grid):
            result = -1
        return result

    def _get(self, x: int, y: int) -> int:
        address = self._address(x, y)
        if address == -1:
            return 0

        value = self.grid[address]
        return value

    def __iter__(self):
        return GridIterator(self)

    def __str__(self) -> str:
        result = ""
        for x in range(0, self.width):
            for y in range(0, self.height):
                if self._get(x, y) == 0:
                    result += "."
                else:
                    result += "*"
            result += "\n"
        return result


class GridIterator:

    def __init__(self, grid: Grid):
        self.grid = grid
        self.x = 0
        self.y = 0

    def __next__(self) -> Tuple[int, int, int]:
        if self.y >= self.grid.height:
            raise StopIteration()

        value = self.grid.get(self.x, self.y)
        old_x = self.x
        old_y = self.y

        self.x = self.x + 1
        if self.x >= self.grid.width:
            self.y = self.y + 1
            self.x = 0

        return old_x, old_y, value


@dataclass
class GameOfLife():

    def __init__(self, generation: int = 1, width: int = 10, height: int = 10, grid: Grid = None):
        self.generation = generation
        self.grid = grid or Grid(width, height)

    def update(self) -> 'GameOfLife':
        new_grid = Grid(self.grid.width, self.grid.height)
        for x, y, cell in self.grid:
            self_alive = cell == 1
            neighbour_count = self.grid.count_neighbours(x, y)
            if self_alive:
                if neighbour_count == 2:
                    new_grid.lives(x, y)
                if neighbour_count == 3:
                    new_grid.lives(x, y)
            else:
                if neighbour_count == 3:
                    new_grid.lives(x, y)

        return GameOfLife(self.generation + 1, self.grid.width, self.grid.height, new_grid)

    def width(self):
        return self.grid.width

    def height(self):
        return self.grid.height
