import products
import cart

customer_menu = """
1 - Browse products
2 - View cart
3 - Remove items from cart
4 - Exit
"""

business_menu = """
1 - Inventory
2 - Customers
3 - Orders
4 - Update inventory
5 - Exit
"""

user_cart = {}

def show_menu(user_type, cursor, connection):
    match user_type:
        case 'customer':
            while (True):
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

                        item_ids = input('Select the IDs of the products to add to cart (separated by space, e.g. "1 3 5 8 11 16"): ')
                        item_ids = item_ids.split()

                        items_to_add = {}

                        for product in product_data:
                            if (str(product[0]) in item_ids):
                                items_to_add[product[1]] = product
                                
                        cart.add_to_cart(items_to_add, user_cart)                  

                    case '2':
                        cart.view_cart(user_cart)
                    case '3':
                        cart.remove_from_cart(user_cart)
                    case '4':
                        break
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