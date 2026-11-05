import datetime
import psycopg2
from psycopg2 import sql

def print_columns(cursor):
    cursor.execute("""
        SELECT * FROM leads LIMIT 0;
    """)

    column_names = [desc[0] for desc in cursor.description]

    print('ID\tField')

    for item in column_names:
        print(column_names.index(item) + 1, f'\t{item}')

    return column_names

def view_all(cursor):
    cursor.execute("""
        SELECT * FROM leads;
    """)

    leads = cursor.fetchall()

    if (not leads):
        print('Currently there are no leads')
        return
    
    print('\nID\tLead Name\tCustomer Name\tDate')
    for lead in leads:
        print(f'{lead[0]}\t{lead[1]}\t\t{lead[2]}\t{lead[3]}')

def create(cursor):
    lead_name = input('Please enter the lead name: ')
    customer_name = input('Please enter the customer name: ')
    date = datetime.datetime.now()

    cursor.execute("""
        INSERT INTO leads (lead_name, customer_name, date)
        VALUES
        (%s, %s, %s)
    """, (lead_name, customer_name, date))

def update(cursor):
    view_all(cursor)

    lead_id = int(input('Please select the ID of the lead you wish to update: '))
    
    cursor.execute("""
        SELECT * FROM leads
        WHERE id = %s;
    """, (lead_id,))

    selected_lead = cursor.fetchone()
    if not (selected_lead):
        print('Failed to find the lead. Returning.')
        return
    
    print(f'You have selected this lead!\n {selected_lead}')
    
    lead_name = input('Please enter the lead name (leave empty to not change): ')
    lead_name = selected_lead[1] if len(lead_name) == 0 else lead_name
    customer_name = input('Please enter the customer name (leave empty to not change): ')
    customer_name = selected_lead[2] if len(customer_name) == 0 else customer_name
    date = datetime.datetime.now()

    cursor.execute("""
        UPDATE leads
        SET lead_name = %s, customer_name = %s, date = %s
        WHERE id = %s
    """, (lead_name, customer_name, date, lead_id))

def delete(cursor, connection):
    view_all(cursor)

    confirmation = ''

    lead_id = int(input('Please select the ID of the lead you wish to delete: '))
    cursor.execute("""
        SELECT * FROM leads
        WHERE id = %s;
    """, (lead_id,))

    selected_lead = cursor.fetchone()

    if not (selected_lead):
        print('Failed to find the lead. Returning.')
        return
    
    while (confirmation.lower() != 'y' or confirmation.lower() != 'n'):
        confirmation = input(f'Are you sure you wish to delete this lead (y/n)?\n{selected_lead}: ')

        if (confirmation.lower() == 'y'):
            cursor.execute("""
                DELETE FROM leads
                WHERE id = %s;
            """, (lead_id,))
            connection.commit()
            return
        elif (confirmation.lower() == 'n'):
            cursor.close()
            print('Returning...')
            return
        else:
            print('Invalid choice, please try again.')

def view_sorted(cursor):
    column_names = print_columns(cursor)

    try:
        field = int(input('By which field you wish to sort? Enter the ID of the field: ')) - 1
    except ValueError as e:
        print(f'Invalid value type. {e}. Returning.')
        return
    
    try: 
        sort_column = column_names[field]
    except IndexError as e:
        print(f'The lead with entered index was not found! {e}. Returning.')
        return

    sort_method = input('Do you wish to sort in Ascending or Descending order? (a/d): ')

    direction = 'ASC' if sort_method.lower() == 'a' else 'DESC'

    query = sql.SQL("SELECT * FROM leads ORDER BY {} %s").format(
        sql.Identifier(sort_column)
    )

    cursor.execute(query, (direction,))

    leads = cursor.fetchall()

    if (not leads):
        print('No leads were found. Returning.')
        return

    # can't call view_all() as it prints out the leads unsorted. This prints out the sorted way.
    print('\nID\tLead Name\tCustomer Name\tDate')
    for lead in leads:
        print(f'{lead[0]}\t{lead[1]}\t\t{lead[2]}\t{lead[3]}')

def search(cursor):
    column_names = print_columns(cursor)

    field = int(input('By which field you wish to search, enter the ID: ')) - 1

    if (field != 3):
        search_query = input('Search query: ')

    search_column = column_names[field]

    if (field == 0):
        query = sql.SQL("SELECT * FROM leads" \
        " WHERE {} = %s").format(
            sql.Identifier(search_column)
        )
    elif (field == 3):
        search_query = input('Enter the date to search for (YYYY-MM-DD): ')
        query = sql.SQL("SELECT * FROM leads" \
        " WHERE {} = %s").format(
            sql.Identifier(search_column),
        )
    else:
        query = sql.SQL("SELECT * FROM leads" \
        " WHERE {} LIKE %s").format(
            sql.Identifier(search_column),
        )
        search_query = '%' + search_query + '%'
    try:
        cursor.execute(query, (search_query,))
    except psycopg2.errors.InvalidDatetimeFormat:
        print('Invalid format. Please input following this format (YYYY-MM-DD).')
        return
    
    results = cursor.fetchall()

    if (not results):
        print('No matching results were found.')
        return

    print('\nID\tLead Name\tCustomer Name\tDate')
    for lead in results:
        print(f'{lead[0]}\t{lead[1]}\t\t{lead[2]}\t{lead[3]}')