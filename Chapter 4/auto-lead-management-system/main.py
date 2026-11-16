import requests

webhook_url = 'http://localhost:5678/webhook-test/3d94d3d1-ef08-4e4f-9a47-b0234402f17b'
services = ['Web Development', 'AI automation', 'Business Process Automation', 'API integration', 'Other']

def main():
    name = input('Please enter your name: ')
    email = input('Please enter your email: ')
    phone = input('Please enter your phone number: ')
    
    for index, service in enumerate(services):
        print(f'{index + 1} - {service}')

    selection = int(input('Please select the service. Enter the number: '))

    service = services[selection - 1]

    message = input('Enter any additional notes: ')

    lead = {'name': name, 'email': email, 'phone': phone, 'service': service, 'message': message}

    res = requests.post(webhook_url, json=lead)

    print(f'Response status code: {res.status_code}\nResponse: {res.text}')

if __name__ == '__main__':
    main()