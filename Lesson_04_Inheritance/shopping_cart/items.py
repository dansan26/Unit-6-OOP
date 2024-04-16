class Item:
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        return f"{self.name} - ${self.price} x {self.quantity}"
    

class DigitalItem(Item):
    def __init__(self, name, price, liscense_key, quantity=1):
        super().__init__(name, price, quantity)
        self.liscense_key = liscense_key
    def __str__(self):
        return super.__str__() + f" - Liscense Key: {self.liscense_key}"

class PerishableItem(Item):
    def __init__(self, name, price, expiration_date, quantity=1):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
    def __str__(self):
        return super.__str__() + f" - Expires on: {self.expiration_date}"