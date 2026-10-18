import sqlite3


DATABASE = "sample.db"


# ---------------------------------------------------
# DATABASE CONNECTION
# ---------------------------------------------------

def get_connection():

    return sqlite3.connect(DATABASE)


# ---------------------------------------------------
# CREATE SAMPLE DATABASE
# ---------------------------------------------------

def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER
        )
    """)

    # ORDERS TABLE
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product TEXT,
            amount REAL
        )
    """)

    # SAMPLE USERS
    cursor.execute("SELECT COUNT(*) FROM users")

    if cursor.fetchone()[0] == 0:

        users = [
            ("Asha", "asha@gmail.com", 24),
            ("Ravi", "ravi@gmail.com", 31),
            ("Meena", "meena@gmail.com", 28),
            ("Karthik", "karthik@gmail.com", 22),
            ("Priya", "priya@gmail.com", 26)
        ]

        cursor.executemany("""
            INSERT INTO users (name, email, age)
            VALUES (?, ?, ?)
        """, users)

    # SAMPLE ORDERS
    cursor.execute("SELECT COUNT(*) FROM orders")

    if cursor.fetchone()[0] == 0:

        orders = [
            (1, "Laptop", 55000),
            (2, "Phone", 25000),
            (3, "Keyboard", 2500),
            (1, "Mouse", 1200),
            (4, "Monitor", 15000)
        ]

        cursor.executemany("""
            INSERT INTO orders (user_id, product, amount)
            VALUES (?, ?, ?)
        """, orders)

    conn.commit()
    conn.close()


# ---------------------------------------------------
# EXECUTE SQL
# ---------------------------------------------------

def execute_sql(query):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(query)

        # SELECT query
        if cursor.description:

            columns = [
                column[0]
                for column in cursor.description
            ]

            rows = cursor.fetchall()

            return {
                "columns": columns,
                "rows": rows
            }

        # INSERT / UPDATE / DELETE
        conn.commit()

        return {
            "message": "Query executed successfully.",
            "affectedRows": cursor.rowcount
        }

    except Exception as error:

        return {
            "error": str(error)
        }

    finally:

        conn.close()