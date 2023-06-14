import pytest

from katas.gameoflife.parser import GameOfLifeParser


@pytest.fixture
def input():
    return """
    Generation 2:
    5 7
    .......
    ...*...
    ...*...
    ...*... 
    ....... 
    """


def test_iterator(input):
    grid = GameOfLifeParser().parse(input).grid
    for x, y, value in grid:
        if x == 3 and y == 1:
            assert value == 1
        if x == 3 and y == 2:
            assert value == 1
        if x == 3 and y == 3:
            assert value == 1


def test_update(input):
    gameOfLife = GameOfLifeParser().parse(input)
    print(gameOfLife.grid)
    next = gameOfLife.update()
    print(next.grid)
    assert next.grid.grid == [0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0,
                              0, 0, 1, 1, 1, 0, 0,
                              0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0]
