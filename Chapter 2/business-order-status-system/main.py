import sys, utils

def main():
    try:
        order_file = sys.argv[1]
    except IndexError:
        print('Order file is not provided')
        sys.exit(1)
    
    orders = utils.read_orders(order_file)
    data = orders['data']

    if (orders['success'] == False):
        print(f'Failed to read orders file. Reason: {orders['message']}')
        sys.exit(1)

    utils.show_orders(data)
    order = utils.select_order(data)

    print('Selected order:')
    print(f'{order['id']} - {order['customer']} - {order['product']} - {order['status']}')

    utils.change_order_status(order)
    utils.update_orders_file(order_file, data)


if __name__ == '__main__':
    main()