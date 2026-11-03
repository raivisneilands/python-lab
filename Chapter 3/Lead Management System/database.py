import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def connect():
	conn_string = f"host='{os.getenv('DB_HOST')}' dbname='{os.getenv('DB_NAME')}' user='{os.getenv('DB_USER')}' password='{os.getenv('DB_PASS')}'"
	print (f'Connecting to database: {conn_string}')

	conn = psycopg2.connect(conn_string)
	cursor = conn.cursor()
	print('Successfully connected!')
	
	return conn, cursor

def disconnect(connection, cursor):
	cursor.close()
	connection.close()