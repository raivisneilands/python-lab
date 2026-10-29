import requests, time, json, hmac, hashlib

secret = 'do-not-show-anyone-top-secret'

def trigger_webhook(order, previous_status):
    payload = {
        'event': f'order.{order['status']}',
        'order_id': order['id'],
        'customer': order['customer'],
        'previous_status': previous_status,
        'updated_status': order['status']
    }

    body = json.dumps(payload)

    signature = hmac.new(
        secret.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()

    s = requests.Session()

    for attempt in range(3):
        try:
            response = s.post(
                'http://localhost:8000/api/webhook',
                data=body,
                headers={
                    'Content-Type': 'application/json',
                    'X-signature': signature
                },
                timeout = 3
            )

            if 200 <= response.status_code < 300:
                print('Webhook delivered successfully.')
                break

            if response.status_code == 429 or response.status_code >= 500:
                print(f'Temporary HTTP failure: {response.status_code}')
            else:
                print(f'Webhook rejected: {response.status_code}')
                break

            break
        except requests.RequestException as e:
            print(f'Attempt {attempt + 1} failed. {e}')
            if (attempt < 2):
                time.sleep(1)
    else:
        print('Failed to deliver webhook 3 times.')