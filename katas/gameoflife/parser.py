from katas.gameoflife.GameOfLife import GameOfLife


class GameOfLifeParser():
    def parse(self, input):
        lines = input.splitlines()
        generation = self.parse_generation(lines[0])
        w, h = self.parse_dimensions(lines[1])
        grid = self.parse_field(w, h, input[2:])
        return GameOfLife(width=w, height=h)

    def parse_generation(self, param):
        return 1

    def parse_dimensions(self, param):
        return (4, 8)

    def parse_field(self, w, h, param):
        return []
