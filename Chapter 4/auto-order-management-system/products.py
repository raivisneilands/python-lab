# Products
def get_all(cursor):
    cursor.execute("""
        SELECT * FROM products
        WHERE in_stock > 0;
    """)

    products = cursor.fetchall()

    print(f"{'ID':<6}{'Product':<30}{'Price':>12}{'Stock':>10}")

    for product in products:
        print(
            f"{product[0]:0>4d}  "
            f"{product[1]:<30}"
            f"{product[2]:>12.2f}"
            f"{product[3]:>10}"
        )