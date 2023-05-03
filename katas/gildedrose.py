# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1

        quality_decay = 1
        if self.sell_in < 0:
            quality_decay = 2

        self.quality = min(50, max(self.quality - quality_decay, 0))

class ConjuredItem(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1

        quality_decay = 2
        if self.sell_in < 0:
            quality_decay = 4

        self.quality = min(50, max(self.quality - quality_decay, 0))


class LegendaryItem(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        pass


class AgingItem(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1

        quality_increase = 1
        if self.sell_in < 0:
            quality_increase = 2

        self.quality = min(50, max(self.quality + quality_increase, 0))


class BackstagePass(Item):
    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update_quality(self):
        self.sell_in -= 1

        quality_increase = 1
        if self.sell_in < 10:
            quality_increase = 2
        if self.sell_in < 5:
            quality_increase = 3
        if self.sell_in < 0:
            quality_increase = -self.quality

        self.quality = min(50, max(self.quality + quality_increase, 0))
