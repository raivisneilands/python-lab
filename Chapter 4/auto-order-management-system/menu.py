import products
import cart

customer_menu = """
1 - Browse products
2 - View cart
"""

business_menu = """
1 - Inventory
2 - Customers
3 - Orders
4 - Update inventory
"""

user_cart = {}

def show_menu(user_type, cursor, connection):
    match user_type:
        case 'customer':
            print(customer_menu)
            user_choice = input('Your selection: ')
            
            match user_choice:
                case '1':
                    product_data = products.get_all(cursor)
                    
                    print(f"{'ID':<6}{'Product':<30}{'Price':>12}{'Stock':>10}")

                    for product in product_data:
                        print(
                            f"{product[0]:0>4d}  "
                            f"{product[1]:<30}"
                            f"{product[2]:>12.2f}"
                            f"{product[3]:>10}"
                        )

                    item_id = int(input('Select the ID of the product to add to cart: '))
                    item = product_data[item_id - 1]

                    cart.add_to_cart(item, user_cart)
                    cart.view_cart(user_cart)
                    cart.remove_from_cart(item, user_cart)

                    print(user_cart)

                case '2':
                    print('see cart contents')
                case _:
                    print('invalid choice')
        
        case 'business':
            print(business_menu)
            user_choice = input('Your selection: ')
            
            match user_choice:
                case '1':
                    print('view inventory')
                case '2':
                    print('view customers')
                case '3':
                    print('view placed orders')
                case '4':
                    print('update inventory stock')
                case _:
                    print('invalid choice')
        
        case _:
            print('Invalid user type')