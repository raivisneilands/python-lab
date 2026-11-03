import datetime

def view_all(cursor):
    cursor.execute("""
        SELECT * FROM leads;
    """)

    leads = cursor.fetchall()

    if (not leads):
        print('Currently there are no leads')
        return
    
    print('\nLead Name\tCustomer Name\tDate')
    for lead in leads:
        print(f'{lead[1]}\t\t{lead[2]}\t{lead[3]}')

def create(cursor):
    lead_name = input('Please enter the lead name: ')
    customer_name = input('Please enter the customer name: ')
    date = datetime.datetime.now()

    cursor.execute("""
        INSERT INTO leads (lead_name, customer_name, date)
        VALUES
        (%s, %s, %s)
    """, (lead_name, customer_name, date))
