import psycopg2
from psycopg2 import errors
from dotenv import load_dotenv
import os

load_dotenv()

credentials = {'host': os.getenv('DB_HOST'), 'name':os.getenv('DB_NAME'), 'user': os.getenv('DB_USER'), 'password': os.getenv('DB_PASS')}

def connect():
	try:
		print('Trying to connect to database...')

		for credential in credentials:
			if (not credentials[credential]):
				print(f'{credential} is missing to successfully connect to database')
				return

		conn = psycopg2.connect(
			host=credentials['host'],
			dbname=credentials['name'],
			user=credentials['user'],
			password=credentials['password'],
		)
		
		cursor = conn.cursor()
		print('Successfully connected!')
		return conn, cursor
	except errors.OperationalError as e:
		print(f'Failed to connect to database: {e}')
		return
	

def disconnect(connection, cursor):
	cursor.close()
	connection.close()