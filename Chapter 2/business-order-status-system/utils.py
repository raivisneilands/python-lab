import json, os

def read_orders(file):
    if (not os.path.exists(file)):
        return {'success': False, 'message': 'File does not exist'}

    if (not os.path.splitext(file)[1] == '.json'):
        return {'success': False, 'message': 'File should be in JSON format.'}
    
    with open(file) as orders:
        reader = json.load(orders)
    
    return {'success': True, 'data': reader}

def show_orders(orders):
    print('Available orders\nID\tCustomer\tProduct\t\tStatus')
    for order in orders:
        print(f'{order['id']}\t{order['customer']}\t{order['product']}\t\t{order['status']}')

def select_order(orders):
    print('Select order ID: ', end='')
    order_id = int(input()) - 1

    return orders[order_id]

def change_order_status(order):
    print('Select the new status from the list:')
    print('1 - Processing\n2 - Shipped\n3 - Delivered\n4 - Cancelled')
    new_status = int(input())

    match new_status:
        case 1:
            status = 'processing'
        case 2:
            status = 'shipped'
        case 3:
            status = 'delivered'
        case 4:
            status = 'cancelled'
        case _:
            'Invalid choice. Please try again.'

    order['status'] = status

def update_orders_file(file, orders):
    with open(file, 'w') as order_file:
        json.dump(orders, order_file)