def authenticate():
    display = """
1 - Authenticate as a customer
2 - Authenticate as a business owner
Please enter 1 or 2: 
    """

    user_type = input(display)

    if (user_type == '1'):
        return 'customer'
    elif ( user_type == '2'):
        return 'business_owner'
    else:
        print('Invalid choice.')
        return