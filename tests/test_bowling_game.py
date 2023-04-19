import pytest

from katas.bowling import Game, Frame


@pytest.fixture
def game() -> Game:
    return Game()


def test_game_score_after_no_pins(game: Game):
    assert game.score() == 0


def test_game_score_after_first_two_rolls(game: Game):
    game.roll(5)
    game.roll(4)
    assert game.score() == 9


def test_game_score_after_first_two_frames(game: Game):
    game.roll(5)
    game.roll(4)
    assert game.score() == 9
    game.roll(4)
    game.roll(3)
    assert game.score() == 9 + 7


def test_spare_score(game: Game):
    game.roll(3)
    game.roll(7)
    game.roll(4)
    game.roll(3)
    assert game.score() == 10 + 4 + 7


def test_strike_score(game: Game):
    game.roll(10)
    game.roll(3)
    game.roll(3)
    assert game.score() == (10 + 6) + 6


def test_strike_ends_frame(game: Game):
    game.roll(10)
    game.roll(10)
    assert len(game.frames) == 2
    assert game.score() == 30


def test_no_more_than_10_frames_allowed(game: Game):
    for i in range(1, 100):
        game.roll(1)
    assert game.score() == 20


def test_perfect_game(game: Game):
    for i in range(1, 20):
        game.roll(10)
    assert game.score() == 300
