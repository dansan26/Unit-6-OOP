from shopping_cart import ShoppingCart
def main():
    cart = ShoppingCart()
    # print(cart)
    while True:
        print('\n---Shopping Cart Menu ---')
        print('0. Exit\n1. Display Cart\n2. Add items\n3.Remove Item from the Cart\n4. Check out')

        choice = input('Please choose an option: ')
        if choice == '0':
            print('Thank you for shopping')
            break
        elif choice == '1':
            print(cart)
        elif choice == '2':
            item = input('Enter the item name: ')
            price = float(input('Enter the price: '))
            quantity = int(input('Enter the quantity: '))
            cart.add_items(item, price, quantity)
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