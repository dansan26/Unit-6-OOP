class ShoppingCart:
    def __init__(self):
        self.__items = []
        
    def add_item(self, item):
        self.__items.append(item)
        self.display_cart()

    def remove_item(self, item_name, quantity=1):
        for item in self.__items:
            if item.name == item_name:
                if item.get_quantity() <= quantity:
                    self.__items.remove(item)
                else:
                    # item.quantity -= quantity
                    item.set_quantity(item.get_quantity() - quantity)
                self.display_cart()
                break

    def display_cart(self):
        if not self.__items:
            print("Your cart is empty!")
        else:
            print("Items in your cart:")
            for item in self.__items:
                print(item)
    
    def checkout(self):
        if not self.__items:
            print("Your shopping cart is empty.")
        else:
            total_amount = sum(item.get_price() * item.get_quantity() for item in self.__items)
            print(f"Total amount due: ${total_amount:.2f}")
            print("Thank you for your purchase!")
            self.__items = []

    def __str__(self):
        return "\n".join(str(item) for item in self.__items)

    def __len__(self):
        return len(self.__items)
