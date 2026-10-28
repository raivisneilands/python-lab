import sys, utils

def main():
    try:
        order_file = sys.argv[1]
    except IndexError:
        print('Order file is not provided')
        sys.exit(1)
    
    orders = utils.read_orders(order_file)

    if (orders['success'] == False):
        print(f'Failed to read orders file. Reason: {orders['message']}')
        sys.exit(1)
    else:
        data = orders['data']

    utils.show_orders(data)

    order = utils.select_order(data)

    if (not order):
        print('Failed to select order.')
        sys.exit(1)

    print('Selected order:')
    print(f'{order['id']} - {order['customer']} - {order['product']} - {order['status']}')

    status_change = utils.change_order_status(order)

    if (not status_change):
        print(f'Failed to update status of the order. Order ID: {order['id']}')
        sys.exit(1)

    print(status_change['message'])

    if (status_change['changed'] == True):
        file_update = utils.update_orders_file(order_file, data)
        print(file_update['message'])

if __name__ == '__main__':
    main()