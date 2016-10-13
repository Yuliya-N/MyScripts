class Item:
    """
    Basic class for internet market
    """
    optional_fields = {'img', 'description', 'type'}  # set is faster

    def __init__(self, name, price, **kwargs):
        self.name = name
        self.price = price
        for field in Item.optional_fields:
            if field in kwargs:
                setattr(self, field, kwargs[field])

    def __hash__(self):
        # best practice to cortage and hash
        return hash((self.name, self.price))

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price
        # return True - equal to everything
        # return self.__dict__ == other.__dict__


# item1 = Item('name', 10)
# print(hash(item1))

# item2 = Item('name', 10)
# print(hash(item2))
