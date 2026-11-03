def display():
    menu = """
        1 - View leads
        2 - Add a lead
        3 - Update a lead (COMING SOON)
        4 - Delete a lead (COMING SOON)
        5 - Exit
        Your choice: 
        """

    print(menu, end='')
    select = int(input())

    if (select > 5 or select < 1):
        return False

    return select