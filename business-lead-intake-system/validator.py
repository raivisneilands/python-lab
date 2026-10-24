import re

def validate_csv_data(record):
    if (not isinstance(record, dict)):
        return False, 'Must be of type "dict"'

    required_fields = ['name', 'email', 'service']

    for field in required_fields:
        if (field not in record):
            return False, f'{field} is required'

    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    if (not re.match(pattern, record['email'])):
        return False, 'Invalid email format'

    return True, 'Successfully validated'