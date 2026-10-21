import sys, os, csv, json
import utils as util

authenticated = util.authenticate()

if (authenticated == 0):
    print('Invalid password. Exiting.')
    sys.exit(1)

if (authenticated):
    try:
        file = sys.argv[1]
        file_name, file_extension = os.path.splitext(file)
        print(f'Provided file: {file}.')
    except IndexError:
        print('No path for file provided. Exiting.')
        sys.exit(1)

    if (not os.path.exists(file)):
        print('Provided file does not exist. Exiting.')
        sys.exit(1)
    if (not os.path.isfile(file)):
        print('Provided path is not a file. Exiting.')
        sys.exit(1)
    if (file_extension != '.csv' and file_extension != '.json'):
        print('The file is not a CSV or JSON file. Exiting.')
        sys.exit(1)

    months = util.prepare_file(file, file_extension)

    while (True):
        user_choice = util.display_menu()

        match(user_choice):
            case '1':
                yearly_amount = util.calculate_total(months)
                print(f'Total amount for all year: {yearly_amount}', end='\n')
            case '2':
                print('Monthly overview:')
                util.print_monthly_view(months)
            case '3':
                print('Weekly overview:')
                util.print_weekly_view(months)
            case '4':
                print('Statistics for user defined period:')
                util.calculate_from_user_defined_period(months)
            case '5':
                print('Finances grouped by category:')
                util.finances_by_category(months)
            case '6':
                break
            case _:
                print('Invalid choice. Enter a number shown from the menu.')
