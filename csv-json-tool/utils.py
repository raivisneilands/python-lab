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

def print_weekly_view(months):
    for month in months:
        print()
        print(month, end='.\n')

        print('Week \t Type \t Amount \t Category')

        for item in months[month]:
            if (not item['type']):
                continue

            print(f'{item['week']} \t {item['type'].capitalize()[:3]} \t {str(item['amount']) + '    '} \t {item['category']}')


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
3 - Show weekly overview
4 - Show user defined period
5 - Group finances by category
6 - Exit
    """

    print(menu)
    user_choice = input()

    return user_choice

def calculate_from_user_defined_period(months):
    print('Please enter the starting week: ', end='')
    starting_week = int(input())
    print('Please enter the ending week: ', end='')
    ending_week = int(input())

    if (ending_week < starting_week):
        print('Starting week must be earlier than ending week')
        return

    total_sum = 0

    print('Week \t Type \t Amount \t Category')

    for month in months:
        for item in months[month]:
            if (not item['type']):
                continue

            if (item['week'] < starting_week or item['week'] > ending_week):
                continue

            if (item['type'].strip().lower() == 'income'):
                total_sum += float(item['amount'])
            else:
                total_sum -= float(item['amount'])

            print(f'{item['week']} \t {item['type'].capitalize()[:3]} \t {str(item['amount']) + '    '} \t {item['category']}')    

    print(f'\n Total amount for the defined period: {total_sum}')

def finances_by_category(months):
    categories = {}
    for month in months:
        for item in months[month]:
            if (item['category'] not in categories):
                categories[item['category']] = []
            categories[item['category']].append({'amount': item['amount'], 'type': item['type']})

    print('Category \t Amount')
    
    for category in categories:
        category_sum = 0
        for item in categories[category]:
            if item['type'] == 'income':
                category_sum += item['amount']
            else:
                category_sum -= item['amount']

        print(f'{category} {'\t' if len(category) > 7 else '\t\t'} ${category_sum:.2f}')        
