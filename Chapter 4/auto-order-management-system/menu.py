import products

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

def show_menu(user_type, cursor, connection):
    match user_type:
        case 'customer':
            print(customer_menu)
            user_choice = input('Your selection: ')
            
            match user_choice:
                case '1':
                    products.get_all(cursor)
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