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
    assert gameOfLife.generation == 1
    assert gameOfLife.width == 8
    assert gameOfLife.height == 4
    assert gameOfLife.grid == [[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 1, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]]


def test_game_of_life_parser2():
    input = """
    Generation 2:
    5 7
    .......
    ...*...
    ...*...
    ...*... 
    ....... 
    """

    gameOfLife = GameOfLifeParser().parse(input)
    assert gameOfLife.generation == 2
    assert gameOfLife.width == 7
    assert gameOfLife.height == 5
    assert gameOfLife.grid == [[0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 1, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0]]


def test_broken_generation_is_default_one():
    input = """
    Generation X:
    5 7
    .......
    """
    gameOfLife = GameOfLifeParser().parse(input)
    assert gameOfLife.generation == 1

def test_broken_dimension_is_default():
    input = """
    Generation X:
    5 Y
    .......
    """
    gameOfLife = GameOfLifeParser().parse(input)
    assert gameOfLife.width == 10
    assert gameOfLife.height == 10