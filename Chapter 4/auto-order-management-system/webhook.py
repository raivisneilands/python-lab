import requests
import dotenv
import os
import uuid

dotenv.load_dotenv()

header_key = os.getenv('N8N_HEADER_KEY')
n8n_url = 'http://localhost:5678/webhook-test/89eb90e9-f620-4d3b-9152-c4f53911446d'

def send(cart):
    print('Preparing order...')

    for item in cart:
        print(f'Adding {item} to order.')

        prod = cart[item]['Product']
        cart[item]['Product'] = prod[:2] + (str(prod[2]),) + prod[3:]

    headers = {
        'security-auth': header_key,
        'content-type': 'application/json'
    }

    payload = {
        'order_id': str(uuid.uuid4()),
        'cart': cart
    }

    print('Confirming and sending order...')

    response = requests.post(n8n_url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Success:", response.json())
    else:
        print(f"Failed ({response.status_code}):", response.text)