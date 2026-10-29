import json, os

def read_orders(file):
    if (not os.path.exists(file)):
        return {'success': False, 'message': 'File does not exist'}

    if (not os.path.splitext(file)[1] == '.json'):
        return {'success': False, 'message': 'File should be in JSON format.'}
    
    with open(file) as orders:
        reader = json.load(orders)

    for item in reader:
        for key in item.keys():
            if(not item[key]):
                return {'success': False, 'message': f'Value is missing for key: {key}. Order ID: {item['id']}'}
    
    return {'success': True, 'data': reader}

def show_orders(orders):
    print('Available orders\nID\tCustomer\tProduct\t\tStatus')
    for order in orders:
        print(f'{order['id']}\t{order['customer']}\t{order['product']}\t\t{order['status']}')

def select_order(orders):
    try:
        print('Select order ID: ', end='')
        order_id = int(input())

        for order in orders:
            if (order['id'] == order_id):
                return order

        print('Order not found.')
        return None

    except ValueError:
        print('ID must be an integer.')
        return None

def change_order_status(order):
    try:
        print('Select the new status from the list:')
        print('1 - Processing\n2 - Shipped\n3 - Delivered\n4 - Cancelled')
        new_status = int(input())
        old_status = order['status']

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
                print('Invalid status choice.')
                status = None

        if (not status):
            print('Failed to change status.')
            return None

        if (old_status == status):
            return {'success': True, 'changed': False, 'message': f'Status was already {status}. No need for order file update.'}

        order['status'] = status
        return {'success': True, 'changed': True, 'message': 'Status updated successfully.', 'prev_status': old_status}

    except ValueError:
        print('You must enter an integer.')
        return None

def update_orders_file(file, orders):
    try:
        with open(file, 'w') as order_file:
            json.dump(orders, order_file)
    except Exception:
        return {'success': False, 'message': 'Failed to update the order file.'}
    
    return {'success': True, 'message': 'Order file updated successfully.'}
    