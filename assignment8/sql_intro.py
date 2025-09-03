# Task 1

import sqlite3

def create_connection(db_file):
    """Create a database connection to the SQLite database"""
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")  
        print("Connected to database:", db_file)
        return conn
    except sqlite3.Error as e:
        print("Error connecting:", e)
        return None

if __name__ == "__main__":
    conn = create_connection("../db/magazines.db")
    if conn:
        conn.close()

# Task 2

def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            publisher_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            magazine_id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER,
            FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            subscriber_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            subscription_id INTEGER PRIMARY KEY,
            subscriber_id INTEGER,
            magazine_id INTEGER,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id)
        );
        """)

        conn.commit()
        print("Database created and connected successfully.")
    except sqlite3.Error as e:
        print("Database file failed:", e)

# Task 3

import sqlite3

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")  
        return conn
    except sqlite3.Error as e:
        print("Error connecting to database:", e)
        return None

def add_publisher(conn, name):
    try:
        conn.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f" Publisher '{name}' already exists.")

def add_magazine(conn, name, publisher_id):
    try:
        conn.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        conn.commit()
    except sqlite3.IntegrityError:
        print(f" Magazine '{name}' already exists or invalid publisher_id.")

def add_subscriber(conn, name, address):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f" Subscriber '{name}' at '{address}' already exists.")
            return
        conn.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
        conn.commit()
    except sqlite3.Error as e:
        print("Error adding subscriber:", e)

def add_subscription(conn, subscriber_id, magazine_id, expiration_date):
    try:
        conn.execute(
            "INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)",
            (subscriber_id, magazine_id, expiration_date)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        print(f" Subscription already exists for subscriber {subscriber_id} and magazine {magazine_id}.")

if __name__ == "__main__":
    conn = create_connection("../db/magazines.db")
    if conn:
       
        add_publisher(conn, "Penguin Media")
        add_publisher(conn, "Global Press")
        add_publisher(conn, "Skyline Publishing")

        # Magazines
        add_magazine(conn, "Tech Weekly", 1)
        add_magazine(conn, "Health Today", 2)
        add_magazine(conn, "Travel World", 3)

        # Subscribers
        add_subscriber(conn, "Alice Smith", "123 Main St")
        add_subscriber(conn, "Bob Johnson", "456 Oak St")
        add_subscriber(conn, "Charlie Brown", "789 Pine St")

        # Subscriptions
        add_subscription(conn, 1, 1, "2026-01-01")
        add_subscription(conn, 1, 2, "2025-12-15")
        add_subscription(conn, 2, 3, "2026-03-01")

        conn.close()

# Task 4

def run_queries(conn):
    cur = conn.cursor()

    print("\nAll subscribers:")
    for row in cur.execute("SELECT * FROM subscribers;"):
        print(row)

    print("\nAll magazines (alphabetical):")
    for row in cur.execute("SELECT * FROM magazines ORDER BY name;"):
        print(row)

    print("\nMagazines by publisher 'Condé Nast':")
    for row in cur.execute("""
        SELECT m.name 
        FROM magazines m
        JOIN publishers p ON m.publisher_id = p.publisher_id
        WHERE p.name = ?;
    """, ("Condé Nast",)):
        print(row)

if __name__ == "__main__":
    conn = create_connection("../db/magazines.db")
    if conn:
        run_queries(conn)
        conn.close()