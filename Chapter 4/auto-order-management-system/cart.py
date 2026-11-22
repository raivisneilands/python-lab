def view_cart(cart):
    if (not cart):
        print('Cart is empty.')
        return

    print(f'{'Item':<30}{'Price':>12}')

    for item in cart:
        print(f'{cart[item][1]:<30}{cart[item][2]:>12.2f}')

def add_to_cart(item, cart):
    cart[item[1]] = item
    print(f'{item} has been added to cart.')

def remove_from_cart(item, cart):
    cart.pop(item[1])
    print(f'{item[1]} was removed from cart.')

    print('Current cart. Should be empty.')
    view_cart(cart)