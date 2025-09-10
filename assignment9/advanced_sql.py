import sqlite3

conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")
cursor = conn.cursor()

# Task 1 
cursor.execute("""
    SELECT o.order_id, SUM(li.quantity * p.price) AS total_price
    FROM orders AS o
    JOIN line_items AS li ON o.order_id = li.order_id
    JOIN products AS p ON li.product_id = p.product_id
    GROUP BY o.order_id
    ORDER BY o.order_id
    LIMIT 5;
""")
for row in cursor.fetchall():
    print(row)

# Task 2 
cursor.execute("""
    SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price
    FROM customers AS c
    LEFT JOIN (
        SELECT o.customer_id AS customer_id_b, SUM(li.quantity * p.price) AS total_price
        FROM orders AS o
        JOIN line_items AS li ON o.order_id = li.order_id
        JOIN products AS p ON li.product_id = p.product_id
        GROUP BY o.order_id
    ) AS order_totals
     ON c.customer_id = order_totals.customer_id_b
    GROUP BY c.customer_id;
""")

for row in cursor.fetchall():
      print(row)

# Task 3 
cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
customer_id = cursor.fetchone()[0]

cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
employee_id = cursor.fetchone()[0]

cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
products = cursor.fetchall()

cursor.execute(f"""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES ({customer_id}, {employee_id}, DATE('now'))
        RETURNING order_id
    """)
order_id = cursor.fetchone()[0]

for p in products:
        cursor.execute(f"""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES ({order_id}, {p[0]}, 10)
        """)

conn.commit()

cursor.execute(f"""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = {order_id};
    """)

for row in cursor.fetchall():
      print(row)

# Task 4 

cursor.execute("""
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees AS e
    JOIN orders AS o On e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
""")

for row in cursor.fetchall():
      print(row)

conn.close()