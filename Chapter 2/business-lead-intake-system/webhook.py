import requests, json

def trigger_webhook(event: str, lead = None):
    print(f'An webhook has been triggered. \nEvent: {event} \nLead: {lead}')

    payload = json.dumps({'event': event, 'lead': lead})

    response = requests.post('http://localhost:8000/api/webhook', json=payload)

    print(response.status_code)
    print(response.text)