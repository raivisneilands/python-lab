import datetime
import psycopg2
from psycopg2 import sql

def print_columns(cursor):
    cursor.execute("""
        SELECT * FROM leads LIMIT 0;
    """)

    column_names = [desc[0] for desc in cursor.description]

    print('ID\tField')

    for index, item in enumerate(column_names, start=1):
        print(index, f'\t{item}')

    return column_names

def view_all(cursor):
    cursor.execute("""
        SELECT * FROM leads
        ORDER by id DESC;
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

    values = {'lead': lead_name, 'customer': customer_name}
    missing_values = []

    for value in values:
        if (not values[value]):
            missing_values.append(value)

    if (len(missing_values) > 0):
        print('Following values are missing: ')
        for value in missing_values:
            print(value)
        return

    try:
        cursor.execute("""
            INSERT INTO leads (lead_name, customer_name, date)
            VALUES
            (%s, %s, %s)
        """, (lead_name, customer_name, date))

        return True
    except psycopg2.Error:
        print('Something went wrong when trying to create a lead. Rolling back changes.')
        return False

def update(cursor):
    view_all(cursor)

    try:
        lead_id = int(input('Please select the ID of the lead you wish to update: '))
    except ValueError:
        print('Please enter a valid integer.')
        return

    try:
        cursor.execute("""
            SELECT * FROM leads
            WHERE id = %s;
        """, (lead_id,))
    except psycopg2.Error:
        print('Failed to get the lead...')
        return False

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

    try:
        cursor.execute("""
            UPDATE leads
            SET lead_name = %s, customer_name = %s, date = %s
            WHERE id = %s
        """, (lead_name, customer_name, date, lead_id))
        return True
    except psycopg2.Error:
        print('Something went wrong when trying to update. Rolling back the changes.')
        return False

def delete(cursor):
    view_all(cursor)

    confirmation = ''

    try:
        lead_id = int(input('Please select the ID of the lead you wish to delete: '))
    except ValueError:
        print('Please enter a valid integer.')
        return

    try:
        cursor.execute("""
            SELECT * FROM leads
            WHERE id = %s;
        """, (lead_id,))
    except psycopg2.Error:
        print('Something went wrong...')
        return False

    selected_lead = cursor.fetchone()

    if not (selected_lead):
        print('Failed to find the lead. Returning.')
        return False
    
    while (confirmation.lower() not in ('y', 'n')):
        confirmation = input(f'Are you sure you wish to delete this lead (y/n)?\n{selected_lead}: ')

        if (confirmation.lower() == 'y'):
            try:
                cursor.execute("""
                    DELETE FROM leads
                    WHERE id = %s;
                """, (lead_id,))
                return True
            except psycopg2.Error:
                print('Something went wrong. Rolling back made changes...')
                return False
        elif (confirmation.lower() == 'n'):
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

    if field < 0 or field >= len(column_names):
        print('Invalid field ID.')
        return
    
    sort_column = column_names[field]

    sort_method = input('Do you wish to sort in Ascending or Descending order? (a/d): ')

    if (sort_method.lower() not in ('a', 'd')):
        print('Invalid sorting method')
        return

    direction = 'ASC' if sort_method.lower() == 'a' else 'DESC'

    query = sql.SQL("SELECT * FROM leads ORDER BY {} {}").format(
        sql.Identifier(sort_column),
        sql.SQL(direction)
    )

    try:
        cursor.execute(query)
    except psycopg2.Error:
        print('Something went wrong')
        return False

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

    try:
        field = int(input('By which field you wish to search, enter the ID: ')) - 1
    except ValueError:
        print('Invalid data type. Please enter a valid integer.')
        return

    if field < 0 or field >= len(column_names):
        print('Invalid field ID.')
        return
    
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
        " WHERE DATE({}) = %s").format(
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

        results = cursor.fetchall()

        if (not results):
            print('No matching results were found.')
            return

        print('\nID\tLead Name\tCustomer Name\tDate')
        for lead in results:
            print(f'{lead[0]}\t{lead[1]}\t\t{lead[2]}\t{lead[3]}')

    except psycopg2.Error:
        print('Something went wrong')
        return False