# -*- coding: utf-8 -*-

HAND = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
AGED_BRIE = "Aged Brie"


class GildedRose(object):

    def _update_brie(self, item):
        self._increase_quality(item)

        self._update_sell_in(item)

        if item.sell_in < 0:
            self._increase_quality(item)

    def _update_hand(self, item):
        pass

    def _update_backstage_passes(self, item):
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
            if item.quality > 0:
                if item.name != HAND:
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < 11:
                        self._increase_quality(item)
                    if item.sell_in < 6:
                        self._increase_quality(item)
        if item.name != HAND:
            self._update_sell_in(item)
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASSES:
                    if item.quality > 0:
                        if item.name != HAND:
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                self._increase_quality(item)

    def _update_normal(self, item):
        if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
            if item.quality > 0:
                if item.name != HAND:
                    item.quality = item.quality - 1
        else:
            if item.quality < 50:
                item.quality = item.quality + 1
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < 11:
                        self._increase_quality(item)
                    if item.sell_in < 6:
                        self._increase_quality(item)
        if item.name != HAND:
            self._update_sell_in(item)
        if item.sell_in < 0:
            if item.name != AGED_BRIE:
                if item.name != BACKSTAGE_PASSES:
                    if item.quality > 0:
                        if item.name != HAND:
                            item.quality = item.quality - 1
                else:
                    item.quality = item.quality - item.quality
            else:
                self._increase_quality(item)

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item == AGED_BRIE:
                self._update_brie(item)
            elif item == HAND:
                self._update_brie(item)
            elif item == BACKSTAGE_PASSES:
                self._update_brie(item)
            else:
                self._update_normal(item)

    def _increase_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1

    def _update_sell_in(self, item):
        item.sell_in = item.sell_in - 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
