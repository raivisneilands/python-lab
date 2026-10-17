expenses = []

def view_expenses(expenses):
    if len(expenses) > 0:
        print('\nEXPENSE LIST\n')
        counter = 1
        print('Nr.\tExpense name\tExpense amount')
        for expense in expenses:
            print(f'{counter}|\t{expense['name']}\t{expense['amount']}')
            counter += 1
    else:
        print('\nList is empty. Nothing to view.\n')
    print('\n')

def add_expense(expenses):
    try:
        print("Enter the expense amount: ", end='')
        exp_amount = float(input())
    except ValueError:
        print('You must enter a number!')
        return
    print("Enter the expense name: ", end='')
    exp_name = input()
    expenses.append({"name": exp_name, "amount": exp_amount})
    print("\nExpense added! Updated list:")
    view_expenses(expenses)

def remove_expense(expenses):
    if len(expenses) > 0:
        view_expenses(expenses)
        try:
            print('Write the number of the expense to remove: ', end='')
            expense_to_remove = int(input()) - 1
        except ValueError:
            print('\nYou must enter a number!\n')
            return
        try:
            expenses.pop(expense_to_remove)    
            print('\nExpense removed! Updated list:')
            view_expenses(expenses)
        except IndexError:
            print('Expense not found in the list. List remains unchanged\n')
    else:
        print('\nList is empty. Nothing to remove.\n')

def update_expense(expenses):
    if len(expenses) > 0:
        view_expenses(expenses)   
        try:     
            print('Enter the number of expense you wish to update: ', end='')
            exp_index = int(input()) - 1    
        except ValueError:
            print('\nMust be a number!\n')   
            return
        if exp_index < 0 or exp_index >= len(expenses):
            print('\nEntered number not found in list\n')
            return
        try:
            print('Enter the updated amount: ', end='')
            exp_amount = float(input())
        except ValueError:
            print('\nMust be a number!\n')
            return        
        print('Enter the updated name: ', end='')
        exp_name = input()
        expenses[exp_index]['name'] = exp_name
        expenses[exp_index]['amount'] = exp_amount
        print('\nExpense list updated:')
        view_expenses(expenses)
    else:
        print('\nList is empty. Nothing to update\n')

def calculate_total_expenses(expenses):
    sum = 0
    for expense in expenses:
        sum += expense['amount']
    print(f'\nTotal calculated expenses: {sum}\n')

while True:
    print('1 - Add expense')
    print('2 - Remove expense')
    print('3 - View expenses')
    print('4 - Update expense')
    print('5 - Calculate total')
    print('6 - Exit')

    try:
        print('Your choice: ', end='')

        user_choice = int(input())
    except ValueError:
        print('\nMust be a number!\n')
        continue

    match user_choice:
        case 1:
            add_expense(expenses)
        case 2:
            remove_expense(expenses)
        case 3:
            view_expenses(expenses)
        case 4:
            update_expense(expenses)
        case 5:
            calculate_total_expenses(expenses)
        case 6:
            break
        case _:
            print('\nInvalid choice. Please try again!\n')