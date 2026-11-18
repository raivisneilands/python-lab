import requests
import validator
import uuid
import datetime

webhook_url = 'http://localhost:5678/webhook-test/3d94d3d1-ef08-4e4f-9a47-b0234402f17b'
services = ['Web Development', 'AI automation', 'Business Process Automation', 'API integration', 'Other']

def main():
    id = str(uuid.uuid4())
    name = input('Please enter your name: ')
    email = input('Please enter your email: ')
    phone = input('Please enter your phone number: ')
    
    for index, service in enumerate(services):
        print(f'{index + 1} - {service}')

    try:
        selection = int(input('Please select the service. Enter the number: '))
    except ValueError:
        print('Must be an integer')
        return

    try:
        service = services[selection - 1]
    except IndexError:
        print('Service not found with that number.')
        return

    message = input('Enter any additional notes: ')

    created_at = str(datetime.datetime.now())
    datetime.datetime.fromisoformat(created_at)

    lead = {'id': id, 'name': name, 'email': email, 'phone': phone, 'service': service, 'message': message, 'created_at': created_at}

    validated = validator.validate(lead)

    if (validated == True):
        res = requests.post(webhook_url, json=lead)
        print(f'Response status code: {res.status_code}\nResponse: {res.text}')
    else:
        print('Failed to validate the input.')
        return


if __name__ == '__main__':
    main()