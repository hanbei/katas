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


    def assert_item(self, item, name="foo", sell_in=-1, quality=0):
        self.assertEquals(name, item.name)
        self.assertEquals(quality, item.quality)
        self.assertEquals(sell_in, item.sell_in)
