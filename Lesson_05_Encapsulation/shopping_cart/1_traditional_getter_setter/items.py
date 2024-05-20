class Item:
    def __init__(self, name, price, quantity=1):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    # Name
    def get_name(self):
        return self.__name
    def set_name(self,name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError('Name must be a string!')
    # Price
    def get_price(self):
        return self.__price
    def set_price(self,price):
        if isinstance(price, (int,float)) and price >= 0:
            self.__price = price
        else:
            raise ValueError('Price must be an integer or float value!')
    # Quantity
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self,quantity):
        if isinstance(quantity, int):
            self.__quantity = quantity
        else:
            raise ValueError('Quantity must be an integer!')
    
    def __str__(self):
        return f"{self.__name} - ${self.__price} x {self.__quantity}"

class DigitalItem(Item):
    def __init__(self, name, price, license_key, quantity=1):
        super().__init__(name, price, quantity)
        self.__license_key = license_key
    
    def __str__(self):
        return super().__str__() + f" - License Key: {self.__license_key}"

class PerishableItem(Item):
    def __init__(self, name, price, expiration_date, quantity=1):
        super().__init__(name, price, quantity)
        self.__expiration_date = expiration_date
    
    def __str__(self):
        return super().__str__() + f" - Expiration Date: {self.__expiration_date}"
