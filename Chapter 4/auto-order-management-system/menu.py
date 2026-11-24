import products
import cart
import webhook
import business

customer_menu = """
1 - Browse products
2 - View cart
3 - Remove items from cart
4 - Confirm and place order
5 - Exit
"""

business_menu = """
1 - Inventory
2 - View customers
3 - Update inventory
4 - View inventory changes
5 - View placed orders
6 - Exit
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
                        cart.view_cart(user_cart)
                        confirmation = input('Are you sure you want to place the order with these items? y/n: ')
                        if (confirmation.lower() == 'y'):
                            webhook.send(user_cart)
                        else:
                            print('Cancelling the order. Returning.')
                    case '5':
                        break
                    case _:
                        print('Invalid choice')
        
        case 'business':
            while (True):
                print(business_menu)
                user_choice = input('Your selection: ')
                
                match user_choice:
                    case '1':
                        products.get_all(cursor)
                    case '2':
                        business.view_customers(cursor)
                    case '3':
                        business.update_inventory(cursor, connection)
                    case '4':
                        business.view_inventory_changes(cursor)
                    case '5':
                        print('View placed orders')
                    case '6':
                        break
                    case _:
                        print('invalid choice')
            
        case _:
            print('Invalid user type')