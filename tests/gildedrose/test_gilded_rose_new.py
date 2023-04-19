# -*- coding: utf-8 -*-
from katas.gildedrose import *

#
# https://www.youtube.com/watch?v=wGQPqPorLQ4
#

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


def test_conjured_item():
    items = [
        ConjuredItem("foo", 0, 0),
        ConjuredItem("foo", 1, 2),
        ConjuredItem("foo", 1, 2),
        ConjuredItem("foo", 3, 10),
        ConjuredItem("foo", 1, -1),
    ]
    update_quality(items)

    assert_item(items[0], sell_in=-1, quality=0)
    assert_item(items[1], sell_in=0, quality=0)
    assert_item(items[2], sell_in=0, quality=0)
    assert_item(items[3], sell_in=2, quality=8)
    assert_item(items[4], sell_in=0, quality=0)

def test_decays_twice_as_fast_after_sell_date():
    items = [
        NormalItem("foo", 0, 5),
        NormalItem("foo", 1, 5),
    ]
    update_quality(items)

    assert_item(items[0], sell_in=-1, quality=3)
    assert_item(items[1], sell_in=0, quality=4)


def test_legendary_item_never_loses_quality_and_sell_in():
    items = [
        LegendaryItem("Sulfuras, Hand of Ragnaros", 5, 10),
        LegendaryItem("Sulfuras, Hand of Ragnaros", 2, 50),
        LegendaryItem("Sulfuras, Hand of Ragnaros", 1, 2),
        LegendaryItem("Sulfuras, Hand of Ragnaros", -3, -1),
    ]
    update_quality(items)

    assert_item(items[0], "Sulfuras, Hand of Ragnaros", sell_in=5, quality=10)
    assert_item(items[1], "Sulfuras, Hand of Ragnaros", sell_in=2, quality=50)
    assert_item(items[2], "Sulfuras, Hand of Ragnaros", sell_in=1, quality=2)
    assert_item(items[3], "Sulfuras, Hand of Ragnaros", sell_in=-3, quality=-1)


def test_brie_increases_in_quality_but_never_more_than_50():
    items = [
        AgingItem("Aged Brie", 0, 5),
        AgingItem("Aged Brie", 5, 5),
        AgingItem("Aged Brie", 0, 50),
    ]
    update_quality(items)

    assert_item(items[0], "Aged Brie", sell_in=-1, quality=7)
    assert_item(items[1], "Aged Brie", sell_in=4, quality=6)
    assert_item(items[2], "Aged Brie", sell_in=-1, quality=50)


def test_backstage_passes():
    items = [
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 30, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 11, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 7, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 6, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 1, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", 0, 5),
        BackstagePass("Backstage passes to a TAFKAL80ETC concert", -1, 5),
    ]
    update_quality(items)

    assert_item(items[0], "Backstage passes to a TAFKAL80ETC concert", sell_in=29, quality=6)
    assert_item(items[1], "Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=6)
    assert_item(items[2], "Backstage passes to a TAFKAL80ETC concert", sell_in=6, quality=7)
    assert_item(items[3], "Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=7)
    assert_item(items[4], "Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=8)
    assert_item(items[5], "Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=8)
    assert_item(items[6], "Backstage passes to a TAFKAL80ETC concert", sell_in=-1, quality=0)
    assert_item(items[7], "Backstage passes to a TAFKAL80ETC concert", sell_in=-2, quality=0)


def assert_item(item, name="foo", sell_in=-1, quality=0):
    assert name == item.name
    assert quality == item.quality
    assert sell_in == item.sell_in


def update_quality(items):
    for item in items:
        item.update_quality()
