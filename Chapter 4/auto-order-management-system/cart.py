def view_cart(cart):
    if (not cart):
        print('Cart is empty.')
        return

    print(f'{'ID':<6}{'Item':<40}{'Price':<12}{'Quantity':>8}')

    total = 0

    for item in cart:
        print(
            f"{cart[item]['Product'][0]:0>4d}  "
            f"{cart[item]['Product'][1]:<40}"
            f"{cart[item]['Product'][2]:<12.2f}"
            f"{cart[item]['Quantity']:>8}"
        )
        total += cart[item]['Product'][2] * cart[item]['Quantity']

    print(f'\nCart total: {total}\n')
    
def add_to_cart(items, cart):
    for item in items:
        cart[items[item]['Product'][1]] = items[item]
        print(f'{items[item]['Product'][1]} has been added to cart.')

def remove_from_cart(cart):
    item_ids = input('Select the IDs of the products to remove from cart (separated by space, e.g. "1 3 5 8 11 16") (if the quantity of product 3, then all 3 products will be removed from cart): ')
    item_ids = item_ids.split()

    for product in list(cart):
        if (str(cart[product]['Product'][0]) in item_ids):
            print(f'Deleting item with key: {cart[product]['Product'][1]}')
            cart.pop(cart[product]['Product'][1])
