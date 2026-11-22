# Products
def get_all(cursor):
    cursor.execute("""
        SELECT * FROM products
        WHERE in_stock > 0;
    """)

    products = cursor.fetchall()

    return products