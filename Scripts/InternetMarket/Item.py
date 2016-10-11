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

    def __eq__(self, other):
       return self.__dict__ == other.__dict__
