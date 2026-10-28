import pytest, utils, os

def test_success_authentication():
    success = '123' == os.getenv('ACCESS_PASSWORD')
    assert success == 1

def test_failed_authentication():
    failure = 'incorrect_password' == os.getenv('ACCESS_PASSWORD')
    assert failure == 0

def test_csv_file_prep():
    file = 'csv-json-tool\\some_data.csv'
    months = utils.prepare_file(file, '.csv')
    assert bool(months) == True

def test_json_file_prep():
    file = 'csv-json-tool\\transactions_2026.json'
    months = utils.prepare_file(file, '.json')
    assert bool(months) == True

def test_weekly_view_not_empty():
    file = 'csv-json-tool\\some_data.csv'
    months = utils.prepare_file(file, '.csv')
    float_number = 12.99
    total = utils.calculate_total(months)
    assert type(total) == type(float_number)

