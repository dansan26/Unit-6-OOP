from items import Item, DigitalItem, PerishableItem

class ShoppingCart:
    # Class Variable
    total_carts = 0
    def __init__(self):
        # self.items = {}
        self.items = []
        # Unique ID for each car instance
        self.cart_id = ShoppingCart.total_carts + 1
        # Increment the class variable
        ShoppingCart.total_carts += 1
    def add_items(self, item):
        self.items.append(item)
    def remove_item(self, item_name, quantity=1):
        # self.items = [item for item in self.items if item.name != item_name]
        for item in self.items:
            if item.name == item_name:
                if item.quantity <= quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity
                break
    def check_out(self):
        if not self.items:
            print('Cart is empty - Nothing to check out!')
        else:
            total = 0
            for value in self.items.values():
                total += value['price'] * value['quantity']
        print(f'Total to pay from cart ID - {self.cart_id}: $ {total}')
        self.items.clear()
    # ***************** Adding magic methods ********************
    def __str__(self):
        if not self.items:
            return 'Your shopping cart is empty!'
        print(f'Cart ID: {self.cart_id} contains:')
        return "\n".join([f'{item} - ${details['price']} x {details['quantity']}' for item,details in self.items])
    def __repr__(self):
        return f'{self.__class__.__name__}({self.items})'
    def __len__(self):
        return sum(item['quantity'] for item in self.items.values())
    def __getitem__(self,key):
        return self.items.get(key, {'price': 0, 'quantity': 0})
    def __setitem__(self, key, value):
        self.items[key] = value
    def __delitem__(self, key):
        if key in self.items:
            del self.items[key]
        else:
            raise KeyError(f'The item {key} is not in the cart!')