import requests
import dotenv
import os
import uuid

dotenv.load_dotenv()

header_key = os.getenv('N8N_HEADER_KEY')
n8n_url = 'http://localhost:5678/webhook-test/89eb90e9-f620-4d3b-9152-c4f53911446d'

def send(user, cart):
    print('Preparing order...')

    total = 0

    for item in cart:
        print(f'Adding {item} to order.')

        prod = cart[item]['Product']
        cart[item]['Product'] = prod[:2] + (str(prod[2]),) + prod[3:]

        total += float(cart[item]['Product'][2]) * cart[item]['Quantity']

    headers = {
        'security-auth': header_key,
        'content-type': 'application/json'
    }

    payload = {
        'order_id': str(uuid.uuid4()),
        'customer_id': user['id_user'],
        'cart': cart,
        'total': total
    }

    print('Confirming and sending order...', payload)

    response = requests.post(n8n_url, json=payload, headers=headers)

    result = response.json()

    if response.status_code == 200:
        print("Success:", response.json())
        print(
            f'Order with ID - {response.json()[0]['json']['id_order']} was confirmed successfully.\n'
            f'Product count: {len(response.json()[0]['json']['products'])}'
        )
    else:
        print(f"Failed ({response.status_code}):", response.text)