class ShoppingCart:
    def __init__(self):
        self.items = {}
    def display_cart(self):
        if not self.items:
            print('Your shopping cart is empty!')
        else:
            pass
    def add_items(self, item, price, quantity):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}