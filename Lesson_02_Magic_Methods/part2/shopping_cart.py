class ShoppingCart:
    def __init__(self):
        self.items = {}
    # def display_cart(self):
    #     if not self.items:
    #         print('Your shopping cart is empty!')
    #     else:
    #         for item,details in self.items.items():
    #             print(f'{item} - ${details['price']} - Quantity: {details['quantity']}')
    
    def add_items(self, item, price, quantity):
        if item in self.items:
            self.items[item]['quantity'] += quantity
        else:
            self.items[item] = {'price': price, 'quantity': quantity}

    def remove_item(self, item, quantity):
        if item in self.items:
            if quantity <= self.items[item]['quantity']:
                new_quantity = self.items[item]['quantity'] - quantity
                if new_quantity < 1:
                    self.__delitem__(item)
                else:
                    self.items[item]['quantity'] -= quantity
            else:
                print('The quantity you want removed exceeds the quantity you have : Please try again!')
        else:
            print('This item does not exist in the cart')
    
    def check_out(self):
        if not self.items:
            print('Cart is empty - Nothing to check out!')
        else:
            total = 0
            for value in self.items.values():
                total += value['price'] * value['quantity']
        print('Total:', total)
        self.items.clear()
    # ***************** Adding magic methods ********************
    def __str__(self):
        if not self.items:
            return 'Your shopping cart is empty!'
        return "\n".join([f'{item} - ${details['price']} x {details['quantity']}' for item,details in self.items.items()])
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