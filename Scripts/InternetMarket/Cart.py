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


    def total_qt(self): # no time for tests
        return sum(qt for item, qt in self._items.items())

    def add(self, item, quantity=1): 
        self._items[item.name] += quantity
        # my tries to solve adding of the similar product
        # if item.name in self._items.keys(): 
        #     self._items[item.name] += quantity
        # else:
        #     self._items[item] += quantity

    @property # iterable for item, qt in cart.items, no tests yet
    def items(self):
        return self._items.items()

    def __len__(self):
        return len(self._items)

