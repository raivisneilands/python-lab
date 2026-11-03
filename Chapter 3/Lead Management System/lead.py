import datetime

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