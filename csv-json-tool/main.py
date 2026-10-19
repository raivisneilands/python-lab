import sys, os, csv
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
    if (file_extension != '.csv'):
        print('The file is not a CSV file. Exiting.')
        sys.exit(1)

    months = {
        'January': [], 'February': [], 'March': [], 'April': [], 'May': [], 'June': [],
        'July': [], 'August': [], 'September': [], 'October': [], 'November': [], 'December': [],
    }

    weeks_per_month = [5, 4, 4, 5, 4, 4, 5, 4, 4, 5, 4, 4]

    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)

        month_index = 0
        weeks_added = 0

        rows_success = 0
        rows_failed = 0

        for row in reader:
            success = True
            if (not row['amount'] or 'O' in row['amount']):
                row['amount'] = 0
                success = False
                rows_failed += 1

            row['amount'] = abs(float(row['amount']))
            
            month = list(months.keys())[month_index]
            months[month].append(row)

            weeks_added += 1

            if (success):
                rows_success += 1

            if weeks_added == weeks_per_month[month_index]:
                month_index += 1
                weeks_added = 0

        print(f'Successfully processed rows: {rows_success}\nFailed rows: {rows_failed}')

        while (True):
            user_choice = util.display_menu()

            match(user_choice):
                case '1':
                    yearly_amount = util.calculate_total(months)
                    print(f'Total amount for all year: {yearly_amount}', end='\n')
                case '2':
                    print('Monthly overview:', end='\n')
                    util.print_monthly_view(months)
                case '3':
                    break
                case _:
                    print('Invalid choice. Enter a number shown from the menu.')
