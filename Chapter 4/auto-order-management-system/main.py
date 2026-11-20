import database
import authentication

def main():
    database.connect()

    user_type = authentication.authenticate()

    if ( user_type ):
        print(f'You have authenticated as a {user_type}')

if __name__ == '__main__':
    main()