def send(cart):
    for item in cart:
        print(f'Adding {item} to order.')

    print('Preparing order...')

    print('Confirming order...')

    # Send the webhook via requests