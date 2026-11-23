def view_cart(cart):
    if (not cart):
        print('Cart is empty.')
        return

    print(f'{'ID':<6}{'Item':<30}{'Price':>12}')

    total = 0

    for item in cart:
        print(
            f"{cart[item][0]:0>4d}  "
            f"{cart[item][1]:<30}"
            f"{cart[item][2]:>12.2f}"
        )
        total += cart[item][2]

    print(f'\nCart total: {total}\n')
    
def add_to_cart(items, cart):
    for item in items:
        cart[items[item][1]] = items[item]
        print(f'{items[item][1]} has been added to cart.')

def remove_from_cart(cart):
    item_ids = input('Select the IDs of the products to remove from cart (separated by space, e.g. "1 3 5 8 11 16"): ')
    item_ids = item_ids.split()

    for product in list(cart):
        if (str(cart[product][0]) in item_ids):
            print(f'Deleting item with key: {cart[product][1]}')
            cart.pop(cart[product][1])
