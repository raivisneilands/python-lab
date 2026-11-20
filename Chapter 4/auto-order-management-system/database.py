import psycopg2
import dotenv
import os

dotenv.load_dotenv()

db_credentials = {'host': os.getenv('DB_HOST'), 'name':os.getenv('DB_NAME'), 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASS')}

def connect():
	try:
		print('Trying to connect to database...')

		for credential in db_credentials:
			if (not db_credentials[credential]):
				print(f'{credential} is missing to successfully connect to database')
				return

		conn = psycopg2.connect(
			host=db_credentials['host'],
			dbname=db_credentials['name'],
			user=db_credentials['user'],
			password=db_credentials['password'],
		)
		
		cursor = conn.cursor()
		print('Successfully connected!')
		return conn, cursor
	except psycopg2.errors.OperationalError as e:
		print(f'Failed to connect to database: {e}')
		return
	
def disconnect(connection, cursor):
    try:
        cursor.close()
        connection.close()
        print('Successfully closed the connection.')
    except Exception as e:
        print(f'Failed to close connection. Reason: {e}')