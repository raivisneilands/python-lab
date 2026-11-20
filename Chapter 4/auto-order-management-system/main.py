import database
import authentication
import menu

def main():
    database.connect()

    user_type = authentication.authenticate()

    if ( user_type ):
        print(f'You have authenticated as a {user_type}')
    else:
        print('User type is not set. Quitting...')
        return

    menu.show_menu( user_type )
    
if __name__ == '__main__':
    main()