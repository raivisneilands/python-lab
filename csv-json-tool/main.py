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

        for row in reader:
            if (not row['amount'] or 'O' in row['amount']):
                row['amount'] = 0

            month = list(months.keys())[month_index]
            months[month].append(row)

            weeks_added += 1

            if weeks_added == weeks_per_month[month_index]:
                month_index += 1
                weeks_added = 0

    for month in months:
        print('\n', month, end='.\n')

        total_sum = 0

        for item in months[month]:
            print(f'Type: {item['type']}, and amount: {item['amount']}')

            if (item['type'] == 'income'):
                total_sum += float(item['amount'])
            else:
                total_sum -= float(item['amount'])

        print(f'Total amount: {total_sum:.2f}')