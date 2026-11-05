import psycopg2
from psycopg2 import errors
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
	conn_string = f"host='{os.getenv('DB_HOST')}' dbname='{os.getenv('DB_NAME')}' user='{os.getenv('DB_USER')}' password='{os.getenv('DB_PASS')}'"
	print (f'Connecting to database: {conn_string}')

	try:
		conn = psycopg2.connect(conn_string)
		cursor = conn.cursor()
		print('Successfully connected!')
		return conn, cursor
	except errors.OperationalError as e:
		print(f'Failed to connect to database: {e}')
		return
	

def disconnect(connection, cursor):
	cursor.close()
	connection.close()