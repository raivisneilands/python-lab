import database as db
import menu
import lead

def main():
    db_conn = db.connect()

    if (db_conn):
        connection = db_conn[0]
        cursor = db_conn[1]
    else:
        print('No connection was made to database. Exiting.')
        return

    try:
        while (True):
            user_input = menu.display()

            match user_input:
                case 1: 
                    lead.view_all(cursor)
                    connection.commit()
                case 2: 
                    result = lead.create(cursor)
                    if result is True:
                        connection.commit()
                    elif result is False:
                        connection.rollback()
                case 3:
                    result = lead.update(cursor)
                    if result is True:
                        connection.commit()
                    elif result is False:
                        connection.rollback()
                case 4:
                    result = lead.delete(cursor)
                    if result is True:
                        connection.commit()
                    elif result is False:
                        connection.rollback()
                case 5:
                    result = lead.view_sorted(cursor)
                    if result is False:
                        connection.rollback()
                    else: 
                        connection.commit()
                case 6:
                    result = lead.search(cursor)
                    if result is False:
                        connection.rollback()
                    else:
                        connection.commit()
                case 7: # Exit
                    break
                case _:
                    print('Invalid choice. Please try again.')
    except Exception as e:
        print(f'Oops... Something went wrong: {e}')
        connection.rollback()
    finally:
        db.disconnect(connection, cursor)


if __name__ == '__main__':
    main()