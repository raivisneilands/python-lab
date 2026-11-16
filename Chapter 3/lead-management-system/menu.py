def display():
    menu = """
1 - View leads
2 - Add a lead
3 - Update a lead
4 - Delete a lead
5 - View leads in sorted order
6 - Search leads
7 - Exit
    """

    print(menu)
    try:
        select = int(input('Your choice: '))
        return select
    except ValueError as e:
        print(f'Invalid input: {e}. Please enter a valid integer.')
        return