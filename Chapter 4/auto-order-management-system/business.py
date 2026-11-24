from decimal import Decimal
import datetime
import products

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

def update_inventory(cursor, connection):
    menu = """
Please select an action.
1 - Add a new product
2 - Add multiple products
3 - Update existing product
4 - Delete a product
    """

    print(menu)
    user_choice = input('Your choice: ')

    match user_choice:
        case '1':
            add_product(cursor, connection)
        case '2':
            amount = int(input('How many products would you like to add: '))
            for i in range(amount):
                add_product(cursor, connection)
        case '3':
            update_product(cursor, connection)
        case '4':
            delete_product(cursor, connection)
        case _:
            print('Invalid choice. Returning')

def add_product(cursor, connection):
    product_name = input('Enter the product name: ')
    price = input('Enter the price of the product: ')
    in_stock = input('Enter the stock amount of the product: ')

    try:
        cursor.execute("""
            INSERT INTO products (name, price, in_stock) VALUES
            (%s, %s, %s)
        """, (product_name, Decimal(price), int(in_stock)))

        connection.commit()

        print('Product added successfully.')

    except Exception as e:
        print(f'Something went wrong: {e}')

def update_product(cursor, connection):
    print('Current inventory:')
    products.get_all(cursor)

    product_id = int(input('Enter the ID of product you wish to change: '))
    try:
        cursor.execute("""
            SELECT * FROM products
            WHERE id_product = %s
        """, (product_id,))

        product = cursor.fetchone()

        if (not product):
            print('Failed to find the product.')
            return

    except Exception as e:
        print(f'Something went wrong: {e}')
        return
    
    update_product_menu = """
1 - Change name and/or price
2 - Change stock amount
    """

    print(update_product_menu)
    change = input('What would you like to change: ')

    match change:
        case '1':
            new_product_name = input('Enter the new product name (leave empty to keep the existing name): ')
            new_price = input('Enter the new price (leave empty to keep the existing price): ')

            if (not new_product_name and not new_price):
                print('No new values were provided. Returning')
                return

            new_product_name = product[1] if len(new_product_name) == 0 else new_product_name 
            new_price = product[2] if len(new_price) == 0 else new_price

            try:
                cursor.execute("""
                    UPDATE products
                    SET name = %s, price = %s
                    WHERE id_product = %s
                """, (new_product_name, Decimal(new_price), product_id))

                connection.commit()

                print('Product updated successfully.')
            except Exception as e:
                print(f'Something went wrong: {e}')
                return
            
        case '2':
            new_stock = int(input('Enter the new amount of stock: '))

            if(product[3] == new_stock):
                print('Stock remains unchanged. Returning.')
                return

            try:
                current_date = datetime.datetime.now()

                cursor.execute("""
                    UPDATE products
                    SET in_stock = %s
                    WHERE id_product = %s
                """, (new_stock, product_id))

                cursor.execute("""
                    INSERT INTO inventory_log (product_id, change, reason, log_date)
                    VALUES
                    (%s, %s, 'Inventory update', %s)
                """, (product_id, new_stock - product[3], current_date))

                connection.commit()

                print('Stock for the product updated successfully.')

            except Exception as e:
                print(f'Something went wrong: {e}')

        case _:
            print('Invalid choice. Returning.')

def delete_product(cursor, connection):
    print('Current inventory:')
    products.get_all(cursor)

    product_id = int(input('Enter the ID of the product you wish to delete: '))

    try:
        cursor.execute("""
            SELECT * FROM products
            WHERE id_product = %s
        """, (product_id,))

        product = cursor.fetchone()

        if (not product):
            print('Failed to find the product.')
            return

    except Exception as e:
        print(f'Something went wrong: {e}')
        return

    confirmation = input('Are you sure you want to delete this product? y/n: ')

    if (confirmation.lower() == 'y'):
        try:
            cursor.execute("""
                DELETE FROM products
                WHERE id_product = %s
            """, (product_id,))

            connection.commit()

            print('Product was deleted successfully.')

            return

        except Exception as e:
            print(f'Something went wrong: {e}')

    print('Returning...')
    return

def view_inventory_changes(cursor):
    try:
        cursor.execute("""
            SELECT p.name, i.change, i.reason, i.log_date FROM inventory_log as i
            INNER JOIN products as p
            ON i.product_id = p.id_product
        """)

        results = cursor.fetchall()

        if (not results):
            print('No changes have been made.')
            return

        print(f'{'Product Name':<30}{'Stock change':<15}{'Reason':<40}{'Log date and time':<30}')

        for log in results:
            stock_change = '+' + str(log[1]) if log[1] > 0 else log[1]
            print(
                f'{log[0]:<30}'
                f'{stock_change:<15}'
                f'{log[2]:<40}'
                f'{log[3].strftime("%Y-%m-%d %H:%M:%S"):<30}'
            )

    except Exception as e:
        print(f'Something went wrong: {e}')
