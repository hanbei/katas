from dataclasses import dataclass


@dataclass
class GameOfLife():

    def __init__(self, width: int = 10, height: int = 10, grid: list[list[int]] = None):
        self.width = width
        self.height = height
        self.grid = grid or [[0 for x in range(width)] for y in range(height)]

    def update(self):
        pass
