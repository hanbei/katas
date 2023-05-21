from katas.gameoflife.parser import GameOfLifeParser


def test_game_of_life_parser():
    input = """
    Generation 1:
    4 8
    ........
    ....*...
    ...**...
    ........ 
    """

    gameOfLife = GameOfLifeParser().parse(input)
    assert gameOfLife.width == 8
    assert gameOfLife.height == 4
    assert gameOfLife.grid == [[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]]
