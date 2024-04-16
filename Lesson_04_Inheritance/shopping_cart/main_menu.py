from shopping_cart import ShoppingCart
from itemFactory import ItemFactory

def main():
    cart = ShoppingCart()
    # print(cart)
    while True:
        print('\n---Shopping Cart Menu ---')
        print('0. Exit\n1. Display Cart\n2. Add items\n3. Remove item\n4. Check out')

        choice = input('Please choose an option: ')
        if choice == '0':
            print('Thank you for shopping')
            print(repr(cart))
            break
        elif choice == '1':
            print(cart)
        elif choice == '2':
            item_type = input('Enter the item type: ')
            name = input('Enter the item name: ')
            price = float(input('Enter the price: '))
            quantity = int(input('Enter quantity: '))
            if item_type == 'digital':
                license_key = input('Enter the license ky')
                item = ItemFactory.create_item(item_type, name, price, license_key, quantity)
            elif item_type == 'perishable':
                expiration_date = input('Enter the expiration date: ')
                item = ItemFactory.create_item(item_type, name, price, expiration_date, quantity)
            else:
                item = ItemFactory.create_item(item_type, name, price, quantity)
            cart.add_items(item)
        elif choice == '3':
            item = input('Enter the item name to remove: ')
            quantity = int(input('Enter the quantity being removed: '))
            cart.remove_item(item, quantity)
        elif choice == '4':
            cart.check_out()
        else:
            print('Invalid Option! Try again!')

if __name__ == '__main__':
    main()