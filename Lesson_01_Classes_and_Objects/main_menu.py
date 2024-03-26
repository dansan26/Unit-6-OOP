from shopping_cart import ShoppingCart
def main():
    cart = ShoppingCart()
    # print(cart)
    while True:
        print('\n---Shopping Cart Menu ---')
        print('0. Exit\n1. Display Cart\n2. Add items')

        choice = input('Please choose an option: ')
        if choice == '0':
            print('Thank you for shopping')
            break
        elif choice == '1':
            cart.display_cart()
        elif choice == '2':
            item = input('Enter the item name: ')
            price = float(input('Enter the price: '))
            quantity = int('Enter the quantity: ')
            cart.add_items(item, price, quantity)
        else:
            print('Invalid Option! Try again!')

if __name__ == '__main__':
    main()