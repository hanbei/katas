from dataclasses import dataclass


class Grid():

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = [0 for x in range(width * height)]

    def get(self, x: int, y: int) -> int:
        value = self.grid[self._address(x, y)]
        return value

    def make_alive(self, x: int, y: int) -> None:
        self.grid[self._address(x, y)] = 1

    def kill(self, x, y):
        self.grid[self._address(x, y)] = 0

    def count_neighbours(self, x: int, y: int) -> int:
        address = self._address(x, y)
        start = max(0, address - 4)
        end = min(self.width * self.height, address + 5)
        return sum(self.grid[start:end]) - self.grid[address]

    def _address(self, x: int, y: int) -> int:
        # TODO Error Handling for out of bounds
        result = x * self.width + y
        return result


@dataclass
class GameOfLife():

    def __init__(self, generation: int = 1, width: int = 10, height: int = 10, grid: Grid = None):
        self.generation = generation
        self.width = width
        self.height = height
        self.grid = grid or Grid(width, height)

    def update(self):
        pass
