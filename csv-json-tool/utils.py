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

def print_monthly_view(months):
    for month in months:
        print()
        print(month, end='.\n')

        total = 0

        print('Type \t Amount')

        for item in months[month]:
            if (not item['type']):
                continue

            if (item['type'].strip().lower() == 'income'):
                total += float(item['amount'])
            else:
                total -= float(item['amount'])

        print(f'{"Inc" if total > 0 else "Exp"} \t ${total:.2f}')


def calculate_total(months):
    total_year = 0
    for month in months:
        for item in months[month]:
            if (not item['type']):
                print(f'Type not provided for week {item['week']}, ignoring this week...')
                continue              

            if (item['type'].strip().lower() == 'income'):
                total_year += float(item['amount'])
            else:
                total_year -= float(item['amount'])

    return (f'{total_year:.2f}')

def display_menu():
    menu = """
        1 - Calculate total for the year
        2 - Show monthly overview
        3 - Exit
    """

    print(menu)
    user_choice = input()

    return user_choice
