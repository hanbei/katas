from katas.bowling2 import parse_game, Frame, Roll


def test_parse_all_strikes():
    game = parse_game("X X X X X X X X X X X X")

    assert game._frames == [Frame(Roll(10))] * 12
    assert game.score() == 300


def test_parse_all_nines():
    game = parse_game("9- 9- 9- 9- 9- 9- 9- 9- 9- 9-")

    assert game._frames == [Frame(Roll(9), Roll(0))] * 10
    assert game.score() == 90


def test_parse_all_spares():
    game = parse_game("5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5")

    rolls = ([Frame(Roll(5), Roll(5))] * 10)
    rolls.append(Frame(Roll(5)))
    assert game._frames == rolls
    assert game.score() == 150


def test_parse_sevens():
    game = parse_game("34 34 34 34 34 34 34 34 34 34")

    assert game._frames == [Frame(Roll(3), Roll(4))] * 10
    assert game.score() == 70


def test_all_misses():
    game = parse_game("-- -- -- -- -- -- -- -- -- --")

    assert game._frames == [Frame(Roll(0), Roll(0))] * 10
    assert game.score() == 0


def test_parse_strike_after_last_split():
    game = parse_game("34 34 34 34 34 34 34 34 34 5/X")

    rolls = ([Frame(Roll(3), Roll(4))] * 9)
    rolls.append(Frame(Roll(5), Roll(5)))
    rolls.append(Frame(Roll(10)))
    assert game._frames == rolls
    assert game.score() == 9 * 7 + 20
