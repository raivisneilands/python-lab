import database
import authentication
import menu

def main():
    db_conn = database.connect()

    if (db_conn):
        connection = db_conn[0]
        cursor = db_conn[1]
    else:
        print('No connection was made to database. Exiting.')
        return

    auth = input('1 - Register\n2 - Login\nYour choice: ')

    match auth:
        case '1':
            user = authentication.register(cursor, connection)
        case '2':
            user = authentication.login(cursor, connection)
        case _:
            print('Not a valid option.')
            return

    if (not user):
        print('Failed to find user. Exiting.')
        return

    menu.show_menu(user, cursor, connection)

if __name__ == '__main__':
    main()