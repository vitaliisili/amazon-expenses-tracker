class Item:
    def __init__(self,
                 name: str = "",
                 purchase_date: str = "",
                 price: float = 0.0,
                 weight: float = 0.0,
                 quantity: int = 0):

        self.name = name
        self.purchase_date = purchase_date
        self.price = price
        self.weight = weight
        self.quantity = quantity

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def purchase_date(self):
        return self._purchase_date

    @purchase_date.setter
    def purchase_date(self, value):
        self._purchase_date = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    def __repr__(self):
        return f"Item({self._name}, {self._purchase_date}, {self._price}, {self._weight}, {self._quantity})"

    def __str__(self):
        return f"Item(name: {self._name}, " \
               f"purchase_date: {self._purchase_date}, " \
               f"price: {self._price}, " \
               f"delivery: {self._weight}, " \
               f"quantity: {self._quantity})"
