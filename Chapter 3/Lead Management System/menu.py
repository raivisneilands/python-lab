def display():
    menu = """
1 - View leads
2 - Add a lead
3 - Update a lead
4 - Delete a lead
5 - View leads in sorted order
6 - Exit
    """

    print(menu)
    select = int(input('Your choice: '))

    return select