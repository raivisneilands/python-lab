import sys, json, csv, os

try:
    file = sys.argv[1]
except IndexError:
    print('File is not provided. Please try again and provide the path to the file.')
    sys.exit(1)

with open(file) as lead:
    reader = json.load(lead)

lead_file_path = 'business-lead-intake-system\\leads\\leads.csv'
file_exists = os.path.exists(lead_file_path)

with open(lead_file_path, 'a', newline='') as leads_file:
    fieldnames = ['name', 'email', 'company', 'service', 'message']
    writer = csv.DictWriter(leads_file, fieldnames=fieldnames)

    if(not file_exists):
        writer.writeheader()
    
    writer.writerow(reader)