import sys, os, csv
import utils as u

authenticated = u.authenticate()

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

    with open(file) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            print(row['amount'])

