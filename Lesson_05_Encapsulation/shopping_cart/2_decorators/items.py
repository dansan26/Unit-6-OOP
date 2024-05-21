class Item:
    def __init__(self, name, price, quantity=1):
        self.__name = name
        self.__price = price
        self.__quantity = quantity
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if isinstance(value, str):
            self.__name = value
        else:
            raise ValueError('Please enter a string!')
    
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self,value):
        if isinstance(value, (int,float)) and value >= 0:
            self.__price = value
        else:
            raise ValueError('Price must be a non-negative number')

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self,value):
        if isinstance(value, int) and value >= 0:
            self.__quantity = value
        else:
            raise ValueError('Quantity must be a non-negative integer')
        
    def __str__(self):
        return f"{self.__name} - ${self.__price} x {self.__quantity}"

class DigitalItem(Item):
    def __init__(self, name, price, license_key, quantity=1):
        super().__init__(name, price, quantity)
        self.__license_key = license_key
    @property
    def license_key(self):
        return self.__license_key
    
    def __str__(self):
        return super().__str__() + f" - License Key: {self.__license_key}"

class PerishableItem(Item):
    def __init__(self, name, price, expiration_date, quantity=1):
        super().__init__(name, price, quantity)
        self.__expiration_date = expiration_date
    @property
    def expiration_date(self):
        return self.__expiration_date
    
    def __str__(self):
        return super().__str__() + f" - Expiration Date: {self.__expiration_date}"
