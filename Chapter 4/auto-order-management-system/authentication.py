import bcrypt

def register(cursor, connection):
    f_name = input('Enter your first name: ')
    l_name = input('Enter your last name: ')
    email = input('Enter your email: ')
    phone = input('Enter your phone number: ')
    user_type = 'customer'
    password = input('Enter your password: ')

    hashed_password = bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    ).decode('utf-8')

    try:
        cursor.execute("""
            INSERT INTO customers
            (first_name, last_name, email, phone, type, password)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (f_name, l_name, email, phone, user_type, hashed_password))

        connection.commit()

        print('User created successfully')

        user = {
            'f_name': f_name, 
            'l_name': l_name,
            'email': email, 
            'phone': phone, 
            'user_type': user_type
        }

        return user
    except Exception as e:
        print(f'Something went wrong. Reason: {e}')
        return

def login(cursor, connection):
    email = input('Enter the email you registered with: ')
    password = input('Enter your password: ')

    cursor.execute("""
        SELECT * FROM customers
        WHERE email = %s
    """, (email,))

    user = cursor.fetchone()

    print(user)

    if user is None:
        print('User not found.')
        return

    stored_hash = user[6]

    if isinstance(stored_hash, bytes):
        stored_hash = stored_hash.decode('utf-8')

    if bcrypt.checkpw(
        password.encode('utf-8'),
        stored_hash.encode('utf-8')
    ):
        print('Login successful!')

        user = {
            'f_name': user[1], 
            'l_name': user[2],
            'email': user[3], 
            'phone': user[4], 
            'user_type': user[5]
        }

        return user
    else:
        print('Incorrect password.')
