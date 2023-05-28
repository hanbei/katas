from katas.gameoflife.GameOfLife import Grid


def test_grid():
    width = 3
    height = 6

    grid = Grid(width, height)

    for i in range(0, height):
        for j in range(0, width):
            grid.set(i, j)
            assert grid.get(i, j) == 1

    assert sum(grid.grid) == height * width


def test_neighbours():
    grid = Grid(3, 3)

    assert grid.count_neighbours(1, 1) == 0

    grid.set(0, 0)
    assert grid.count_neighbours(1, 1) == 1
    grid.set(0, 1)
    assert grid.count_neighbours(1, 1) == 2
    grid.set(0, 2)
    assert grid.count_neighbours(1, 1) == 3

    grid.set(1, 0)
    assert grid.count_neighbours(1, 1) == 4
    grid.set(1, 1)
    assert grid.count_neighbours(1, 1) == 4
    grid.set(1, 2)
    assert grid.count_neighbours(1, 1) == 5

    grid.set(2, 0)
    assert grid.count_neighbours(1, 1) == 6
    grid.set(2, 1)
    assert grid.count_neighbours(1, 1) == 7
    grid.set(2, 2)
    assert grid.count_neighbours(1, 1) == 8
