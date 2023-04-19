# -*- coding: utf-8 -*-
import unittest

from katas.gildedrose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_normal_item(self):
        items = [
            Item("foo", 0, 0),
            Item("foo", 1, 1),
            Item("foo", 1, 2),
            Item("foo", 1, -1),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assert_item(items[0], sell_in=-1, quality=0)
        self.assert_item(items[1], sell_in=0, quality=0)
        self.assert_item(items[2], sell_in=0, quality=1)
        self.assert_item(items[3], sell_in=0, quality=-1)

    def test_decays_twice_as_fast_after_sell_date(self):
        items = [
            Item("foo", 0, 5),
            Item("foo", 1, 5),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assert_item(items[0], sell_in=-1, quality=3)
        self.assert_item(items[1], sell_in=0, quality=4)

    def test_legendary_item_never_loses_quality_and_sell_in(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 5, 10),
            Item("Sulfuras, Hand of Ragnaros", 2, 50),
            Item("Sulfuras, Hand of Ragnaros", 1, 2),
            Item("Sulfuras, Hand of Ragnaros", -3, -1),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assert_item(items[0], "Sulfuras, Hand of Ragnaros", sell_in=5, quality=10)
        self.assert_item(items[1], "Sulfuras, Hand of Ragnaros", sell_in=2, quality=50)
        self.assert_item(items[2], "Sulfuras, Hand of Ragnaros", sell_in=1, quality=2)
        self.assert_item(items[3], "Sulfuras, Hand of Ragnaros", sell_in=-3, quality=-1)

    def test_brie_increases_in_quality_but_never_more_than_50(self):
        items = [
            Item("Aged Brie", 0, 5),
            Item("Aged Brie", 5, 5),
            Item("Aged Brie", 0, 50),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assert_item(items[0], "Aged Brie", sell_in=-1, quality=7)
        self.assert_item(items[1], "Aged Brie", sell_in=4, quality=6)
        self.assert_item(items[2], "Aged Brie", sell_in=-1, quality=50)

    def assert_item(self, item, name="foo", sell_in=-1, quality=0):
        self.assertEqual(name, item.name)
        self.assertEqual(quality, item.quality)
        self.assertEqual(sell_in, item.sell_in)
