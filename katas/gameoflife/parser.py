import re
from typing import Tuple

from katas.gameoflife.GameOfLife import GameOfLife


class GameOfLifeParser():
    def parse(self, input: str) -> GameOfLife:
        lines = self.parse_lines(input)
        generation = self.parse_generation(lines[0])
        w, h = self.parse_dimensions(lines[1])
        grid = self.parse_field(w, h, input[2:])
        return GameOfLife(generation=generation, width=w, height=h, grid=grid)

    def parse_lines(self, input: str) -> list[str]:
        return list(map(lambda s: s.strip(), input.strip().splitlines()))

    def parse_generation(self, generation_string: str) -> int:
        match = re.search(r"Generation (\d+)", generation_string)
        if match:
            return int(match.group(1))
        return 1

    def parse_dimensions(self, dimension_string: str) -> Tuple[int, int]:
        match = re.search(r"(\d+)\s+(\d+)", dimension_string)
        if match:
            return int(match.group(2)), int(match.group(1))

        return (10, 10)

    def parse_field(self, width: int, height: int, lines: list[str]) -> list[list[int]]:
        result = []

        return result
