from collections import defaultdict


class Cart:
    def __init__(self, user):
        self.user = user
        self._items = defaultdict(int)

    def total(self):
        # sum_ = 0
        # dict.items() returns (key, value); item =key, qt = value
        # for item, qt in self._items.items():
        #     sum_ += item.price * qt
        # generator expression
        return sum(item.price * qt for item, qt in self._items.items())

    def add(self, item, quantity=1):
        self._items[item] += quantity
