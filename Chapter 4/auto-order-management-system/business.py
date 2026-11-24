def view_customers(cursor):
    cursor.execute("""
        SELECT * FROM customers
        WHERE type = 'customer'
    """)

    customers = cursor.fetchall()

    if (not customers):
        print('No customers were found.')
        return

    print(f'{'Name':<40}{'Email':<40}{'Phone Number':<20}')

    for customer in customers:
        print(
            f'{customer[1] + ' ' + customer[2]:<40}'
            f'{customer[3]:<40}'
            f'{customer[4]:<20}'
        )
