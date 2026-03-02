class AddOn:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def to_dict(self):
        return self.__dict__
