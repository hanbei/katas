# -*- coding: utf-8 -*-
from katas.gildedrose import *


def test_normal_item():
    items = [
        NormalItem("foo", 0, 0),
        NormalItem("foo", 1, 1),
        NormalItem("foo", 1, 2),
        NormalItem("foo", 1, -1),
    ]
    update_quality(items)

    assert_item(items[0], sell_in=-1, quality=0)
    assert_item(items[1], sell_in=0, quality=0)
    assert_item(items[2], sell_in=0, quality=1)
    assert_item(items[3], sell_in=0, quality=0)


def test_decays_twice_as_fast_after_sell_date():
    items = [
        NormalItem("foo", 0, 5),
        NormalItem("foo", 1, 5),
    ]
    update_quality(items)

    assert_item(items[0], sell_in=-1, quality=3)
    assert_item(items[1], sell_in=0, quality=4)


def assert_item(item, name="foo", sell_in=-1, quality=0):
    assert name == item.name
    assert quality == item.quality
    assert sell_in == item.sell_in


def update_quality(items):
    for item in items:
        item.update_quality()
