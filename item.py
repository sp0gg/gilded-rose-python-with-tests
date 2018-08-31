class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality


class RegularItem(Item):
    def __init__(self, *args):
        super(RegularItem, self).__init__(*args)
        self.QUALITY_RATE = -1
        self.SELL_IN_RATE = -1

    def age(self):
        self._add_sell_in(self.SELL_IN_RATE)
        self._add_quality(self._get_quality_rate())

    def _add_sell_in(self, amount):
        self.sell_in = self.sell_in + amount

    def _add_quality(self, amount):
        new_quality = self.quality + amount
        self.quality = new_quality if new_quality < 50 else 50

    def _get_quality_rate(self):
        return self.QUALITY_RATE if self.sell_in > 0 else self.QUALITY_RATE * 2


class ImprovingItem(RegularItem):
    def __init__(self, *args):
        super(ImprovingItem, self).__init__(*args)
        self.QUALITY_RATE = 1

    def _get_quality_rate(self):
        if self.sell_in > 10:
            return self.QUALITY_RATE
        if self.sell_in > 5:
            return self.QUALITY_RATE * 2
        if self.sell_in > 0:
            return self.QUALITY_RATE * 3
        return self.quality * -1


class LegendaryItem(RegularItem):
    def __init__(self, *args):
        super(LegendaryItem, self).__init__(*args)
        self.SELL_IN_RATE = 0

    def _add_quality(self, amount):
        pass


class ConjuredItem(RegularItem):
    def __init__(self, *args):
        super(ConjuredItem, self).__init__(*args)
        self.QUALITY_RATE = self.QUALITY_RATE * 2
