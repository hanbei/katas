from dataclasses import dataclass


@dataclass
class GameOfLife():

    def __init__(self, width: int = 10, height: int = 10):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(width)] for y in range(height)]

    def update(self):
        pass
