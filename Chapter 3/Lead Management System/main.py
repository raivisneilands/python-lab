import database as db
import menu
import lead

def main():
    db_conn = db.connect()

    connection = db_conn[0]
    cursor = db_conn[1]

    while (True):
        user_input = menu.display()

        match user_input:
            case 1: 
                lead.view_all(cursor)
            case 2: 
                lead.create(cursor)
                connection.commit()
            case 3:
                lead.update(cursor)
                connection.commit()
            case 4:
                lead.delete(cursor, connection)
            case 5: # Exit
                break
            case _:
                print('Invalid choice. Please try again.')

    db.disconnect(connection, cursor)

if __name__ == '__main__':
    main()