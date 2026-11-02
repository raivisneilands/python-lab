import database as db

def main():
    db_conn = db.db_connect()

    db_conn.execute('SELECT version();')
    records = db_conn.fetchall()

    print(records)

    db_conn.close()

if __name__ == '__main__':
    main()