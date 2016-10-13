from collections import defaultdict


class Cart:
    def __init__(self, user):
        self.user = user
        self._items = defaultdict(int)

    def total(self):
        # ---solution before optimization
        # sum_ = 0
        # dict.items() returns (key, value); item =key, qt = value
        # for item, qt in self._items.items():
        #     sum_ += item.price * qt
        # ---generator expression
        return sum(item.price * qt for item, qt in self._items.items())

    def total_qt(self):
        return sum(self._items.values())

    def add(self, item, qt=1):
        self._items[item] += qt

    def __iter__(self):
        # cannot return self._items, becasue it cannot give next(self._items)
        return iter(self._items)

    def __len__(self):
        return len(self._items)
