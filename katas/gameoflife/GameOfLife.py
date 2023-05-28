from dataclasses import dataclass


class Grid():

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = [0 for x in range(width * height)]

    def get(self, x: int, y: int) -> int:
        value = self.grid[self._address(x, y)]
        return value

    def set(self, x: int, y: int) -> None:
        self.grid[self._address(x, y)] = 1

    def count_neighbours(self, x: int, y: int) -> int:
        address = self._address(x, y)
        start = max(0, address - 4)
        end = min(self.width * self.height, address + 5)
        return sum(self.grid[start:end]) - self.grid[address]

    def _address(self, x: int, y: int) -> int:
        result = x * self.width + y
        return result


@dataclass
class GameOfLife():

    def __init__(self, generation: int = 1, width: int = 10, height: int = 10, grid: list[list[int]] = None):
        self.generation = generation
        self.width = width
        self.height = height
        self.grid = grid or [[0 for x in range(width)] for y in range(height)]

    def update(self):
        pass

    def _count_neighbours(self, i: int, j: int) -> int:
        pass
