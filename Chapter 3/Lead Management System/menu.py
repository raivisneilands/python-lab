def display():
    menu = """
1 - View leads
2 - Add a lead
3 - Update a lead
4 - Delete a lead
5 - Exit
    """

    print(menu)
    select = int(input('Your choice: '))

    if (select > 5 or select < 1):
        return False

    return select