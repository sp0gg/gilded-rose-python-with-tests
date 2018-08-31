class GildedRose:
    @staticmethod
    def update_quality(items):
        for item in items:
            item.age()
        return items
