import pytest

from katas.bowling import Game, Frame


def test_frame_is_strike():
    frame = Frame().first_roll(10)
    assert frame.is_strike() is True
    assert frame.is_spare() is False


def test_spare_frame_is_no_strike():
    frame = Frame().first_roll(8).second_roll(2)
    assert frame.is_strike() is False
    assert frame.is_spare() is True


def test_frame_score():
    assert Frame().first_roll(7).second_roll(2).score() == 9


def test_frame_score_spare():
    assert Frame().first_roll(7).second_roll(3).score() == 10


def test_frame_score_strike():
    assert Frame().first_roll(10).score() == 10


def test_frame_score_with_bonus():
    assert Frame().first_roll(10).add_bonus(5).score() == 15


def test_frame_ended_normal_score():
    assert Frame().first_roll(3).second_roll(0).ended() is True
    assert Frame().first_roll(3).second_roll(4).ended() is True


def test_spare_frame_ended():
    assert Frame().first_roll(3).second_roll(7).ended() is True


def test_frame_with_one_roll_is_not_ended():
    assert Frame().first_roll(3).ended() is False


def test_strike_frame_ends_after_first_roll():
    assert Frame().first_roll(10).ended() is True


def test_strike_frame_cant_add_more_rolls():
    assert Frame().first_roll(10).second_roll(5).ended() is True
    assert Frame().first_roll(10).second_roll(5).score() == 10
