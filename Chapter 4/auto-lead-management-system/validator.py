import validators
import phonenumbers

def validate_name(name):
    if (not name):
        print('Name is required.')
        return
    if (len(name) > 50):
        print('Name is too long. It must be between 2 - 50 characters.')
        return
    if (len(name) < 2):
        print('Name is too short. It must be between 2 - 50 characters.')
        return
    return True

def validate_email(email):
    if (not email):
        print('Email is required.')
        return
    if (not validators.email(email)):
        print('Invalid email format.')
        return
    return True

def validate_phone(phone):
    if (not phone):
        print('Phone is required.')
        return

    try:
        parsed = phonenumbers.parse(phone)
        return phonenumbers.is_valid_number(parsed)
    except:
        print('Invalid phone number format.')
        return


def validate_message(message):
    if (not message):
        print('Message is required.')
        return
    if (len(message) > 2000):
        print('Message is too long. It must be between 5 - 2000 characters.')
        return
    if (len(message) < 5):
        print('Message is too short. It must be between 5 - 2000 characters.')
        return

def validate(data):
    if (not data['id']):
        print('ID is missing.')
        return
    validate_name(data['name'])
    validate_email(data['email'])
    validate_phone(data['phone'])
    validate_message(data['message'])