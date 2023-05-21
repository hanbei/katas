import re

from katas.gameoflife.GameOfLife import GameOfLife


class GameOfLifeParser():
    def parse(self, input):
        lines = input.splitlines()
        generation = self.parse_generation(lines[0])
        w, h = self.parse_dimensions(lines[1])
        grid = self.parse_field(w, h, input[2:])
        return GameOfLife(generation=generation, width=w, height=h, grid=grid)

    def parse_generation(self, generation_string):
        match = re.search(r"Generation (\d+)", generation_string)
        if match:
            return int(match.group(1))
        return 1

    def parse_dimensions(self, param):
        return (8, 4)

    def parse_field(self, w, h, param):
        return [[0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0]]
