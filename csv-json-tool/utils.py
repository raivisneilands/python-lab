from dotenv import load_dotenv
import os

load_dotenv()

correct_password = os.getenv('ACCESS_PASSWORD')

def authenticate():
    for i in range(3):
        print('Please enter password: ', end='')
        password = input()
        if (password == correct_password):
            return 1

    return 0
